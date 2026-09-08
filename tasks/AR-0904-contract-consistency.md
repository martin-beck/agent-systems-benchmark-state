---
{
  "branch": "feature/contract-consistency",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-08T11:10:07+00:00",
  "depends_on": [
    "AR-0101",
    "AR-1001"
  ],
  "id": "AR-0904",
  "next_action": "Integrate the checker into required quality/failure gates, add semantic compatibility and generated capability/support coverage, then run focused and full validation.",
  "observed_branch": "feature/contract-consistency",
  "observed_dirty": 5,
  "observed_head": "a97c3ed708cc16522383ecde41ec9fa2e642bc61",
  "owner": "quality_20260906",
  "plan": "../plans/AR-0904.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Make schemas, Rust types, protocol examples, CLI capability output and documentation mechanically agree.",
  "task_revision": 31,
  "title": "Machine-check protocol and artifact consistency",
  "updated_at": "2026-09-08T09:28:38+00:00",
  "worktree_key": "agent-systems-benchmark-contract-consistency"
}
---
## AR-0904

Make schemas, Rust types, protocol examples, CLI capability output and documentation mechanically agree.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-08T09:10:05+00:00: Dependencies AR-0101 and AR-1001 are done; promote machine-checkable
  contract consistency as the next independent P1 lane.

- 2026-09-08T09:10:07+00:00: Claimed by quality_20260906.

- 2026-09-08T09:10:39+00:00: Recorded command exit 0; command argv SHA-256
  8974344a1eef5d647af1102865ce8ad4245f7ecf975e3ae0c3ee58143340f5a5.

- 2026-09-08T09:10:58+00:00: Recorded command exit 0; command argv SHA-256
  dd74f78fa3cac69e52c5fc50cfaf86ed6c8fd1f409fd32d236c0c3409fff51ab.

- 2026-09-08T09:15:17+00:00: AR-0904 canonical-source audit completed at clean isolated worktree
  feature/contract-consistency, exact base a97c3ed708cc16522383ecde41ec9fa2e642bc61. Required
  DEVELOPMENT, ARCHITECTURE, QUALITY, FORMAL_ASSURANCE, complete AR and linked plan were read.
  Existing crate-local gates already compare Rust-generated schemas and round-trip public fixtures
  for asb-protocol, asb-control, asb-replay, asb-bundle and asb-workloads, and stateful asb-control
  tests cover negotiation/bounds/cancellation/errors. Concrete gap: there is no closed
  repository-wide registry proving every checked-in Rust contract schema and positive example is
  enrolled, no single deterministic generated catalog, and no negative proving an added/unregistered
  schema fails. A first apply_patch composition failed locally before handoffctl execution because
  template backticks were parsed by the JavaScript shell; no wrapper command ran and product
  worktree remains clean. Next action is the same bounded four-path
  registry/checker/test/generated-doc patch using corrected argument encoding.

- 2026-09-08T09:16:10+00:00: Recorded command exit 0; command argv SHA-256
  67c97ff5d746f85208b14063ff20084aa6483d63cb04f8acb508591b445106e3.

- 2026-09-08T09:17:19+00:00: Recorded command exit 0; command argv SHA-256
  e94f51df5dde88e2b47fa276dd5fc65ec75c8284eca007fb68065a97123afba0.

- 2026-09-08T09:18:20+00:00: Recorded command exit 0; command argv SHA-256
  5cc81e92d1309596818ac51f784a10afa9b02f4ee2ea68fd430242c053123401.

- 2026-09-08T09:18:50+00:00: Recorded command exit 0; command argv SHA-256
  4bf69611ce1d914fdee12a0e33da2a66eeb1b379e0bddbb1ce13e4de63b2afa4.

- 2026-09-08T09:19:47+00:00: Recorded command exit 0; command argv SHA-256
  b298dcdf23f8e666af28773b55e9d697040a5942c693525dac2cc312e1e143ae.

- 2026-09-08T09:20:15+00:00: Recorded command exit 0; command argv SHA-256
  9393977e1e5467f7f33f3be4b57f810afa18138752eb693cd5f7033967e2e436.

