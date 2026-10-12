---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1729", "AR-1731", "AR-1732", "AR-1733", "AR-1779", "AR-1797", "AR-1799"],
  "id": "AR-1810",
  "next_action": "Replace the ordinary CLI's cli2key rejection with runtime-owned bootstrap and prove real run and sweep execution.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1810-cli2key-standard-cli-integration.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {"evidence_class":"environmental","evidence_digest":"","evidence_ref":"","spec_ref":"specs/AR-1810.json","spec_revision":1,"status":"pending"},
  "spec_ref": "specs/AR-1810.json",
  "spec_revision": 1,
  "status": "planned",
  "summary": "Repair the missing ordinary-ASB CLI bootstrap so cli2key can execute live Codex-agent workloads and sweeps.",
  "task_revision": 1,
  "title": "Complete cli2key Standard CLI Integration",
  "updated_at": "2026-10-12T10:30:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1810-cli2key-standard-cli"
}
---

## Outcome

The installed `asb` executable—not only an injected Rust test API—can run and
sweep a workload with the `cli2key` provider and Codex agent. It resolves the
verified project-local bridge receipt, constructs the runtime-owned sidecar
authority, and passes only its opaque attempt factory to normal run/sweep
dispatch.

## Acceptance

- Remove the direct executable's `cli2key live execution requires a
  runtime-issued sidecar launch` dead end by bootstrapping that authority in
  the ordinary `asb run` and `asb sweep` path.
- Resolve only a verified AR-1779 project-local cli2key installation and its
  pinned identity; no caller endpoint, key, executable, or unverified bridge
  can enter the runtime path.
- Retain one loopback-only sidecar through a run or bounded sweep, expose only
  the opaque per-attempt factory to the CLI, and reap the process/private
  staging on every terminal outcome.
- Add public command-level fake tests from installation through selection, run,
  sweep, results, report, comparison, cancellation, and typed failure paths.
- Run one opt-in live development workload with a manually logged-in bridge and
  retain only redacted outcome/provenance evidence. No external authorization
  policy or production-release requirement may block this development test.
