---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-09T16:07:31+00:00",
  "depends_on": [
    "AR-1732"
  ],
  "id": "AR-1733",
  "next_action": "Credential-free qualification implementation committed at 12e28f8 and pushed. Run independent review, focused/full tests, open PR, exact-head CI, then merge through merge_pr.py.",
  "owner": "codex-asb-ar1733-cli2key-20261009",
  "plan": "../plans/AR-1733-cli2key-qualification.md",
  "priority": "P1",
  "schema_version": 1,
  "spec_ref": "specs/AR-1733.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Qualify the complete cli2key setup, run, sweep, fault, cleanup, and privacy journey and document its development-only limits.",
  "task_revision": 27,
  "title": "Qualify and document cli2key development mode",
  "updated_at": "2026-10-09T14:08:39+00:00",
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

- 2026-10-09T13:59:32+00:00: Recorded command exit 0; command argv SHA-256
  86343af567a67fed5c07fe17b9f989e6eda69a94e8452ce52b64a6b1db442ae2.

- 2026-10-09T13:59:45+00:00: Added one-lifetime bounded fake journey, typed fault/privacy matrix,
  cleanup/reset checks, CI workflow step, and user-facing cli2key
  setup/status/reset/cost/methodology guidance.

- 2026-10-09T14:00:13+00:00: Recorded command exit 0; command argv SHA-256
  0af787791bbfbaf33beadf62599df47465b661ad54c1845d159c1d270a82ba73.

- 2026-10-09T14:01:26+00:00: Recorded command exit 0; command argv SHA-256
  342ad6d8c94d5f062f75cdaec0b4171a0da19ea96f098ffa25d0055df575bfac.

- 2026-10-09T14:01:36+00:00: Recorded command exit 0; command argv SHA-256
  72673139415753e2f6bffd22ba55248186289da8b29756a957764de2642ad4e0.

- 2026-10-09T14:01:48+00:00: Recorded command exit 0; command argv SHA-256
  48b26b7f73cfaf6accac1676e298681355088b2a0049f0d9ccc792e2eb79bdde.

- 2026-10-09T14:02:07+00:00: Recorded command exit 0; command argv SHA-256
  e91f86faa2dc32d89c8e7071e6594d54c9e3cb85697eb1fbc02d872ac1ae8320.

- 2026-10-09T14:02:24+00:00: Heartbeat by codex-asb-ar1733-cli2key-20261009.

- 2026-10-09T14:03:34+00:00: Heartbeat by codex-asb-ar1733-cli2key-20261009.

- 2026-10-09T14:04:58+00:00: Heartbeat by codex-asb-ar1733-cli2key-20261009.

- 2026-10-09T14:05:18+00:00: Recorded command exit 0; command argv SHA-256
  bc0ee1d4c99767ed45fd8e72b5d5fca4bd4e3424ac38e4cd47472eb7d346f4f3.

- 2026-10-09T14:06:40+00:00: Recorded command exit 0; command argv SHA-256
  f482422a2ee47377990b6dbd4dedc5553df280925f41eaee65bcc6f89e5f29e4.

- 2026-10-09T14:06:49+00:00: Recorded command exit 0; command argv SHA-256
  72673139415753e2f6bffd22ba55248186289da8b29756a957764de2642ad4e0.

- 2026-10-09T14:07:04+00:00: Recorded command exit 0; command argv SHA-256
  48b26b7f73cfaf6accac1676e298681355088b2a0049f0d9ccc792e2eb79bdde.

- 2026-10-09T14:07:20+00:00: Recorded command exit 0; command argv SHA-256
  f3ca7f65ca03d7ede234f0281a2cfa77075f63f8b97c2263551241e7528d8e75.

- 2026-10-09T14:07:31+00:00: Heartbeat by codex-asb-ar1733-cli2key-20261009.

- 2026-10-09T14:07:42+00:00: Recorded command exit 0; command argv SHA-256
  46760351daaa67cd730a55537cf2b1370b96abe864f8942a75d12a0bc3633a8b.

- 2026-10-09T14:08:16+00:00: Recorded command exit 0; command argv SHA-256
  342ad6d8c94d5f062f75cdaec0b4171a0da19ea96f098ffa25d0055df575bfac.

- 2026-10-09T14:08:25+00:00: Recorded command exit 0; command argv SHA-256
  72673139415753e2f6bffd22ba55248186289da8b29756a957764de2642ad4e0.

- 2026-10-09T14:08:39+00:00: Recorded command exit 0; command argv SHA-256
  48b26b7f73cfaf6accac1676e298681355088b2a0049f0d9ccc792e2eb79bdde.
