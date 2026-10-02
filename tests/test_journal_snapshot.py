# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Contract tests for the deeply immutable journal snapshot envelope."""

from __future__ import annotations

import unittest
from collections.abc import Mapping, MutableMapping, MutableSequence
from typing import cast

from tools.upgrade_engine import JournalSnapshot


class JournalSnapshotTests(unittest.TestCase):
    def test_nested_values_are_immutable_and_detached(self) -> None:
        source = {
            "status": "running",
            "phase": "backup",
            "records": [{"result": {"items": ["before"]}}],
        }
        snapshot = JournalSnapshot.from_mapping(source)

        source_records = cast(list[dict[str, object]], source["records"])
        source_result = cast(dict[str, object], source_records[0]["result"])
        cast(list[object], source_result["items"]).append("after")
        self.assertEqual(
            snapshot.as_mapping()["records"],
            [{"result": {"items": ["before"]}}],
        )
        record = snapshot.records[0]
        with self.assertRaises(TypeError):
            cast(MutableMapping[str, object], record)["result"] = "tampered"
        nested = cast(Mapping[str, object], record["result"])
        with self.assertRaises(TypeError):
            cast(MutableMapping[str, object], nested)["items"] = ("tampered",)
        items = cast(tuple[object, ...], nested["items"])
        with self.assertRaises(TypeError):
            cast(MutableSequence[object], items)[0] = "tampered"

    def test_as_mapping_is_a_detached_mutable_copy(self) -> None:
        snapshot = JournalSnapshot.from_mapping(
            {"status": "complete", "phase": None, "records": [{"ok": True}]}
        )
        exported = snapshot.as_mapping()
        records = exported["records"]
        assert isinstance(records, list)
        cast(dict[str, object], records[0])["ok"] = False
        self.assertEqual(snapshot.records[0]["ok"], True)

    def test_input_shape_is_strict(self) -> None:
        malformed: tuple[object, ...] = (
            None,
            {"status": "running", "phase": None},
            {"status": "running", "phase": None, "records": [], "extra": True},
            {"status": 1, "phase": None, "records": []},
            {"status": "running", "phase": 1, "records": []},
            {"status": "running", "phase": None, "records": ()},
            {"status": "running", "phase": None, "records": ["not a record"]},
        )
        for value in malformed:
            with self.subTest(value=value), self.assertRaises(ValueError):
                JournalSnapshot.from_mapping(cast(Mapping[str, object], value))


if __name__ == "__main__":
    unittest.main()
