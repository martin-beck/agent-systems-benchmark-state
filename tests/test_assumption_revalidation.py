# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Negative-path coverage for explicit task assumption revalidation."""

from __future__ import annotations

import argparse
import shlex
import subprocess
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from tools import assumption_revalidation, change_drift, handoffctl

REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
EXPECTED_COMPLEXITY_COMMAND = [
    "uv",
    "run",
    "lizard",
    "-l",
    "python",
    "--CCN",
    "14",
    "tools/handoffctl.py",
    "tools/assumption_revalidation.py",
    "tools/retry_circuit.py",
]


def git(root: Path, *arguments: str) -> None:
    subprocess.run(  # noqa: S603
        ["/usr/bin/git", "-C", str(root), *arguments],
        check=True,
        capture_output=True,
    )


class AssumptionRevalidationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = TemporaryDirectory()
        self.root = Path(self.temp.name) / "state"
        self.root.mkdir()
        self.projects = Path(self.temp.name) / "projects"
        self.projects.mkdir()
        self.worktree = self.projects / "worker"
        self.worktree.mkdir()
        git(self.worktree, "init")
        git(self.worktree, "config", "user.email", "test@example.invalid")
        git(self.worktree, "config", "user.name", "Test")
        (self.worktree / "source.txt").write_text("initial\n", encoding="utf-8")
        git(self.worktree, "add", ".")
        git(self.worktree, "commit", "-m", "initial")
        (self.root / "observation.txt").write_text("one\n", encoding="utf-8")
        self.meta: dict[str, object] = {
            "id": "AR-0001",
            "owner": "worker",
            "status": "in_progress",
            "task_revision": 2,
            "worktree_key": "worker",
        }
        self.tasks: list[dict[str, object]] = [
            self.meta,
            {"id": "AR-0002", "task_revision": 7, "status": "done"},
        ]

    def tearDown(self) -> None:
        self.temp.cleanup()

    def args(self, action: str, assumption_id: str, **values: object) -> argparse.Namespace:
        return argparse.Namespace(
            task="AR-0001",
            owner="worker",
            expected_revision=values.get("expected_revision", self.meta["task_revision"]),
            assumption_action=action,
            assumption_id=assumption_id,
            kind=values.get("kind"),
            reference=values.get("reference"),
            material=values.get("material"),
            reason=values.get("reason", ""),
        )

    def apply(self, args: argparse.Namespace) -> str:
        return assumption_revalidation.apply(self.root, self.projects, args, self.meta, self.tasks)

    def test_moved_base_requires_explicit_revalidation_before_done(self) -> None:
        self.apply(self.args("declare", "base", kind="base", material=True))
        git(self.worktree, "commit", "--allow-empty", "-m", "moved base")
        self.assertEqual(
            "ASSUMPTION_REVALIDATION_REQUIRED: base (base)",
            assumption_revalidation.admission_error(
                self.root, self.projects, self.meta, self.tasks
            ),
        )
        self.meta["task_revision"] = 3
        self.apply(self.args("revalidate", "base"))
        self.assertIsNone(
            assumption_revalidation.admission_error(self.root, self.projects, self.meta, self.tasks)
        )

    def test_dependency_revision_race_requires_revalidation_but_nonmaterial_does_not_block(
        self,
    ) -> None:
        self.apply(
            self.args(
                "declare", "dependency", kind="dependency", reference="AR-0002", material=True
            )
        )
        self.tasks[1]["task_revision"] = 8
        self.assertIn(
            "dependency (dependency)",
            assumption_revalidation.admission_error(self.root, self.projects, self.meta, self.tasks)
            or "",
        )

        separate: dict[str, object] = {
            "id": "AR-0003",
            "owner": "worker",
            "status": "in_progress",
            "task_revision": 2,
        }
        assumptions = [separate, self.tasks[1]]
        separate_args = self.args(
            "declare", "harmless", kind="dependency", reference="AR-0002", material=False
        )
        separate_args.task = "AR-0003"
        assumption_revalidation.apply(
            self.root,
            self.projects,
            separate_args,
            separate,
            assumptions,
        )
        self.tasks[1]["task_revision"] = 9
        self.assertIsNone(
            assumption_revalidation.admission_error(self.root, self.projects, separate, assumptions)
        )

    def test_observation_change_requires_revalidation_or_explicit_disposition(self) -> None:
        self.apply(
            self.args(
                "declare", "scan", kind="observation", reference="observation.txt", material=True
            )
        )
        (self.root / "observation.txt").write_text("two\n", encoding="utf-8")
        self.assertIn(
            "scan (observation)",
            assumption_revalidation.admission_error(self.root, self.projects, self.meta, self.tasks)
            or "",
        )
        self.meta["task_revision"] = 3
        self.apply(self.args("dispose", "scan", reason="superseded by fresh integration check"))
        self.assertIsNone(
            assumption_revalidation.admission_error(self.root, self.projects, self.meta, self.tasks)
        )

    def test_malformed_and_unsafe_records_fail_closed(self) -> None:
        self.meta["assumption_revalidation"] = [{}]
        self.assertIn(
            "fields are not exact", assumption_revalidation.metadata_error(self.meta) or ""
        )
        self.meta.pop("assumption_revalidation")
        with self.assertRaisesRegex(RuntimeError, "kind and material"):
            self.apply(self.args("declare", "missing"))
        with self.assertRaisesRegex(RuntimeError, "unsafe"):
            self.apply(
                self.args(
                    "declare", "unsafe", kind="observation", reference="../escape", material=True
                )
            )

    def _parse_workflow_complexity_command(self, workflow: str) -> list[str]:
        lines = [line.strip() for line in workflow.splitlines() if "uv run lizard" in line]
        self.assertEqual(1, len(lines), "verify workflow must declare one complexity command")
        return shlex.split(lines[0])

    def _workflow_complexity_command(self) -> list[str]:
        workflow = (REPOSITORY_ROOT / ".github/workflows/verify.yml").read_text(encoding="utf-8")
        return self._parse_workflow_complexity_command(workflow)

    @staticmethod
    def _is_expected_complexity_command(command: list[str]) -> bool:
        return command == EXPECTED_COMPLEXITY_COMMAND

    def test_v074_modules_are_covered_by_the_enforced_complexity_budget(self) -> None:
        self.assertTrue(self._is_expected_complexity_command(self._workflow_complexity_command()))

    def test_complexity_contract_rejects_missing_v074_module(self) -> None:
        workflow = (REPOSITORY_ROOT / ".github/workflows/verify.yml").read_text(encoding="utf-8")
        candidate = workflow.replace(" tools/retry_circuit.py", "")
        self.assertFalse(
            self._is_expected_complexity_command(self._parse_workflow_complexity_command(candidate))
        )

    def test_complexity_contract_rejects_extra_module(self) -> None:
        workflow = (REPOSITORY_ROOT / ".github/workflows/verify.yml").read_text(encoding="utf-8")
        candidate = workflow.replace(
            " tools/retry_circuit.py", " tools/retry_circuit.py tools/role_registry.py"
        )
        self.assertFalse(
            self._is_expected_complexity_command(self._parse_workflow_complexity_command(candidate))
        )

    def test_complexity_contract_rejects_lower_threshold(self) -> None:
        workflow = (REPOSITORY_ROOT / ".github/workflows/verify.yml").read_text(encoding="utf-8")
        candidate = workflow.replace("--CCN 14", "--CCN 13")
        self.assertFalse(
            self._is_expected_complexity_command(self._parse_workflow_complexity_command(candidate))
        )

    def test_followups_are_fenced_and_cannot_change_policy_or_revalidate_same_binding(self) -> None:
        self.apply(self.args("declare", "base", kind="base", material=True))
        self.meta["task_revision"] = 3
        with self.assertRaisesRegex(RuntimeError, "requires a changed binding"):
            self.apply(self.args("revalidate", "base"))
        with self.assertRaisesRegex(RuntimeError, "cannot change"):
            self.apply(self.args("revalidate", "base", kind="dependency"))
        stale = self.args("dispose", "base", reason="handled")
        stale.expected_revision = 2
        with self.assertRaisesRegex(RuntimeError, "stale revision"):
            self.apply(stale)

    def test_parser_and_transition_route_assumption_without_external_gate(self) -> None:
        parser = argparse.ArgumentParser()
        commands = parser.add_subparsers(dest="command", required=True)
        assumption_revalidation.add_command_parser(commands)
        parsed = parser.parse_args(
            [
                "assumption",
                "declare",
                "AR-0001",
                "--owner",
                "worker",
                "--expected-revision",
                "2",
                "--assumption-id",
                "base",
                "--kind",
                "base",
                "--material",
            ]
        )
        self.assertTrue(parsed.material)
        self.assertEqual("declare", parsed.assumption_action)
        with self.assertRaises(SystemExit):
            parser.parse_args(["assumption", "declare", "AR-0001"])

        args = self.args("declare", "base", kind="base", material=True)
        with (
            patch.object(assumption_revalidation, "apply", return_value="recorded") as apply,
            patch.object(handoffctl, "config", return_value={"projects_root": str(self.projects)}),
        ):
            self.assertEqual(
                "recorded", handoffctl.apply_transition(args, "assumption", self.meta, [])
            )
        self.assertEqual(args, apply.call_args.args[2])

    def test_top_level_cli_dispatches_assumption_as_lifecycle_mutation(self) -> None:
        with (
            patch.object(handoffctl, "assert_project_binding"),
            patch.object(handoffctl, "mutate", return_value=None) as mutate,
            patch(
                "sys.argv",
                [
                    "handoffctl",
                    "assumption",
                    "declare",
                    "AR-0001",
                    "--owner",
                    "worker",
                    "--expected-revision",
                    "2",
                    "--assumption-id",
                    "base",
                    "--kind",
                    "base",
                    "--material",
                ],
            ),
        ):
            self.assertEqual(0, handoffctl.main())
        parsed, command = mutate.call_args.args
        self.assertEqual("assumption", command)
        self.assertEqual("assumption", parsed.cmd)
        self.assertEqual("declare", parsed.assumption_action)

    def test_done_admission_rejects_stale_material_assumption_after_spec_checks(self) -> None:
        self.apply(self.args("declare", "base", kind="base", material=True))
        git(self.worktree, "commit", "--allow-empty", "-m", "changed")
        with (
            patch.object(handoffctl, "done_admission_error", return_value=None),
            patch.object(change_drift, "done_admission_error", return_value=None),
            patch.object(handoffctl, "config", return_value={"projects_root": str(self.projects)}),
            self.assertRaisesRegex(RuntimeError, "ASSUMPTION_REVALIDATION_REQUIRED"),
        ):
            handoffctl.require_done_admission(self.meta, [(Path("task"), self.meta, "")])

    def test_empty_assumption_history_does_not_require_runtime_config(self) -> None:
        with (
            patch.object(handoffctl, "done_admission_error", return_value=None),
            patch.object(change_drift, "done_admission_error", return_value=None),
            patch.object(handoffctl, "config", side_effect=AssertionError("not needed")),
        ):
            handoffctl.require_done_admission(self.meta, [(Path("task"), self.meta, "")])

    def test_accept_without_assumptions_does_not_require_runtime_config(self) -> None:
        args = argparse.Namespace(owner="worker")
        with (
            patch.object(handoffctl, "require_role_admission"),
            patch.object(handoffctl, "config", side_effect=AssertionError("not needed")),
            patch.object(
                handoffctl, "apply_acceptance", side_effect=lambda *_args: _args[-1]()
            ) as accept,
        ):
            self.assertIsNone(handoffctl.apply_accept(args, self.meta, None, []))
        self.assertIsNone(accept.call_args.args[-1]())


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
