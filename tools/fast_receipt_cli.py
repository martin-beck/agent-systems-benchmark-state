# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Opt-in Git receipt commands; queue admission is not authority completion."""

from __future__ import annotations

import json
from argparse import Namespace
from typing import Any

from .fast_observation import ObservationCache
from .fast_receipt_socket import public_receipt
from .fast_receipt_worker import (
    process_pending,
    publication_lock,
    publish_pending,
    serve_local,
    serve_publication,
)
from .fast_receipts import ReceiptStore


def dispatch_fast(core: Any, args: Namespace) -> int:  # noqa: C901 - explicit receipt dispatch
    """Access one bound per-project queue without changing strict CLI semantics."""
    core.assert_project_binding()
    if core.backend_selection()["backend"] != "git":
        raise RuntimeError("fast receipts require Git authority")
    if args.fast_action == "observe":
        # Without the resident socket there is no cross-process cache.  This
        # remains an explicit alternate observation contract, but the direct
        # fallback always performs a fresh bounded scan.
        try:
            observed = ObservationCache().observe(core, args.max_age_seconds)
        except ValueError as error:
            raise RuntimeError(str(error)) from error
        print(json.dumps(observed, sort_keys=True))
        return 0
    path = core.coordinator_lock_path().parent / "fast-receipts.sqlite3"
    with ReceiptStore(path, core.project_binding()["project_id"]) as store:
        if args.fast_action == "heartbeat":
            receipt = store.enqueue_heartbeat(
                key=args.key,
                task=args.task,
                owner=args.owner,
                expected_revision=args.expected_revision,
                lease_minutes=args.lease_minutes,
            )
            print(json.dumps(public_receipt(receipt), sort_keys=True))
            return 0
        if args.fast_action == "claim":
            receipt = store.enqueue_claim(
                key=args.key,
                task=args.task,
                owner=args.owner,
                expected_revision=args.expected_revision,
                lease_minutes=args.lease_minutes,
                worker_pid=getattr(args, "worker_pid", None),
                worker_start_time=getattr(args, "worker_start_time", None),
            )
            print(json.dumps(public_receipt(receipt), sort_keys=True))
            return 0
        if args.fast_action == "promote":
            receipt = store.enqueue_promote(
                key=args.key,
                task=args.task,
                expected_revision=args.expected_revision,
                note=args.note,
            )
            print(json.dumps(public_receipt(receipt), sort_keys=True))
            return 0
        if args.fast_action == "update":
            changes = {
                name: value
                for name in ("status", "priority", "summary", "next_action")
                if (value := getattr(args, name)) is not None
            }
            receipt = store.enqueue_update(
                key=args.key,
                task=args.task,
                owner=args.owner,
                expected_revision=args.expected_revision,
                changes=changes,
                note=args.note,
            )
            print(json.dumps(public_receipt(receipt), sort_keys=True))
            return 0
        if args.fast_action == "receipt":
            found = store.read(args.receipt_id)
            if found is None:
                raise RuntimeError("unknown fast receipt")
            print(json.dumps(public_receipt(found), sort_keys=True))
            return 0
        if args.fast_action == "worker":
            if args.serve:
                serve_local(core, store, limit=args.limit, poll_seconds=args.poll_seconds)
                return 0
            local = process_pending(core, store, limit=args.limit)
            with publication_lock(core):
                remote = publish_pending(core, store)
            print(
                json.dumps(
                    {
                        "local": [public_receipt(item) for item in local],
                        "remote": [public_receipt(item) for item in remote],
                    },
                    sort_keys=True,
                )
            )
            return 0
        if args.fast_action == "publisher":
            if args.serve:
                serve_publication(core, store, poll_seconds=args.poll_seconds)
                return 0
            with publication_lock(core):
                remote = publish_pending(core, store)
            print(
                json.dumps(
                    {"remote": [public_receipt(item) for item in remote]},
                    sort_keys=True,
                )
            )
            return 0
    raise RuntimeError("unknown fast receipt action")
