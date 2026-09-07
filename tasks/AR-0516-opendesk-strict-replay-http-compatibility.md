---
{
  "branch": "feature/opendesk-strict-replay-http-compatibility",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-07T16:52:10+00:00",
  "depends_on": [
    "AR-0502",
    "AR-0503",
    "AR-0504",
    "AR-0302"
  ],
  "id": "AR-0516",
  "next_action": "Repair exact mutation-count oracle for the additional caught request_matches branch, rerun focused mutation fixture, sign successor, and request immutable review before lease-safe PR update.",
  "observed_branch": "feature/opendesk-strict-replay-http-compatibility",
  "observed_dirty": 2,
  "observed_head": "cf64758a6e9ed49d3eca1607fa1ea8135be700f9",
  "owner": "quality_20260906",
  "plan": "../plans/AR-0516.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Add narrowly scoped strict-replay compatibility for pinned OpenDesk traffic.",
  "task_revision": 64,
  "title": "OpenDesk strict-replay HTTP compatibility",
  "updated_at": "2026-09-07T14:34:51+00:00",
  "worktree_key": "agent-systems-benchmark-opendesk-strict-replay-http-compatibility"
}
---
## AR-0516

Implement the shared, fail-closed replay compatibility required by the pinned OpenDesk 0.3.5 evidence: lowercase underscore-bearing header names including redacted `span_id`; absent `stream` paired only with an exact recorded SSE content type; and the two bounded credential-free model-catalog GET probes. Preserve strict ordering, accounting, network denial, and negative cases.

Acceptance requires schema/runtime parity, adversarial positives and negatives, exact socket-byte SSE replay, catalog ordering/accounting, privacy/Gitleaks/formal/full x86_64+aarch64 gates, and a real loopback OpenDesk rerun. Do not claim OpenDesk support until AR-0507 consumes this reviewed merge.

- 2026-09-07T13:28:39+00:00: Promote shared replay compatibility repair discovered by AR-0507
  evidence; serialize schema/service changes separately.

- 2026-09-07T13:28:41+00:00: Claimed by root.

- 2026-09-07T13:28:51+00:00: Coordinator created and promoted AR-0516; release claim because all
  four stable workers are occupied. Keep planned for next safe serialized slot.

- 2026-09-07T13:52:07+00:00: Promote shared OpenDesk replay compatibility repair now that AR-0508
  released and a worker slot is free.

- 2026-09-07T13:52:10+00:00: Claimed by quality_20260906.

- 2026-09-07T13:52:58+00:00: Recorded command exit 0; command argv SHA-256
  195449c186722fe0b769c793877c599856ce076ac8181bc5b9a600a9dd38eec9.

- 2026-09-07T13:57:32+00:00: Recorded command exit 0; command argv SHA-256
  279684299b6a4f7bcdab8980675f55ad1d66f160c4802953878e25e916c9a863.

- 2026-09-07T13:57:51+00:00: Recorded command exit 1; command argv SHA-256
  c0dc1f34cd998dc456d44afacdaf4a24fa3d03748cc7b6165330680a53aa5763.

- 2026-09-07T13:58:06+00:00: Recorded command exit 0; command argv SHA-256
  5e9694509038c5216d4f02627782683082ff47c5e43f8d8abe20b0d12b95136d.

- 2026-09-07T13:58:29+00:00: Recorded command exit 101; command argv SHA-256
  c0dc1f34cd998dc456d44afacdaf4a24fa3d03748cc7b6165330680a53aa5763.

- 2026-09-07T13:58:51+00:00: Recorded command exit 0; command argv SHA-256
  dcc921c7318383697a10e1813d189e6524409e5444bcc9d46758f055d898e29c.

- 2026-09-07T13:59:12+00:00: Recorded command exit 0; command argv SHA-256
  c0dc1f34cd998dc456d44afacdaf4a24fa3d03748cc7b6165330680a53aa5763.

- 2026-09-07T14:00:51+00:00: Recorded command exit 0; command argv SHA-256
  976dd9a59563747b46328642f09cb1e74330171f764d6372243d6e2954a46d48.

- 2026-09-07T14:01:39+00:00: Recorded command exit 0; command argv SHA-256
  f235d0c549fa7568ec631b95cd307a13cac5c1c2c840b65f5aebab4ac24038aa.

- 2026-09-07T14:03:11+00:00: Recorded command exit 0; command argv SHA-256
  3990fdc285c13d815a7d626fe9eb513bbe5ece51e1f05ee32386c689a5bbe9d3.

- 2026-09-07T14:04:34+00:00: Recorded command exit 0; command argv SHA-256
  9812bfdd87da0c5659ca3cb21ea1aac202ae06ea0731fda8ae798f116295ebcf.

- 2026-09-07T14:04:49+00:00: Recorded command exit 0; command argv SHA-256
  5e9694509038c5216d4f02627782683082ff47c5e43f8d8abe20b0d12b95136d.

