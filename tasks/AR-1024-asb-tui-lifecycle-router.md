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
  "next_action": "Add signed-channel and resumable/truncation/concurrency negatives, validate copied schemas/docs, run clippy and full relevant gates, then commit for independent review after exact AR-1010 contract integration.",
  "observed_branch": "feature/asb-tui-lifecycle-router",
  "observed_dirty": 10,
  "observed_head": "32df706413a6f165f086941426a5c793bd5e01e8",
  "owner": "codex-ar1024-router-20260910",
  "plan": "../plans/AR-1024.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Add the trusted ASB-side bootstrap and lifecycle router for the optional frontend.",
  "task_revision": 100,
  "title": "Implement `asb tui` lifecycle routing",
  "updated_at": "2026-09-10T21:26:51+00:00",
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

- 2026-09-10T21:00:56+00:00: Recorded command exit 101; command argv SHA-256
  8d9b771dcd2f0ed50e24c471e556561595dcbab100bf2ff2c24324c0b7e2f70c.

- 2026-09-10T21:01:14+00:00: Recorded command exit 0; command argv SHA-256
  45060be3e3b5d7eed63146cdb9251eb8195e6892e9c6be97719b33a4296ea642.

- 2026-09-10T21:01:32+00:00: Recorded command exit 0; command argv SHA-256
  8d9b771dcd2f0ed50e24c471e556561595dcbab100bf2ff2c24324c0b7e2f70c.

- 2026-09-10T21:02:19+00:00: Recorded command exit 0; command argv SHA-256
  0e5d9ea9adc35471cba94f7f3a39823a04f5fcad71cb2ad16beef865e447b0b8.

- 2026-09-10T21:02:39+00:00: Recorded command exit 0; command argv SHA-256
  55567313761b549ce8f8adb2244cf2f1912794007c8beedd347ef9fd5698afa6.

- 2026-09-10T21:03:19+00:00: Recorded command exit 0; command argv SHA-256
  e61646471989e91b5cccd9472f16ad9a4d6b18bc6b12a9361a7d851d4b3954e5.

- 2026-09-10T21:03:41+00:00: Recorded command exit 101; command argv SHA-256
  f8330dc8efbb15e872bf9fe4188660b4b2de6a8a5b3f701aaad94d322c539548.

- 2026-09-10T21:03:59+00:00: Recorded command exit 0; command argv SHA-256
  d3c3ecae3544d5337d7b0ada526f5a31a5f25d5fc5bcfb648345fc704f4b7126.

- 2026-09-10T21:04:58+00:00: Recorded command exit 1; command argv SHA-256
  ad4e8d6ed5f1bac296b5566d07664f8ae17bf9ccf9e1e0b23ca9f2a38cc025bf.

- 2026-09-10T21:05:32+00:00: Recorded command exit 0; command argv SHA-256
  7c04a0365342099c136165e185c0ceca483e1ffae2ed988bd2e50ceac81eb8d8.

- 2026-09-10T21:05:58+00:00: Recorded command exit 0; command argv SHA-256
  f3d1cd413bc90fcd598f30b48836688b0657453f2f8104d593751b670228601b.

- 2026-09-10T21:06:14+00:00: Recorded command exit 0; command argv SHA-256
  55567313761b549ce8f8adb2244cf2f1912794007c8beedd347ef9fd5698afa6.

- 2026-09-10T21:06:31+00:00: Recorded command exit 101; command argv SHA-256
  8d9b771dcd2f0ed50e24c471e556561595dcbab100bf2ff2c24324c0b7e2f70c.

- 2026-09-10T21:06:47+00:00: Recorded command exit 1; command argv SHA-256
  ac1182096aad63aa934d18af7ca210c50bf93e2765e632b553c32f8de794281a.

- 2026-09-10T21:07:15+00:00: Recorded command exit 0; command argv SHA-256
  174b1f857537f1968d12e5ab1ec8a5134a4f9c164aa03e4538de14b2c831d2a9.

- 2026-09-10T21:09:37+00:00: Recorded command exit 0; command argv SHA-256
  8210a158d7eee7bf2be3c35db314b803883d4df175469304107d3a1e991073af.

- 2026-09-10T21:10:43+00:00: Recorded command exit 0; command argv SHA-256
  e4705f07d7d71f7c094a37cd7f82a8fa61669aa030785e77f7d756ae7b99401d.

