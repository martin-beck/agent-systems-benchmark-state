# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Ensure every known SQLite authority write route enters the shared fence."""

from __future__ import annotations

import ast
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "tools" / "sqlite_storage.py"
INVENTORY = ROOT / "formal" / "upgrade" / "sqlite-route-inventory.json"


def _methods() -> dict[str, ast.FunctionDef | ast.AsyncFunctionDef]:
    tree = ast.parse(SOURCE.read_text(encoding="utf-8"))
    backend = next(
        node
        for node in tree.body
        if isinstance(node, ast.ClassDef) and node.name == "SQLiteBackend"
    )
    return {
        node.name: node
        for node in backend.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }


def _calls_transaction(node: ast.AST) -> bool:
    return any(
        isinstance(candidate, ast.Attribute)
        and candidate.attr == "transaction"
        and isinstance(candidate.value, ast.Name)
        and candidate.value.id == "self"
        for candidate in ast.walk(node)
    )


def test_inventory_is_explicit_and_every_route_uses_shared_transaction_gate() -> None:
    inventory = json.loads(INVENTORY.read_text(encoding="utf-8"))
    methods = _methods()
    routes = inventory["routes"]
    assert routes
    assert len({route["method"] for route in routes}) == len(routes)
    for route in routes:
        method = route["method"]
        assert method in methods
        assert route["gate"] == "SQLiteBackend.transaction"
        assert route["operations"]
        assert _calls_transaction(methods[method])


def test_inventory_stays_bounded_and_fail_closed() -> None:
    inventory = json.loads(INVENTORY.read_text(encoding="utf-8"))
    assert inventory["implementation"] == "tools/sqlite_storage.py"
    assert any("does not prove" in claim for claim in inventory["nonclaims"])
