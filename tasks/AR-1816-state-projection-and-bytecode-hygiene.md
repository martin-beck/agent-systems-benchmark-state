---
{
  "branch": "repair/ar-1816-projection-hygiene",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-12T14:57:42+00:00",
  "depends_on": [],
  "id": "AR-1816",
  "next_action": "PR #121 now targets 1c396d1d9e; launcher quality repairs pushed. Await exact-head CI and independent review. Then merge and run configured reconcile/snapshot/doctor receipt.",
  "owner": "ar1816_projection_hygiene",
  "plan": "../plans/AR-1816-state-projection-and-bytecode-hygiene.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1816.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Repair recurring stale ASB coordinator projections and generated Python bytecode that breaches the state-file size guard.",
  "task_revision": 54,
  "title": "Coordinator projection and bytecode hygiene recovery",
  "updated_at": "2026-10-12T13:06:14+00:00",
  "worktree_key": "agent-systems-benchmark-state-ar1816-projection-hygiene"
}
---

# AR-1816 — Coordinator projection and bytecode hygiene recovery

Repair the ASB coordinator-state failure mode where `handoffctl doctor --live`
reports stale generated `PROJECT_STATE.md` and `WORKTREES.md`, and where Python
execution writes `tools/__pycache__/handoffctl*.pyc` large enough to violate the
state-file size guard. This is a coordinator repair, not a product-output or
channel-implementation task; AR-1674 remains the owner of the ASB project
channel contract.

The implementation must keep generated views derived-only. It must serialize
or retry reconciliation safely around the existing coordinator lock, publish a
matched projection set atomically, and make all supported coordinator entry
points bytecode-safe without relying on every caller remembering an environment
variable. Existing developer workflows must retain explicit typed lock-timeout
diagnostics rather than silently racing or treating a partial render as valid.

Acceptance requires deterministic unit/fault tests for lock contention,
interrupted rendering, stale projection detection/recovery, and bytecode
suppression or redirection; an integration test must demonstrate clean
`reconcile`, `snapshot`, and `doctor --live` from a configured primary state
checkout while concurrent mutation is either serialized or clearly rejected.
No generated projection may be edited manually, and no tracked/untracked
bytecode, credentials, or host-private runtime configuration may enter commits.

- 2026-10-12T12:40:20+00:00: dependencies verified; begin projection and bytecode hygiene repair

- 2026-10-12T12:40:50+00:00: Claimed by ar1816_projection_hygiene.

- 2026-10-12T12:41:11+00:00: Recorded command exit 0; command argv SHA-256
  99be4e722646927da94d62e568b3dca6f55d686c88195f84abbcebd396588338.

- 2026-10-12T12:41:25+00:00: Bound worktree agent-systems-benchmark-state-ar1816-projection-hygiene
  on branch repair/ar-1816-projection-hygiene.

- 2026-10-12T12:41:51+00:00: Heartbeat by ar1816_projection_hygiene.

- 2026-10-12T12:44:00+00:00: Heartbeat by ar1816_projection_hygiene.

- 2026-10-12T12:45:23+00:00: Recorded command exit 0; command argv SHA-256
  2d4ac874cc3cfc726764c3bcb0fe1014e73bef96a2fa6458cfc9373d6acdd159.

- 2026-10-12T12:46:03+00:00: Heartbeat by ar1816_projection_hygiene.

- 2026-10-12T12:46:06+00:00: Heartbeat by ar1816_projection_hygiene.

- 2026-10-12T12:46:30+00:00: Recorded command exit 0; command argv SHA-256
  5ab8bfbbf186ae8354cec6df43dbafc69cb1e3f98857a4b8f62f2c0ea35efe3d.

- 2026-10-12T12:46:34+00:00: Recorded command exit 0; command argv SHA-256
  26c1601b80f6a79685d584fd5acedda1ed23986d45e0546bd447b64b8e628f7b.

- 2026-10-12T12:46:54+00:00: Recorded command exit 0; command argv SHA-256
  26c1601b80f6a79685d584fd5acedda1ed23986d45e0546bd447b64b8e628f7b.

- 2026-10-12T12:47:18+00:00: Heartbeat by ar1816_projection_hygiene.

