---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1805"],
  "id": "AR-1808",
  "next_action": "Define and implement the universal --list discovery and selection contract.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1808-universal-list-selection-contract.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {"evidence_class":"contract-test","evidence_digest":"","evidence_ref":"","spec_ref":"specs/AR-1808.json","spec_revision":1,"status":"pending"},
  "spec_ref": "specs/AR-1808.json",
  "spec_revision": 1,
  "status": "planned",
  "summary": "Make every ASB command discover its valid choices through a consistent, typed --list interface.",
  "task_revision": 1,
  "title": "Universal List and Selection Contract",
  "updated_at": "2026-10-12T10:15:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1808-universal-list-selection"
}
---

## Outcome

Every public command accepts `--list`: without a domain it lists the available
selection domains for that route; with a domain it lists valid selectable IDs,
labels, availability, and the flag that consumes the ID. Commands with no
runtime choice return a clear empty-domain result rather than rejecting the
flag or inventing data.

## Acceptance

- Support root command discovery and every route listed by AR-1805, including
  `asb tui --list`, `asb tool --list`, and `asb workload --list`.
- Cover agents, providers, models/catalogs, workloads, tools, benchmark
  measures, output formats/levels, channels/profiles, and route-specific
  selectors; expose stable IDs plus concise human labels.
- Keep listing read-only and bounded by default. Network refresh, installation,
  and configuration changes require separately explicit flags.
- Provide matching human and `--json` schemas, deterministic ordering, clear
  unavailable/requires-setup states, and tests that each listed ID is accepted
  by its documented selection flag.
