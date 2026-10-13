# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Focused compatibility and safety coverage for concise task titles."""

import argparse
import unittest

import test_handoffctl


class ConciseTitleTest(unittest.TestCase):
    """Reuse the isolated handoffctl fixture without growing its capped source file."""

    def setUp(self) -> None:
        self.fixture = test_handoffctl.HandoffTest(
            "test_project_profile_is_strict_and_controls_optional_status"
        )
        self.fixture.setUp()
        self.addCleanup(self.fixture.tearDown)

    def test_atomic_task_round_trip_and_render(self) -> None:
        path = self.fixture.make_task(short_title="Test navigation label")
        meta, body = test_handoffctl.CORE.read_task(path)
        self.assertEqual("AR-0001", meta["id"])
        self.assertEqual("# Test\n", body)
        current = test_handoffctl.CORE.render_current(test_handoffctl.CORE.all_tasks())
        self.assertIn("## Open", current)
        self.assertIn("[AR-0001 — Test navigation label]", current)
        status = test_handoffctl.CORE.render_status_view(test_handoffctl.CORE.all_tasks())
        self.assertIn("flowchart LR", status)
        self.assertIn("**1 ARs tracked**", status)

    def test_short_title_is_optional_but_strict_when_present(self) -> None:
        path = self.fixture.make_task(short_title="One two three four")
        self.assertEqual(
            [],
            test_handoffctl.CORE.basic_task_errors(path, test_handoffctl.CORE.read_task(path)[0]),
        )
        meta, body = test_handoffctl.CORE.read_task(path)
        meta["short_title"] = "x" * 120
        test_handoffctl.CORE.write_task(path, meta, body)
        self.assertEqual(
            [],
            test_handoffctl.CORE.basic_task_errors(path, test_handoffctl.CORE.read_task(path)[0]),
        )
        meta["short_title"] = "x" * 121
        test_handoffctl.CORE.write_task(path, meta, body)
        self.assertIn(
            "short_title exceeds 120 characters", "\n".join(test_handoffctl.CORE.validate())
        )
        meta["short_title"] = "one two three four five"
        test_handoffctl.CORE.write_task(path, meta, body)
        self.assertIn("short_title exceeds four words", "\n".join(test_handoffctl.CORE.validate()))
        meta["short_title"] = "bad\nlabel"
        test_handoffctl.CORE.write_task(path, meta, body)
        self.assertIn("invalid short_title", "\n".join(test_handoffctl.CORE.validate()))

    def test_short_title_is_escaped_in_current_view(self) -> None:
        self.fixture.make_task(short_title="Bad ](https://example.invalid)")

        current = test_handoffctl.CORE.render_current(test_handoffctl.CORE.all_tasks())

        self.assertIn("Bad \\]\\(https://example.invalid\\)", current)
        self.assertNotIn("[AR-0001 — Bad ](https://example.invalid)]", current)

    def test_rollback_removes_short_title_missing_from_checkpoint(self) -> None:
        path = self.fixture.make_task(short_title="Later added title")
        meta, _ = test_handoffctl.CORE.read_task(path)
        checkpoint_state = dict(meta)
        checkpoint_state.pop("short_title")

        test_handoffctl.CORE.apply_rollback(
            argparse.Namespace(
                rollback_checkpoint={
                    "name": "AR-0001-r0001",
                    "source_commit": "a" * 40,
                    "state": checkpoint_state,
                }
            ),
            meta,
        )

        self.assertNotIn("short_title", meta)
