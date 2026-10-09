---
{
  "branch": "feature/ar-1762-tool-discovery",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-09T18:40:34+00:00",
  "depends_on": [
    "AR-1759",
    "AR-1760"
  ],
  "id": "AR-1762",
  "next_action": "Implement deterministic system/project inventory discovery after AR-1759 and AR-1760.",
  "observed_branch": "feature/ar-1762-tool-discovery",
  "observed_dirty": 0,
  "observed_head": "ea5e52bfe843969c493f22146f66ccfa2415159a",
  "owner": "codex-asb-ar1762-tool-discovery-20261009",
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
  "status": "in_progress",
  "summary": "Auto-detect system-installed and project-configured ASB tools with deterministic diagnostics.",
  "task_revision": 9,
  "title": "Discover system and project ASB tools",
  "updated_at": "2026-10-09T15:41:26+00:00",
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

- 2026-10-09T15:40:34+00:00: Claimed by codex-asb-ar1762-tool-discovery-20261009.

- 2026-10-09T15:40:42+00:00: Recorded command exit 128; command argv SHA-256
  2b8452adb1cbcc0952c2f41b8b70232a83047aa768bbd7488006338526dde2ed.

- 2026-10-09T15:40:52+00:00: Recorded command exit 0; command argv SHA-256
  5345cd4b5f66285dc80cddfe59c0a95475263f9ff88d25d2639fce3c300aa4b9.

- 2026-10-09T15:41:07+00:00: Recorded command exit 0; command argv SHA-256
  156749639bcb11d86ef75ad637b668e71f48e845c32368d2c361047aafb3757e.

- 2026-10-09T15:41:18+00:00: Recorded command exit 0; command argv SHA-256
  2b8452adb1cbcc0952c2f41b8b70232a83047aa768bbd7488006338526dde2ed.

- 2026-10-09T15:41:23+00:00: Recorded command exit 0; command argv SHA-256
  bf795ab4a4e7de6c388d3af04e25fd72922ec79e8f19a28042f403ef2ef76d3b.
