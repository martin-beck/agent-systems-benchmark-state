---
{
  "branch": "feature/ar-1810-cli2key-standard-cli",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1729",
    "AR-1731",
    "AR-1732",
    "AR-1733",
    "AR-1779",
    "AR-1797",
    "AR-1799",
    "AR-1812"
  ],
  "id": "AR-1810",
  "next_action": "AR-1812 is the promoted prerequisite for the missing runtime/control-to-CLI cli2key bootstrap seam. After AR-1812 merges, rebase and resume AR-1810 implementation, then complete exact-head review, merge, and post-merge verification.",
  "observed_branch": "feature/ar-1810-cli2key-standard-cli",
  "observed_dirty": 0,
  "observed_head": "07c590e712df11e555228abf1b9de4add3510d4f",
  "owner": "",
  "plan": "../plans/AR-1810-cli2key-standard-cli-integration.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "environmental",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1810.json",
    "spec_revision": 1,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1810.json",
  "spec_revision": 1,
  "status": "blocked",
  "summary": "Repair the missing ordinary-ASB CLI bootstrap so cli2key can execute live Codex-agent workloads and sweeps.",
  "task_revision": 15,
  "title": "Complete cli2key Standard CLI Integration",
  "updated_at": "2026-10-12T10:09:54+00:00",
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

- 2026-10-12T10:01:07+00:00: dependencies AR-1729, AR-1731, AR-1732, AR-1733, AR-1779, AR-1797 and
  AR-1799 verified done; claim for runtime-owned standard cli2key integration

- 2026-10-12T10:01:11+00:00: Claimed by ar1810-cli2key-luna56.

- 2026-10-12T10:02:03+00:00: Dependency-safe AR-1810 selected and claimed after all seven
  dependencies were verified done. Implementation is currently blocked on coordinator metadata: task
  declares worktree_key agent-systems-benchmark-ar-1810-cli2key-standard-cli but branch is empty;
  bind-worktree refuses non-empty legacy metadata, while handoffctl run refuses product mutations
  without declared branch. No product changes made and no gate weakened.

- 2026-10-12T10:02:33+00:00: Released open: handoffctl-only metadata repair is required. Task has
  prefilled worktree_key agent-systems-benchmark-ar-1810-cli2key-standard-cli but empty branch;
  bind-worktree rejects non-empty legacy metadata and no supported handoffctl command clears it. No
  product worktree or implementation mutation was made. Coordinator must repair branch/worktree
  identity durably before re-claim.

- 2026-10-12T10:04:23+00:00: Claimed by ar1810-cli2key-luna56.

- 2026-10-12T10:04:39+00:00: Released to coordinator for supported repair of malformed prefilled
  worktree metadata; no product mutation.

- 2026-10-12T10:05:04+00:00: Claimed by ar1810-cli2key-luna56.

- 2026-10-12T10:05:04+00:00: Bound worktree agent-systems-benchmark-ar-1810-cli2key-standard-cli on
  branch feature/ar-1810-cli2key-standard-cli.

- 2026-10-12T10:05:47+00:00: Coordinator metadata repair completed: malformed prefilled worktree key
  was cleared and rebound with feature/ar-1810-cli2key-standard-cli to the isolated product
  worktree. Product implementation may proceed.

- 2026-10-12T10:08:16+00:00: Reconciled generated state and live doctor successfully after archiving
  oversized generated pycache. Non-TLC gates: focused runtime-control 3/3 passed; full asb-cli
  library suite 437/437 passed offline. No TLC run.

- 2026-10-12T10:09:46+00:00: Heartbeat by ar1810-cli2key-luna56.

- 2026-10-12T10:09:50+00:00: Dependency audit found no existing ownerless AR for the missing seam.
  AR-1779 is marked done but only owns generic tool installation;
  AR-1729/1730/1731/1732/1733/1797/1799 are complete yet expose no production resolver from verified
  project-local receipt to Cli2KeyRuntimeAuthority. Existing handoffctl has no create-task command,
  so no successor was fabricated. AR-1810 remains implementation-blocked pending a
  coordinator-created prerequisite.

- 2026-10-12T10:09:54+00:00: Blocked after repeated audit: no existing ownerless prerequisite owns
  the missing runtime/control-to-CLI cli2key bootstrap seam, and handoffctl has no supported
  task-creation command. Coordinator must create/promote that narrowly scoped prerequisite, then
  re-open AR-1810 with the dependency recorded.
