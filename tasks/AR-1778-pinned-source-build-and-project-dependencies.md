---
{
  "branch": "feature/ar-1778-pinned-source-build-and-project-dependencies",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1776"],
  "id": "AR-1778",
  "next_action": "Implement catalog-pinned source fallback builds and project-local dependency materialization for supported tools without root or ambient package-manager mutation.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1778-pinned-source-build-and-project-dependencies.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {"evidence_class": "property-or-fuzz", "evidence_digest": "", "evidence_ref": "", "spec_ref": "specs/AR-1778.json", "spec_revision": 1, "status": "pending"},
  "spec_ref": "specs/AR-1778.json",
  "spec_revision": 1,
  "status": "planned",
  "summary": "Build supported tools from verified pinned source and materialize missing dependencies in a project-owned prefix.",
  "task_revision": 1,
  "title": "Pinned source builds and project dependencies",
  "updated_at": "2026-10-10T09:49:36+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1778-pinned-source-build-and-project-dependencies"
}
---

When no compatible verified prebuilt artifact exists, `asb tool install` must
build the supported tool from the acquisition catalog's exact source revision.
Materialize every missing declared build/runtime dependency into a bounded,
project-owned prefix using its own pinned source/artifact recipe, rather than
requiring a user to preinstall it, invoking `sudo`, or mutating global package
manager state. Reuse a system dependency only after validating its catalog
identity and compatibility; record every reuse/build dependency in the receipt.

Builds run in a bounded isolated staging environment with a declared compiler/
toolchain, environment, network phase, resource/time limits, no inherited
credentials, and no arbitrary project shell hooks. Verify source identity before
build, verify declared outputs/entrypoint afterward, collect only safe bounded
diagnostics, atomically publish the final tool and dependency closure, and clean
only transaction-owned staging data. Missing compiler/platform support, failed
dependency build, build-script policy rejection, output mismatch, and resource
limit are distinct actionable outcomes.
