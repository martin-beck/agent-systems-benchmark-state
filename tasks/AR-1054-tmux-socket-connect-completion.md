---
{
  "branch": "fix/tmux-socket-connect-completion",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-11T06:29:21+00:00",
  "depends_on": [],
  "id": "AR-1054",
  "next_action": "Create signed+DCO one-file checkpoint, run clean-tree coverage/promoted-self-test and remaining gates, then freeze for fresh immutable review before publication.",
  "owner": "codex-ar1054-tmux-connect-completion-20260911",
  "plan": "../plans/AR-1054.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Repair trusted tmux socket connection completion without weakening authenticated cleanup authority.",
  "task_revision": 32,
  "title": "Repair tmux socket connection completion",
  "updated_at": "2026-09-11T04:42:02+00:00",
  "worktree_key": "agent-systems-benchmark-asb-tui-tmux-socket-connect-completion"
}
---

Trusted-main run 34562090773 at exact asb-tui merge
7a398032246aa935b13b5d3139949c2375fa7309 failed five live tmux fixtures at the closed
`socket_connection_unavailable` stage before peer credentials. Correct only the proven Linux
AF_UNIX `EAGAIN` and bounded completion portability gap under the detailed plan. No renderer, UI,
lifecycle protocol, dependency, workflow or ASB source change is in scope.

- 2026-09-11T04:29:14+00:00: Approved narrow recovery from exact trusted-main failure 34562090773;
  scope remains one test harness file and dependencies are satisfied.

- 2026-09-11T04:29:21+00:00: Claimed by codex-ar1054-tmux-connect-completion-20260911.

- 2026-09-11T04:29:42+00:00: Recorded command exit 0; command argv SHA-256
  3007ebf91e08cba6b09952c5654222362fb1a001d9f38b0a7912fbd43ae03b79.

- 2026-09-11T04:29:56+00:00: Recorded command exit 0; command argv SHA-256
  60bb2a547688bd82301e613edaf13eeb04d7e7624fe86f9e6e5d3bb5263c099f.

- 2026-09-11T04:30:30+00:00: Recorded command exit 0; command argv SHA-256
  fbbb8baab4c150ce20bdc8d85401d2dfc943fee58fc3b2bdc22394acd74288e0.

- 2026-09-11T04:30:38+00:00: Recorded command exit 0; command argv SHA-256
  738ea78cf8089e5e2a6e3ad890832a7400ecd21551f0cae953caa6f1d2788c9b.

- 2026-09-11T04:32:06+00:00: Recorded command exit 2; command argv SHA-256
  d420898b33bff8cc18958320c098878727cf3410391c337a6a1d55867ce16381.

- 2026-09-11T04:33:01+00:00: Recorded command exit 127; command argv SHA-256
  a7fcc48b487f6ca0e003075e415135885fdf22dedc50f6395e1eb3a101bce9f0.

- 2026-09-11T04:33:09+00:00: Recorded command exit 127; command argv SHA-256
  b772de0eaa2d5e35cfe9faa9327022c613818de3c6210baed07cad4eaaff64f5.

- 2026-09-11T04:33:17+00:00: Recorded command exit 127; command argv SHA-256
  c6210b206fb6900ad6b9d4c0d3ed90a3774ea83715c7525efc347be3cca33975.

- 2026-09-11T04:33:45+00:00: Recorded command exit 0; command argv SHA-256
  89e67f83c5b87b12f7ea4e4eac30afc7561f9c2142bf7fb870e1aa7afb91015f.

- 2026-09-11T04:34:02+00:00: Recorded command exit 0; command argv SHA-256
  cb0fb6ea8f922bcdde68326122fdceeceb574fdf2981e0d39b8e024ea54c781b.

- 2026-09-11T04:34:10+00:00: Recorded command exit 0; command argv SHA-256
  c61d6000289bb9a9f61970028fe23a908334cff4b2b0e428c2266562578c268c.

- 2026-09-11T04:34:39+00:00: Recorded command exit 0; command argv SHA-256
  41cf1013f8d8cc0d1f306e0c5995f4d015372f0e98badfe4d2528ff6a76eb907.

- 2026-09-11T04:35:48+00:00: Recorded command exit 0; command argv SHA-256
  8f9a2f01f32c7930505a9b922f645c7e245a4afb2e214f0af401c092ae92636a.

