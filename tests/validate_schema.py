#!/usr/bin/env python3
# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Validate every task document against the published strict schema."""

import json
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parent.parent


def metadata(path: Path) -> object:
    """Return the JSON-compatible front matter."""
    text = path.read_text()
    end = text.index("\n---\n", 4)
    return json.loads(text[4:end])


def main() -> int:
    """Validate the schema itself and every task."""
    schema = json.loads((ROOT / "schema/task-schema.json").read_text())
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    failures: list[str] = []
    for path in sorted((ROOT / "tasks").glob("AR-*.md")):
        failures.extend(
            f"{path.name}: {error.message}"
            for error in sorted(validator.iter_errors(metadata(path)), key=str)
        )
    if failures:
        raise SystemExit("\n".join(failures))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
