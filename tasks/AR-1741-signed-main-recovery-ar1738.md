---
{
  "branch": "repair/ar-1741-signed-main-recovery-ar1738",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-08T12:10:37+00:00",
  "depends_on": [],
  "id": "AR-1741",
  "next_action": "Monitor exact protected-main post-merge workflows for bbe25d0 (runs 37761614825, 37761614612, 37761614776, 37761614739, 37761614829, 37761614748, 37761614807); after all required workflows are green, release AR-1741 and update/release AR-1738 with exact signed-main evidence.",
  "observed_branch": "repair/ar-1741-signed-main-recovery-ar1738",
  "observed_dirty": 0,
  "observed_head": "0c100e4624a6dc3972660dc24713940d87753709",
  "owner": "codex-ar1738-rustup-permission",
  "plan": "../plans/AR-1741-signed-main-recovery-ar1738.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1741.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Recover signed protected-main provenance after the preserved GitHub-generated AR-1738 merge.",
  "task_revision": 21,
  "title": "Signed protected-main recovery for AR-1738",
  "updated_at": "2026-10-08T10:19:49+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1741-signed-main-recovery-ar1738"
}
---

AR-1741 is an independent publication-integrity recovery for AR-1738/PR #504.
Preserve historical merge `2f7387e`; do not rewrite or force-update protected
main. AR-1740 is a separate publication incident and is intentionally excluded.

- 2026-10-08T09:48:24+00:00: Claimed by codex-ar1738-rustup-permission.

- 2026-10-08T09:49:37+00:00: Recorded command exit 0; command argv SHA-256
  8955c1a4f9d012421dbe400da15b32bf2b4d6fd81e7b7229f8d7a55bcc174a6c.

- 2026-10-08T09:51:32+00:00: Heartbeat by codex-ar1738-rustup-permission.

- 2026-10-08T09:51:39+00:00: Forward-only descendant 0c100e4 has parent current protected main
  a9abcf2 and identical tree (zero product changes), SSH signature and matching DCO verified. Push
  remains blocked by recurring shared handoffctl lock; no remote effect yet.

- 2026-10-08T09:56:06+00:00: Recorded command exit 0; command argv SHA-256
  8b345685eff1898e70d2ebe7333b76c16a982b199126a5513c0641f29e46f3d9.

- 2026-10-08T09:59:27+00:00: Recorded command exit 0; command argv SHA-256
  c421c34f778e6835543f9cd6bd52216a6bf5a5fd52ad00e973d1bb476cff16eb.

- 2026-10-08T10:07:06+00:00: Heartbeat by codex-ar1738-rustup-permission.

- 2026-10-08T10:07:09+00:00: Recorded command exit 0; command argv SHA-256
  1709c8ef0a4e862e1aecf02723498ed1079408e720748fcf58ca984ae4cd6519.

- 2026-10-08T10:07:41+00:00: PR #508 is open at exact base a9abcf2e63f761e314593e9abc6bf074b7418e5e
  and head 0c100e4624a6dc3972660dc24713940d87753709. Independent review: clean zero-diff tree, Good
  SSH signature, matching DCO, parent is exact protected main. Checks pass except Repository quality
  and emulated aarch64, both still in progress; Rust checks now pass. Main remains unchanged.

- 2026-10-08T10:08:42+00:00: Recorded command exit 1; command argv SHA-256
  ad2ec1484c5019c384fff25680d94fc0ba872c244fe086172a8de096de50d4dc.

- 2026-10-08T10:09:31+00:00: Recorded command exit 0; command argv SHA-256
  04e24d198ebe314f7a737e475ffe70f6fca331dab2d9be16d14cf72f1fae8573.

- 2026-10-08T10:10:05+00:00: Recorded command exit 0; command argv SHA-256
  5e93c159288a84c74ea030275ba3a0d35c7ca99714c62b6d5612243578565a39.

- 2026-10-08T10:10:37+00:00: Heartbeat by codex-ar1738-rustup-permission.

- 2026-10-08T10:10:40+00:00: Recorded command exit 0; command argv SHA-256
  1709c8ef0a4e862e1aecf02723498ed1079408e720748fcf58ca984ae4cd6519.

- 2026-10-08T10:12:12+00:00: PR #508 locally signed-integrated through tools/integration/merge_pr.py
  as protected-main bbe25d0c516b29a38a66908cbb025204dfe9e4d8. Exact parents
  a9abcf2e63f761e314593e9abc6bf074b7418e5e and 0c100e4624a6dc3972660dc24713940d87753709; tree
  befcb782d6ce260d1d4dd0e4fe25c2fb0b1b900f; Martin Beck signed with matching DCO. Local repository
  policy passed. Post-merge workflows running; retain open until all green.

- 2026-10-08T10:18:21+00:00: Recorded command exit 1; command argv SHA-256
  b1d1e67cd1f5fe96358fa2af9c033880293a7b5c23134ce4fe937d4b7db1e561.

- 2026-10-08T10:18:54+00:00: Recorded command exit 1; command argv SHA-256
  bb4f017ccd88e04b32fea9fb881aded8f460dd9c579bcb1c9eb939008baa4b0e.

- 2026-10-08T10:19:49+00:00: Recorded command exit 1; command argv SHA-256
  885b2d4bd1f380232b3efb1c37557b964ff0cf7c3d124b2e4a76698df7f1bd33.