- 2026-09-11T04:36:39+00:00: Recorded command exit 0; command argv SHA-256
  c167b7bdd1405febc7d3ef88a0ac5748c769e4698beb68f870e28821a480740f.

- 2026-09-11T04:37:15+00:00: Recorded command exit 0; command argv SHA-256
  7fd1fb5e18a7d7e7cd893f135f06d3f104e880f46818cda9b021719640430015.

- 2026-09-11T04:37:44+00:00: Recorded command exit 0; command argv SHA-256
  966e9967e63e57d6c13597e84ca0cad56482dca6cc5fab80639bfa4d59431dba.

- 2026-09-11T04:37:53+00:00: Recorded command exit 0; command argv SHA-256
  5777a93f0fd4deeadbb655485c169d7e15e46bdd9e5045d07e5a89c68808fa0a.

- 2026-09-11T04:38:23+00:00: Recorded command exit 0; command argv SHA-256
  2b76dd432a68c57c2088905d327c55446e8500ff18672c7e1fd0c7bbc687df52.

- 2026-09-11T04:38:32+00:00: Recorded command exit 0; command argv SHA-256
  15cc433c17e40b6aa86f1a21e468b19aa95d4189ea8fdbf16e1376640912cee6.

- 2026-09-11T04:39:09+00:00: Recorded command exit 1; command argv SHA-256
  a3e48605bbd6d573c2c085de07f82c8eeff7211d9d47a9164a6731122c03b25f.

- 2026-09-11T04:39:28+00:00: Recorded command exit 1; command argv SHA-256
  62b7706163ba1a3b68f670769a09f4f92625d929fbdb17101b1314f17991920b.

- 2026-09-11T04:39:55+00:00: Recorded command exit 0; command argv SHA-256
  2bba44e0419b2e3593bbeb505559dbd837b6e4267578e7241f3e4f4d5a34de7b.

- 2026-09-11T04:40:17+00:00: Implementation checkpoint: exact one-file test-harness diff now accepts
  Linux AF_UNIX EAGAIN or EINPROGRESS only as incomplete, requires bounded poll completion and exact
  zero SO_ERROR, and retains all peer/socket/process authority checks. New pure negatives cover bad
  errno, timeout/readiness, POLLNVAL, bad SO_ERROR length/status/value, NUL and overlong paths.
  Focused tests pass; full serial 29/29; five repeated serial suites 145/145; five repeated parallel
  suites 145/145; full locked tests, fmt, all-target Clippy, rustdoc, release, deny,
  schema/release/publication, shell/workflow and privacy gates pass. Three initial exit-127 commands
  omitted the wrapper-required absolute Cargo path and were invocation-only; corrected. Coverage
  exit 1 was expected clean-tree precondition on the intentional uncommitted diff. Cargo audit
  completed its scan with no advisory failure, then wrapper evidence hit coordinator LOCK_TIMEOUT;
  rerun after commit is required.

- 2026-09-11T04:40:25+00:00: Recorded command exit 0; command argv SHA-256
  4f439593a61e62e73569029a0402214af47dea78a1481008123b417d9a6f44fc.

- 2026-09-11T04:40:34+00:00: Recorded command exit 0; command argv SHA-256
  6fdd2b3f1d3bb17dd0fcfe201a707668aaa9afa5494ffb8c888875fb8396ff27.

- 2026-09-11T04:40:58+00:00: Recorded command exit 0; command argv SHA-256
  0687954b1b878c35f869678241639665e61e1bb41c7e299dffd3c9ad27135cef.

- 2026-09-11T04:41:30+00:00: Recorded command exit 0; command argv SHA-256
  a3e48605bbd6d573c2c085de07f82c8eeff7211d9d47a9164a6731122c03b25f.

- 2026-09-11T04:41:44+00:00: Recorded command exit 0; command argv SHA-256
  4549587201f3d962813ec0ddfa80623d5727473be3fbd257f5a29f765f5df349.

- 2026-09-11T04:42:02+00:00: Recorded command exit 0; command argv SHA-256
  a33d3917ce062defa3ccce7dce220b9f79ff7aa5d00138ae7b51796630352117.
