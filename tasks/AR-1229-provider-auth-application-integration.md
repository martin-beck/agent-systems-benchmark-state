---
{
  "branch": "feature/ar-1229-auth-application-integration",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-15T23:49:08+00:00",
  "depends_on": [
    "AR-1228",
    "AR-1230"
  ],
  "id": "AR-1229",
  "next_action": "Wire the durable auth registry into RunnerBackend and add bounded asb auth CLI dispatch plus positive, negative, idempotency, and privacy tests; current signed head 8c9eca7 is only the protocol/compile correction and remains fail-closed.",
  "observed_branch": "feature/ar-1229-auth-application-integration",
  "observed_dirty": 0,
  "observed_head": "8c9eca7af1fe5021463dccb5cc00662807ad1fd2",
  "owner": "asb_ar1229_cli_admission",
  "plan": "../plans/AR-1229.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Integrate provider authentication into ASB config, control and CLI surfaces.",
  "task_revision": 48,
  "title": "Provider authentication application integration",
  "updated_at": "2026-09-15T21:58:03+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1229-auth-application-integration"
}
---

Own the cross-crate application integration split from AR-1228. Do not add credential values to
public state or weaken the existing resolver and authenticated-control boundaries.

- 2026-09-15T18:20:00+00:00: Created after AR-1228 implementation review identified that durable
  config/registry and authenticated CLI/control enrollment are a separate cross-crate contract.

- 2026-09-15T21:38:42+00:00: Dependencies AR-1228 and AR-1230 complete; AR-1228 merged at
  efe741a75a8a3e7bd14afd8c6cef119f46a21c74 with all required checks green.

- 2026-09-15T21:38:45+00:00: Claimed by asb_ar1229_auth_application.

- 2026-09-15T21:39:19+00:00: Heartbeat by asb_ar1229_auth_application.

- 2026-09-15T21:41:05+00:00: Heartbeat by asb_ar1229_auth_application.

- 2026-09-15T21:42:31+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-15T21:42:44+00:00: Recorded command exit 101; command argv SHA-256
  31a05f46a65b4172cfcc5ef4e1ed2b4ddd54c042ac56eff6dc51f4205a4051b1.

- 2026-09-15T21:43:34+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-15T21:43:44+00:00: Recorded command exit 0; command argv SHA-256
  31a05f46a65b4172cfcc5ef4e1ed2b4ddd54c042ac56eff6dc51f4205a4051b1.

- 2026-09-15T21:43:53+00:00: Recorded command exit 0; command argv SHA-256
  36526a6e9ff3db476eb511221f8972449d92d2caa68260e3e97de3b8a6725047.

- 2026-09-15T21:44:02+00:00: Recorded command exit 0; command argv SHA-256
  1eadb9598d619901e8517867d52259abd2a268e158b1773b0f6ce878261d82e1.

- 2026-09-15T21:44:13+00:00: Recorded command exit 0; command argv SHA-256
  a0c2360b730c03657315f98732a490198a2b31e0fa7a67d72a11960872659141.

- 2026-09-15T21:45:37+00:00: Heartbeat by asb_ar1229_auth_application.

- 2026-09-15T21:45:40+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-15T21:45:54+00:00: Recorded command exit 0; command argv SHA-256
  03328a0a99a34775b12a565e745253d3fc9d9131c09400a098b97a37cfa3a7ff.

- 2026-09-15T21:46:13+00:00: Recorded command exit 0; command argv SHA-256
  c0c99e8386c3d396af92f5474cc84a25319b97812939b1006299b37138fc3d61.

- 2026-09-15T21:46:22+00:00: Recorded command exit 0; command argv SHA-256
  57298835f3810bd2e24e7f8b9c2864b2da9054481a8a8eb682daedad49af1133.

- 2026-09-15T21:46:34+00:00: Recorded command exit 0; command argv SHA-256
  9599102ffaa7296c7b9559c4ac6b11eac178a844a6b0f7026129b8fccd02c7e6.