- 2026-09-07T14:05:10+00:00: Recorded command exit 0; command argv SHA-256
  5d70464abfe059f7c62df8cf185695dc6220002156d4e96f96e0abd830dc3337.

- 2026-09-07T14:06:38+00:00: Recorded command exit 1; command argv SHA-256
  4566e388b2c03b58af4c8ef29f7481e6db2c0d0daa0533e3807959ffe6e361a0.

- 2026-09-07T14:09:40+00:00: Recorded command exit 1; command argv SHA-256
  2e086b8b83af13e1d3333985e8b55b5d4bfbb90b0d89cbe5701ad393a564251a.

- 2026-09-07T14:10:15+00:00: Recorded command exit 0; command argv SHA-256
  06b7d25b5d0e1a2982295c8fe174b9fb69c3acf2e3aa5d9ecb3ce76a4b556178.

- 2026-09-07T14:11:44+00:00: Recorded command exit 0; command argv SHA-256
  88628f26ff88e7aa804f9b9ce50a0bdc10d98afc409aebb001948462a67fc605.

- 2026-09-07T14:11:59+00:00: Recorded command exit 0; command argv SHA-256
  5e9694509038c5216d4f02627782683082ff47c5e43f8d8abe20b0d12b95136d.

- 2026-09-07T14:12:21+00:00: Recorded command exit 0; command argv SHA-256
  2cc15bff5200e61c764a35f5fcb34f0a9a6b254bc6a1a931134a6ee671965f99.

- 2026-09-07T14:15:33+00:00: Recorded command exit 0; command argv SHA-256
  225a2c6a21adde6c706bc7e47fdc1bb37f2061b7eac126fee7bb07ff7be368cd.

- 2026-09-07T14:15:50+00:00: Recorded command exit 0; command argv SHA-256
  e212dce3104c4f2cb341ae31eb17107d42390af64aa54db541b147bcf95ea2d1.

- 2026-09-07T14:16:38+00:00: Recorded command exit 0; command argv SHA-256
  d10af40211a957f6ed4b33d741cca9a6c2d394a6b3a715da9f87a9731e3a4ccd.

- 2026-09-07T14:17:14+00:00: Recorded command exit 0; command argv SHA-256
  cb83a5bafb221cfc0798f2e09567944bbb38dbe79f160c29dcdc3bd19d4cccbe.

- 2026-09-07T14:17:30+00:00: Recorded command exit 0; command argv SHA-256
  8a2a27f84a80a83ebe7d5372deb9a39931a0c541782ce6a0dacfafa58e2728df.

- 2026-09-07T14:17:52+00:00: Recorded command exit 0; command argv SHA-256
  ced03889a1638f2777fd87a622f3a15a5da3f5c8367975a5dac1df8edd334135.

- 2026-09-07T14:19:05+00:00: Recorded command exit 0; command argv SHA-256
  09fee1d6e554bcecbf1e8874bbf6e781dfd00730ba1df69a2f3bdcfe884de5b1.

- 2026-09-07T14:19:26+00:00: Recorded command exit 0; command argv SHA-256
  e0dcd72c99fde4c74f24b014b0f23cfc4f906ee3c143dfeda3592c91fb937f51.

- 2026-09-07T14:20:05+00:00: Recorded command exit 0; command argv SHA-256
  24c30e94070201013cd6fb6e10b9af89bbaae53754d048f47d63f461da07558a.

- 2026-09-07T14:20:52+00:00: Recorded command exit 0; command argv SHA-256
  8d10b49da737b89864c3bdc4a421e6cfaa45dc1b04146b4f41f4fa71c52c4dd2.

- 2026-09-07T14:21:20+00:00: Recorded command exit 0; command argv SHA-256
  3b581368103e13b85052de963700edfe51dd675f0f5823bc2a0e9602825573ed.

- 2026-09-07T14:21:35+00:00: Recorded command exit 0; command argv SHA-256
  dec42f8ca58ac5a0a22d2a6e33cc84d82f48451bf71177eac1b0589814b14419.

- 2026-09-07T14:21:48+00:00: Recorded command exit 0; command argv SHA-256
  fc7f153e795a969c0d26d782e5ef972601ad6dede56cfba9a50eec5813d61b92.

- 2026-09-07T14:22:37+00:00: Recorded command exit 0; command argv SHA-256
  29c92d2785d62c684d6d203238de9dacf73f7049020d538cfd8cd63d319ead42.

- 2026-09-07T14:22:57+00:00: Recorded command exit 0; command argv SHA-256
  708e59e8e4239b58a8686a54bd4b3793005e3ed5781a9c081bc8a5c6245a1335.

- 2026-09-07T14:23:11+00:00: Recorded command exit 0; command argv SHA-256
  1bddf59f255a7b2652090c140409037cd8f459808de520ef6c64162d50793371.

- 2026-09-07T14:23:28+00:00: Recorded command exit 0; command argv SHA-256
  59c855d2fd92088370d9836c61172027117d5c34d8be9bd2e53aff51e9fbd470.

