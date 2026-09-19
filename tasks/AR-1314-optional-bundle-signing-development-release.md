---
{
  "branch": "feature/ar-1314-optional-bundle-signing",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-19T09:56:27+00:00",
  "depends_on": [],
  "id": "AR-1314",
  "next_action": "Add CLI/profile coverage, run full ASB gates, then review and publish the clean signed PR; formal AR-1307/1308 remain signature-required.",
  "observed_branch": "feature/ar-1314-optional-bundle-signing",
  "observed_dirty": 9,
  "observed_head": "78a8e9fc2144623311e315fcc4e46c2831b0b2c1",
  "owner": "ar1314_bundle_profile",
  "plan": "../plans/AR-1314.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Make runtime-bundle signatures optional only through an explicit, truthfully labelled development/release profile.",
  "task_revision": 27,
  "title": "Optional runtime-bundle signing for development and tagged releases",
  "updated_at": "2026-09-19T07:58:41+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1314-optional-bundle-signing"
}
---

# AR-1314

ASB development and tagged-release workflows must be able to publish a runtime bundle without a
detached bundle signature when explicitly selected. This does not remove commit/DCO integrity,
exact content digests, SBOMs, provenance, target checks, or release/tag verification. The default
installer/verifier remains signature-required; unsigned output must be opt-in, clearly labelled,
and rejected as formal qualification evidence.

The implementation must add versioned policy/profile metadata, positive and negative tests,
updated schemas/generated documentation, helpful failure messages, and an offline path. It must
not weaken AR-1307/AR-1308 full-exhaustive formal gates: those continue to require the exact
reviewed signed input bundle and terminal attestation.

- 2026-09-19T07:45:37+00:00: Dependencies are empty; promote explicit unsigned development/release
  profile implementation while preserving formal gates.

- 2026-09-19T07:46:29+00:00: Claimed by ar1314_bundle_profile.

- 2026-09-19T07:47:01+00:00: Recorded command exit 0; command argv SHA-256
  9ce28bbb59af15b4a34d9cab9cde7b29c5b76683dd446d280ae4b21f09407d2e.

- 2026-09-19T07:47:30+00:00: Recorded command exit 0; command argv SHA-256
  416936102312518bc032ec45a68736d742b34b9271d7a68688aaf99b9c8c3bf0.

- 2026-09-19T07:48:13+00:00: Recorded command exit 0; command argv SHA-256
  c4826fc3c54b3fad6bc5209245ff2566a6f53630576266e097eef91f8a96beef.

- 2026-09-19T07:50:32+00:00: Recorded command exit 101; command argv SHA-256
  7d8f9b35dbe47dc283e140e0f2c100bfc96671e55e1e272123a46160b04a26cd.

- 2026-09-19T07:50:51+00:00: Recorded command exit 101; command argv SHA-256
  98b14edf2a525dfaacad74b297750831f9e57ed7549e2624c0a5420cc564f3e2.

- 2026-09-19T07:51:14+00:00: Recorded command exit 0; command argv SHA-256
  5c2c153e2f434c40c78a037ecd2a0e260614332d83a927394666575b66c616a9.

- 2026-09-19T07:51:34+00:00: Recorded command exit 0; command argv SHA-256
  98b14edf2a525dfaacad74b297750831f9e57ed7549e2624c0a5420cc564f3e2.

- 2026-09-19T07:51:51+00:00: Focused cargo test first exited 101 because generated schema/v2 lagged
  the new profile/status fields; regenerated the checked schema and reran cargo test -p asb-bundle
  successfully (21 verifier, 2 schema, 4 unit tests). No product failure or gate weakening.

- 2026-09-19T07:53:30+00:00: Recorded command exit 0; command argv SHA-256
  d43baaf07b37e5983d58e89055f9e3b8e7d46904dbf7bcb4724239874b87409e.

- 2026-09-19T07:53:49+00:00: Recorded command exit 0; command argv SHA-256
  3ead084eabc4aa358936eebefbc35e828aadd8d496ece3d76bd51125cd9da724.

- 2026-09-19T07:55:41+00:00: Heartbeat by ar1314_bundle_profile.

- 2026-09-19T07:55:51+00:00: The full focused cargo test reached terminal success: 4 unit, 21
  offline verifier, 2 schema-conformance, and 0 doctests passed. The handoffctl post-record then
  exited 101 with LOCK_TIMEOUT after 10s while acquiring the coordinator lock; this is coordination
  bookkeeping only, not a product test failure. Heartbeat renewed and retrying state update.

- 2026-09-19T07:56:27+00:00: Heartbeat by ar1314_bundle_profile.

- 2026-09-19T07:56:30+00:00: Recorded command exit 0; command argv SHA-256
  d43baaf07b37e5983d58e89055f9e3b8e7d46904dbf7bcb4724239874b87409e.

- 2026-09-19T07:56:45+00:00: Recorded command exit 101; command argv SHA-256
  98b14edf2a525dfaacad74b297750831f9e57ed7549e2624c0a5420cc564f3e2.

- 2026-09-19T07:56:58+00:00: Recorded command exit 0; command argv SHA-256
  d43baaf07b37e5983d58e89055f9e3b8e7d46904dbf7bcb4724239874b87409e.

- 2026-09-19T07:57:16+00:00: Recorded command exit 0; command argv SHA-256
  98b14edf2a525dfaacad74b297750831f9e57ed7549e2624c0a5420cc564f3e2.

- 2026-09-19T07:57:42+00:00: Recorded command exit 0; command argv SHA-256
  2d322e3f6936159dcff6cb659168fcdf40d0225f6c4e837ce3423d8bab95826f.

- 2026-09-19T07:58:41+00:00: Recorded command exit 0; command argv SHA-256
  f09a28f66e1fc227b80abbbc9e6e5e4b1484e1d40abc5d88794ac34795421ba6.
