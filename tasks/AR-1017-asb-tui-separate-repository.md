---
{
  "branch": "feature/asb-tui-separate-repository",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-10T11:57:32+00:00",
  "depends_on": [
    "AR-0803",
    "AR-0804",
    "AR-0805",
    "AR-0806",
    "AR-0851"
  ],
  "id": "AR-1017",
  "next_action": "Create the standalone asb-tui repository boundary and stable CLI/JSON protocol contract.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "contracts_20260906",
  "plan": "../plans/AR-1017.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Build asb-tui as an isolated optional repository and extension.",
  "task_revision": 7,
  "title": "Create the standalone asb-tui extension repository",
  "updated_at": "2026-09-10T08:58:53+00:00",
  "worktree_key": "agent-systems-benchmark-asb-tui-separate-repository"
}
---
Create a separate public asb-tui repository containing the optional terminal frontend only. Consume
the latest immutable releases of `martin-beck/agent-workflow-coordinator` and
`martin-beck/agent-workflow-quality`, recording exact tags/commits, artifact digests, signatures,
licenses, and compatibility in a lock manifest. Define a versioned, capability-negotiated CLI/JSON
protocol to the installed ASB program; do not share Cargo
workspace manifests, provider code, benchmark execution, or private coordination history.

Acceptance criteria: isolated repository and worktree, latest-release discovery that rejects mutable
or unsigned inputs, pinned coordinator/quality/Ratatui/Crossterm inputs, explicit
unverified-extension classification, protocol compatibility matrix, sanitized SBOM/license/provenance
metadata, and tests proving the main benchmark runs independently when the TUI is absent.

- 2026-09-10T08:55:59+00:00: Promote standalone asb-tui extension boundary after dependency
  preflight.

- 2026-09-10T08:57:32+00:00: Claimed by contracts_20260906.

- 2026-09-10T08:58:06+00:00: Recorded command exit 0; command argv SHA-256
  42a502c9a2ee9cf5bea7b8a16c82cd4845a0f513fde9cfb55f13095b40b120a4.

- 2026-09-10T08:58:20+00:00: Recorded command exit 0; command argv SHA-256
  b0ed9dcaecd924d95cf0a33d420a9fe950657c7e20599add0036d47e052af603.

- 2026-09-10T08:58:39+00:00: Recorded command exit 0; command argv SHA-256
  92dd972edd1a176a56751859e55d72e93598cd4098694b248effb76fa55a9631.

- 2026-09-10T08:58:53+00:00: Recorded command exit 0; command argv SHA-256
  b93e4b1ba3ebf72928cac6689e8562cc6c1e940c8a1759dc1b3e981716383910.