- 2026-09-07T14:24:11+00:00: Recorded command exit 0; command argv SHA-256
  c73f44f493fa4239dd6aff4c1c057688b01d4b9535303ec436c0099e3b90abbf.

- 2026-09-07T14:24:28+00:00: Recorded command exit 127; command argv SHA-256
  b54cbe226a08e7270316326e57e7633033dfd48ceb0c438865fcac5465384821.

- 2026-09-07T14:24:49+00:00: Recorded command exit 0; command argv SHA-256
  292be8a1bef2427fd77398f0dc5077c8251daca2cf112293f0b542798c911057.

- 2026-09-07T14:25:34+00:00: Recorded command exit 0; command argv SHA-256
  49ae7ce178cf9eab3354c9ba376ade509e856e840437ffe2ccf6d3642313d38c.

- 2026-09-07T14:25:54+00:00: Recorded command exit 0; command argv SHA-256
  a447c9647ab46eed6c973744657fec01dc6ee919cb53b3d596c0816782d8b91c.

- 2026-09-07T14:26:09+00:00: Recorded command exit 0; command argv SHA-256
  63d39cccde4e84475c76e90869a03baed8b2b37470ee6654f7b8324a9be61247.

- 2026-09-07T14:26:22+00:00: Recorded command exit 0; command argv SHA-256
  0f5954ac120518c4c67bfe9df3f52a917c29e7d5611404ea00b8e24260f8f39c.

- 2026-09-07T14:26:58+00:00: Signed candidate cf64758a6e9ed49d3eca1607fa1ea8135be700f9 (tree
  917cd02e824932e512daf170e0e54608ac2ee661, base 40cfa75ca195aaf13be1d5bc8025f96e5f4d3e7c) is clean,
  SSH-signature verified, DCO certified, and repository policy/Gitleaks introduced-history clean.
  Eight-path replay-only scope implements underscore header schema/runtime/redaction parity,
  Chat-only absent-stream exact SSE, and strict ordered catalog GET syntax with bounded fail-closed
  negatives. Focused/package/workspace fmt-clippy-test-doc-release, configured coverage (asb-replay
  97.66% lines), supply chain, workflow policy, failure fixtures, platforms, privacy, Loom/state
  models, Kani 5/5, and deliberate Kani negative passed. Durable AR-0507 evidence proves span_id,
  absent stream plus SSE, and at least one pre-completion catalog GET but did not retain exact GET
  headers; candidate invents no live header claim. Required real pinned OpenDesk rerun remains an
  explicit post-merge AR-0507 acceptance boundary.

- 2026-09-07T14:27:37+00:00: Recorded command exit 0; command argv SHA-256
  570dabf9edffd4125d21ef78768dd7a405e00bd4b62eb797a5ad1737825b024f.

- 2026-09-07T14:27:59+00:00: Recorded command exit 0; command argv SHA-256
  caabc6ebde069f424cc87914e5f574b7afa2e959ac0045477a3930df1dedaa1a.

- 2026-09-07T14:28:31+00:00: Recorded command exit 0; command argv SHA-256
  598732ce29b5cd1b60758e8f92098604555ae4d72925a2865e8f2278127c0ede.

- 2026-09-07T14:28:58+00:00: Independent immutable review approved
  cf64758a6e9ed49d3eca1607fa1ea8135be700f9. Published exact branch under absent-ref lease and opened
  product PR #42 https://github.com/martin-beck/agent-systems-benchmark/pull/42. GitHub reports base
  40cfa75ca195aaf13be1d5bc8025f96e5f4d3e7c, exact head cf64758a, clean mergeable PR. Exact-head runs
  started: quality 34133139622, Rust x86_64+aarch64 34133139626, formal 34133139642, fault assurance
  34133139627; all currently in progress.

- 2026-09-07T14:32:54+00:00: PR #42 exact cf64758a CI investigation: Rust aarch64 job 101777820780
  passed fmt/clippy/tests then failed before native Goose execution because the official pinned
  archive download returned HTTP 504; x86 Rust passed. Fault job 101777820409 ran all mutants and
  caught 7/7, then failed because run-mutation-sentinels.sh and README hard-code the prior exact
  count 6. The added fail-closed GET dialect inequality inside request_matches creates the seventh
  viable caught mutant. This is a narrow owned test-oracle update, not a gate weakening; record both
  failures before mutation.

- 2026-09-07T14:33:26+00:00: Recorded command exit 0; command argv SHA-256
  514ddce738f63b862e92da0859bae2dc22ac8457e98a7109985eb3ab3b0b7e09.

- 2026-09-07T14:33:52+00:00: Recorded command exit 101; command argv SHA-256
  c3f3d73ee84a96160faa9e6674d0fa1babdc052d27bff25d96ed1d725e5e5d37.

- 2026-09-07T14:34:51+00:00: Recorded command exit 0; command argv SHA-256
  514197ace864f915a0f9d022925ea62898a437762fd5f22e9db6da38aaebc207.
