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
  "next_action": "Add a closed repository-wide contract catalog, deterministic generated catalog document, and fail-closed registry tests; then run the registered Rust schema/fixture/control conformance commands.",
  "observed_branch": "feature/contract-consistency",
  "observed_dirty": 2,
  "observed_head": "a97c3ed708cc16522383ecde41ec9fa2e642bc61",
  "owner": "quality_20260906",
  "plan": "../plans/AR-0904.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Make schemas, Rust types, protocol examples, CLI capability output and documentation mechanically agree.",
  "task_revision": 10,
  "title": "Machine-check protocol and artifact consistency",
  "updated_at": "2026-09-08T09:17:16+00:00",
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
