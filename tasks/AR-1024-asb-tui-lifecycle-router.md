---
{
  "branch": "feature/asb-tui-lifecycle-router",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-10T22:52:27+00:00",
  "depends_on": [
    "AR-0820",
    "AR-0821",
    "AR-0822",
    "AR-1022",
    "AR-1023"
  ],
  "id": "AR-1024",
  "next_action": "Add signed synthetic channel/bundle and filesystem/delegation adversarial tests, incorporate the pending asb-tui controlling-TTY and foldhash-Zlib contract revision, then harden docs/schema and run focused clippy/tests.",
  "observed_branch": "feature/asb-tui-lifecycle-router",
  "observed_dirty": 5,
  "observed_head": "32df706413a6f165f086941426a5c793bd5e01e8",
  "owner": "codex-ar1024-router-20260910",
  "plan": "../plans/AR-1024.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Add the trusted ASB-side bootstrap and lifecycle router for the optional frontend.",
  "task_revision": 43,
  "title": "Implement `asb tui` lifecycle routing",
  "updated_at": "2026-09-10T21:00:31+00:00",
  "worktree_key": "agent-systems-benchmark-asb-tui-lifecycle-router"
}
---
Implement `asb tui install`, launch, status, upgrade, doctor and remove without linking the frontend
into the ASB runtime. ASB owns trusted channel discovery and first verification; the exact verified
candidate independently reverifies and performs its transactional lifecycle.

Acceptance requires safe default XDG paths, signed immutable release selection, downgrade and
redirect resistance, bounded/resumable acquisition, offline support, typed delegation, network-free
status/launch/remove, removal of the legacy bundled-TUI bootstrap assumption, adversarial tests,
complete gates, exact-head CI and post-merge verification.

- 2026-09-10T20:31:20+00:00: AR-1022 and AR-1023 are durably done; begin the trusted ASB-side
  lifecycle router without renderer or UI ownership.

- 2026-09-10T20:31:26+00:00: Claimed by codex-ar1024-router-20260910.

- 2026-09-10T20:32:17+00:00: Recorded command exit 0; command argv SHA-256
  1629c9f9a24c48825d6b7660c64f1bb238f910e17d68a4d23bb57a3efb94f807.

- 2026-09-10T20:34:34+00:00: Initial audit complete at exact ASB origin/main
  32df706413a6f165f086941426a5c793bd5e01e8. Read repository AGENTS, DEVELOPMENT, ARCHITECTURE,
  QUALITY, AR task/plan, current asb-cli/asb-bundle/control boundaries, and exact merged asb-tui
  d58eda9 lifecycle request/response/bundle contracts. First implementation target is
  crates/asb-cli/src/tui.rs with crates/asb-cli/tests/tui_lifecycle.rs; ASB will contain only
  trusted installation/lifecycle routing, never Ratatui/Crossterm/render/UI application code or a
  source link to asb-tui.

- 2026-09-10T20:35:59+00:00: Recorded command exit 1; command argv SHA-256
  bc1a8e34e1b3da829c192d079e163f6453d39b19ad42cea81cd9a33bf24802b8.

- 2026-09-10T20:36:31+00:00: Recorded command exit 2; command argv SHA-256
  b84823fb21760eb3782237a6d4cb3b2dd5929b7f0b5a350df8f49035886353b1.

- 2026-09-10T20:37:06+00:00: Recorded command exit 0; command argv SHA-256
  4de739f7381c22b5019c373288e1a0c2873ddd027cce8c343359e79b4c6da89e.

- 2026-09-10T20:42:32+00:00: Recorded command exit 0; command argv SHA-256
  e188734dfe2986b93a79c6ca4b955defa2be74011e2aa366405287600628c353.

- 2026-09-10T20:42:56+00:00: Recorded command exit 101; command argv SHA-256
  5b8d0bdcae55fb2393a6d3bf3d7fadd7798168cbc1aa5e7804a4e9d4baf455c0.

- 2026-09-10T20:43:28+00:00: Recorded command exit 101; command argv SHA-256
  6dd9ffc774942c0e5de045fd4b4629a14ac7f8326afeba88ccaf0e201b920d80.

- 2026-09-10T20:44:43+00:00: Recorded command exit 0; command argv SHA-256
  ae5320c8c3c211585aa3e94bfb6bd732b4d9b0fd611f36c71a8af96b76f7e15a.

- 2026-09-10T20:44:56+00:00: Recorded command exit 101; command argv SHA-256
  057d88de3f2510f09ec097ec56abf31a365aeb8e65924db862f2c3f4701f98e4.

- 2026-09-10T20:45:05+00:00: Recorded command exit 0; command argv SHA-256
  e64948d9ee0f449f49bfebd1ce3821b2a82ab3e973f45c0fb73af564729a2833.

- 2026-09-10T20:46:38+00:00: Recorded command exit 0; command argv SHA-256
  3f9764d445632316cebc1bc2a607d4643047a228bb46dc635dc1f7cf1af50e8e.

- 2026-09-10T20:46:52+00:00: Recorded command exit 0; command argv SHA-256
  51d87bccac489dd034a1b922037aa778b9a245af319c0ba9dcf6fb65d06e6cb2.

- 2026-09-10T20:47:04+00:00: Recorded command exit 101; command argv SHA-256
  e64948d9ee0f449f49bfebd1ce3821b2a82ab3e973f45c0fb73af564729a2833.

