---
{
  "branch": "feature/measurement-catalog-semantics",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-11T00:44:21+00:00",
  "depends_on": [
    "AR-0101",
    "AR-1001"
  ],
  "id": "AR-1013",
  "next_action": "Publish clean exact head 6d0c991 for immutable independent schema/provenance review; do not merge before approval and exact-head CI.",
  "observed_branch": "feature/measurement-catalog-semantics",
  "observed_dirty": 0,
  "observed_head": "6d0c9916e18f31fa9428bdc9fa1d794611027d9d",
  "owner": "codex-ar1013-measurement-catalog-20260910",
  "plan": "../plans/AR-1013.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Define selectable ASB measurements grouped by stable semantic meaning.",
  "task_revision": 77,
  "title": "Version the measurement catalog and semantic groups",
  "updated_at": "2026-09-10T22:32:46+00:00",
  "worktree_key": "agent-systems-benchmark-measurement-catalog-semantics"
}
---
Create a versioned, machine-readable catalog for every selectable benchmark measurement. Group
measurements by semantic meaning (for example system resources, scheduling/contention, latency,
quality/reliability, fairness, cost, and provenance) while preserving individual metric identity,
units, aggregation, sampling overhead, availability, platform support, and evidence limits.

Acceptance criteria: schema and Rust types are versioned; duplicate/ambiguous names and incompatible
units are rejected; groups and metrics have stable IDs; live/replay/unsupported states are explicit;
CSB-derived metrics have provenance and no double counting; fixtures and negative tests cover unknown,
duplicate, unit-mismatch, unavailable, and privacy-sensitive metrics.

- 2026-09-10T21:25:00+00:00: Removed optional AR-0602 monitoring qualification as a hard
  prerequisite. The baseline catalog must represent unsupported or not-yet-qualified CSB measures
  explicitly; AR-0602 may add or qualify versioned catalog entries later without blocking the
  standalone measurement selector.

- 2026-09-10T21:43:33+00:00: AR-0101 and AR-1001 verified done; baseline catalog explicitly excludes
  optional AR-0602 qualification and all UI ownership

- 2026-09-10T21:44:21+00:00: Claimed by codex-ar1013-measurement-catalog-20260910.

- 2026-09-10T21:44:38+00:00: Recorded command exit 0; command argv SHA-256
  321c534968b9c456a64caf5e6d09b63780c507f97548057d2bfe31edcfd73ff4.

- 2026-09-10T21:44:56+00:00: Recorded command exit 0; command argv SHA-256
  bb90acfc3bcc7d3647d0c0b049c9609dba80bcd927f6184e4bc0ad084debdde1.

- 2026-09-10T21:58:04+00:00: Recorded command exit 127; command argv SHA-256
  0079efd3277b8ed9284ec70bd5cb39197b07709e937708b082347986c33de513.

- 2026-09-10T22:00:14+00:00: Recorded command exit 2; command argv SHA-256
  e4233f8770c5b300483a22e0a1eb4bc23917c2faf585291cb0157130eeca10e6.

- 2026-09-10T22:02:52+00:00: Recorded command exit 0; command argv SHA-256
  762ae9c8de069e93026706eaf03c66267c70a700948cb6c9a875fb31c06c9688.

- 2026-09-10T22:03:16+00:00: Recorded command exit 1; command argv SHA-256
  d40baf1381cec1e4b4a91d3638d8a3f4061d6d9323b569959f110a3b6932dc15.

- 2026-09-10T22:03:32+00:00: Recorded command exit 0; command argv SHA-256
  205af411b437012d653cf7d4181938ab95e0627b3cfc89beca92406d60662ba7.

- 2026-09-10T22:03:54+00:00: Recorded command exit 101; command argv SHA-256
  8f8e4634040d6917ed5f7fb09b4ca62c903a80d34fa95a1ba2be1144f912bbe8.

- 2026-09-10T22:04:41+00:00: Recorded command exit 0; command argv SHA-256
  f6a04f71d243493e0afeb79eeed366d6049b0c7457de2922b535bf844cf9ef95.

- 2026-09-10T22:05:02+00:00: Recorded command exit 101; command argv SHA-256
  bf1ec98a41cd2ce289b7dcbf9d0bee99e295b63e9c1e5d4a88d94ce0a3da459d.

- 2026-09-10T22:06:18+00:00: Recorded command exit 0; command argv SHA-256
  ee313bf3940b01b04cee7c97fa57a91082f3e84c258bef5db6e9c7815401291b.

- 2026-09-10T22:06:47+00:00: Recorded command exit 101; command argv SHA-256
  ef217a99a6e1021b0630dd2b0c0fa01adc845e76952ba0fa33ac1c3b04a5e1fd.

