---
{
  "branch": "release/asb-tui-verified-channel",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-0823", "AR-0903", "AR-1012", "AR-1026"],
  "id": "AR-1027",
  "next_action": "Publish the first verified asb-tui release only after ASB release, complete UI/install qualification and exact cross-repository evidence are done.",
  "owner": "",
  "plan": "../plans/AR-1027.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Create and independently promote the first installable signed asb-tui release channel.",
  "task_revision": 1,
  "title": "Publish the verified asb-tui release",
  "updated_at": "2026-09-10T19:00:00+00:00",
  "worktree_key": "agent-systems-benchmark-asb-tui-verified-release"
}
---
Publish immutable signed release artifacts only after the exact ASB release exposes the router and
protocol and every standalone UI, lifecycle, platform, security and usability gate passes. Promote
the signed channel index only after independent download and installation verification.

Acceptance requires signed tag and manifest, executable/source/license/SBOM/provenance artifacts,
reproducible hosted/trusted builds, clean-machine public installation, rollback proof, truthful
channel status, permanent protection restoration and exact post-release evidence.