- 2026-10-12T12:48:21+00:00: Recorded command exit 0; command argv SHA-256
  26c1601b80f6a79685d584fd5acedda1ed23986d45e0546bd447b64b8e628f7b.

- 2026-10-12T12:49:41+00:00: Implementation committed and PR published; focused coordinator gates
  passed; full suite requires missing jsonschema/pytest in this checkout.

- 2026-10-12T12:57:33+00:00: Recovered expired claim formerly owned by ar1816_projection_hygiene.
  Lease expired at 12:57:18Z; no matching worker process; preserving PR #121 vendor-digest rejection
  and replacement repair worktree.

- 2026-10-12T12:57:42+00:00: Claimed by ar1816_projection_hygiene.

- 2026-10-12T12:57:48+00:00: Recorded command exit 0; command argv SHA-256
  c1125500f804e0d1369c4918ac1365fd4455ae373836eb9db8b2e5462643cb97.

- 2026-10-12T12:58:09+00:00: Recorded command exit 0; command argv SHA-256
  df65c9b2abc879c1d2682a25968013e60812e240d0fb1cebd93cd2eb87209771.

- 2026-10-12T12:58:18+00:00: Recorded command exit 0; command argv SHA-256
  e1ef73b9fae965fe846d4f7df81882aea1800fd10e05bb744a6ec446ec42f299.

- 2026-10-12T12:58:31+00:00: Recorded command exit 0; command argv SHA-256
  c233db80fe50b78777e4fc60cb116af81b1d5e2c3dd8deae0d87f7157fd1d32b.

- 2026-10-12T12:58:35+00:00: Recorded command exit 0; command argv SHA-256
  95b4278421e9d683cb9bc0ddd042e8935f7e11f6d6c12015e519d32249c6e3a1.

- 2026-10-12T12:58:42+00:00: Recorded command exit 2; command argv SHA-256
  0fca468fcba1182f9ee02fb32ddfaf44dc2defedf6401d794c25681b3a1a18d6.

- 2026-10-12T12:59:16+00:00: Recorded command exit 0; command argv SHA-256
  618ec9fb444fd62c2ee7e4ffa3a3e45f75be5d1b4c7c864fa810fc316aa1983b.

- 2026-10-12T12:59:29+00:00: Recorded command exit 0; command argv SHA-256
  4832757b62f8293adafd0162e2b4048d6fd7de60113724863c3bd7f62a7df0c9.

- 2026-10-12T12:59:41+00:00: Recovered expired lease after no worker process. PR #121 vendor digest
  failure was repaired by restoring immutable handoffctl snapshot and moving ASB projection logic to
  tools/awq-handoffctl; focused downstream and 148 existing coordinator tests pass. Await exact-head
  review and CI.

- 2026-10-12T12:59:57+00:00: Recorded command exit 0; command argv SHA-256
  604adef68586098eb5288028094479aa182bda03b97960c22cf62bff136997a1.

- 2026-10-12T13:00:01+00:00: Recorded command exit 0; command argv SHA-256
  ffd5a9c1b2521782ad1518ef695cb0d08d6861404bbcf549b98636bab1c82bbc.

- 2026-10-12T13:00:10+00:00: Recorded command exit 0; command argv SHA-256
  4832757b62f8293adafd0162e2b4048d6fd7de60113724863c3bd7f62a7df0c9.

- 2026-10-12T13:00:23+00:00: CI found missing canonical Huawei/MIT header in downstream test; added
  it in signed DCO commit ed4bc979fe and pushed. Prior vendor-digest issue remains repaired by
  restoring all immutable snapshot files.

- 2026-10-12T13:01:03+00:00: Recorded command exit 0; command argv SHA-256
  2c906f042705074c12b7fb0a3d51e13b160e623282d45b3cddb6b48b28665f3a.

- 2026-10-12T13:01:07+00:00: Recorded command exit 0; command argv SHA-256
  883f76276818179109970f1f1dcc4cbc59b9cf1dbc4dcb4cbe3283b5f57bb273.

- 2026-10-12T13:01:12+00:00: Recorded command exit 0; command argv SHA-256
  09c6f17104ca1ddbc55baa9d2fd139fce1b68e185c348a2604b24b1c43e52594.

