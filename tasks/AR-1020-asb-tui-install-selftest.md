---
{
  "branch": "feature/asb-tui-install-selftest",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1019"
  ],
  "id": "AR-1020",
  "next_action": "Publish c5454fa through a protected pull request, verify exact-head hosted CI, merge with DCO and verified signature, then run hosted and trusted local post-merge CI.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1020.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "done",
  "summary": "Install and operate asb-tui safely as an optional extension.",
  "task_revision": 9,
  "title": "Add isolated asb-tui install and self-test lifecycle",
  "updated_at": "2026-09-10T16:40:52+00:00",
  "worktree_key": "agent-systems-benchmark-asb-tui-install-selftest"
}
---
Provide `asb tui install`, `asb tui`, `asb tui status`, `asb tui upgrade`, and `asb tui remove`. Install
only into an isolated user directory, never overwrite ASB core files, run a protocol/terminal self-test
before launch, validate the locked coordinator and workflow-quality release versions, and show the
extension's verified/unverified boundary and exact versions. Preserve the
main benchmark process when the TUI disconnects or is removed.

Acceptance criteria: fresh install/upgrade/remove/reconnect tests, interrupted-install recovery,
read-only status, detached-run continuity, permissions/privacy checks, and clear actionable errors.

- 2026-09-10T15:53:31+00:00: AR-1019 is complete on public exact main
  990517eda77d4d42ff51ca5d1da03b56e7b8cdda with hosted and trusted local validation; isolated
  install lifecycle may begin.

- 2026-09-10T15:53:34+00:00: Claimed by contracts_20260906.

- 2026-09-10T15:54:28+00:00: Exact public ASB source audit found versioned external executable
  protocol types and conformance fixtures, but docs/EXTENSIONS.md explicitly says general
  external-extension discovery and transport are not yet a CLI feature. The current ASB TUI remains
  a built-in startup shell. Therefore this standalone repository cannot alone make asb tui route to
  an extension without overwriting/shadowing ASB core, which is prohibited. Proceed with isolated
  user-space install/status/upgrade/remove/launch implementation and tests in asb-tui, define a
  fail-closed delegated invocation contract, and record a separate product-side routing dependency
  rather than claiming current end-to-end ASB CLI availability.

- 2026-09-10T16:05:45+00:00: Heartbeat by contracts_20260906.

- 2026-09-10T16:05:56+00:00: Checkpoint 040adfb adds owner-private retained-directory lifecycle
  storage with kernel-released exclusive locking, bounded inode-stable reads, digest-addressed
  executable versions, atomic active-state replacement, interrupted-stage recovery, read-only
  verification, idempotent install/remove, and lifecycle tests. Clippy and 7 focused tests pass.
  Product ASB routing remains an explicit separate dependency.

- 2026-09-10T16:29:52+00:00: Heartbeat by contracts_20260906.

- 2026-09-10T16:30:08+00:00: Standalone AR-1020 implementation is complete at signed+DCO head
  c5454fa. It provides closed delegated install/upgrade/status/launch/remove JSON contracts,
  authenticated complete-bundle verification, owner-private transactional storage, exact-candidate
  bounded protocol/terminal self-test, digest recheck before launch, interrupted recovery, and no
  benchmark-process ownership. Full locked suite passes (74 tests plus doctests); coverage passes at
  90.52% lines; clippy/rustfmt/docs/schema, ShellCheck/shfmt, actionlint/zizmor, Gitleaks (7
  commits, no leaks), and ASB isolation (16 tests plus 2 doctests) pass. The first ASB isolation
  invocation lacked cargo on PATH; rerun with exact Rust 1.93.0 passed.

- 2026-09-10T16:40:52+00:00: Completed on public asb-tui main at GitHub-verified DCO commit
  524f0f5871a87b34c08b63b679ce5b27fd30a8b9. PR #6 delivered the lifecycle and PR #7 closed the
  acceptance-audit reuse edge case. Exact reviewed trees match both squash merges; signed-commit
  protection is restored. Final hosted run 34503439341 and trusted local run 34503439327 pass on
  exact main. Local evidence includes 90.55% line coverage, full locked tests, lint/docs/schema,
  workflow/shell/privacy gates, and ASB isolation. Product-side top-level asb tui routing remains a
  separate dependency and is not claimed by this standalone completion.
