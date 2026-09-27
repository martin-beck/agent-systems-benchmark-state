---
{
  "branch": "qualification/ar-1491-self-contained-package-qualification-fixture",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-27T17:42:54+00:00",
  "depends_on": [
    "AR-1461",
    "AR-1462",
    "AR-1488",
    "AR-1489"
  ],
  "id": "AR-1491",
  "next_action": "Promote and claim, then implement the non-production signed-test-key package qualification fixture and local/mock/replay harness.",
  "observed_branch": "qualification/ar-1491-self-contained-package-qualification-fixture",
  "observed_dirty": 3,
  "observed_head": "b048fef92f4bdb4eedd5379d645f4288a4b6ab20",
  "owner": "ar1332-record-replay-luna56",
  "plan": "../plans/AR-1491-self-contained-package-qualification-fixture.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Add a self-contained non-production package qualification fixture using the offline verifier test-key pattern.",
  "task_revision": 8,
  "title": "Self-contained package qualification fixture",
  "updated_at": "2026-09-27T15:44:46+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1491-self-contained-package-qualification-fixture"
}
---

AR-1490 is blocked because the exact external signed release package and signing
inputs are absent. This bounded successor supplies deterministic qualification
evidence without pretending to be a production release.

- Use the existing `asb-bundle` offline verifier test-key fixture pattern.
- Exercise checksum/manifest/signature positive and negative cases, then run a
  fresh owner-only local/mock/replay journey with no provider, credentials,
  network, or asb-tui dependency.
- Label every artifact and report as non-production qualification. Preserve the
  real signed-package, allowed-signer, provenance, and release gate for AR-1490
  and customer publication.

No live-provider or release-signing input may be fabricated.

- 2026-09-27T15:42:45+00:00: Dependencies complete; deterministic non-production test-key fixture
  successor for missing external package inputs.

- 2026-09-27T15:42:47+00:00: Claimed by ar1332-record-replay-luna56.

- 2026-09-27T15:42:54+00:00: Heartbeat by ar1332-record-replay-luna56.

- 2026-09-27T15:43:03+00:00: Recorded command exit 0; command argv SHA-256
  5b8ef22b482c1177ec1bc3af92d5bdc2d724a960cbc295cf64ac6bb59ac6b067.

- 2026-09-27T15:43:24+00:00: Recorded command exit 0; command argv SHA-256
  42ce9cf796b72617fca4b356d427d5ae5cd33c5e69b04b9704275ce54f168d05.

- 2026-09-27T15:44:33+00:00: Recorded command exit 1; command argv SHA-256
  44a62e054d9a703da4c2ece6d679e00125d6513c1b1eb9a4a51232f56dcd8834.
