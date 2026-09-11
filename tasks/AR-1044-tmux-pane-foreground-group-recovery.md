---
{
  "branch": "fix/tmux-pane-foreground-group-recovery",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-11T03:24:35+00:00",
  "depends_on": [],
  "id": "AR-1044",
  "next_action": "Await immutable review of exact signed head df96e13b58ddcab0000ed2f0947e5217f43f23ae; if approved, push/open draft PR and require exact-head CI before any merge.",
  "owner": "codex-ar1044-tmux-foreground-20260911",
  "plan": "../plans/AR-1044.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Bind tmux cleanup to the exact pane TTY foreground process group across acquisition and signalling.",
  "task_revision": 24,
  "title": "Recover tmux foreground-group qualification",
  "updated_at": "2026-09-11T01:39:23+00:00",
  "worktree_key": "agent-systems-benchmark-asb-tui-tmux-pane-foreground-group-recovery"
}
---

AR-1042 merged the reviewed test-only readiness repair as `eb4960e`, but trusted-main run
34550197610 proved that tmux's pane PID is not necessarily the pane's foreground process-group ID.
Recover the qualification without weakening ownership: acquire and retain one bounded exact
`pane_pid`/`pane_tty`/foreground-`tpgid` observation, and signal only after the same live tuple is
revalidated. Always clean the uniquely owned tmux server and socket even when group authority is
absent or changes. Do not change renderer or application behavior.


- 2026-09-11T01:24:35+00:00: Claimed by codex-ar1044-tmux-foreground-20260911.

- 2026-09-11T01:24:55+00:00: Recorded command exit 128; command argv SHA-256
  010ac80d31c060eeee068ab0f46eb6c978ebd81062aa03d4c7238b338840d59a.

- 2026-09-11T01:25:21+00:00: Recorded command exit 0; command argv SHA-256
  5a44054869e3537ce393c5cbc4da3dbf228826668ae93ab7a7fcd4c5f6179014.

- 2026-09-11T01:26:17+00:00: Recorded command exit 0; command argv SHA-256
  2e596cb82e9b821ae42d346f01fdd09597041e9565254ecec65309ac9f1c68db.

- 2026-09-11T01:27:13+00:00: Recorded command exit 0; command argv SHA-256
  59a4fe48a4cb5572d41c29ef277233a29552124616ef80130756f655e34e5bb3.

- 2026-09-11T01:28:21+00:00: Recorded command exit 0; command argv SHA-256
  80a5971b926abd295b0c7a9540dfd3ece1820852f901a9898aa30789e01bb939.

- 2026-09-11T01:28:38+00:00: Recorded command exit 1; command argv SHA-256
  509f2a1a8c228ebfca9aeed50676e871ec8024023ff82a34fa3fba94372826d1.

- 2026-09-11T01:28:56+00:00: Recorded command exit 0; command argv SHA-256
  81a66a0207bbc220eb89d651964780b1b4a2fcd9c0502bcb10fe8e0a9d350432.

- 2026-09-11T01:29:16+00:00: Recorded command exit 0; command argv SHA-256
  92146577f96ba133ffab932c367cad7686eede858447e9b18549f813f83f8104.

- 2026-09-11T01:29:58+00:00: Recorded command exit 0; command argv SHA-256
  6b54d6c5d1e2c4627bb63da7deb1b012ba23853a5629ee0862765f77f1c7c657.

- 2026-09-11T01:30:16+00:00: Recorded command exit 0; command argv SHA-256
  359d7d17ac7319f65d735a60c7e8f25bdc80fef5c6a1cafe164dda65b290b3c8.

- 2026-09-11T01:31:04+00:00: Recorded command exit 0; command argv SHA-256
  53e522ab85bc4fa487858f9433b43cade496ba501f57125c00f7761eef47b4aa.

- 2026-09-11T01:31:26+00:00: Recorded command exit 0; command argv SHA-256
  7f2f1bf633d124e92720c977b4c5895866b6571025f80a45b15b2985734f255e.

- 2026-09-11T01:31:57+00:00: Dirty test-only implementation replaces pane_pid==PGID with bounded
  pane_pid/pane_tty/tpgid/UID/EUID observation and exact pre-signal revalidation. Early review
  blockers are fixed: ps receives pts/N, all TTY rows must share the pane foreground tpgid, an exact
  current-UID/EUID foreground leader is required, and inconsistent/unrelated/wrong-UID fixtures
  reject. Parser, HUP-resistant cleanup, no-authority cleanup, real tmux+screen focused tests and
  the serial 17-test terminal suite pass. Classified earlier failures: nonexistent canonical asb-tui
  alias and fmt drift were invocation/formatting issues corrected before tests.

- 2026-09-11T01:32:48+00:00: Recorded command exit 0; command argv SHA-256
  d4e8f51a5daf7c90b1e457d35590e80cb31143f850b7c809b39684ab74c003d8.

- 2026-09-11T01:33:45+00:00: Recorded command exit 1; command argv SHA-256
  ef7de63c74a18c5d73f593448971469ccdba124d2ab77ed9d3b5cd4690542433.

- 2026-09-11T01:34:05+00:00: Recorded command exit 0; command argv SHA-256
  860c092e769021f88f991494cab3ea396da5be2cd56564bf481614bb91e4d47c.

- 2026-09-11T01:34:22+00:00: Recorded command exit 1; command argv SHA-256
  469ec7a2f6ed766402eaea1d531baa13ab5bb991ac0521cd2d49ba549b9d6389.

- 2026-09-11T01:34:54+00:00: Recorded command exit 0; command argv SHA-256
  776123a35c3410e3f29a88e02d855aebbea5faed148fed9dbf8cd395b45b084c.

- 2026-09-11T01:35:53+00:00: Recorded command exit 0; command argv SHA-256
  ff16574c0d1d5fe5ea93a7744a5ea951ed0419b39fe001570155693997b1f305.

- 2026-09-11T01:36:31+00:00: Frozen signed+DCO head df96e13b58ddcab0000ed2f0947e5217f43f23ae tree
  a8528cb923c810217f51703dd4710873555b39d9 is one test-only file (+207/-45) over eb4960e. Five
  consecutive serial 17-test terminal suites passed with zero exact-worktree-binary leaks after
  each. Full fmt, clippy, locked tests, rustdoc, release build, deny, audit, coverage 91.44% lines,
  schema/release/publication/promoted-self-test, JSON, shell/workflow, gitleaks and clean-tree gates
  pass. Exit 1 at 01:33:45 occurred at cargo-audit after prior gates; isolated identical rerun
  passed and is classified transient advisory fetch/tool state. Exit 1 at 01:34:22 was expected
  clean-coverage refusal because the reviewed change was still dirty; committing signed+DCO then
  rerunning coverage resolved it. Root early diff review found no blocker. Head is intentionally not
  pushed pending immutable review.

- 2026-09-11T01:37:28+00:00: Recorded command exit 0; command argv SHA-256
  71798ce202dbfe9c3939453be64634ff0f3bd0ce09805f0e810e68fe95f5bb59.

- 2026-09-11T01:39:23+00:00: Recorded command exit 0; command argv SHA-256
  a2d2960dda8abc1a5e41de826ed50546fd53c67c6f958d9995f4ef6ee1896929.
