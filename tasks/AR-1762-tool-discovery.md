---
{
  "branch": "feature/ar-1762-tool-discovery",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1759",
    "AR-1760"
  ],
  "id": "AR-1762",
  "next_action": "Implement deterministic system/project inventory discovery after AR-1759 and AR-1760.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1762-tool-discovery.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "contract-test",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1762.json",
    "spec_revision": 1,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1762.json",
  "spec_revision": 1,
  "status": "open",
  "summary": "Auto-detect system-installed and project-configured ASB tools with deterministic diagnostics.",
  "task_revision": 2,
  "title": "Discover system and project ASB tools",
  "updated_at": "2026-10-09T15:40:31+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1762-tool-discovery"
}
---

Add a discovery command/API that scans configured project roots and system PATH
locations for known agents, harnesses, benchmarks, workloads, and support tools,
then merges them with project records. Report canonical path, kind, version,
capabilities, digest/availability, and a reason when unavailable. Discovery
must be deterministic, bounded, symlink/path safe, and must not overwrite the
configuration authority; live probes are allowlisted and warning-only when
development authentication/signatures/keys are absent.

- 2026-10-09T15:40:31+00:00: AR-1759 and AR-1760 accepted/released; dependencies verified for
  deterministic tool discovery
