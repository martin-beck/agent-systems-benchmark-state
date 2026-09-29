---
{
  "branch": "feature/replay-openhands-environment-pin",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-0309"
  ],
  "id": "AR-0521",
  "next_action": "Use the recorded AR-0514 failure evidence to define an immutable, reproducible OpenHands environment bundle and verifier; AR-0514 remains blocked until this evidence is independently verified.",
  "observed_branch": "feature/replay-openhands-environment-pin",
  "observed_dirty": 0,
  "observed_head": "bd7d10d4a760a84fa42de2b1fa9e97e8ea85ba09",
  "owner": "",
  "plan": "../plans/AR-0521.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "blocked",
  "summary": "Repair OpenHands replay environment provenance and reproducibility.",
  "task_revision": 11,
  "title": "Reproduce and pin the OpenHands replay environment",
  "updated_at": "2026-09-29T10:31:27+00:00",
  "worktree_key": "agent-systems-benchmark-replay-openhands-environment-pin"
}
---
## AR-0521

Repair missing reproducible provenance for the approved OpenHands replay environment. Do not bypass the digest or use unverifiable proprietary artifacts.

Acceptance requires a content-addressed environment bundle, offline verifier, dependency and license evidence, reproducible rebuild instructions, and a negative altered-input test. Only then may AR-0514 be reclaimed.

- 2026-09-08T10:50:00+00:00: Restored the required zero-hash sentinel for an unobserved
  planned worktree.

- 2026-09-29T10:15:22+00:00: AR-0309 is done; AR-0514 failure evidence is independently reviewed and
  is an explicit repair input, not a circular completion dependency. Begin immutable OpenHands
  provenance repair.

- 2026-09-29T10:15:29+00:00: Claimed by ar0521-environment-pin-luna56.

- 2026-09-29T10:17:07+00:00: Heartbeat by ar0521-environment-pin-luna56.

- 2026-09-29T10:18:42+00:00: Recorded command exit 0; command argv SHA-256
  7c6e56db809ea67d791db0aad45a1d0b4e7fe93c6218faa4f1f1856d76d6bc4e.

- 2026-09-29T10:25:52+00:00: Heartbeat by ar0521-environment-pin-luna56.

- 2026-09-29T10:25:55+00:00: Heartbeat by ar0521-environment-pin-luna56.

- 2026-09-29T10:30:11+00:00: Recorded command exit 2; command argv SHA-256
  ff9297d17c0732874297929773bce1e7f679caddd77de7a11179d73b2a300879.

- 2026-09-29T10:31:27+00:00: Bounded repair audit complete: AR-0309 retains only source
  revision/tree, wheel/source hashes, CPython digest, 120-line version freeze, and approved
  environment digest 6372756912734f6275362a8b66c3758fd2b2adeab776eb2a0be7935f34abb9b2. Five
  dependency-preserving recipes remain non-matching (prefixes 10857178, 74e71e58, 006ea070,
  cb50d5ad, bca74255). No lock archive, exact interpreter, hashed wheels, site-packages tree, SBOMs,
  or signature exists in retained/public inputs. No digest override, proprietary artifact,
  credentials, provider, or native replay used. Isolated worktree was created; product
  implementation was not applied because exact provenance inputs are unavailable and a verifier
  cannot truthfully manufacture them. Next action: recover those retained/public inputs, then build
  and independently verify the signed offline bundle before AR-0514 native replay.
