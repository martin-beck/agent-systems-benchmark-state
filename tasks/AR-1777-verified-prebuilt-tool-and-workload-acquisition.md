---
{
  "branch": "feature/ar-1777-verified-prebuilt-tool-and-workload-acquisition",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1776"],
  "id": "AR-1777",
  "next_action": "Implement catalog-driven verified compatible-binary reuse and official prebuilt tool/workload acquisition into project-local storage.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1777-verified-prebuilt-tool-and-workload-acquisition.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {"evidence_class": "contract-test", "evidence_digest": "", "evidence_ref": "", "spec_ref": "specs/AR-1777.json", "spec_revision": 1, "status": "pending"},
  "spec_ref": "specs/AR-1777.json",
  "spec_revision": 1,
  "status": "planned",
  "summary": "Acquire, verify, and atomically install official compatible prebuilt executable tools into a project-local root.",
  "task_revision": 2,
  "title": "Verified prebuilt tool acquisition",
  "updated_at": "2026-10-10T09:49:36+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1777-verified-prebuilt-tool-and-workload-acquisition"
}
---

Implement catalog-driven acquisition for a compatible existing system binary and
for official prebuilt executable tools. The resolver selects only an entry
matching the current OS, architecture, libc/ABI and catalog identity; downloads
only from the catalog's primary source; verifies TLS transfer policy, immutable
digest, signature/provenance when declared, archive boundaries, executable
entrypoint, and license metadata before atomically publishing under the
selected project. It records the exact catalog revision, source identity,
artifact digest, verifier outcome, platform, and usable entrypoint.

No partial output becomes active. Failed transfer, checksum/signature mismatch,
wrong platform, archive traversal, unsafe executable, revoked artifact, and
offline/unavailable source must be separately diagnosed and leave the previous
usable installation intact. Do not execute downloaded installer scripts, require
root, persist credentials, or use a package manager. Use the shared human status
reporting contract when available while keeping machine-mode output safe.