- 2026-09-15T21:47:05+00:00: Added renderer-neutral authenticated lifecycle control request variants
  and deny-unknown-fields parameter structs for enroll/status/rotate/revoke, with stable JSON schema
  derivation. cargo check --locked -p asb-control passes. Signed DCO product commit 1cce200 pushed
  to feature/ar-1229-auth-application-integration. Config registry foundation remains in prior
  signed commit 05a9374; no PR created until control/CLI behavior is implemented.

- 2026-09-15T21:48:23+00:00: Releasing claim because cross-crate admission/CLI implementation cannot
  be completed safely in this turn; preserve signed control/config commits for next worker.

- 2026-09-15T21:49:08+00:00: Claimed by asb_ar1229_cli_admission.

- 2026-09-15T21:50:50+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-15T21:51:02+00:00: Recorded command exit 0; command argv SHA-256
  503d79820a7b6b35a054619882f81ce11f3c8065f8ea848fb8256c7d82b97d61.

- 2026-09-15T21:51:24+00:00: Recorded command exit 101; command argv SHA-256
  69487790cd46864562a51f207e108eea84da8519a17023da666d53127f8fc1e6.

- 2026-09-15T21:51:43+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-15T21:51:54+00:00: Recorded command exit 101; command argv SHA-256
  69487790cd46864562a51f207e108eea84da8519a17023da666d53127f8fc1e6.

- 2026-09-15T21:52:17+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-15T21:52:29+00:00: Recorded command exit 0; command argv SHA-256
  69487790cd46864562a51f207e108eea84da8519a17023da666d53127f8fc1e6.

- 2026-09-15T21:52:53+00:00: Recorded command exit 101; command argv SHA-256
  9b0ef1835dbac63dd5284f2c34e60ef7065cb7f6abedeb477212ffb917801a44.

- 2026-09-15T21:53:11+00:00: Recorded command exit 0; command argv SHA-256
  f489a19876782722ed16d09ca01ff72aa074415a2bb4183d7206b5819538e360.

- 2026-09-15T21:54:32+00:00: Recorded command exit 0; command argv SHA-256
  e7a3b2dda05e1858ecb105874379df45b5884bc2c86078cc21fa0d90f4c88be4.

- 2026-09-15T21:54:55+00:00: Recorded command exit 0; command argv SHA-256
  f489a19876782722ed16d09ca01ff72aa074415a2bb4183d7206b5819538e360.

- 2026-09-15T21:55:25+00:00: Recorded command exit 0; command argv SHA-256
  0f5284aa38fecf9c691345d354518fd2fa8f52dffb2451c625511c0b78205add.

- 2026-09-15T21:55:34+00:00: Recorded command exit 0; command argv SHA-256
  1d92af454501e9aa6484e116caa2cfd5905cac201ff6c1f06fcdc43d07abbad2.

- 2026-09-15T21:55:46+00:00: Recorded command exit 0; command argv SHA-256
  af49f1a2c12fe610e176334d1e1f0199956efc75923a96939ff24df4a977e040.

- 2026-09-15T21:56:02+00:00: Signed DCO product commit 8c9eca7 pushed. cargo test -p asb-control
  --offline --lib: 35 passed; cargo test -p asb-cli --lib --offline: 63 passed. Auth lifecycle calls
  validate and match typed results, but backend deliberately returns CapabilityUnavailable until
  durable registry and CLI dispatch are implemented; AR remains in_progress.

- 2026-09-15T21:56:29+00:00: Recorded command exit 2; command argv SHA-256
  48458d4adcbc2714c4ae60f17ec39d916357031118af6e75d9a5cd826c73f20e.

- 2026-09-15T21:56:47+00:00: Recorded command exit 1; command argv SHA-256
  620d9a97264e5adff4f81fd584eedcb0f28888621bfbadf2a3fd8b4fd721c112.

- 2026-09-15T21:57:09+00:00: Recorded command exit 2; command argv SHA-256
  aaa632a0ac7f9da297b5ecf9c7827a996b367b2d2d45bb670791379669d1467e.

- 2026-09-15T21:58:03+00:00: Recorded command exit 101; command argv SHA-256
  69487790cd46864562a51f207e108eea84da8519a17023da666d53127f8fc1e6.
