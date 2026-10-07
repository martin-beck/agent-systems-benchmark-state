# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Subprocess fixtures for rollback control-store durability tests."""

# These subprocess fixtures cover only WAL/SHM rollback after process death and
# clean control-plane reopen. The caller-owned mode additionally exercises the
# lock/recheck seam, but does not prove ambiguous recovery, mutation fencing,
# authority integration, or formal refinement.
SUBPROCESS_SESSION_SCRIPT = r"""
import os
import signal
import sqlite3
import sys
import time
from contextlib import closing
from pathlib import Path

from tools.rollback_control_store import (
    BarrierSessionState,
    SQLiteBarrierSessionStore,
    SQLiteRollbackControlStore,
)
from tools.upgrade_identity import BarrierChildIdentity, BarrierSessionIdentity


def _reopen_evidence(state, target):
    child = state.rollback_child if target == "rollback" else state.forward_child
    assert child is not None
    return {
        "operation_id": child.operation_id,
        "target": child.target,
        "barrier_identity_digest": state.identity.identity_digest,
        "validated": True,
    }


control_path = Path(sys.argv[1])
authority_path = Path(sys.argv[2])
project_id = sys.argv[3]
mode = sys.argv[4]
ready_path = Path(sys.argv[5])
identity_record = {
    "schema_version": 1,
    "project_id": project_id,
    "attempt_id": "subprocess-attempt",
    "state_revision": 3,
    "authority_revision_at_acquire": "authority-3",
    "durable_barrier_id": "barrier-subprocess",
    "fencing_token": "fence-subprocess",
    "fencing_owner": "owner-subprocess",
    "identity_digest": "0" * 64,
}
from tools.upgrade_identity import canonical_barrier_session_digest

identity_record["identity_digest"] = canonical_barrier_session_digest(identity_record)
identity = BarrierSessionIdentity.from_record(identity_record)
control = SQLiteRollbackControlStore(control_path, project_id, authority_path)
store = SQLiteBarrierSessionStore(control, lambda: "authority-3")

if mode == "probe-after-sidecar":
    from tools.handoffctl import locked

    with locked() as guard, store.lock_owned_by_caller(guard), control._connection() as connection:
        journal_mode = str(connection.execute("PRAGMA journal_mode").fetchone()[0]).lower()
        if journal_mode != "wal":
            raise SystemExit("WAL mode was not enabled")
        ready_path.write_text(journal_mode + "\n", encoding="utf-8")
        with ready_path.open("rb") as ready:
            os.fsync(ready.fileno())
    raise SystemExit(0)

store.create(identity)
if mode not in {
    "kill-after-ambiguous-replacement-commit",
    "kill-after-ambiguous-reconciliation-outcome-publication",
}:
    store.bind_child(1, BarrierChildIdentity.bind(identity, "subprocess-forward", "new"))

if mode == "kill-after-ambiguous-replacement-commit":
    store.mark_ambiguous(1, "seed-ambiguity")
    replacement_record = dict(identity_record)
    replacement_record.update(
        {
            "attempt_id": "subprocess-replacement",
            "state_revision": 4,
            "durable_barrier_id": "barrier-replacement",
            "fencing_token": "fence-replacement",
        }
    )
    replacement_record["identity_digest"] = canonical_barrier_session_digest(replacement_record)
    replacement = BarrierSessionState(
        BarrierSessionIdentity.from_record(replacement_record), "held", 1
    )
    original_mark_intent = store._mark_intent_locked

    def kill_before_reconciled(connection, intent_id, outcome, cause_code=None):
        ready_path.write_text("replacement-committed-before-outcome\n", encoding="utf-8")
        with ready_path.open("rb") as ready:
            os.fsync(ready.fileno())
        os.kill(os.getpid(), signal.SIGKILL)
        original_mark_intent(connection, intent_id, outcome, cause_code)

    store._mark_intent_locked = kill_before_reconciled
    store.reconcile_ambiguous(2, replacement)

if mode == "kill-after-ambiguous-reconciliation-outcome-publication":
    store.mark_ambiguous(1, "seed-ambiguity")
    replacement_record = dict(identity_record)
    replacement_record.update(
        {
            "attempt_id": "subprocess-replacement",
            "state_revision": 4,
            "durable_barrier_id": "barrier-replacement",
            "fencing_token": "fence-replacement",
        }
    )
    replacement_record["identity_digest"] = canonical_barrier_session_digest(replacement_record)
    replacement = BarrierSessionState(
        BarrierSessionIdentity.from_record(replacement_record), "held", 1
    )
    original_reconcile = store.reconcile_ambiguous

    def kill_after_reconciled(expected_revision, replacement):
        result = original_reconcile(expected_revision, replacement)
        ready_path.write_text("reconciliation-outcome-published\n", encoding="utf-8")
        with ready_path.open("rb") as ready:
            os.fsync(ready.fileno())
        os.kill(os.getpid(), signal.SIGKILL)
        return result

    store.reconcile_ambiguous = kill_after_reconciled
    store.reconcile_ambiguous(2, replacement)

if mode == "clean":
    with closing(sqlite3.connect(control_path)) as connection, connection:
        journal_mode = str(connection.execute("PRAGMA journal_mode").fetchone()[0]).lower()
    ready_path.write_text(journal_mode + "\n", encoding="utf-8")
    with ready_path.open("rb") as ready:
        os.fsync(ready.fileno())
    raise SystemExit(0)

if mode == "replace-active-wal-sidecars":
    from tools.handoffctl import locked

    replace_path = ready_path.with_suffix(".replace")
    with locked() as guard, store.lock_owned_by_caller(guard), control._connection() as connection:
        journal_mode = str(connection.execute("PRAGMA journal_mode").fetchone()[0]).lower()
        if journal_mode != "wal":
            raise SystemExit("WAL mode was not enabled")
        ready_path.write_text(journal_mode + "\n", encoding="utf-8")
        with ready_path.open("rb") as ready:
            os.fsync(ready.fileno())
        while not replace_path.exists():
            time.sleep(0.01)
        for suffix in ("-wal", "-shm"):
            sidecar = Path(f"{control_path}{suffix}")
            sidecar.unlink()
            sidecar.write_bytes(b"replaced-sidecar")
            sidecar.chmod(0o600)
        connection.execute("SELECT count(*) FROM barrier_session").fetchone()
    raise SystemExit(0)

if mode == "kill-during-caller-owned-recheck":
    from tools.handoffctl import locked

    with locked() as guard, store.lock_owned_by_caller(guard), control._connection() as connection:
        connection.execute("BEGIN IMMEDIATE")
        connection.execute(
            "UPDATE barrier_session SET status='releasing', revision=revision+1 WHERE project_id=?",
            (project_id,),
        )
        journal_mode = str(connection.execute("PRAGMA journal_mode").fetchone()[0]).lower()
        ready_path.write_text(journal_mode + "\n", encoding="utf-8")
        with ready_path.open("rb") as ready:
            os.fsync(ready.fileno())
        os.kill(os.getpid(), signal.SIGKILL)

if mode == "kill-after-session-commit":
    original_mark_intent = store._mark_intent_locked

    def kill_before_outcome(connection, intent_id, outcome, cause_code=None):
        ready_path.write_text("committed-before-outcome\n", encoding="utf-8")
        with ready_path.open("rb") as ready:
            os.fsync(ready.fileno())
        os.kill(os.getpid(), signal.SIGKILL)
        original_mark_intent(connection, intent_id, outcome, cause_code)

    store._mark_intent_locked = kill_before_outcome
    store.begin_reopen(2, "new", _reopen_evidence(store.snapshot(), "new"))

if mode == "kill-after-outcome-publication":
    original_begin_reopen = store.begin_reopen

    def kill_after_return(expected_revision, target, evidence):
        result = original_begin_reopen(expected_revision, target, evidence)
        ready_path.write_text("committed-after-outcome\n", encoding="utf-8")
        with ready_path.open("rb") as ready:
            os.fsync(ready.fileno())
        os.kill(os.getpid(), signal.SIGKILL)
        return result

    store.begin_reopen = kill_after_return
    store.begin_reopen(2, "new", _reopen_evidence(store.snapshot(), "new"))

if mode in {
    "kill-after-effect-committed-publication",
    "kill-after-effect-ambiguous-publication",
    "kill-after-integrated-effect-committed-finish",
    "kill-after-integrated-effect-ambiguous-finish",
}:
    operation_id = (
        "subprocess-integrated-effect"
        if mode.startswith("kill-after-integrated")
        else "subprocess-effect"
    )
    outcome = (
        "committed"
        if mode.endswith("committed-publication") or mode.endswith("committed-finish")
        else "ambiguous"
    )
    if mode.startswith("kill-after-integrated"):
        from tools.authority_mutation import DurableBoundAuthorityMutation
        from tools.authority_neutral_commit import CommitAdmissionBundle

        admission = CommitAdmissionBundle(
            backend="sqlite",
            target="new",
            operation_id=operation_id,
            fencing_token=identity.fencing_token,
            state_revision=2,
            barrier_id=identity.durable_barrier_id,
            artifact_identity="artifact-subprocess",
            manifest_identity="manifest-subprocess",
            selector_identity="selector-subprocess",
            runtime_identity="runtime-subprocess",
        )
        original_finish_effect = store.finish_authority_effect

        def kill_after_effect_return(intent, effect_outcome, receipt=None):
            result = original_finish_effect(intent, effect_outcome, receipt)
            ready_path.write_text(
                f"integrated-effect-{effect_outcome}-after-finish\n", encoding="utf-8"
            )
            with ready_path.open("rb") as ready:
                os.fsync(ready.fileno())
            os.kill(os.getpid(), signal.SIGKILL)
            return result

        store.finish_authority_effect = kill_after_effect_return
        capability = DurableBoundAuthorityMutation(admission, store, session_revision=2)

        def integrated_effect():
            if outcome == "ambiguous":
                raise TimeoutError("subprocess effect outcome is unknown")
            return {
                "backend": "sqlite",
                "target": "new",
                "operation_id": operation_id,
                "state_revision": 2,
                "barrier_id": identity.durable_barrier_id,
                "artifact_identity": "artifact-subprocess",
                "manifest_identity": "manifest-subprocess",
                "selector_identity": "selector-subprocess",
                "runtime_identity": "runtime-subprocess",
                "fencing_token": identity.fencing_token,
                "mutates_authority": True,
            }

        capability.execute(integrated_effect)
    else:
        effect = store.prepare_authority_effect(2, operation_id, "sqlite")
        original_finish_effect = store.finish_authority_effect

        def kill_after_effect_return(intent, effect_outcome, receipt=None):
            result = original_finish_effect(intent, effect_outcome, receipt)
            ready_path.write_text(
                f"effect-{effect_outcome}-after-outcome\n", encoding="utf-8"
            )
            with ready_path.open("rb") as ready:
                os.fsync(ready.fileno())
            os.kill(os.getpid(), signal.SIGKILL)
            return result

        store.finish_authority_effect = kill_after_effect_return
        store.finish_authority_effect(effect, outcome)

if mode != "kill-during-transaction":
    raise SystemExit("unknown test mode")

with control.operation_lock(), control._connection() as connection:
    connection.execute("BEGIN IMMEDIATE")
    connection.execute(
        "UPDATE barrier_session SET status='releasing', revision=revision+1 WHERE project_id=?",
        (project_id,),
    )
    journal_mode = str(connection.execute("PRAGMA journal_mode").fetchone()[0]).lower()
    ready_path.write_text(journal_mode + "\n", encoding="utf-8")
    with ready_path.open("rb") as ready:
        os.fsync(ready.fileno())
    os.kill(os.getpid(), signal.SIGKILL)
"""


