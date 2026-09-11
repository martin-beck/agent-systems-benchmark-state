---
{
  "branch": "fix/tmux-pane-foreground-group-recovery",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-11T03:24:35+00:00",
  "depends_on": [],
  "id": "AR-1044",
  "next_action": "Await fresh independent immutable approval of PR #14 exact head 837403aeb37fcfb335d2fc2491d5a58b17baede7; do not merge without root authorization.",
  "owner": "codex-ar1044-tmux-foreground-20260911",
  "plan": "../plans/AR-1044.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Bind tmux cleanup to the exact pane TTY foreground process group across acquisition and signalling.",
  "task_revision": 56,
  "title": "Recover tmux foreground-group qualification",
  "updated_at": "2026-09-11T02:02:32+00:00",
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

- 2026-09-11T01:39:59+00:00: Recorded command exit 0; command argv SHA-256
  3bedfae4b05ced973d362969c59e8709e5ba3635e14df1a05420eeacfb1905b4.

- 2026-09-11T01:40:32+00:00: Recorded command exit 0; command argv SHA-256
  5b022eb3cfb16f04f46dbf154f5726b2402a5b21a5684c7503fe733c6bdefee6.

- 2026-09-11T01:41:02+00:00: Recorded command exit 0; command argv SHA-256
  e87bab0801aa42b012ea421cead159668e191828a3b8e4c0b65028bf9cc79dea.

- 2026-09-11T01:41:20+00:00: Recorded command exit 101; command argv SHA-256
  8b308d114fb77d82deaa4831d37f75a32c4dc245540300fe6ee6a289566df967.

- 2026-09-11T01:41:46+00:00: Recorded command exit 0; command argv SHA-256
  9b02a411cddf98413dac4847b94562ff8d277fd87434a5928523b69e69f124ef.

- 2026-09-11T01:42:03+00:00: Recorded command exit 101; command argv SHA-256
  540dbc79044df09999358fc20ebb5c44ea838270b6733fe4031e720b59356d1b.

- 2026-09-11T01:42:18+00:00: Recorded command exit 0; command argv SHA-256
  089dcf5812c261d4d2ce655f1747d3789d4b57ac552bf4e9ae94331b406157e8.

- 2026-09-11T01:42:40+00:00: Recorded command exit 101; command argv SHA-256
  602fbfc4f73f1c11c6f1379da75f5e489da379786910142c56d4c28f3bd518e8.

- 2026-09-11T01:43:07+00:00: Recorded command exit 101; command argv SHA-256
  c81a0839c8a794fa1c4eef39f2c4c39e2fedd42e32b9ec2542ea530b5a1d8c59.

- 2026-09-11T01:43:32+00:00: Recorded command exit 101; command argv SHA-256
  f479727b96c121768a5fa11df028df6a8f3d38dc47e3706f2439325ddbf20124.

- 2026-09-11T01:44:04+00:00: Recorded command exit 0; command argv SHA-256
  3ad0acd37f272ba8b84e79c9bb2fa0eec5cf1103e33793e7b286da01ff4be1b5.

- 2026-09-11T01:44:34+00:00: Recorded command exit 101; command argv SHA-256
  72f9adbae99cf0f86b5fc8caae43b569b3f8a256b67b3187e56ece753069b769.

- 2026-09-11T01:45:41+00:00: Recorded command exit 101; command argv SHA-256
  9fffaaed90267d6fd3e2eb7629d96b340b2f4286d4de3760535931b1732d7cd5.

- 2026-09-11T01:46:27+00:00: Recorded command exit 0; command argv SHA-256
  c452cee192a9e93b93a0f3aac75a8415e1dc1718372a5d83e3289e9b4c21607e.

- 2026-09-11T01:46:50+00:00: Recorded command exit 0; command argv SHA-256
  811fb270484aa189cf8cecfc4535f89f71c67eb80bac5306c18de1a556c556ee.

- 2026-09-11T01:47:22+00:00: Recorded command exit 101; command argv SHA-256
  a912583cd6123752f2acf27f485b3138736a7a8f94c0ff1ea993edc9c2d19d60.

- 2026-09-11T01:47:45+00:00: Recorded command exit 0; command argv SHA-256
  a4feb300095dcd7455987b66d6d44eac9bc79ced5fa378beb9bf2d07476b05e9.

- 2026-09-11T01:48:06+00:00: Recorded command exit 101; command argv SHA-256
  f479727b96c121768a5fa11df028df6a8f3d38dc47e3706f2439325ddbf20124.

- 2026-09-11T01:48:43+00:00: Recorded command exit 0; command argv SHA-256
  c4982480cb0ad1eb94a3ec09335c197c22aa38dee226d908996a72ade7ac8032.

- 2026-09-11T01:49:20+00:00: Recorded command exit 0; command argv SHA-256
  93291fe9fa7cd7a6b764bdf647c5e3b8c555bd809614f7f0284c8927e414238d.

- 2026-09-11T01:49:56+00:00: Recorded command exit 0; command argv SHA-256
  933aaaba4a89ecfb7d2c18254d679224e4beeb157c59c9c07729925291c6f75f.

- 2026-09-11T01:50:21+00:00: Recorded command exit 101; command argv SHA-256
  9ffc863d9338d19be9be7fc47a0404a183231e46c24a9fa96b90c47ec4580692.

- 2026-09-11T01:51:28+00:00: Recorded command exit 0; command argv SHA-256
  d2fc4fdb09e8d0049c459a9138c4e00f31a76757bfb684da39d3200405799c38.

- 2026-09-11T01:51:54+00:00: Recorded command exit 0; command argv SHA-256
  9ffc863d9338d19be9be7fc47a0404a183231e46c24a9fa96b90c47ec4580692.

- 2026-09-11T01:52:13+00:00: Recorded command exit 0; command argv SHA-256
  33d3c846b7b3330e8e73a2bffca668563ef322068c7a66cace1a9b96b128278a.

- 2026-09-11T01:52:53+00:00: Recorded command exit 0; command argv SHA-256
  0d8078313ba38ee5d799de843b530db571377fd17e68dcd6b242147665023996.

- 2026-09-11T01:53:11+00:00: Recorded command exit 0; command argv SHA-256
  893d3b61d5d9934f32f0a018034408c68721d0a4a51f67cf51b1e34bed30641a.

- 2026-09-11T01:53:39+00:00: Recorded command exit 1; command argv SHA-256
  717978f3c0726320f0718e544c9c3ffc2dc14143fcafc99192bbeb8bd5ac18ef.

- 2026-09-11T01:55:23+00:00: Recorded command exit 0; command argv SHA-256
  2bc1c8615be61bab14ce81778e6cb2fc5374324b7fc72e4bc60ce6da127a7dff.

- 2026-09-11T01:55:49+00:00: Second-review repair exact signed+DCO head
  837403aeb37fcfb335d2fc2491d5a58b17baede7 tree a06c628a16db0fd3f3bf9204b9dadf277168cdd0 is pushed
  to draft PR #14. It adds generation-bound pane/leader authority, stable TTY dev/ino/rdev, pre-TERM
  and pre-KILL exact reobservation with signal-recorder tests, global PID/leader uniqueness, safe
  server-generation/socket unlink, symlink_metadata NotFound absence,
  dangling/symlink/nondevice/wrong-owner negatives and hostile TMUX_TMPDIR isolation. Exact-head
  Repository quality run 34552452268 passed. Local fmt, clippy, complete locked tests including 20
  terminal tests, rustdoc, release, deny, audit, 91.42% line coverage,
  schema/release/publication/promoted-self-test, JSON, shell/workflow, gitleaks and clean-tree gates
  pass. One full-gate attempt used a wrong guessed full hash and ran nothing; the next retry hit
  coordinator lock before execution; the corrected wrapped exact-head run passed fully.

- 2026-09-11T02:02:12+00:00: Recorded command exit 0; command argv SHA-256
  5630689fe7ba507ebd137ce0cc3d9682f2d4965ea36f8b9a780f713958daca93.

- 2026-09-11T02:02:32+00:00: Recorded command exit 101; command argv SHA-256
  fa6f500e5e6da41ea9b1e9d60fdb498ba8ccfb22c74039e7392f2516bb540695.