- 2026-09-10T21:11:10+00:00: Recorded command exit 0; command argv SHA-256
  357f8ee41a50f5e06f1ee635c09c08532f0f077037a5d2d37942b709a1eb1a84.

- 2026-09-10T21:11:31+00:00: Recorded command exit 0; command argv SHA-256
  86ca7e43a384435a4ecef10e68ae7c04aec62cac05708e685e9a451802cd404c.

- 2026-09-10T21:11:57+00:00: Recorded command exit 0; command argv SHA-256
  1cad2da5f033527cd64bb9f661dca43913806b95dd150a779dd5c5fbe6cef5f4.

- 2026-09-10T21:12:13+00:00: Recorded command exit 0; command argv SHA-256
  55567313761b549ce8f8adb2244cf2f1912794007c8beedd347ef9fd5698afa6.

- 2026-09-10T21:12:26+00:00: Recorded command exit 0; command argv SHA-256
  8d9b771dcd2f0ed50e24c471e556561595dcbab100bf2ff2c24324c0b7e2f70c.

- 2026-09-10T21:12:39+00:00: Recorded command exit 0; command argv SHA-256
  f8330dc8efbb15e872bf9fe4188660b4b2de6a8a5b3f701aaad94d322c539548.

- 2026-09-10T21:13:26+00:00: Recorded command exit 0; command argv SHA-256
  5d580acac7db5545a09861864f44a04fd8589e40035d40b7c5fe6ce6877f8f54.

- 2026-09-10T21:13:42+00:00: Recorded command exit 101; command argv SHA-256
  a03abefc92ab061304aec011daf43ebbf849e03c9225e8955dad1566b6e008bb.

- 2026-09-10T21:14:02+00:00: Recorded command exit 0; command argv SHA-256
  67d03ba7cfc0a2e366990c51d47b02d0c1fdfa658b3d8292c7ff7b63dfea1af7.

- 2026-09-10T21:14:21+00:00: Recorded command exit 101; command argv SHA-256
  a03abefc92ab061304aec011daf43ebbf849e03c9225e8955dad1566b6e008bb.

- 2026-09-10T21:14:48+00:00: Recorded command exit 0; command argv SHA-256
  cd38c1c03b8a73a94dd31a1c2a572d469e2e89a50127c22430e61f5edddf216d.

- 2026-09-10T21:15:14+00:00: Recorded command exit 0; command argv SHA-256
  a03abefc92ab061304aec011daf43ebbf849e03c9225e8955dad1566b6e008bb.

- 2026-09-10T21:15:55+00:00: Recorded command exit 0; command argv SHA-256
  b482dd68b98ef01c43eab6cf20d64e0670623baee711b9bbc594e1aed7a5c7ff.

- 2026-09-10T21:16:32+00:00: Recorded command exit 0; command argv SHA-256
  64ad312e9c68658488bc4154fb98deff66918581433722fa63ca311481c4e31e.

- 2026-09-10T21:17:03+00:00: Recorded command exit 0; command argv SHA-256
  55567313761b549ce8f8adb2244cf2f1912794007c8beedd347ef9fd5698afa6.

- 2026-09-10T21:17:17+00:00: Recorded command exit 0; command argv SHA-256
  be3b1b9468f63440e624fa6b0263b0abfe4b90a7f018db5119ca1776053a0b92.

- 2026-09-10T21:17:32+00:00: Recorded command exit 0; command argv SHA-256
  c408d256d9d0c1290afa41c255859fd4309be2ba493b0dca7646dc6dac50584e.

- 2026-09-10T21:17:54+00:00: Hardening checkpoint: modified crates/asb-cli/src/tui.rs, lib.rs,
  Cargo.toml/lock, tests/tui_lifecycle.rs, schema/tui/v1, fixtures/tui, docs/ASB_TUI_LIFECYCLE.md
  and QUICKSTART. Resolved audit findings with strict verified success/operation response matrix and
  corrected verified_installation spelling; exact component/executable/coordinator/quality identity;
  sealed candidate memfd; crash-durable pending+accepted rollback floor; retained nofollow
  directory-fd reads/writes, unique exclusive temps, rename+parent fsync; truthful combined --launch
  network result; contradictory dry-run/launch rejection; stable absent/repeated-remove exits; exact
  upstream schema/signature pins; PTY fixture proving /dev/tty output, q exit, parseable lifecycle
  JSON and unchanged runner sentinel. AR-1010 exact interactive qualification head is
  10df38759371a4f6addb78dcfd970b65b3c90be5. Focused unit 14/14 and process tests 3/3 pass.
  Classified exits: compile/test fixture errors were source-test issues fixed; one filtered
  zero-test invocation was invocation-only and was rerun correctly; one wrapper exit was
  post-command coordinator AR-1036 dependency failure, repaired by root and doctor now passes.

