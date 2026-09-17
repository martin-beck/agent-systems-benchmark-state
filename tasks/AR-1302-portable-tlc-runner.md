---
{
  "branch": "feature/ar-1302-portable-tlc-runner",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1302",
  "next_action": "Promote and provision a digest-pinned x86_64 container/VM runner with portable cgroup containment, bounded thread/memory/swap capacity, and owner-private evidence paths for AR-1293.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "98acd6d5f5a206b351a54689e7817dd43af406ca",
  "owner": "",
  "plan": "../plans/AR-1302.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Provision a clean portable TLC CI/VM runner for state formal admission.",
  "task_revision": 1,
  "title": "Portable TLC CI/VM runner",
  "updated_at": "2026-09-17T07:07:00+00:00",
  "worktree_key": "agent-systems-benchmark-state-ar-1302-portable-tlc-runner"
}
---

## AR-1302

Provision the clean, portable-containment runner required to unblock AR-1293. Keep all images,
VMs, caches, queues, locks and evidence under `/srv/data/projects`; use immutable provenance,
offline-after-install behavior, no network or host-mount access, bounded execution and sanitized
evidence. Native ARM64 is optional and must not be a gate. Do not modify ASB product code,
asb-tui, handoffctl, or unrelated root-owned admission locks.
