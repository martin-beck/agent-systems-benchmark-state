---
{
  "branch": "feature/asb-tui-lifecycle-router",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-11T00:19:33+00:00",
  "depends_on": [
    "AR-0820",
    "AR-0821",
    "AR-0822",
    "AR-1022",
    "AR-1023"
  ],
  "id": "AR-1024",
  "next_action": "Await immutable reviewed AR-1010 successor, repin exact contract, rerun cross-repo PTY and full exact-head gates, then publish for independent review.",
  "observed_branch": "feature/asb-tui-lifecycle-router",
  "observed_dirty": 6,
  "observed_head": "fbbf6f48f2a27300823011f9347ef60eb2b35c44",
  "owner": "codex-ar1024-router-20260910",
  "plan": "../plans/AR-1024.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Add the trusted ASB-side bootstrap and lifecycle router for the optional frontend.",
  "task_revision": 224,
  "title": "Implement `asb tui` lifecycle routing",
  "updated_at": "2026-09-10T22:30:04+00:00",
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

- 2026-09-10T21:27:11+00:00: Recorded command exit 101; command argv SHA-256
  fcbfe33949d7d44192a2ac14101d847b92e5f8e2bd718941adab1a255a3a8c10.

- 2026-09-10T21:27:32+00:00: Recorded command exit 0; command argv SHA-256
  b8f5c2e950df2d50104452e152fc7331daf433f144811c3e6c43cf7b7a32269a.

- 2026-09-10T21:27:52+00:00: Recorded command exit 0; command argv SHA-256
  fcbfe33949d7d44192a2ac14101d847b92e5f8e2bd718941adab1a255a3a8c10.

- 2026-09-10T21:28:08+00:00: Recorded command exit 101; command argv SHA-256
  c408d256d9d0c1290afa41c255859fd4309be2ba493b0dca7646dc6dac50584e.

- 2026-09-10T21:28:30+00:00: Recorded command exit 0; command argv SHA-256
  0db719932183172d34a3ae95cce2adf07108fafdc020709500db74e3881928e2.

- 2026-09-10T21:28:49+00:00: Recorded command exit 0; command argv SHA-256
  c408d256d9d0c1290afa41c255859fd4309be2ba493b0dca7646dc6dac50584e.

- 2026-09-10T21:29:15+00:00: Recorded command exit 0; command argv SHA-256
  f8330dc8efbb15e872bf9fe4188660b4b2de6a8a5b3f701aaad94d322c539548.

- 2026-09-10T21:29:35+00:00: Recorded command exit 0; command argv SHA-256
  b1eb94a760c0ebb491d1feebace78ab2c2ba673a85d41bffbf32c71c06a412e0.

- 2026-09-10T21:29:56+00:00: Recorded command exit 0; command argv SHA-256
  ca3c7a5876fb5a9362ace477fba92ff5ed55332c64cce5360c66af90361ad6c5.

- 2026-09-10T21:30:17+00:00: Recorded command exit 0; command argv SHA-256
  40afa1018331702dc1c2f6028bf18167a444f45b3d70cc6a784d3ca385778302.

- 2026-09-10T21:30:43+00:00: Recorded command exit 0; command argv SHA-256
  312f751736230340c8424328efbb26808b6461fb99b622c3b46c0be799ac0747.

- 2026-09-10T21:31:04+00:00: Recorded command exit 0; command argv SHA-256
  9abe37ae2717636dcc52b9a4f2cd92831191e10c82445960c6075fc92882dad9.

- 2026-09-10T21:31:20+00:00: Recorded command exit 0; command argv SHA-256
  fe93ae67cc7ccd5b6ce09ae153ebef82c1de11530e74ba5c6e5d6fe9f941141b.

- 2026-09-10T21:31:51+00:00: Recorded command exit 1; command argv SHA-256
  aaac96c24bdb5d844a74f1c7660afcce0cc652b8fb5526a449d4e2c28e5104fa.

- 2026-09-10T21:32:11+00:00: Recorded command exit 0; command argv SHA-256
  55567313761b549ce8f8adb2244cf2f1912794007c8beedd347ef9fd5698afa6.

- 2026-09-10T21:32:43+00:00: Recorded command exit 0; command argv SHA-256
  1d17fb76d850b876f12a11ba3d35706daf1dd34ad8662b0ed5cb7f2bec7e8b7d.

- 2026-09-10T21:33:25+00:00: Recorded command exit 101; command argv SHA-256
  86c82e511f854ad0efe2a10c0c45ba77aa38fdc32c02b62c8ddbf3b2029209e5.

- 2026-09-10T21:33:51+00:00: Recorded command exit 0; command argv SHA-256
  1bc45362251b67ef719b982dab7b9ecceb93a9e7ab4716b87e31b13559ccedde.

- 2026-09-10T21:34:09+00:00: Recorded command exit 0; command argv SHA-256
  df1713a7eb601b85f66a0d87948a2c2b2bce26e2db68d27ad452714625008b56.

- 2026-09-10T21:34:28+00:00: Recorded command exit 0; command argv SHA-256
  cf317f700779d738af1cbea03d62241bc11ffdca2fa2a139cd165715fcfef5bf.

- 2026-09-10T21:35:55+00:00: Recorded command exit 0; command argv SHA-256
  99cb9c2be4ff08c41448cb9ec5afea2dde5b883a028b16edf99b70c24ac77be9.

- 2026-09-10T21:36:15+00:00: Recorded command exit 0; command argv SHA-256
  8b91af4597388501871e51a8b0a4ddd6ca33c4e49dc9849a1cd925d2d5e784d5.

- 2026-09-10T21:36:31+00:00: Recorded command exit 0; command argv SHA-256
  cf47f0be1df1f6466ff705cb539320de4fa67d3e97e5f7de6065a044fc74e6d5.

- 2026-09-10T21:36:52+00:00: Recorded command exit 0; command argv SHA-256
  b8c55b99dbdf858e1fd6d57571942e05c064d68278272445e2b461de0c2c831d.

- 2026-09-10T21:37:18+00:00: Recorded command exit 0; command argv SHA-256
  c408d256d9d0c1290afa41c255859fd4309be2ba493b0dca7646dc6dac50584e.

- 2026-09-10T21:38:06+00:00: Heartbeat by codex-ar1024-router-20260910.

- 2026-09-10T21:39:13+00:00: Recorded command exit 0; command argv SHA-256
  a5ee1b71f21dbc5f974bc3be32ef9cc8a4b4ae924e4d9cbdfb392121238fa8ec.

- 2026-09-10T21:39:43+00:00: Recorded command exit 0; command argv SHA-256
  b8b9fb129d6e60f6786fcf9c870535597e9c70327ab8696247c73fd514f575c5.

- 2026-09-10T21:42:01+00:00: Heartbeat by codex-ar1024-router-20260910.

- 2026-09-10T21:42:15+00:00: Recorded command exit 0; command argv SHA-256
  eca52d023f4b8d7076ac46233825ce3a7bc826bb9f070219ff1475eafe6aac24.

- 2026-09-10T21:44:24+00:00: Recorded command exit 1; command argv SHA-256
  aaac96c24bdb5d844a74f1c7660afcce0cc652b8fb5526a449d4e2c28e5104fa.

- 2026-09-10T21:44:47+00:00: Recorded command exit 0; command argv SHA-256
  55567313761b549ce8f8adb2244cf2f1912794007c8beedd347ef9fd5698afa6.

- 2026-09-10T21:45:07+00:00: Recorded command exit 0; command argv SHA-256
  1d17fb76d850b876f12a11ba3d35706daf1dd34ad8662b0ed5cb7f2bec7e8b7d.

- 2026-09-10T21:45:35+00:00: Recorded command exit 0; command argv SHA-256
  00ab7ec4005eb664ec1dffdfdee36c509c52248450a53b3db19751684c0b28bf.

- 2026-09-10T21:46:20+00:00: Recorded command exit 0; command argv SHA-256
  5ec3c804774c177a2360c36839182a979ed3a20db629056a28ca41cf357060ef.

- 2026-09-10T21:47:43+00:00: Recorded command exit 2; command argv SHA-256
  48458d4adcbc2714c4ae60f17ec39d916357031118af6e75d9a5cd826c73f20e.

- 2026-09-10T21:48:14+00:00: Recorded command exit 0; command argv SHA-256
  fae185b75c9c4440aec2ddbd49f93a63671bd7c008c105527a1385d71afbe74c.

- 2026-09-10T21:48:37+00:00: Recorded command exit 127; command argv SHA-256
  305b1ee32750c70062956b8dccca32a9ffc2662a05a3a3afb90baf41fb21d6ff.

- 2026-09-10T21:48:51+00:00: Recorded command exit 0; command argv SHA-256
  67b4c241075a536d1cedc322afebec12bb779312fc35050e63878b9fe94a8141.

- 2026-09-10T21:49:29+00:00: Recorded command exit 0; command argv SHA-256
  52fd82e960ca0f6472e5fbd126ac70a7d2cff5a2e8c19e947f5043c0fdbf9fca.

- 2026-09-10T21:49:54+00:00: Recorded command exit 0; command argv SHA-256
  8faf6bc3f6a7a60f94cf0a19ee54dd5b782e790af6914fc36913c4a50d4d77e6.

- 2026-09-10T21:52:31+00:00: Recorded command exit 0; command argv SHA-256
  527c5896b0fbbc011efa9309dc4d94290e1fa5296df028ac66a37046540426df.

- 2026-09-10T21:53:25+00:00: Recorded command exit 0; command argv SHA-256
  7d3b0e913cdf8f4c95318344e06e0b31099c3f7c10adff0862064363cc8478c0.

- 2026-09-10T21:54:42+00:00: Recorded command exit 0; command argv SHA-256
  858a046b7aa6d1d7f3b91e40531e85b66dd9a8084e620cff9515630562ba13ea.

- 2026-09-10T21:55:23+00:00: Recorded command exit 0; command argv SHA-256
  3e2777dc07418e1a674692b626902387d83bb57d29edefd111ee065e226e8a92.

- 2026-09-10T21:55:40+00:00: Recorded command exit 0; command argv SHA-256
  7172361bc08b42d050ad43a54c46cd9dd11657c7d887dd33f682a92029ffe972.

- 2026-09-10T21:56:23+00:00: Recorded command exit 0; command argv SHA-256
  c2d2f27a507fea6bd35d60f55a53b7f99a3c0eea35395093eff735033e02c187.

- 2026-09-10T21:56:52+00:00: Recorded command exit 0; command argv SHA-256
  0b4a9413a1b7c8f45cf4e3934064adb228e20a7db4d535cc02915856a92b0ac8.

- 2026-09-10T21:57:20+00:00: Recorded command exit 1; command argv SHA-256
  8faf6bc3f6a7a60f94cf0a19ee54dd5b782e790af6914fc36913c4a50d4d77e6.

- 2026-09-10T21:57:38+00:00: Recorded command exit 0; command argv SHA-256
  6ab35a8e9cd1e98057bd75331ee5321e623be87bef2518a7f1343541537a1075.

- 2026-09-10T21:58:39+00:00: Recorded command exit 0; command argv SHA-256
  0f1797ba6a468d7266792976fbb455a6dd0fbf73651d729f17e5bb4569cb5ee3.

- 2026-09-10T21:59:29+00:00: Recorded command exit 0; command argv SHA-256
  3d74286b0fb9cd615604154436026ea27cc917501ccbfb4c74050b856b526059.

- 2026-09-10T22:02:23+00:00: Recorded command exit 0; command argv SHA-256
  3d73b0e14a3baef38d26688ae8393899cf4b90a3a33b32707f4b366f9733d3a2.

- 2026-09-10T22:03:00+00:00: Recorded command exit 0; command argv SHA-256
  611928b0cd38a84b9bab210d74a9ba587c29d53bfd2b5b20ab5ea373f5ece25e.

- 2026-09-10T22:03:25+00:00: Recorded command exit 1; command argv SHA-256
  ad0a6777caa4c6142a4d589a5128e42549b7b8c1cf554ecc93de7bdda14c556e.

- 2026-09-10T22:04:01+00:00: Recorded command exit 0; command argv SHA-256
  42ee3d02114b281de67825640aef4fb17bc8511f29c13e77cc1275899a19dcd0.

- 2026-09-10T22:04:33+00:00: Recorded command exit 0; command argv SHA-256
  994f594239e45ca7757ba5b450c43279729d7a20c436fa034d234ef630943ec6.

- 2026-09-10T22:05:12+00:00: Recorded command exit 0; command argv SHA-256
  5ea154a78fc4ae309bec5ea643400fec4c801a46fdd5e78495cfd011a7865376.

- 2026-09-10T22:06:15+00:00: Hardening checkpoint: fixed cached exact-size boundary; durable signed
  manifest/signature now precede pending activation and every local status/doctor/remove/launch
  reauthenticates active release/source/compatibility/executable before execution. Added
  authenticated PTY fixture, unsigned active/executable substitution rejection, explicit
  acquisition-time expiry versus installed structural validation, exact delegated-status binding,
  complete license-report/SPDX identity equality, and GitHub proxy redirect fixture. Focused router
  19/19, lifecycle PTY/schema 4/4, and focused all-target Clippy pass. Format-only and
  invocation-only failures were corrected; no unexplained code failures. Rootless same-UID replay
  limitation and per-atomic-operation dirfd scope are documented without overclaiming. No UI/render
  dependencies or implementation exist in ASB.

- 2026-09-10T22:06:39+00:00: Recorded command exit 101; command argv SHA-256
  6c914cf4c4bc7afc1057e0d467eaa0248fb5fe5cf089dfcd32c657596960490b.

- 2026-09-10T22:07:15+00:00: Recorded command exit 0; command argv SHA-256
  79e6d0580dd6829ce76e441795665a288393095dfbd52caeaeab336cf4ebc5f9.

- 2026-09-10T22:07:32+00:00: Recorded command exit 0; command argv SHA-256
  217caef39b5b9404b0b7c39c5fadf67436e1d39d6fa61314482ca062afb5f6d6.

- 2026-09-10T22:07:43+00:00: Recorded command exit 0; command argv SHA-256
  f9d2202f6fb433bcbd8c984137d013c6a09f76306be2ae14a9aeff074ad44e30.

- 2026-09-10T22:08:29+00:00: Recorded command exit 0; command argv SHA-256
  cb6a2251f3c5aa8feafc257a337ea8c3336c83af020432d386870e0299bd6191.

- 2026-09-10T22:08:44+00:00: Recorded command exit 1; command argv SHA-256
  848687fcf1e1077d8a6d8a5fe1616d5afe856d7f99e3677b7a3fa635abe71d4c.

- 2026-09-10T22:09:09+00:00: Recorded command exit 0; command argv SHA-256
  5ea154a78fc4ae309bec5ea643400fec4c801a46fdd5e78495cfd011a7865376.

- 2026-09-10T22:09:38+00:00: Recorded command exit 0; command argv SHA-256
  6c914cf4c4bc7afc1057e0d467eaa0248fb5fe5cf089dfcd32c657596960490b.

- 2026-09-10T22:10:03+00:00: Recorded command exit 0; command argv SHA-256
  74b331344048400b846bf2717f47800fed31c0a5a385d676f64304e8794f365a.

- 2026-09-10T22:10:17+00:00: Recorded command exit 0; command argv SHA-256
  29ba223ff6023c791974abe869c70d7b5397ad2994e41ef511fe228fe703e271.

- 2026-09-10T22:10:31+00:00: Recorded command exit 0; command argv SHA-256
  72d982203bfc8b874f89e0d470839903f8b54c7366969bb20fe7a5cd415b8e7c.

- 2026-09-10T22:10:54+00:00: Recorded command exit 1; command argv SHA-256
  2431e2495209eb1c9b00458e3bec07b04bb1d45c30edb5a2bfdeddf6437fa880.

- 2026-09-10T22:11:15+00:00: Recorded command exit 0; command argv SHA-256
  8f7089ebe4bfc05ff7c037e23d2579c8a33d2231ffe2c226ab2137007bffc7dd.

- 2026-09-10T22:12:08+00:00: Recorded command exit 0; command argv SHA-256
  77a8aa4ad25faaa4c08210bdc0d6c9f5c2e5a3e081d67dcc23c967d49f042a75.

- 2026-09-10T22:12:28+00:00: Recorded command exit 0; command argv SHA-256
  7172361bc08b42d050ad43a54c46cd9dd11657c7d887dd33f682a92029ffe972.

- 2026-09-10T22:12:52+00:00: Recorded command exit 0; command argv SHA-256
  57d49b010c7b8cbcc10f03ea6967306826d92094acec0b38fdb1caee62e109f4.

- 2026-09-10T22:13:05+00:00: Recorded command exit 0; command argv SHA-256
  cedce6e9db698a43922fcbaa84820726f3c709768d12a9013ed699ab1730aece.

- 2026-09-10T22:13:18+00:00: Recorded command exit 0; command argv SHA-256
  2431e2495209eb1c9b00458e3bec07b04bb1d45c30edb5a2bfdeddf6437fa880.

- 2026-09-10T22:13:57+00:00: Recorded command exit 101; command argv SHA-256
  26b8b2f380c1e158a0b9204f384b0bc71114d19bf153e1e3beef86512cf18dd5.

- 2026-09-10T22:14:20+00:00: Recorded command exit 7; command argv SHA-256
  b0c59026d0b1002be9fb4ac062789593051dd41aba2b550640859c9d442eac0e.

- 2026-09-10T22:14:36+00:00: Recorded command exit 0; command argv SHA-256
  df636f58d257b33f872cb396c317a5c48a09df4c545bcc7cdce9443c6c7f2393.

- 2026-09-10T22:16:04+00:00: Recorded command exit 0; command argv SHA-256
  f90c1c0b6cc0afa625239036bd65e24aef6b26d08fbfe32e11322e9299fe4387.

- 2026-09-10T22:16:32+00:00: Recorded command exit 0; command argv SHA-256
  11f889238265a8109a303a6b1b50c0f848390a1e8a4f2dc70ba52f5dd490a5d2.

- 2026-09-10T22:17:14+00:00: Recorded command exit 0; command argv SHA-256
  e03373ec864095d1b99636482f03b0a2a2a9fccaf19b11a60ea9b9f74dea135a.

- 2026-09-10T22:17:28+00:00: Recorded command exit 0; command argv SHA-256
  e03373ec864095d1b99636482f03b0a2a2a9fccaf19b11a60ea9b9f74dea135a.

- 2026-09-10T22:19:07+00:00: Recorded command exit 0; command argv SHA-256
  b62912d09c3bdb10af0d503ebfe021fef0a536589e93baa39799ec3a24b1f664.

- 2026-09-10T22:19:33+00:00: Heartbeat by codex-ar1024-router-20260910.

- 2026-09-10T22:20:07+00:00: Recorded command exit 0; command argv SHA-256
  0e301fef3e2daf193a50af181ba6c1dd352c618956146ff1cba887ef2814af4e.

- 2026-09-10T22:20:31+00:00: Recorded command exit 0; command argv SHA-256
  87d46f3f81cf9e45a01116c143086bb308a5f3743435ac920ee21aa32346b240.

- 2026-09-10T22:22:53+00:00: Recorded command exit 0; command argv SHA-256
  dc4324dd29bfecbaff467668f171dff1b2921f4774ae3c487451de38bf186a6e.

- 2026-09-10T22:24:23+00:00: Recorded command exit 0; command argv SHA-256
  99f32af17f6f542e24a036f5b2cac7bee3f47bd2a73dc78b03d1b0b2e8bf796e.

- 2026-09-10T22:24:46+00:00: Recorded command exit 0; command argv SHA-256
  3f18041c4f55386e8f21186b422ae9ff3936f0c502223c8b357704b54ca63259.

- 2026-09-10T22:25:43+00:00: Recorded command exit 0; command argv SHA-256
  165441a6579dde76b88b796146eacf7ef573e67e66bfac155f05fe5b6e687d71.

- 2026-09-10T22:26:25+00:00: Recorded command exit 2; command argv SHA-256
  812d1bb62d6552fb9c4ea409963c844f8a6380972ffe1d8a55b301297b91f615.

- 2026-09-10T22:26:41+00:00: Recorded command exit 2; command argv SHA-256
  d52a3bf720b24e6e51e14e8c568e9a777490e1b489f36fdd508115d68efe4b3f.

- 2026-09-10T22:28:00+00:00: Recorded command exit 0; command argv SHA-256
  c816a5dfdd418bdf71a6a7c9ca929df13a2f47c5481ad9b24702c3f566d5d068.

- 2026-09-10T22:28:22+00:00: Recorded command exit 0; command argv SHA-256
  28ff5e706d59cef3a9da2613c70f961aae5e6509792f690aa6fa29af585901b9.

- 2026-09-10T22:28:42+00:00: Recorded command exit 0; command argv SHA-256
  3dbd6ddbe37d7f2beb154dbfd36ef3e536999273b7748e4e51d4766bca253ac8.

- 2026-09-10T22:29:06+00:00: Recorded command exit 0; command argv SHA-256
  d2ec334b88a309e7435c9e671a10b2f058a2cfcdfe2451519c8648390de89b8f.

- 2026-09-10T22:29:24+00:00: Recorded command exit 1; command argv SHA-256
  9492d55859bcf673b6ec40519c7bc1a738e16f1b6ddbb513d88fd9ada3977c60.

- 2026-09-10T22:29:44+00:00: Recorded command exit 0; command argv SHA-256
  23ea787361309341107b55f66107936e2521172dba17c4afecd430c78ceb31b8.

- 2026-09-10T22:30:04+00:00: Recorded command exit 0; command argv SHA-256
  a0a106de367820edeab0171d9bcca7813fc9e3d498cac951bd07c1b8ec280838.
