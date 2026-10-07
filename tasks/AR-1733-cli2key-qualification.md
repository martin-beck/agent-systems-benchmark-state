---
{
  "id": "AR-1733",
  "title": "Qualify and document cli2key development mode",
  "priority": "P1",
  "depends_on": ["AR-1732"],
  "plan": "../plans/AR-1733-cli2key-qualification.md",
  "summary": "Qualify the complete cli2key setup, run, sweep, fault, cleanup, and privacy journey and document its development-only limits.",
  "status": "planned",
  "next_action": "Promote after AR-1732; run independent fake and opt-in live qualification and publish user-facing setup/status/reset guidance.",
  "owner": "",
  "claim_expires": "",
  "checkpoint_commit": "",
  "task_revision": 1,
  "schema_version": 1,
  "spec_ref": "specs/AR-1733.json",
  "spec_revision": 1,
  "updated_at": "2026-10-07T23:21:33+00:00",
  "branch": "",
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
