---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-09T15:56:19+00:00",
  "depends_on": [
    "AR-1732"
  ],
  "id": "AR-1733",
  "next_action": "Audit public cli2key setup/status/run/sweep/result/reset surfaces and existing fake-sidecar coverage in fresh worktree; add qualification journey, hostile fault/privacy tests, and user documentation.",
  "owner": "codex-asb-ar1733-cli2key-20261009",
  "plan": "../plans/AR-1733-cli2key-qualification.md",
  "priority": "P1",
  "schema_version": 1,
  "spec_ref": "specs/AR-1733.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Qualify the complete cli2key setup, run, sweep, fault, cleanup, and privacy journey and document its development-only limits.",
  "task_revision": 7,
  "title": "Qualify and document cli2key development mode",
  "updated_at": "2026-10-09T13:59:16+00:00",
  "worktree_key": ""
}
---

Add complete credential-free CI using a protocol-faithful fake sidecar and a
separate opt-in live Codex OAuth qualification. Cover setup, status, model
discovery, run, bounded concurrent sweep, results, comparison, cancellation,
reset, and cleanup. Add hostile tests for stale/wrong keys, non-loopback bind,
substitution, symlinks/modes, malformed or oversized responses, timeout,
crash/orphan/restart, concurrent sweeps, and redaction.

Document that the generated key authenticates only the local proxy, that live
usage consumes the user's Codex entitlement subject to upstream policy, and
that this path is unofficial, development-only, opt-in, and not a production
or official OpenAI Platform API-key claim.

- 2026-10-09T13:56:16+00:00: AR-1732 is durably accepted/released at signed merge 942c7b1 with green
  exact-main workflows; dependency verified.

- 2026-10-09T13:56:19+00:00: Claimed by codex-asb-ar1733-cli2key-20261009.

- 2026-10-09T13:56:25+00:00: Recorded command exit 0; command argv SHA-256
  e073b6eb0501ee117c85b38fcec7db7cddc75e8f66009a0de796940e5415d617.

- 2026-10-09T13:56:50+00:00: Fresh isolated worktree created at
  /srv/data/projects/agent-systems-benchmark-ar-1733-cli2key-qualification on
  feature/ar-1733-cli2key-qualification.

- 2026-10-09T13:58:49+00:00: Recorded command exit 0; command argv SHA-256
  311e78f4651f64e5ca0220849f0db93a5918b520108dbabecb12e0aed427ecb7.

- 2026-10-09T13:59:16+00:00: Recorded command exit 0; command argv SHA-256
  1b3820eb6d0676ce20ffb79a91f900a6e8fe6bdbd2311b558f68f3fe2793896a.
