# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Concurrent and fail-closed tests for the opt-in cached observation contract."""

from __future__ import annotations

import threading
import time
import unittest
import uuid
from typing import Any
from unittest.mock import patch

from tools.fast_observation import ObservationCache, validate_max_age


class ObservationCore:
    def __init__(self) -> None:
        self.binding = {"project_id": str(uuid.uuid4())}
        self.configuration: dict[str, object] = {"product_worktree": "product"}
        self.scan_count = 0
        self.scan_started = threading.Event()
        self.release_scan = threading.Event()

    def backend_selection(self) -> dict[str, str]:
        return {"backend": "git"}

    def project_binding(self) -> dict[str, str]:
        return dict(self.binding)

    def config(self) -> dict[str, object]:
        return dict(self.configuration)

    def project_scan(self) -> dict[str, object]:
        self.scan_count += 1
        self.scan_started.set()
        if not self.release_scan.wait(2):
            raise RuntimeError("test scan release timed out")
        return {
            "remote_main": "a" * 40,
            "origin_main": "b" * 40,
            "primary_head": "c" * 40,
            "worktrees": [{"key": "product", "dirty": 0}],
            "prs": [],
            "runs": [],
        }


class FastObservationTests(unittest.TestCase):
    def test_validate_max_age_is_bounded_and_type_strict(self) -> None:
        self.assertEqual(0, validate_max_age(0))
        self.assertEqual(300, validate_max_age(300))
        for value in (-1, 301, True, "1"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                validate_max_age(value)

    def test_concurrent_callers_share_one_scan_and_receive_explicit_contract(self) -> None:
        core = ObservationCore()
        cache = ObservationCache()
        results: list[dict[str, object]] = []
        errors: list[BaseException] = []

        def observe() -> None:
            try:
                results.append(cache.observe(core, 30))
            except BaseException as error:  # pragma: no cover - asserted below
                errors.append(error)

        workers = [threading.Thread(target=observe) for _ in range(16)]
        for worker in workers:
            worker.start()
        self.assertTrue(core.scan_started.wait(1))
        time.sleep(0.02)
        core.release_scan.set()
        for worker in workers:
            worker.join(2)
        self.assertFalse(errors)
        self.assertEqual(16, len(results))
        self.assertEqual(1, core.scan_count)
        self.assertEqual({"cached-observation-v1"}, {item["contract"] for item in results})
        self.assertEqual({False}, {item["strict_equivalent"] for item in results})
        self.assertEqual(1, len({str(item["observation_sha256"]) for item in results}))
        self.assertIn("fresh-scan", {str(item["freshness"]) for item in results})
        self.assertTrue(
            {str(item["freshness"]) for item in results} <= {"fresh-scan", "bounded-cache"}
        )

    def test_concurrent_zero_age_callers_share_the_same_fresh_generation(self) -> None:
        core = ObservationCore()
        cache = ObservationCache()
        results: list[dict[str, object]] = []
        errors: list[BaseException] = []

        def observe() -> None:
            try:
                results.append(cache.observe(core, 0))
            except BaseException as error:  # pragma: no cover - asserted below
                errors.append(error)

        workers = [threading.Thread(target=observe) for _ in range(16)]
        for worker in workers:
            worker.start()
        self.assertTrue(core.scan_started.wait(1))
        time.sleep(0.02)
        core.release_scan.set()
        for worker in workers:
            worker.join(2)
        self.assertFalse(errors)
        self.assertEqual(16, len(results))
        self.assertEqual(1, core.scan_count)
        self.assertEqual({"fresh-scan"}, {str(item["freshness"]) for item in results})

    def test_changed_input_during_scan_rejects_without_caching_stale_state(self) -> None:
        core = ObservationCore()
        cache = ObservationCache()
        outcome: list[Any] = []

        def observe() -> None:
            try:
                outcome.append(cache.observe(core, 30))
            except RuntimeError as error:
                outcome.append(error)

        workers = [threading.Thread(target=observe) for _ in range(16)]
        for worker in workers:
            worker.start()
        self.assertTrue(core.scan_started.wait(1))
        time.sleep(0.02)
        core.configuration["product_worktree"] = "changed-product"
        core.release_scan.set()
        for worker in workers:
            worker.join(2)
        self.assertEqual(16, len(outcome))
        self.assertTrue(all(isinstance(item, RuntimeError) for item in outcome))
        self.assertTrue(all("OBSERVATION_INPUT_CHANGED" in str(item) for item in outcome))
        self.assertEqual(1, core.scan_count)

    def test_scan_failure_releases_the_single_flight_for_a_retry(self) -> None:
        core = ObservationCore()
        cache = ObservationCache()
        with (
            self.assertRaisesRegex(ValueError, "scan failed"),
            patch.object(core, "project_scan", side_effect=ValueError("scan failed")),
        ):
            cache.observe(core, 30)
        core.release_scan.set()
        observed = cache.observe(core, 30)
        self.assertEqual("fresh-scan", observed["freshness"])