- 2026-09-08T09:20:32+00:00: Recorded command exit 0; command argv SHA-256
  731501719400239e93adc27f25320775b084fee7cfc0f917a0082b2eb6e3bc36.

- 2026-09-08T09:21:24+00:00: Recorded command exit 0; command argv SHA-256
  6b7b1e4478f9a6f07604f1ddb2cd26dc4f21731689836949ecf0dcc8e12f684c.

- 2026-09-08T09:21:39+00:00: Recorded command exit 0; command argv SHA-256
  d24fdb427e8404a01124a837e23dec87902d13fbf53b18d539cf30e408843a9b.

- 2026-09-08T09:22:00+00:00: Substantive AR-0904 implementation checkpoint at clean base
  a97c3ed708cc16522383ecde41ec9fa2e642bc61 with four intended untracked paths:
  contracts/v1/catalog.json, tools/quality/contract_consistency.py,
  tools/quality/test_contract_consistency.py, docs/CONTRACT_CATALOG.md. The closed registry enrolls
  every one of the 14 discovered Rust-owned v1 schemas across
  protocol/control/replay/bundle/workloads, 20 positive JSON examples, a named Rust round-trip gate
  per contract, and six exact conformance commands. Determатар? skeleton no.

- 2026-09-08T09:22:16+00:00: Correction and completion of the prior truncated checkpoint note: exact
  dirty scope is four new intended paths: contracts/v1/catalog.json,
  tools/quality/contract_consistency.py, tools/quality/test_contract_consistency.py, and
  docs/CONTRACT_CATALOG.md. The closed registry enrolls all 14 discovered Rust-owned v1 schemas
  across protocol, control, replay, bundle, and workloads; 20 positive JSON examples; one named Rust
  round-trip gate per contract; and six conformance commands. Deterministic document generation and
  zero-diff validation pass. Two Python negative groups pass and prove duplicate or unregistered
  contracts, path traversal, unknown catalog fields, and missing Rust bindings fail closed. The
  registry-run Rust suite exited 0: protocol schema 7/7, control schema 4/4, replay schema 4/4,
  bundle schema 2/2, workload validity 5/5, and stateful control
  negotiation/bounds/cancellation/error suite 14/14. Git diff-check is clean. No existing schema,
  product type, fixture, or other AR lane was modified.

- 2026-09-08T09:23:53+00:00: Recorded command exit 0; command argv SHA-256
  b70fe5c7792dc9c8b32d9d7703dd5e2441803e9867e3aa32f6393f33e31e6b01.

- 2026-09-08T09:24:24+00:00: Recorded command exit 0; command argv SHA-256
  1724b14a72ec012108a49ee729dbeb9964a11410a1f2b696c2a0584ea8668bea.

- 2026-09-08T09:24:43+00:00: Recorded command exit 127; command argv SHA-256
  bc8d482198b6225ade3b33dc8833065f7ff5d7cae814309dc2c8f672c7f2f09d.

- 2026-09-08T09:25:15+00:00: Recorded command exit 1; command argv SHA-256
  723f966c1c071c465c4ef340c0530bbc52de0f3def281226b33a79fe6b037295.

- 2026-09-08T09:25:36+00:00: Recorded command exit 0; command argv SHA-256
  fc90fac593bb8325d6d448cef214d1d35ce9cfbd8fb0e9c5cdc680058db697d5.

- 2026-09-08T09:27:16+00:00: Recorded command exit 0; command argv SHA-256
  75e375d63dbdfef8e0836437210e10ace4cdb3cd233e7d54269d8ace7faa9b0f.

- 2026-09-08T09:28:07+00:00: Recorded command exit 0; command argv SHA-256
  38881e93d6797f4460d6440f3500e7880e8df9bbebb0ad150db43e49b9a3eb62.

- 2026-09-08T09:28:38+00:00: Recorded command exit 0; command argv SHA-256
  ead3b8431bff30d3d78eb4c08c5259ba735a0916e4475b26f7cee07729654ad9.
