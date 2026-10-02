# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Generate and validate a release upgrade contract without side effects."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from .generate_upgrade_contract import generate
from .validate_upgrade_contract import ContractError, validate_contract


def verify(input_path: Path, output_path: Path) -> dict[str, Any]:
    document = generate(json.loads(input_path.read_text(encoding="utf-8")))
    validate_contract(document)
    output_path.write_text(json.dumps(document, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return {
        "status": "pass",
        "operation_id": document["operation_id"],
        "backend": document["backend"],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args(argv)
    try:
        print(json.dumps(verify(args.input, args.output), sort_keys=True))
    except (OSError, ValueError, ContractError):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