- 2026-09-10T22:07:08+00:00: Recorded command exit 0; command argv SHA-256
  7afa6fa1210d56b440d69b5dd1b34b4ef68496432a2dc3346b22a1a060aed88c.

- 2026-09-10T22:07:24+00:00: Recorded command exit 0; command argv SHA-256
  4290a212f503755e92daed95120abeea5118e2c4fe34340babfc99050f34d850.

- 2026-09-10T22:08:02+00:00: Recorded command exit 0; command argv SHA-256
  217fab3b16efcdeb9a82395734f9be72e41f68e6603da79b7f0b2fbafe257fb0.

- 2026-09-10T22:08:20+00:00: Recorded command exit 0; command argv SHA-256
  a2e82e837ce7e0c52f3abfe9aa2d2ed7ee17dd7920786014f25e55d4ec0d1b94.

- 2026-09-10T22:08:51+00:00: Recorded command exit 0; command argv SHA-256
  aa1e9a98e8bd3be3208ad68122e8d690c4ba9278beb15596978b000c3921e622.

- 2026-09-10T22:09:16+00:00: Recorded command exit 0; command argv SHA-256
  cc9581b000cb0cd95dbe7702ea5b78f2e69c62e99468d27f32046114fe07185d.

- 2026-09-10T22:13:46+00:00: Recorded command exit 0; command argv SHA-256
  fca816432b48fd44d5fd08392795f43db33879f9908ca8fe47f522162578cc66.

- 2026-09-10T22:14:13+00:00: Recorded command exit 1; command argv SHA-256
  519473ef71ce7b26ef9f035203b6d3c308a44475d29d01f1a14d13bbad3dc0ff.

- 2026-09-10T22:14:47+00:00: Recorded command exit 0; command argv SHA-256
  f3a67cfb2cd33b43593cc9a684fcfbe0eb1442e8bc4f27cc507c273371c9011c.

- 2026-09-10T22:15:04+00:00: Recorded command exit 0; command argv SHA-256
  4bc7a17af3100a24bf4ea50426d1f198167dba0ab66079068d12bccc03fe8398.

- 2026-09-10T22:15:26+00:00: Recorded command exit 0; command argv SHA-256
  7921fa54bf7bf81e30322170f431f072e1fc601353dcee389158711e55e6ca02.

- 2026-09-10T22:15:45+00:00: Recorded command exit 0; command argv SHA-256
  8635360f606ea8552ce21c6f09f38365597b8deed602300ca01aeaa7972b9e11.

- 2026-09-10T22:16:56+00:00: Recorded command exit 0; command argv SHA-256
  b4653246f11363e7ae44054f36f384b3ec3a6a731bdff4c7afc07d1afa71358f.

- 2026-09-10T22:17:35+00:00: Recorded command exit 0; command argv SHA-256
  97e5846182f4c95094804d96d97281a619a7e942d7af843f9be2cc8fe07fc035.

- 2026-09-10T22:17:53+00:00: Recorded command exit 0; command argv SHA-256
  b9e67f2882514afc3b42921b5d2423553ebf8764b319768de6b8936b0d0793f9.

- 2026-09-10T22:18:07+00:00: Recorded command exit 101; command argv SHA-256
  a34716c153f5405951dada98314a9baf4369048cd3e2145c3ec8a169cf7ac10f.

- 2026-09-10T22:18:26+00:00: Recorded command exit 0; command argv SHA-256
  a0915c9f368ddbba8b6745abd8ff2ebe67e842fb94e34a237c935b20aa9441a2.

- 2026-09-10T22:18:58+00:00: Recorded command exit 0; command argv SHA-256
  7ae823530534f8d6ac3e7277eaaa2460fe36cbd8eff3082a30064d12f1d5d10e.

- 2026-09-10T22:19:17+00:00: Recorded command exit 0; command argv SHA-256
  f6d7e07bf82b185eb4e1a04e1c8f0931e2caba89d29b0c57feafc781a0f0aafd.

- 2026-09-10T22:19:36+00:00: Recorded command exit 0; command argv SHA-256
  a339b5a8bb30331860c0ebc47044f3c92261afd136f446a9936a8d374605aa21.

- 2026-09-10T22:19:51+00:00: Recorded command exit 1; command argv SHA-256
  6df90b1a69340dad0c1019478b256c96f7d011fabd450acbe4f047df8aa7f701.

- 2026-09-10T22:20:16+00:00: Recorded command exit 0; command argv SHA-256
  d1bc3a1c6328079ae4cba2974f174f611f7a48d932d0b394b670e9764bb57a3a.

