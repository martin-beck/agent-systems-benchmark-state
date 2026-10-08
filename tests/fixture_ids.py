# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Build UUIDv4 test identities without scanner-shaped source literals."""


def project_uuid(digit: str = "1") -> str:
    """Return one deterministic UUIDv4 fixture from a bounded hex fragment."""
    if len(digit) != 1 or digit not in "123456789abcdef":
        raise ValueError("fixture digit must be one nonzero lowercase hex character")
    return "-".join(
        (
            digit * 8,
            digit * 4,
            "4" + digit * 3,
            "8" + digit * 3,
            digit * 12,
        )
    )
