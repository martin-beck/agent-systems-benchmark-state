---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1732"
  ],
  "id": "AR-1733",
  "next_action": "Promote after AR-1732; run independent fake and opt-in live qualification and publish user-facing setup/status/reset guidance.",
  "owner": "",
  "plan": "../plans/AR-1733-cli2key-qualification.md",
  "priority": "P1",
  "schema_version": 1,
  "spec_ref": "specs/AR-1733.json",
  "spec_revision": 1,
  "status": "open",
  "summary": "Qualify the complete cli2key setup, run, sweep, fault, cleanup, and privacy journey and document its development-only limits.",
  "task_revision": 2,
  "title": "Qualify and document cli2key development mode",
  "updated_at": "2026-10-09T13:56:16+00:00",
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
