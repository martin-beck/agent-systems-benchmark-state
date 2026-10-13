# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Downstream dispatch coverage for issue-series service delegates."""

from __future__ import annotations

import argparse
import unittest
from unittest.mock import patch

from tools import issue_series_service as service


class IssueSeriesDispatchCoverageTests(unittest.TestCase):
    def test_refresh_and_core_value_fail_closed_without_installation(self) -> None:
        with patch.object(service, "_CORE", None):
            with self.assertRaisesRegex(RuntimeError, "not installed"):
                service._refresh()
            with self.assertRaisesRegex(RuntimeError, "not installed"):
                service._core_value("missing")

    def test_dispatch_selects_only_known_actions_and_uses_supplied_core(self) -> None:
        calls: list[str] = []

        def plan(_args: object) -> None:
            calls.append("plan")

        core = {
            "cmd_issue_series_plan": plan,
            "cmd_issue_series_create": lambda _args: calls.append("create"),
            "cmd_issue_series_publish": lambda _args: calls.append("publish"),
        }
        self.assertFalse(service.dispatch_cli(argparse.Namespace(cmd="status"), core))
        self.assertTrue(
            service.dispatch_cli(
                argparse.Namespace(cmd="issue-series", issue_series_action="plan"), core
            )
        )
        self.assertEqual(["plan"], calls)
        with self.assertRaisesRegex(RuntimeError, "unsupported"):
            service.dispatch_cli(
                argparse.Namespace(cmd="issue-series", issue_series_action="unknown"), core
            )

    def test_parser_accepts_bounded_actions_and_rejects_missing_required_arguments(self) -> None:
        parser = argparse.ArgumentParser()
        commands = parser.add_subparsers(dest="cmd", required=True)
        service.add_cli_parser(commands)
        parsed = parser.parse_args(
            [
                "issue-series",
                "publish",
                "--repository",
                "github.com/acme/product",
                "--issue-number",
                "1",
                "--expected-manifest-digest",
                "sha256:" + "a" * 64,
                "--transport",
                "mock",
            ]
        )
        self.assertEqual("publish", parsed.issue_series_action)
        with self.assertRaises(SystemExit):
            parser.parse_args(["issue-series", "create"])