# Two independent interpreters exercise the stale-writer boundary: one
# replaces a released session with a distinct newer fence, while the other
# attempts to commit using the old session identity and revision.
STALE_FENCE_SCRIPT = r"""
import sys
import time
from pathlib import Path

from tools.rollback_control_store import (
    BarrierSessionState,
    ControlStoreError,
    SQLiteBarrierSessionStore,
    SQLiteRollbackControlStore,
)
from tools.upgrade_identity import BarrierSessionIdentity, canonical_barrier_session_digest

control_path = Path(sys.argv[1])
authority_path = Path(sys.argv[2])
ready_path = Path(sys.argv[3])
role = sys.argv[4]
project_id = sys.argv[5]

def identity(attempt_id: str, revision: int, barrier_id: str, fence_value: str) -> BarrierSessionIdentity:
    record = {
        "schema_version": 1,
        "project_id": project_id,
        "attempt_id": attempt_id,
        "state_revision": revision,
        "authority_revision_at_acquire": "authority-3",
        "durable_barrier_id": barrier_id,
        "fencing_token": fence_value,
        "fencing_owner": "owner-1",
        "identity_digest": "0" * 64,
    }
    record["identity_digest"] = canonical_barrier_session_digest(record)
    return BarrierSessionIdentity.from_record(record)

store = SQLiteBarrierSessionStore(
    SQLiteRollbackControlStore(control_path, project_id, authority_path),
    lambda: "authority-3",
)

if role == "replace":
    current = store.snapshot()
    assert current is not None
    releasing = BarrierSessionState(current.identity, "releasing", current.revision + 1)
    store.cas(current.revision, releasing)
    store.cas(
        releasing.revision,
        BarrierSessionState(current.identity, "released", releasing.revision + 1),
    )
    newer = identity("attempt-2", 4, "barrier-2", "fence-2")
    store.cas(0, BarrierSessionState(newer, "held", 1))
    ready_path.write_text("replaced\n", encoding="utf-8")
    raise SystemExit(0)

if role != "stale":
    raise SystemExit("unknown role")
deadline = time.monotonic() + 10
while not ready_path.exists() and time.monotonic() < deadline:
    time.sleep(0.01)
if not ready_path.exists():
    raise SystemExit("replacement checkpoint timeout")
stale = identity("attempt-1", 3, "barrier-1", "fence-1")
try:
    store.cas(1, BarrierSessionState(stale, "releasing", 2))
except ControlStoreError as error:
    if "identity changed" not in str(error):
        raise
    raise SystemExit(0)
raise SystemExit("stale writer was accepted")
"""
