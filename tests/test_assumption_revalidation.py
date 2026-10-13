# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Negative-path coverage for explicit task assumption revalidation."""

from __future__ import annotations

import argparse
import subprocess
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from tools import assumption_revalidation, change_drift, handoffctl

REPOSITORY_ROOT = Path(__file__).resolve().parent.parent


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

    def test_unavailable_bindings_are_rejected_without_recording_an_assumption(self) -> None:
        cases = (
            ("base", "", "assumption base requires a safely bound worktree"),
            ("dependency", "not-an-ar", "assumption dependency is invalid"),
            ("dependency", "AR-9999", "assumption dependency is unavailable"),
            ("observation", "missing.txt", "assumption observation is unavailable"),
        )
        for index, (kind, reference, error) in enumerate(cases):
            with self.subTest(kind=kind, reference=reference):
                if kind == "base":
                    self.meta.pop("worktree_key")
                with self.assertRaisesRegex(RuntimeError, error):
                    self.apply(
                        self.args(
                            "declare",
                            f"missing-{index}",
                            kind=kind,
                            reference=reference,
                            material=True,
                        )
                    )
                self.assertNotIn("assumption_revalidation", self.meta)
                self.meta["worktree_key"] = "worker"

        directory = self.root / "directory.txt"
        directory.mkdir()
        with self.assertRaisesRegex(RuntimeError, "bounded regular file"):
            self.apply(
                self.args(
                    "declare",
                    "directory",
                    kind="observation",
                    reference="directory.txt",
                    material=True,
                )
            )

    def test_tampered_or_unlinked_history_fails_closed_before_admission(self) -> None:
        declaration = assumption_revalidation._record(
            "declare", "base", "base", True, {"head": "a" * 40}, 3, ""
        )
        duplicate = assumption_revalidation._record(
            "declare", "base", "base", True, {"head": "b" * 40}, 4, declaration["digest"]
        )
        revalidation = assumption_revalidation._record(
            "revalidate", "base", "base", True, {"head": "b" * 40}, 4, ""
        )
        dispose_without_reason = assumption_revalidation._record(
            "dispose", "base", "base", True, {"head": "b" * 40}, 4, declaration["digest"]
        )
        cases = (
            ([declaration, duplicate], "assumption is declared more than once"),
            ([revalidation], "assumption follow-up is not linked to declaration"),
            ([declaration, dispose_without_reason], "assumption disposition reason is invalid"),
            (
                [declaration] * (assumption_revalidation.MAX_RECORDS + 1),
                "assumption history is invalid",
            ),
        )
        for ledger, error in cases:
            with self.subTest(error=error):
                self.meta["assumption_revalidation"] = ledger
                self.assertIn(error, assumption_revalidation.metadata_error(self.meta) or "")
                self.assertEqual(
                    f"ASSUMPTION_REVALIDATION_REQUIRED: {error}",
                    assumption_revalidation.admission_error(
                        self.root, self.projects, self.meta, self.tasks
                    ),
                )

    def test_owner_and_followup_fences_prevent_mutating_a_different_assumption(self) -> None:
        wrong_task = self.args("declare", "base", kind="base", material=True)
        wrong_task.task = "AR-0002"
        with self.assertRaisesRegex(RuntimeError, "does not match"):
            self.apply(wrong_task)
        wrong_owner = self.args("declare", "base", kind="base", material=True)
        wrong_owner.owner = "other"
        with self.assertRaisesRegex(RuntimeError, "is owned by worker"):
            self.apply(wrong_owner)
        self.meta["status"] = "planned"
        with self.assertRaisesRegex(RuntimeError, "require an active task"):
            self.apply(self.args("declare", "base", kind="base", material=True))
        self.meta["status"] = "in_progress"
        with self.assertRaisesRegex(RuntimeError, "must be declared before follow-up"):
            self.apply(self.args("dispose", "unknown", reason="not applicable"))

    def test_disposed_material_assumption_needs_no_lookup_but_corrupt_active_binding_blocks(
        self,
    ) -> None:
        self.apply(
            self.args(
                "declare", "scan", kind="observation", reference="observation.txt", material=True
            )
        )
        self.meta["task_revision"] = 3
        self.apply(self.args("dispose", "scan", reason="superseded"))
        (self.root / "observation.txt").unlink()
        self.assertFalse(assumption_revalidation.needs_admission(self.meta))
        self.assertIsNone(
            assumption_revalidation.admission_error(self.root, self.projects, self.meta, self.tasks)
        )

        self.meta["assumption_revalidation"] = [
            assumption_revalidation._record(
                "declare",
                "scan",
                "observation",
                True,
                {"ref": "missing.txt", "digest": "sha256:" + "a" * 64},
                3,
                "",
            )
        ]
        self.assertTrue(assumption_revalidation.needs_admission(self.meta))
        self.assertEqual(
            "ASSUMPTION_REVALIDATION_REQUIRED: assumption observation is unavailable",
            assumption_revalidation.admission_error(
                self.root, self.projects, self.meta, self.tasks
            ),
        )

    def test_assumption_validator_is_covered_by_the_enforced_complexity_budget(self) -> None:
        workflow = (REPOSITORY_ROOT / ".github/workflows/verify.yml").read_text(encoding="utf-8")
        self.assertIn(
            "lizard -l python --CCN 14 tools/handoffctl.py tools/assumption_revalidation.py",
            workflow,
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
