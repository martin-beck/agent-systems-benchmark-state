# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Additional non-vendored coverage for AR-1954 root compatibility branches."""

import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from tools.execution_envelope import (
    envelope_sandbox_mounts,
    envelope_scope_path,
    validate_external_root,
)


class EnvelopeCompatibilityCoverageTests(unittest.TestCase):
    def test_roots_and_mounts(self) -> None:
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            product = root / "product"
            state = root / "state"
            source = root / "source"
            for path in (product, state / "tasks", source / "src"):
                path.mkdir(parents=True)
            self.assertEqual(state.resolve(), validate_external_root(state, "state"))
            mounts = envelope_sandbox_mounts(
                product,
                ["product-root", "state:tasks", "source-root"],
                ["state:tasks"],
                state_root=state,
                source_root=source,
            )
            self.assertEqual(
                ["product/.", "state/tasks", "source/.", "state/tasks"],
                [mount[0] for mount in mounts],
            )
            with self.assertRaisesRegex(RuntimeError, "unavailable root"):
                envelope_sandbox_mounts(product, ["source-root"], [], state_root=state)

    def test_invalid_roots_and_symlinks_fail_closed(self) -> None:
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            product = root / "product"
            product.mkdir()
            with self.assertRaisesRegex(RuntimeError, "root is unavailable"):
                validate_external_root(root / "missing", "state")
            outside = root / "outside"
            outside.mkdir()
            (product / "alias").symlink_to(outside, target_is_directory=True)
            with self.assertRaisesRegex(RuntimeError, "contains a symlink"):
                envelope_scope_path(product, "alias")


if __name__ == "__main__":
    unittest.main()