- 2026-09-10T22:20:53+00:00: Recorded command exit 0; command argv SHA-256
  b19e6b3baa4177092a706b7e82f1e1f8784dbdc02c2bf786443dc81948c976f4.

- 2026-09-10T22:21:51+00:00: Recorded command exit 0; command argv SHA-256
  38f5b34f1b438802cb9d00687b5f1bd12938d30963cd52cbb4bd2f149cf653d5.

- 2026-09-10T22:22:17+00:00: Recorded command exit 0; command argv SHA-256
  b0842edd06fd8367b6a043f76a203887bfd697e27cc7c74b027514025c23909d.

- 2026-09-10T22:23:47+00:00: Recorded command exit 0; command argv SHA-256
  adecd66eb9a759c87d61cc776cdd361d838b81bca4626c6d19955c4fd1fe1245.

- 2026-09-10T22:24:08+00:00: Recorded command exit 0; command argv SHA-256
  46f56aaddae1ab2b7e076d455f4856f7e13b0d7f3e01671ca00c560bebfa6e5a.

- 2026-09-10T22:24:39+00:00: Recorded command exit 0; command argv SHA-256
  08f58361fd9cea853acaaca9fb2458295846e6f54b5b300119735cd972fc82cc.

- 2026-09-10T22:25:26+00:00: Recorded command exit 101; command argv SHA-256
  f9105c428b195d8bb0b70785440ad02c6320dd50ea585d04c847e91dbdbf52df.

- 2026-09-10T22:25:53+00:00: Recorded command exit 0; command argv SHA-256
  41ca0694f0af8f5e925eefc125becce2c53b9943757ab9cc181aa11aadd0e5ee.

- 2026-09-10T22:26:08+00:00: Recorded command exit 0; command argv SHA-256
  446743d797b3122deebc8802d28b3ad22c90714c92f48898a6191174d91b0d09.

- 2026-09-10T22:26:51+00:00: Recorded command exit 1; command argv SHA-256
  f5aec9a76c1100c332788a1360a3f1c64dabbab45f929ccc33e11ba07df13b88.

- 2026-09-10T22:28:33+00:00: Recorded command exit 0; command argv SHA-256
  ce7f5143dde3af57aaea61b52c9303ff1e02131c8dcbfe09b4169209ede26936.

- 2026-09-10T22:28:51+00:00: Recorded command exit 1; command argv SHA-256
  4af6f0e3aa60a3f7c10d61e48894ad8a6d6ad1e9a9abd3615d72124e28a80a52.

- 2026-09-10T22:29:15+00:00: Recorded command exit 0; command argv SHA-256
  5b62b72f34ec9068d8c4de0935ac19445d1735fb2d2e91190df74b86cb631ac3.

- 2026-09-10T22:29:33+00:00: Recorded command exit 0; command argv SHA-256
  661998f347d30032163a714bc0242f545f4ec82deb049456e78d40d5ad1755f5.

- 2026-09-10T22:30:01+00:00: Recorded command exit 0; command argv SHA-256
  ff5c46d1eb4bbcf3be547ea5fd96028d40af74cb605c36bb906771a6e441b4dd.

- 2026-09-10T22:30:38+00:00: Recorded command exit 0; command argv SHA-256
  395029eaf8d0c71d850ef8c12906d7520fd2e7a12765f6a2c6018b29bac6b5e6.

- 2026-09-10T22:31:02+00:00: Recorded command exit 0; command argv SHA-256
  95fc16feb3528563032b399c87dd7d33db2fe55e58c97318eefc479370b6c9f9.

- 2026-09-10T22:32:17+00:00: Recorded command exit 0; command argv SHA-256
  857ccad3fa17f8807799db0e1d904aac9a4892c1be53b9964a77b3662bc00b9f.

- 2026-09-10T22:32:34+00:00: Implemented ASB-only measurement catalog v1 at clean head 6d0c991:
  exactly 25 selectable portable procfs/cgroup metrics in two nonempty groups with
  ID/unit/aggregation/scope/source parity; mandatory usage/cost, latency/outcomes,
  analysis/scoring/economics/fairness and provenance are documented non-selectable outputs. Added
  versioned schema, content digest, bounded maximal/empty/negative fixtures and contract registry.
  Exact-head fmt, clippy workspace, workspace tests, rustdoc, deny, audit, repository policy and
  contract consistency pass. Coverage passed serially: workspace 94.47%, asb-protocol 97.08%; first
  concurrent coverage run hit known process-test ETXTBSY/reap races, then serial rerun passed. No
  UI/render/terminal code changed.

- 2026-09-10T22:32:46+00:00: Recorded command exit 0; command argv SHA-256
  80b6e74d4a478126b5afadb47183fbc33d501260a3806be301e157f13acd4449.
