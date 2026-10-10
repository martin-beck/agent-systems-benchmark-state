---
{
  "branch": "feature/ar-1765-tool-project-e2e-qualification",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-10T13:55:07+00:00",
  "depends_on": [
    "AR-1760",
    "AR-1761",
    "AR-1762",
    "AR-1763",
    "AR-1764"
  ],
  "id": "AR-1765",
  "next_action": "Wait for AR-1771 output-router merge, then rebase this signed parser repair onto current main and complete the fresh-user JSON-silence, negative-recovery, full-gate, PR, review, CI, merge, and post-merge qualification.",
  "observed_branch": "feature/ar-1765-tool-project-e2e-qualification",
  "observed_dirty": 0,
  "observed_head": "0bd71b645a1d31ae23749d3c22621d663b1aa165",
  "owner": "ar1765-tool-project-e2e-terra",
  "plan": "../plans/AR-1765-tool-project-e2e-qualification.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "contract-test",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1765.json",
    "spec_revision": 1,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1765.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Qualify the complete fresh-user flow from project init through tool install/discovery/catalog selection and benchmark results.",
  "task_revision": 11,
  "title": "End-to-end qualification of ASB tool projects",
  "updated_at": "2026-10-10T11:55:07+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1765-tool-project-e2e-qualification"
}
---

Build a disposable-machine qualification that starts with a fresh ASB install,
runs `asb project init`, installs at least one fixture of every tool kind,
discovers system and project tools, generates/selects catalogs, executes a
small benchmark, and verifies results and machine-readable config remain in
the project. Cover clean-machine detection, repeatability, partial failures,
unsafe paths, missing credentials/signatures in development mode, human output,
and `--json`. Record a short fresh-user help/tutorial path and exact CI evidence.

- 2026-10-10T11:40:42+00:00: AR-1764 merged at fd61b856570bf1d57e9dba4f8bee1da99b77189e; all
  exact-main post-merge workflows terminal-success and receipt recorded. Start fresh-user end-to-end
  qualification.

- 2026-10-10T11:40:55+00:00: Claimed by ar1765-tool-project-e2e-terra.

- 2026-10-10T11:41:48+00:00: Recorded command exit 0; command argv SHA-256
  8c73f2b423a7f7ef08a6a03236ad094855706daa60df5194e4c4fc21225249fd.

- 2026-10-10T11:42:15+00:00: Completed AR/spec/plan/development-doc review and established the fresh
  merged-base worktree; qualification baseline is in progress.

- 2026-10-10T11:44:17+00:00: Recorded command exit 0; command argv SHA-256
  e274074a17e0682b5edf79b5caca577a41520ed9ca8daf9342f0433b678582a1.

- 2026-10-10T11:44:58+00:00: Disposable five-tool journey reached project-bound execution. Signed
  commit 0bd71b64 accepts the documented --project PATH --local-mock order for run and sweep. JSON
  local-mock stderr leakage is recorded as an AR-1771 output-router dependency and remains out of
  scope.

- 2026-10-10T11:55:07+00:00: Heartbeat by ar1765-tool-project-e2e-terra.
