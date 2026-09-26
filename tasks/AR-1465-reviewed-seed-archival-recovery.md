---
{
  "branch": "repair/ar-1465-reviewed-seed-archival-recovery",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1464"],
  "id": "AR-1465",
  "next_action": "Search approved durable archives for the exact reviewed seed digest b3383756b5cd357f58d923216effea33be35b793034de321c3c9ce460ece4b28; do not regenerate or substitute a different seed.",
  "owner": "",
  "plan": "../plans/AR-1465-reviewed-seed-archival-recovery.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Follow-on recovery for the exact reviewed AR-1308 full-exhaustive seed, which is absent from current approved runner roots and Git objects.",
  "task_revision": 1,
  "title": "Reviewed full-exhaustive seed archival recovery",
  "updated_at": "2026-09-26T00:00:00+00:00",
  "worktree_key": "agent-systems-benchmark-state-ar-1465-reviewed-seed-archival-recovery"
}
---

This P0 repair is deliberately limited to recovering the immutable seed input
needed by AR-1308. It must not weaken formal gates or invent equivalent input.

- 2026-09-26: Created from AR-1464's signed preflight result. The exact seed
  digest is absent from the approved second-disk runner roots and state Git
  objects; existing fixtures have different digests. No QEMU/TLC run is
  authorized until the exact bytes are independently recovered.