- 2026-09-10T20:47:13+00:00: Recorded command exit 0; command argv SHA-256
  8526ad54d28f0be2d2f20d79c0ce9d80a9d7dc0dcddd55aa4f4b2486abd3f782.

- 2026-09-10T20:47:27+00:00: Recorded command exit 0; command argv SHA-256
  e64948d9ee0f449f49bfebd1ce3821b2a82ab3e973f45c0fb73af564729a2833.

- 2026-09-10T20:47:54+00:00: Recorded command exit 0; command argv SHA-256
  410aaa85bbc4e367957471f5f39e6a8ea35ba12e0c01cda79db8343bde2b6334.

- 2026-09-10T20:48:22+00:00: Early compiling checkpoint: new private asb-cli tui router module and
  typed dispatch compile at ASB base 32df706; six parser/XDG/channel/redirect/response tests pass.
  XDG roots are split correctly: installs in DATA, durable rollback/lock in STATE, resumable
  artifacts/index in CACHE. Fixed absolute root-owned non-writable curl/ssh-keygen tools, curl
  config disabled, manual HTTPS redirect allow-list for github.com to
  release-assets.githubusercontent.com, bounded range retry/resume, static trust root,
  manifest/artifact/document verification, memfd candidate delegation, network-free local
  operations, and narrow foldhash 0.2.0 Zlib policy are present. Cross-repo launch and license fixes
  are coordinated with AR-1010. Failure classification: initial locked build exit 101 only meant
  Cargo.lock needed the intentional direct rustix dependency update; subsequent exit 101 exposed two
  ordinary compile errors in the new parser/lifetime code and they were fixed; one direct cargo
  invocation failed before compile because rustc PATH was omitted, then the exact command with fixed
  toolchain PATH passed. The check+test wrapper did execute both newline-separated commands; it was
  not an argv concatenation.

- 2026-09-10T20:49:42+00:00: Recorded command exit 0; command argv SHA-256
  a6b6611dec337de11366052ecacbcfb330c65e3ca7da863d0695e1a79ab4978b.

- 2026-09-10T20:52:27+00:00: Heartbeat by codex-ar1024-router-20260910.

- 2026-09-10T20:52:39+00:00: Recorded command exit 0; command argv SHA-256
  55567313761b549ce8f8adb2244cf2f1912794007c8beedd347ef9fd5698afa6.

- 2026-09-10T20:52:58+00:00: Recorded command exit 0; command argv SHA-256
  02b11b15e5b349a7369d15211df14b36f417284d989ebddc0bb42a0bcc9e0a05.

- 2026-09-10T20:53:20+00:00: Recorded command exit 101; command argv SHA-256
  8d9b771dcd2f0ed50e24c471e556561595dcbab100bf2ff2c24324c0b7e2f70c.

- 2026-09-10T20:53:37+00:00: Recorded command exit 0; command argv SHA-256
  f9d8632cc067c972175fda0956b525a6d140775ec0e9a0a0e6a150937a149115.

- 2026-09-10T20:53:55+00:00: Recorded command exit 127; command argv SHA-256
  be89fd8e029ffe8f0507fc79ee87cc4b8b2ee92d6fa3fea997327fa17f4ab112.

- 2026-09-10T20:54:09+00:00: Recorded command exit 0; command argv SHA-256
  55567313761b549ce8f8adb2244cf2f1912794007c8beedd347ef9fd5698afa6.

- 2026-09-10T20:54:26+00:00: Recorded command exit 0; command argv SHA-256
  8d9b771dcd2f0ed50e24c471e556561595dcbab100bf2ff2c24324c0b7e2f70c.

- 2026-09-10T20:56:59+00:00: Recorded command exit 0; command argv SHA-256
  55567313761b549ce8f8adb2244cf2f1912794007c8beedd347ef9fd5698afa6.

- 2026-09-10T20:57:12+00:00: Recorded command exit 0; command argv SHA-256
  02b11b15e5b349a7369d15211df14b36f417284d989ebddc0bb42a0bcc9e0a05.

- 2026-09-10T20:57:25+00:00: Recorded command exit 101; command argv SHA-256
  8d9b771dcd2f0ed50e24c471e556561595dcbab100bf2ff2c24324c0b7e2f70c.

- 2026-09-10T20:57:57+00:00: Recorded command exit 0; command argv SHA-256
  233882b20224a4e0a62d15d02f069bd45c5497f370bb31a057f4457452eedd7f.

- 2026-09-10T20:59:22+00:00: Recorded command exit 0; command argv SHA-256
  deedd4e90674e56cc8ed15d74233747fe45d077b2bea326a3e9f5b77b2c4c574.

- 2026-09-10T20:59:35+00:00: Recorded command exit 0; command argv SHA-256
  55567313761b549ce8f8adb2244cf2f1912794007c8beedd347ef9fd5698afa6.

- 2026-09-10T20:59:54+00:00: Recorded command exit 101; command argv SHA-256
  02b11b15e5b349a7369d15211df14b36f417284d989ebddc0bb42a0bcc9e0a05.

- 2026-09-10T21:00:12+00:00: Recorded command exit 0; command argv SHA-256
  ae507c6a4ad29331ccc4257c357817ce28a6c6107bc82aca746f8065a74fe40e.

- 2026-09-10T21:00:31+00:00: Recorded command exit 0; command argv SHA-256
  02b11b15e5b349a7369d15211df14b36f417284d989ebddc0bb42a0bcc9e0a05.
