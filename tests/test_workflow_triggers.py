# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Regression tests for exact coordination-content workflow routing."""

from __future__ import annotations

import fnmatch
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "verify.yml"
FORMAL_WORKFLOW = ROOT / ".github" / "workflows" / "handoffctl-formal.yml"
SOURCE_HEADERS_WORKFLOW = ROOT / ".github" / "workflows" / "source-headers.yml"
AWQ_SHADOW_WORKFLOW = ROOT / ".github" / "workflows" / "awq-shadow.yml"
PUSH_WORKFLOWS = (WORKFLOW, FORMAL_WORKFLOW, SOURCE_HEADERS_WORKFLOW)
REQUIRED_COORDINATION_PATHS = frozenset({"CURRENT.md", "STATUS.md", "plans/**", "tasks/**"})


def event_paths(event: str) -> tuple[str, ...]:
    """Read one event's path list from the deliberately simple workflow shape."""
    lines = WORKFLOW.read_text(encoding="utf-8").splitlines()
    event_marker = f"  {event}:"
    try:
        event_start = lines.index(event_marker)
        paths_start = lines.index("    paths:", event_start + 1)
    except ValueError as error:
        raise AssertionError(f"missing {event} paths") from error
    paths: list[str] = []
    for line in lines[paths_start + 1 :]:
        if line.startswith("  ") and not line.startswith("      "):
            break
        if line.startswith("      - "):
            paths.append(json.loads(line.removeprefix("      - ")))
    if not paths:
        raise AssertionError(f"empty {event} paths")
    return tuple(paths)


def triggers(paths: tuple[str, ...], changed: tuple[str, ...]) -> bool:
    """Model GitHub's positive path-filter decision for bounded fixtures."""
    return any(fnmatch.fnmatchcase(path, pattern) for path in changed for pattern in paths)


class WorkflowTriggerTests(unittest.TestCase):
    def test_main_pushes_queue_while_pull_requests_may_cancel(self) -> None:
        expected = "  cancel-in-progress: ${{ github.event_name != 'push' }}"
        for path in PUSH_WORKFLOWS:
            with self.subTest(workflow=path.name):
                workflow = path.read_text(encoding="utf-8")
                self.assertIn("  push:", workflow)
                self.assertIn("  pull_request:", workflow)
                self.assertEqual(1, workflow.count(expected))
                self.assertNotIn("  cancel-in-progress: true", workflow)

        awq_shadow = AWQ_SHADOW_WORKFLOW.read_text(encoding="utf-8")
        self.assertNotIn("  push:", awq_shadow)
        self.assertIn("  pull_request:", awq_shadow)
        self.assertEqual(1, awq_shadow.count("  cancel-in-progress: true"))

    def test_formal_admission_paths_are_scoped_to_the_private_run_root(self) -> None:
        workflow = FORMAL_WORKFLOW.read_text(encoding="utf-8")
        root = "/srv/data/projects/.asb-tlc/ci-${{ github.run_id }}"
        self.assertIn(f"TLC_RUNTIME_ROOT: {root}", workflow)
        workflow_env, formal_step = workflow.split(
            "      - name: Check exhaustive concurrent-state model", maxsplit=1
        )
        self.assertNotIn("TLC_ADMISSION_QUEUE:", workflow_env)
        self.assertNotIn("TLC_ADMISSION_LOCK:", workflow_env)
        self.assertIn(f"TLC_ADMISSION_QUEUE: {root}/queue", formal_step)
        self.assertIn(f"TLC_ADMISSION_LOCK: {root}/admission.lock", formal_step)

    def test_pull_requests_cover_every_coordination_projection(self) -> None:
        paths = event_paths("pull_request")
        self.assertTrue(REQUIRED_COORDINATION_PATHS.issubset(paths))
        for changed in (
            ("tasks/AR-0001.md",),
            ("plans/AR-0001.md",),
            ("CURRENT.md",),
            ("STATUS.md",),
            ("docs/unrelated.md", "tasks/AR-0001.md"),
            ("tasks/deleted.md",),
            ("plans/old-name.md", "plans/new-name.md"),
        ):
            with self.subTest(changed=changed):
                self.assertTrue(triggers(paths, changed))
        self.assertFalse(triggers(paths, ("docs/unrelated.md",)))

    def test_push_and_checker_changes_remain_verified(self) -> None:
        for event in ("push", "pull_request"):
            with self.subTest(event=event):
                paths = event_paths(event)
                self.assertTrue(REQUIRED_COORDINATION_PATHS.issubset(paths))
                self.assertIn("tests/test_workflow_triggers.py", paths)

    def test_pull_request_uses_exact_head_and_complete_dco_range(self) -> None:
        workflow = WORKFLOW.read_text(encoding="utf-8")
        self.assertIn("fetch-depth: 0", workflow)
        self.assertIn("github.event.pull_request.head.sha", workflow)
        self.assertIn('revision_range="$PR_BASE_SHA..$PR_HEAD_SHA"', workflow)
        self.assertIn('git rev-list "$revision_range"', workflow)


if __name__ == "__main__":
    unittest.main()
