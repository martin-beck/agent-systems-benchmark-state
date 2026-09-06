---
{
  "branch": "feature/experiment-comparability",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-06T22:08:22+00:00",
  "depends_on": [
    "AR-0101",
    "AR-0203"
  ],
  "id": "AR-1001",
  "next_action": "Complete comparison fixtures, generated schema, Cargo integration, and full gates after serialized fence transfer.",
  "observed_branch": "feature/experiment-comparability",
  "observed_dirty": 4,
  "observed_head": "bda6bc41760a914ffc1a9305fc88422eaace302b",
  "owner": "quality-20260906",
  "plan": "../plans/AR-1001.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Make every comparison content-addressed and explicit about agent, model, workload and platform confounders.",
  "task_revision": 23,
  "title": "Define experiment identity and comparability",
  "updated_at": "2026-09-06T20:21:23+00:00",
  "worktree_key": "agent-systems-benchmark-experiment-comparability"
}
---
## AR-1001

Make every comparison content-addressed and explicit about agent, model, workload and platform confounders.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-06T20:05:38+00:00: Claimed by quality-20260906.

- 2026-09-06T20:05:51+00:00: Recorded command exit 0; command argv SHA-256
  a87e6936612e0fe8006c110e65eb3032b43e306fe9daefeff2ae697b86690107.

- 2026-09-06T20:08:22+00:00: Heartbeat by quality-20260906.

- 2026-09-06T20:10:50+00:00: Recorded command exit 2; command argv SHA-256
  48458d4adcbc2714c4ae60f17ec39d916357031118af6e75d9a5cd826c73f20e.

- 2026-09-06T20:13:22+00:00: Recorded command exit 0; command argv SHA-256
  655a9b3e54d71c46d82ae8f5dc856d108816b96812b584054c1dc06c69c4f1c9.

- 2026-09-06T20:14:56+00:00: Recorded command exit 0; command argv SHA-256
  cd04871ebcbd721769286eeb65a26c1b026a799daa53696c99c538153d1d1098.

- 2026-09-06T20:15:24+00:00: Recorded command exit 0; command argv SHA-256
  710cb76ba0832d99e05dd0b97943369f3d8f0f5a58dc8795ac70e9b642f8dee7.

- 2026-09-06T20:15:43+00:00: Recorded command exit 0; command argv SHA-256
  9eb4a59131362f6308fcdd1af3a2ac9d3abf39328231207e85800dcce0547fb1.

- 2026-09-06T20:16:22+00:00: Recorded command exit 0; command argv SHA-256
  acb729de8c0dfef7a151e8decb21568cad5ab92fd2388c5dd975e1657c6430e1.

- 2026-09-06T20:16:37+00:00: Recorded command exit 0; command argv SHA-256
  e6a5c2e233ca93dde81b2e072b434e7f3dd229bfbd1ffaaa44ce0ac60d16c5ce.

- 2026-09-06T20:17:15+00:00: Recorded command exit 0; command argv SHA-256
  ff885f4e69f07b31f539454648b53438e81b6f6290c6b94237f715e86100fca2.

- 2026-09-06T20:18:40+00:00: Recorded command exit 0; command argv SHA-256
  5a334fc9961543439c95cad314f1e481d6c08e3b563fcbe95cf5f6cc3348171a.

- 2026-09-06T20:19:04+00:00: Implemented isolated source modules only: typed credential-free v1
  experiment identity, deterministic SHA-256 content address excluding its own digest, strict
  field/replay/bounds validation, and fail-closed comparison that reports deterministic confounder
  dimensions without raw values. Added protocol negative unit coverage. Did not touch Cargo.toml,
  Cargo.lock, generated schemas, fixtures, or registries while root AR-0301 holds the shared fence.
  First wrapped apply_patch attempt failed exit 2 because run stdin is DEVNULL; no product mutation.
  One later wrapped patch waited safely behind AR-0504 long coverage state lock, then applied after
  serialization.

- 2026-09-06T20:20:03+00:00: Recorded command exit 0; command argv SHA-256
  57975b9d36bf1e516aef1d2e97dca8486d066bc49c3bab18003b80f851da928a.

- 2026-09-06T20:20:47+00:00: Recorded command exit 1; command argv SHA-256
  b790f511afc61f9b1f73609956a900a0b4f4db06a4cecca4d4b28d2d8dd8295d.

- 2026-09-06T20:20:56+00:00: Recorded command exit 0; command argv SHA-256
  acae82902d4c8e17584017569d4c40fc10205ffd8eb2b80c4f71355c170258c8.

- 2026-09-06T20:21:23+00:00: Recorded command exit 0; command argv SHA-256
  133b32255181471858ea96a1689aef776e0d7bb604a303063023e10717c962a3.
