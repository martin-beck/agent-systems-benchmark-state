---
{
  "branch": "qualification/ar-1491-self-contained-package-qualification-fixture",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1461", "AR-1462", "AR-1488", "AR-1489", "AR-1490"],
  "id": "AR-1491",
  "next_action": "Promote and claim, then implement the non-production signed-test-key package qualification fixture and local/mock/replay harness.",
  "observed_branch": "qualification/ar-1491-self-contained-package-qualification-fixture",
  "observed_dirty": 0,
  "observed_head": "b048fef92f4bdb4eedd5379d645f4288a4b6ab20",
  "owner": "",
  "plan": "../plans/AR-1491-self-contained-package-qualification-fixture.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Add a self-contained non-production package qualification fixture using the offline verifier test-key pattern.",
  "task_revision": 1,
  "title": "Self-contained package qualification fixture",
  "updated_at": "2026-09-27T15:45:00+00:00",
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
