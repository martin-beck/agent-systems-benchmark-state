---
{
  "branch": "feature/cli-setup-wizard",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-0869",
    "AR-1100",
    "AR-1101",
    "AR-1102"
  ],
  "id": "AR-1103",
  "next_action": "Implement the CLI setup wizard and config print/validate commands after the registry, registry profiles and UserConfigV1 exist.",
  "observed_branch": "feature/cli-setup-wizard",
  "observed_dirty": 0,
  "observed_head": "9dc31ce19ecbf3014ba2bdeec7e44b801d823e95",
  "owner": "",
  "plan": "../plans/AR-1103.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Add the interactive and non-interactive setup wizard that writes UserConfigV1 and selection output.",
  "task_revision": 2,
  "title": "Add the CLI setup wizard",
  "updated_at": "2026-09-22T10:16:40+00:00",
  "worktree_key": "agent-systems-benchmark-cli-setup-wizard"
}
---
Add the `asb setup` wizard (interactive and `--non-interactive`) that selects a registry provider,
then a model offered by that provider, chooses default vs selected-agent scope, accepts a redacted
credential reference, and atomically writes a UserConfigV1 file and/or provider-plan selection.
Repository: `martin-beck/agent-systems-benchmark`.

- 2026-09-13T09:57:00+00:00: Frozen scope for parallel setup-wizard series AR-1100..AR-1106.
  The wizard never requires live APIs, network, credential values or a user in CI: it runs fully
  non-interactively and stores only the reference digest.
