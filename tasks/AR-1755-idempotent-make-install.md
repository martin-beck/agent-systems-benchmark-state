---
{
  "branch": "fix/ar-1755-idempotent-make-install",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-09T11:33:25+00:00",
  "depends_on": [
    "AR-1745"
  ],
  "id": "AR-1755",
  "next_action": "Promote and claim; reproduce the existing-destination failure on exact ASB main, make plain `make install` safely idempotent, add repeat-install regressions, and complete independent reviewed integration with exact-head and exact-main CI.",
  "observed_branch": "fix/ar-1755-idempotent-make-install",
  "observed_dirty": 0,
  "observed_head": "64eaad2215e4f08fe8e803022acb6e9146b95d94",
  "owner": "codex-asb-ar1755-install-20261009",
  "plan": "../plans/AR-1755-idempotent-make-install.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1755.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Repair the ASB Make install path so rerunning plain `make install` replaces its existing ASB binary without advertising an invalid Make option.",
  "task_revision": 7,
  "title": "Make ASB installation safely idempotent",
  "updated_at": "2026-10-09T09:35:45+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1755-idempotent-make-install"
}
---

On current protected ASB main, a first `make install` succeeds, but a second
install into the same prefix delegates to `cargo install` without Cargo's
overwrite flag. Cargo reports that the binary already exists and recommends
`--force`. Passing that text back as `make install --force` fails earlier because
GNU Make does not recognize `--force` as one of its options.

Restore the idempotent reinstall contract accepted by AR-1745. Plain
`make install` must safely replace the ASB-managed executable inside the already
validated prefix without requiring an additional user option. Preserve all
absolute-prefix, traversal, repository-root, filesystem-root, symlink-chain,
ownership-boundary, cleanup-marker, and out-of-prefix protections. Do not broaden
the change into TUI installation, release packaging, runtime installation, or
system-wide privilege handling.


- 2026-10-09T09:33:22+00:00: AR-1745 is done; exact ASB main reproduces the Cargo
  existing-destination failure and GNU Make rejects the suggested --force spelling.

- 2026-10-09T09:33:25+00:00: Claimed by codex-asb-ar1755-install-20261009.

- 2026-10-09T09:33:55+00:00: Recorded command exit 0; command argv SHA-256
  048c8e1fefac351386dd2444042d2e0c10f87c1379dbb29985451c5f4351ec1e.

- 2026-10-09T09:34:55+00:00: Recorded command exit 0; command argv SHA-256
  b1c2c9d69651561e32b970415591af09bcaa14d36b0791d31ae69d5ab57387c7.

- 2026-10-09T09:35:45+00:00: Recorded command exit 2; command argv SHA-256
  ff9297d17c0732874297929773bce1e7f679caddd77de7a11179d73b2a300879.
