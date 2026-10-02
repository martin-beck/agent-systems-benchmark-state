# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Hostile tests for the backend-neutral authority effect contract."""

from __future__ import annotations

import unittest

from tools.authority_mutation import (
    AuthorityMutationAmbiguousError,
    AuthorityMutationError,
    AuthorityMutationRejectedError,
    BoundAuthorityMutation,
    DurableBoundAuthorityMutation,
    DurableBoundBackendMutation,
)
from tools.authority_neutral_commit import CommitAdmissionBundle
from tools.git_authority_mutation import GitCommitResult, GitMutationAmbiguousError
from tools.rollback_control_store import ControlStoreAmbiguousError, ControlStoreError
from tools.sqlite_authority_mutation import SQLiteMutationAmbiguousError


def _admission(backend: str = "git") -> CommitAdmissionBundle:
    return CommitAdmissionBundle(
        backend=backend,
        target="new",
        operation_id="op-1:commit",
        fencing_token="fence-1",  # noqa: S106
        state_revision=1,
        barrier_id="barrier-1",
        artifact_identity="artifact-1",
        manifest_identity="manifest-1",
        selector_identity="selector-1",
        runtime_identity="runtime-1",
    )


class AuthorityMutationTests(unittest.TestCase):
    @staticmethod
    def _result(backend: str = "git") -> dict[str, object]:
        return {
            "backend": backend,
            "target": "new",
            "operation_id": "op-1:commit",
            "state_revision": 1,
            "barrier_id": "barrier-1",
            "artifact_identity": "artifact-1",
            "manifest_identity": "manifest-1",
            "selector_identity": "selector-1",
            "runtime_identity": "runtime-1",
            "fencing_token": "fence-1",
            "mutates_authority": True,
        }

    def test_effect_is_single_use_and_identity_bound(self) -> None:
        capability = BoundAuthorityMutation(_admission())
        receipt = capability.execute(
            "git",
            lambda: GitCommitResult(
                backend="git",
                target="new",
                operation_id="op-1:commit",
                state_revision=1,
                barrier_id="barrier-1",
                artifact_identity="artifact-1",
                manifest_identity="manifest-1",
                selector_identity="selector-1",
                runtime_identity="runtime-1",
                before_head="a" * 40,
                after_head="b" * 40,
                branch="main",
                fencing_token="fence-1",  # noqa: S106
            ),
        )
        self.assertEqual("git", receipt.backend)
        with self.assertRaisesRegex(AuthorityMutationError, "already consumed"):
            capability.execute("git", self._result)

    def test_rejects_backend_or_result_identity_drift(self) -> None:
        with self.assertRaisesRegex(AuthorityMutationError, "backend identity"):
            BoundAuthorityMutation(_admission()).execute("sqlite", self._result)
        with self.assertRaisesRegex(AuthorityMutationAmbiguousError, "result identity"):
            BoundAuthorityMutation(_admission()).execute(
                "git", lambda: {**self._result(), "fencing_token": "foreign"}
            )

    def test_rejects_any_full_receipt_identity_drift(self) -> None:
        changes: dict[str, object] = {
            "backend": "sqlite",
            "target": "rollback",
            "operation_id": "foreign-operation",
            "state_revision": 2,
            "barrier_id": "foreign-barrier",
            "artifact_identity": "foreign-artifact",
            "manifest_identity": "foreign-manifest",
            "selector_identity": "foreign-selector",
            "runtime_identity": "foreign-runtime",
            "fencing_token": "foreign-fence",
        }
        for field, value in changes.items():

            def drifted_result(
                field_name: str = field, field_value: object = value
            ) -> dict[str, object]:
                result = self._result()
                result[field_name] = field_value
                return result

            with (
                self.subTest(field=field),
                self.assertRaisesRegex(
                    AuthorityMutationAmbiguousError,
                    "result identity mismatch; recovery is required",
                ),
            ):
                BoundAuthorityMutation(_admission()).execute("git", drifted_result)

    def test_rejects_noncallable_effect_before_consuming_capability(self) -> None:
        capability = BoundAuthorityMutation(_admission())
        with self.assertRaisesRegex(AuthorityMutationError, "effect is invalid"):
            capability.execute("git", None)  # type: ignore[arg-type]
        capability.execute("git", self._result)

    def test_durable_rejects_noncallable_effect_before_journaling(self) -> None:
        journal_calls: list[str] = []

        class Journal:
            def prepare_authority_effect(self, *_args: object, **_kwargs: object) -> str:
                journal_calls.append("prepare")
                return "intent"

            def finish_authority_effect(
                self, _intent: object, _outcome: str, _receipt: object | None = None
            ) -> None:
                journal_calls.append("finish")

        capability = DurableBoundAuthorityMutation(_admission(), Journal(), session_revision=1)
        with self.assertRaisesRegex(AuthorityMutationError, "effect is invalid"):
            capability.execute(None)  # type: ignore[arg-type]
        self.assertEqual([], journal_calls)
        capability.execute(lambda: self._result())

    def test_durable_backend_wrapper_journals_backend_receipt(self) -> None:
        journal: list[tuple[str, object | None]] = []

        class Journal:
            def prepare_authority_effect(self, *_args: object, **_kwargs: object) -> str:
                journal.append(("prepared", None))
                return "intent"

            def finish_authority_effect(
                self, _intent: object, outcome: str, receipt: object | None = None
            ) -> None:
                journal.append((outcome, receipt))

        wrapper = DurableBoundBackendMutation(
            _admission(),
            Journal(),
            session_revision=1,
            backend_effect=lambda message: {
                **self._result(),
                "operation_id": f"op-1:{message}",
            },
        )
        receipt = wrapper.execute("commit")
        self.assertTrue(receipt.mutates_authority)
        self.assertEqual("prepared", journal[0][0])
        self.assertEqual("committed", journal[1][0])

    def test_durable_capability_rejects_invalid_session_revision(self) -> None:
        with self.assertRaisesRegex(AuthorityMutationError, "session revision is invalid"):
            DurableBoundAuthorityMutation(_admission(), object(), session_revision=0)  # type: ignore[arg-type]

    def test_durable_capability_rejects_admission_session_revision_mismatch(self) -> None:
        with self.assertRaisesRegex(AuthorityMutationError, "revision mismatch"):
            DurableBoundAuthorityMutation(_admission(), object(), session_revision=2)  # type: ignore[arg-type]

    def test_ambiguous_effect_consumes_token_and_cannot_retry(self) -> None:
        capability = BoundAuthorityMutation(_admission("sqlite"))

        def ambiguous() -> object:
            raise TimeoutError("commit timeout")

        with self.assertRaises(AuthorityMutationAmbiguousError):
            capability.execute("sqlite", ambiguous)
        with self.assertRaisesRegex(AuthorityMutationError, "already consumed"):
            capability.execute("sqlite", self._result)

    def test_backend_ambiguity_is_normalized_and_cannot_retry(self) -> None:
        for backend, error in (
            ("git", GitMutationAmbiguousError("git uncertain")),
            ("sqlite", SQLiteMutationAmbiguousError("sqlite uncertain")),
        ):
            capability = BoundAuthorityMutation(_admission(backend))

            def ambiguous(error: Exception = error) -> object:
                raise error

            with self.assertRaisesRegex(AuthorityMutationAmbiguousError, "outcome is ambiguous"):
                capability.execute(backend, ambiguous)
            with self.assertRaisesRegex(AuthorityMutationError, "already consumed"):
                capability.execute(backend, self._result)

    def test_termination_exception_is_ambiguous_and_cannot_retry(self) -> None:
        capability = BoundAuthorityMutation(_admission())

        def terminated() -> object:
            raise SystemExit(17)

        with self.assertRaisesRegex(AuthorityMutationAmbiguousError, "outcome is ambiguous"):
            capability.execute("git", terminated)
        with self.assertRaisesRegex(AuthorityMutationError, "already consumed"):
            capability.execute("git", self._result)

    def test_termination_during_result_identity_read_is_ambiguous_and_consumes_token(self) -> None:
        class TerminatingReceipt:
            def __getattr__(self, _name: str) -> object:
                raise KeyboardInterrupt("injected termination")

        capability = BoundAuthorityMutation(_admission())
        with self.assertRaisesRegex(AuthorityMutationAmbiguousError, "result identity mismatch"):
            capability.execute("git", lambda: TerminatingReceipt())
        with self.assertRaisesRegex(AuthorityMutationError, "already consumed"):
            capability.execute("git", self._result)

    def test_durable_effect_publishes_only_after_verified_receipt(self) -> None:
        journal: list[tuple[str, str, object | None]] = []

        class Journal:
            def prepare_authority_effect(
                self,
                expected_revision: int,
                operation_id: str,
                _backend: str,
                _target: str,
                *,
                expected_fencing_token: str | None = None,
                expected_barrier_id: str | None = None,
                expected_artifact_identity: str | None = None,
                expected_manifest_identity: str | None = None,
                expected_selector_identity: str | None = None,
                expected_runtime_identity: str | None = None,
            ) -> str:
                del (
                    expected_fencing_token,
                    expected_barrier_id,
                    expected_artifact_identity,
                    expected_manifest_identity,
                    expected_selector_identity,
                    expected_runtime_identity,
                )
                self.expected_revision = expected_revision
                journal.append(("prepared", operation_id, None))
                return "intent-1"

            def finish_authority_effect(
                self, intent: object, outcome: str, receipt: object | None = None
            ) -> None:
                self.intent = intent
                journal.append((outcome, str(intent), receipt))

        receipt = DurableBoundAuthorityMutation(
            _admission(), Journal(), session_revision=1
        ).execute(lambda: self._result())
        self.assertTrue(receipt.mutates_authority)
        self.assertEqual("prepared", journal[0][0])
        self.assertEqual("committed", journal[1][0])
        self.assertEqual("intent-1", journal[1][1])
        self.assertEqual(receipt, journal[1][2])

    def test_durable_identity_rejection_is_journaled_ambiguous_without_publication(self) -> None:
        journal: list[tuple[str, object | None]] = []

        class Journal:
            def prepare_authority_effect(
                self,
                _expected_revision: int,
                _operation_id: str,
                _backend: str,
                _target: str,
                *,
                expected_fencing_token: str | None = None,
                expected_barrier_id: str | None = None,
                expected_artifact_identity: str | None = None,
                expected_manifest_identity: str | None = None,
                expected_selector_identity: str | None = None,
                expected_runtime_identity: str | None = None,
            ) -> str:
                del (
                    expected_fencing_token,
                    expected_barrier_id,
                    expected_artifact_identity,
                    expected_manifest_identity,
                    expected_selector_identity,
                    expected_runtime_identity,
                )
                journal.append(("prepared", None))
                return "intent-rejected"

            def finish_authority_effect(
                self, _intent: object, outcome: str, receipt: object | None = None
            ) -> None:
                journal.append((outcome, receipt))

        with self.assertRaisesRegex(
            AuthorityMutationAmbiguousError, "result identity mismatch; recovery is required"
        ):
            DurableBoundAuthorityMutation(_admission(), Journal(), session_revision=1).execute(
                lambda: {**self._result(), "fencing_token": "foreign"}
            )
        self.assertEqual([("prepared", None), ("ambiguous", None)], journal)

    def test_durable_pre_effect_rejection_is_journaled_without_fencing_session(self) -> None:
        journal: list[tuple[str, object | None]] = []

        class Journal:
            def prepare_authority_effect(
                self,
                _expected_revision: int,
                _operation_id: str,
                _backend: str,
                _target: str,
                *,
                expected_fencing_token: str | None = None,
                expected_barrier_id: str | None = None,
                expected_artifact_identity: str | None = None,
                expected_manifest_identity: str | None = None,
                expected_selector_identity: str | None = None,
                expected_runtime_identity: str | None = None,
            ) -> str:
                del (
                    expected_fencing_token,
                    expected_barrier_id,
                    expected_artifact_identity,
                    expected_manifest_identity,
                    expected_selector_identity,
                    expected_runtime_identity,
                )
                journal.append(("prepared", None))
                return "intent-rejected-before-effect"

            def finish_authority_effect(
                self, _intent: object, outcome: str, receipt: object | None = None
            ) -> None:
                journal.append((outcome, receipt))

        with self.assertRaisesRegex(AuthorityMutationRejectedError, "admission rejected"):
            DurableBoundAuthorityMutation(_admission(), Journal(), session_revision=1).execute(
                lambda: (_ for _ in ()).throw(AuthorityMutationRejectedError("admission rejected"))
            )
        self.assertEqual([("prepared", None), ("rejected", None)], journal)

    def test_durable_effect_forwards_exact_admission_identity_to_journal(self) -> None:
        captured: list[object] = []

        class Journal:
            def prepare_authority_effect(
                self,
                expected_revision: int,
                operation_id: str,
                backend: str,
                target: str,
                *,
                expected_fencing_token: str | None = None,
                expected_barrier_id: str | None = None,
                expected_artifact_identity: str | None = None,
                expected_manifest_identity: str | None = None,
                expected_selector_identity: str | None = None,
                expected_runtime_identity: str | None = None,
            ) -> str:
                captured.extend(
                    [
                        expected_revision,
                        operation_id,
                        backend,
                        target,
                        expected_fencing_token,
                        expected_barrier_id,
                        expected_artifact_identity,
                        expected_manifest_identity,
                        expected_selector_identity,
                        expected_runtime_identity,
                    ]
                )
                return "intent-identity"

            def finish_authority_effect(
                self, _intent: object, _outcome: str, _receipt: object | None = None
            ) -> None:
                return None

        DurableBoundAuthorityMutation(_admission("sqlite"), Journal(), session_revision=1).execute(
            lambda: self._result("sqlite")
        )
        self.assertEqual(
            [
                1,
                "op-1:commit",
                "sqlite",
                "new",
                "fence-1",
                "barrier-1",
                "artifact-1",
                "manifest-1",
                "selector-1",
                "runtime-1",
            ],
            captured,
        )

    def test_durable_ambiguous_effect_is_durably_marked_ambiguous(self) -> None:
        journal: list[str] = []

        class Journal:
            def prepare_authority_effect(
                self,
                _expected_revision: int,
                _operation_id: str,
                _backend: str,
                _target: str,
                *,
                expected_fencing_token: str | None = None,
                expected_barrier_id: str | None = None,
                expected_artifact_identity: str | None = None,
                expected_manifest_identity: str | None = None,
                expected_selector_identity: str | None = None,
                expected_runtime_identity: str | None = None,
            ) -> str:
                del (
                    expected_fencing_token,
                    expected_barrier_id,
                    expected_artifact_identity,
                    expected_manifest_identity,
                    expected_selector_identity,
                    expected_runtime_identity,
                )
                return "intent-uncertain"

            def finish_authority_effect(
                self, intent: object, outcome: str, _receipt: object | None = None
            ) -> None:
                journal.append(f"{intent}:{outcome}")

        capability = DurableBoundAuthorityMutation(_admission(), Journal(), session_revision=1)
        with self.assertRaisesRegex(AuthorityMutationAmbiguousError, "outcome is ambiguous"):
            capability.execute(lambda: (_ for _ in ()).throw(TimeoutError("unknown")))
        self.assertEqual(["intent-uncertain:ambiguous"], journal)

    def test_durable_capability_fails_closed_if_ambiguity_cannot_be_journaled(self) -> None:
        class Journal:
            def prepare_authority_effect(
                self,
                _revision: int,
                _operation: str,
                _backend: str,
                _target: str,
                *,
                expected_fencing_token: str | None = None,
                expected_barrier_id: str | None = None,
                expected_artifact_identity: str | None = None,
                expected_manifest_identity: str | None = None,
                expected_selector_identity: str | None = None,
                expected_runtime_identity: str | None = None,
            ) -> str:
                del (
                    expected_fencing_token,
                    expected_barrier_id,
                    expected_artifact_identity,
                    expected_manifest_identity,
                    expected_selector_identity,
                    expected_runtime_identity,
                )
                return "intent-journal-failure"

            def finish_authority_effect(
                self, _intent: object, _outcome: str, _receipt: object | None = None
            ) -> None:
                raise OSError("journal unavailable")

        with self.assertRaisesRegex(AuthorityMutationAmbiguousError, "recovery journal"):
            DurableBoundAuthorityMutation(_admission(), Journal(), session_revision=1).execute(
                lambda: (_ for _ in ()).throw(TimeoutError("unknown"))
            )

    def test_durable_capability_fails_closed_if_journal_prepare_is_ambiguous(self) -> None:
        class Journal:
            def prepare_authority_effect(self, *_args: object, **_kwargs: object) -> str:
                raise OSError("journal prepare uncertain")

            def finish_authority_effect(
                self, _intent: object, _outcome: str, _receipt: object | None = None
            ) -> None:
                return None

        effect_called = False

        def effect() -> dict[str, object]:
            nonlocal effect_called
            effect_called = True
            return self._result()

        with self.assertRaisesRegex(
            AuthorityMutationAmbiguousError, "journal preparation is ambiguous"
        ):
            DurableBoundAuthorityMutation(_admission(), Journal(), session_revision=1).execute(
                effect
            )
        self.assertFalse(effect_called)

    def test_durable_capability_classifies_termination_during_journal_prepare_as_ambiguous(
        self,
    ) -> None:
        class Journal:
            def prepare_authority_effect(self, *_args: object, **_kwargs: object) -> str:
                raise KeyboardInterrupt("injected termination")

            def finish_authority_effect(
                self, _intent: object, _outcome: str, _receipt: object | None = None
            ) -> None:
                raise AssertionError("termination during prepare has no safe intent handle")

        effect_called = False

        def effect() -> dict[str, object]:
            nonlocal effect_called
            effect_called = True
            return self._result()

        with self.assertRaisesRegex(
            AuthorityMutationAmbiguousError, "journal preparation is ambiguous"
        ):
            DurableBoundAuthorityMutation(_admission(), Journal(), session_revision=1).execute(
                effect
            )
        self.assertFalse(effect_called)

    def test_durable_capability_fails_closed_if_journal_prepare_returns_no_intent(self) -> None:
        class Journal:
            def prepare_authority_effect(self, *_args: object, **_kwargs: object) -> None:
                return None

            def finish_authority_effect(
                self, _intent: object, _outcome: str, _receipt: object | None = None
            ) -> None:
                return None

        effect_called = False

        def effect() -> dict[str, object]:
            nonlocal effect_called
            effect_called = True
            return self._result()

        with self.assertRaisesRegex(
            AuthorityMutationAmbiguousError, "journal preparation returned no intent"
        ):
            DurableBoundAuthorityMutation(_admission(), Journal(), session_revision=1).execute(
                effect
            )
        self.assertFalse(effect_called)

    def test_durable_capability_preserves_control_store_admission_rejection(self) -> None:
        class Journal:
            def prepare_authority_effect(self, *_args: object, **_kwargs: object) -> None:
                raise ControlStoreError("barrier session revision conflict")

            def finish_authority_effect(
                self, _intent: object, _outcome: str, _receipt: object | None = None
            ) -> None:
                raise AssertionError("a rejected preparation must not be finished")

        with self.assertRaisesRegex(ControlStoreError, "revision conflict"):
            DurableBoundAuthorityMutation(_admission(), Journal(), session_revision=1).execute(
                lambda: self._result()
            )

    def test_durable_capability_fences_control_store_boundary_ambiguity(self) -> None:
        class Journal:
            def prepare_authority_effect(self, *_args: object, **_kwargs: object) -> None:
                raise ControlStoreAmbiguousError("sidecar identity changed")

            def finish_authority_effect(
                self, _intent: object, _outcome: str, _receipt: object | None = None
            ) -> None:
                raise AssertionError("an ambiguous preparation has no safe intent handle")

        with self.assertRaisesRegex(
            AuthorityMutationAmbiguousError, "journal preparation is ambiguous"
        ):
            DurableBoundAuthorityMutation(_admission(), Journal(), session_revision=1).execute(
                lambda: self._result()
            )

    def test_durable_capability_fails_closed_if_success_publication_is_uncertain(self) -> None:
        class Journal:
            def prepare_authority_effect(
                self,
                _revision: int,
                _operation: str,
                _backend: str,
                _target: str,
                *,
                expected_fencing_token: str | None = None,
                expected_barrier_id: str | None = None,
                expected_artifact_identity: str | None = None,
                expected_manifest_identity: str | None = None,
                expected_selector_identity: str | None = None,
                expected_runtime_identity: str | None = None,
            ) -> str:
                del (
                    expected_fencing_token,
                    expected_barrier_id,
                    expected_artifact_identity,
                    expected_manifest_identity,
                    expected_selector_identity,
                    expected_runtime_identity,
                )
                return "intent-publication-failure"

            def finish_authority_effect(
                self, _intent: object, outcome: str, _receipt: object | None = None
            ) -> None:
                if outcome == "committed":
                    raise OSError("publication unavailable")

        with self.assertRaisesRegex(AuthorityMutationAmbiguousError, "publication"):
            DurableBoundAuthorityMutation(_admission(), Journal(), session_revision=1).execute(
                lambda: self._result()
            )


if __name__ == "__main__":
    unittest.main()