- 2026-09-10T21:18:35+00:00: Recorded command exit 0; command argv SHA-256
  f7fa5ab86fbb46dde0f154965af10a8ff4dd2888e29c36def1e93a46dce7eac2.

- 2026-09-10T21:18:51+00:00: Recorded command exit 0; command argv SHA-256
  55567313761b549ce8f8adb2244cf2f1912794007c8beedd347ef9fd5698afa6.

- 2026-09-10T21:19:05+00:00: Recorded command exit 0; command argv SHA-256
  c408d256d9d0c1290afa41c255859fd4309be2ba493b0dca7646dc6dac50584e.

- 2026-09-10T21:19:43+00:00: Recorded command exit 0; command argv SHA-256
  e5329c2dd969cce59ebaf5eed3c459c126f242efe1f5a2672a80da370982c12c.

- 2026-09-10T21:19:56+00:00: Recorded command exit 0; command argv SHA-256
  55567313761b549ce8f8adb2244cf2f1912794007c8beedd347ef9fd5698afa6.

- 2026-09-10T21:20:13+00:00: Recorded command exit 0; command argv SHA-256
  c408d256d9d0c1290afa41c255859fd4309be2ba493b0dca7646dc6dac50584e.

- 2026-09-10T21:20:33+00:00: Recorded command exit 0; command argv SHA-256
  fcbfe33949d7d44192a2ac14101d847b92e5f8e2bd718941adab1a255a3a8c10.

- 2026-09-10T21:21:05+00:00: Recorded command exit 0; command argv SHA-256
  0a1f79b993f1f59d28cbd0ab8ae5bf8106985e02de2c71a0028ec15ec1d758be.

- 2026-09-10T21:21:17+00:00: Recorded command exit 0; command argv SHA-256
  f8330dc8efbb15e872bf9fe4188660b4b2de6a8a5b3f701aaad94d322c539548.

- 2026-09-10T21:21:57+00:00: Recorded command exit 0; command argv SHA-256
  4666b90295db305d5013a4b5fea1e4ea49250e34c4c4f52046d1ff7d01bc319c.

- 2026-09-10T21:22:20+00:00: Recorded command exit 101; command argv SHA-256
  de1e7596e2ac84fa377e3e5845aa2a5331d271a8f49223f7b2748603ef7d72d4.

- 2026-09-10T21:22:46+00:00: Recorded command exit 0; command argv SHA-256
  2eda7639269440a30f20d5c6de6aa6bb5d1be4a9e2a74fc1693111797128bba0.

- 2026-09-10T21:23:07+00:00: Recorded command exit 101; command argv SHA-256
  de1e7596e2ac84fa377e3e5845aa2a5331d271a8f49223f7b2748603ef7d72d4.

- 2026-09-10T21:23:20+00:00: Recorded command exit 0; command argv SHA-256
  7e53649e71c94f53e768e0bdc48b5a686b2ed8c0af5b086e97fd6a6b5b5098d8.

- 2026-09-10T21:25:17+00:00: Recorded command exit 0; command argv SHA-256
  0f288a4a5c9856ad64dda0af91e0b923e5952c793f065ef6bebaecd532d5daf9.

- 2026-09-10T21:25:52+00:00: Recorded command exit 0; command argv SHA-256
  118a72d074f38d3bc0c03919b02d8f4379ddc20983ff1faaa99d17a9eba6884e.

- 2026-09-10T21:26:12+00:00: Recorded command exit 0; command argv SHA-256
  3cb4fccbdbae1d74acf1d749ec1027ecc1a8a48d3499fc66af38a9088fe58976.

- 2026-09-10T21:26:51+00:00: Recorded command exit 0; command argv SHA-256
  55567313761b549ce8f8adb2244cf2f1912794007c8beedd347ef9fd5698afa6.