- 2026-10-12T13:01:17+00:00: Recorded command exit 0; command argv SHA-256
  4832757b62f8293adafd0162e2b4048d6fd7de60113724863c3bd7f62a7df0c9.

- 2026-10-12T13:01:26+00:00: Strict state consistency diagnosed as ruff-format-only failure in
  downstream launcher; formatted tools/awq-handoffctl.py in signed DCO commit bbba35817b and pushed.
  Vendor digest remains clean.

- 2026-10-12T13:02:12+00:00: Recorded command exit 0; command argv SHA-256
  cd386233ea7b9692c882e23dd7005dfdccef45e1d1630f73378a5d4c502243f0.

- 2026-10-12T13:02:29+00:00: Recorded command exit 0; command argv SHA-256
  bd3882ffbd4816f7f729a3ec322cb3b59c180f3118b4d43d90b5a5296c819766.

- 2026-10-12T13:02:33+00:00: Recorded command exit 0; command argv SHA-256
  0175486afc4db1547318c97484bf497bc2f1421717d1a85fb3df0062318ee801.

- 2026-10-12T13:03:18+00:00: Recorded command exit 1; command argv SHA-256
  618ec9fb444fd62c2ee7e4ffa3a3e45f75be5d1b4c7c864fa810fc316aa1983b.

- 2026-10-12T13:03:27+00:00: Recorded command exit 0; command argv SHA-256
  40b9014e067df2310a0b3eeaed18c9399ab326bb80141df4fb42d292bd1d4aee.

- 2026-10-12T13:03:31+00:00: Recorded command exit 0; command argv SHA-256
  018d06216279fc7a4a5200cde98acddd25bc4c90269e9e318af336c3a545ec2b.

- 2026-10-12T13:03:35+00:00: Recorded command exit 0; command argv SHA-256
  edf0ecfdd3d16f3787dc1d9485b96d1f85e1e781993c714e9446114dc0d43bce.

- 2026-10-12T13:03:40+00:00: Recorded command exit 0; command argv SHA-256
  4832757b62f8293adafd0162e2b4048d6fd7de60113724863c3bd7f62a7df0c9.

- 2026-10-12T13:03:51+00:00: Refactored transaction helpers to satisfy complexity gate, renamed
  launcher module to awq_handoffctl, added narrow S603 rationale, and corrected test import path.
  Focused tests 2/2 pass; signed DCO commit 1c396d1d9e pushed.

- 2026-10-12T13:04:34+00:00: Recorded command exit 0; command argv SHA-256
  29a40c88674c878b36f5604b9a83aa47b82a85cb5546eb64ffe3fd57f3740956.

- 2026-10-12T13:04:38+00:00: Recorded command exit 0; command argv SHA-256
  19b342c84b799a7ec154cd1bf6f691a1ac7b7608f9844755f4a1062ba77ead03.

- 2026-10-12T13:04:43+00:00: Recorded command exit 0; command argv SHA-256
  4832757b62f8293adafd0162e2b4048d6fd7de60113724863c3bd7f62a7df0c9.

- 2026-10-12T13:05:37+00:00: Recorded command exit 0; command argv SHA-256
  bd3882ffbd4816f7f729a3ec322cb3b59c180f3118b4d43d90b5a5296c819766.

- 2026-10-12T13:05:41+00:00: Recorded command exit 0; command argv SHA-256
  0175486afc4db1547318c97484bf497bc2f1421717d1a85fb3df0062318ee801.

- 2026-10-12T13:05:46+00:00: Recorded command exit 1; command argv SHA-256
  211c4769de96e5520aa1d45bf6d6c7514dd29f3cec44cee3fbed2d58ee2c0be9.

- 2026-10-12T13:06:00+00:00: Recorded command exit 1; command argv SHA-256
  c51be55b8dd556c317176a058d44d6e2217da35af59ada0bf95d2a75b64e5f2e.

- 2026-10-12T13:06:10+00:00: Recorded command exit 0; command argv SHA-256
  c51be55b8dd556c317176a058d44d6e2217da35af59ada0bf95d2a75b64e5f2e.

- 2026-10-12T13:06:14+00:00: Recorded command exit 0; command argv SHA-256
  863474d472e25d518c6c4bee7e6af410c7504c2fa33f26845fad3dbb6722aefb.
