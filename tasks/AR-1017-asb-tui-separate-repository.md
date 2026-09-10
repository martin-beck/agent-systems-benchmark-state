---
{
  "branch": "feature/asb-tui-separate-repository",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-0803", "AR-0804", "AR-0805", "AR-0806"],
  "id": "AR-1017",
  "next_action": "Create the standalone asb-tui repository boundary and stable CLI/JSON protocol contract.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1017.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Build asb-tui as an isolated optional repository and extension.",
  "task_revision": 1,
  "title": "Create the standalone asb-tui extension repository",
  "updated_at": "2026-09-10T00:00:00+00:00",
  "worktree_key": "agent-systems-benchmark-asb-tui-separate-repository"
}
---
Create a separate public asb-tui repository containing the optional terminal frontend only. Define a
versioned, capability-negotiated CLI/JSON protocol to the installed ASB program; do not share Cargo
workspace manifests, provider code, benchmark execution, or private coordination history.

Acceptance criteria: isolated repository and worktree, pinned Ratatui/Crossterm inputs, explicit
unverified-extension classification, protocol compatibility matrix, sanitized SBOM/license/provenance
metadata, and tests proving the main benchmark runs independently when the TUI is absent.
