# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
# mypy: disable-error-code=attr-defined
"""ASB-only dispatch and error-path coverage for vendored handoffctl."""

from __future__ import annotations

import argparse
import io
import json
import sys
import unittest
from contextlib import redirect_stderr, redirect_stdout
from unittest.mock import MagicMock, patch

from tools import handoffctl


class HandoffctlDispatchCoverageTests(unittest.TestCase):
    """Exercise safe parser and dispatch seams without a live coordinator."""

    def test_read_only_dispatch_routes_and_returns_runtime_status(self) -> None:
        snapshot = argparse.Namespace(cmd="snapshot", task="AR-0042")
        board = argparse.Namespace(cmd="board")
        metrics = argparse.Namespace(cmd="metrics")
        preflight = argparse.Namespace(cmd="preflight", task="AR-0042")
        with (
            patch.object(handoffctl, "cmd_snapshot") as cmd_snapshot,
            patch.object(handoffctl, "cmd_board") as cmd_board,
            patch.object(handoffctl, "cmd_metrics") as cmd_metrics,
            patch.object(handoffctl, "print_execution_preflight", return_value=19) as preflight_fn,
        ):
            self.assertEqual(0, handoffctl.dispatch_read_only_command(snapshot))
            self.assertEqual(0, handoffctl.dispatch_read_only_command(board))
            self.assertEqual(0, handoffctl.dispatch_read_only_command(metrics))
            self.assertEqual(19, handoffctl.dispatch_read_only_command(preflight))
        cmd_snapshot.assert_called_once_with("AR-0042")
        cmd_board.assert_called_once_with()
        cmd_metrics.assert_called_once_with()
        preflight_fn.assert_called_once_with(preflight)

    def test_dispatch_standard_handles_run_marker_side_effect_and_unknown(self) -> None:
        run_args = argparse.Namespace(cmd="run", command=["--", "true"])
        side_effect_args = argparse.Namespace(cmd="render-status", check=True)
        unknown_args = argparse.Namespace(cmd="unrecognized")
        with (
            patch.object(handoffctl, "cmd_run", return_value=7) as cmd_run,
            patch.object(handoffctl, "cmd_render_status") as render,
        ):
            self.assertEqual(7, handoffctl.dispatch_bound_standard_command(run_args))
            self.assertEqual(0, handoffctl.dispatch_bound_standard_command(side_effect_args))
            self.assertEqual(0, handoffctl.dispatch_bound_standard_command(unknown_args))
        self.assertEqual(["true"], run_args.command)
        cmd_run.assert_called_once_with(run_args)
        render.assert_called_once_with(check=True)

    def test_dispatch_returning_routes_doctor_and_lifecycle_note(self) -> None:
        doctor = argparse.Namespace(cmd="doctor", live=True)
        lifecycle = argparse.Namespace(cmd="accept")
        with (
            patch.object(handoffctl, "cmd_doctor", return_value=3) as cmd_doctor,
            patch.object(handoffctl, "mutate", return_value="accepted") as mutate,
            patch("builtins.print") as output,
        ):
            self.assertEqual(3, handoffctl.dispatch_returning_command(doctor))
            self.assertEqual(0, handoffctl.dispatch_bound_standard_command(lifecycle))
        cmd_doctor.assert_called_once_with(live=True)
        mutate.assert_called_once_with(lifecycle, "accept")
        output.assert_called_once_with("accepted")

    def test_retry_status_defaults_and_validates_durable_state(self) -> None:
        lock = MagicMock()
        lock.__enter__.return_value = None
        clean = {"id": "AR-0042"}
        recorded = {
            "id": "AR-0042",
            "retry_circuit": {
                "schema_version": handoffctl.retry_circuit.SCHEMA_VERSION,
                "attempts": [],
                "recoveries": [],
                "hold": None,
                "reservations": [],
                "abandoned": [],
            },
        }
        output = io.StringIO()
        with (
            patch.object(handoffctl, "locked", return_value=lock) as locked,
            patch.object(
                handoffctl, "locate", side_effect=[(None, clean, None), (None, recorded, None)]
            ),
            patch.object(handoffctl.retry_circuit, "validate") as validate,
            redirect_stdout(output),
        ):
            self.assertEqual(0, handoffctl.cmd_retry_circuit_status("AR-0042"))
            self.assertEqual(0, handoffctl.cmd_retry_circuit_status("AR-0042"))
        defaults, persisted = [json.loads(line) for line in output.getvalue().splitlines()]
        self.assertEqual([], defaults["attempts"])
        self.assertEqual(recorded["retry_circuit"], persisted)
        self.assertEqual(2, locked.call_count)
        validate.assert_called_once_with(recorded["retry_circuit"])

    def test_main_parses_fast_and_rejects_binding_before_dispatch(self) -> None:
        argv = [
            "handoffctl",
            "fast",
            "receipt",
            "receipt-42",
        ]
        with (
            patch.object(sys, "argv", argv),
            patch.object(handoffctl, "assert_project_binding") as binding,
            patch.object(handoffctl, "dispatch_bound_command", return_value=11) as dispatch,
        ):
            self.assertEqual(11, handoffctl.main())
        binding.assert_called_once_with()
        parsed = dispatch.call_args.args[0]
        self.assertEqual(
            ("fast", "receipt", "receipt-42"), (parsed.cmd, parsed.fast_action, parsed.receipt_id)
        )

    def test_main_entrypoint_maps_retry_repair_and_generic_errors(self) -> None:
        outcomes = [
            (handoffctl.RetryableCoordinatorError("wait"), 75, "RETRYABLE: wait"),
            (handoffctl.RepairRequiredCoordinatorError("repair"), 76, "REPAIR_REQUIRED: repair"),
            (RuntimeError("broken"), 1, "ERROR: broken"),
        ]
        for error, expected_status, expected_text in outcomes:
            with (
                self.subTest(error=type(error).__name__),
                patch.object(handoffctl, "main", side_effect=error),
            ):
                stderr = io.StringIO()
                with redirect_stderr(stderr):
                    self.assertEqual(expected_status, handoffctl.main_entrypoint())
                self.assertEqual(expected_text, stderr.getvalue().strip())
