---
{
  "branch": "feature/ar-1801-tool-discovery-cargo-fixture-isolation",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-12T06:18:42+00:00",
  "depends_on": [
    "AR-1762"
  ],
  "id": "AR-1801",
  "next_action": "Repair the tool-discovery version-probe fixture so full-workspace tests isolate ambient Cargo and retain deterministic unavailable/version observations.",
  "observed_branch": "feature/ar-1801-tool-discovery-cargo-fixture-isolation",
  "observed_dirty": 1,
  "observed_head": "98327152f2e92308b5bcf5b21cfe0c9f285cf950",
  "owner": "ar1801-cargo-fixture-luna56",
  "plan": "../plans/AR-1801-tool-discovery-cargo-fixture-isolation.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "contract-test",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1801.json",
    "spec_revision": 1,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1801.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Make tool-discovery Cargo version fixture deterministic under full workspace execution.",
  "task_revision": 7,
  "title": "Tool-discovery Cargo fixture isolation",
  "updated_at": "2026-10-12T02:19:55+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1801-tool-discovery-cargo-fixture-isolation"
}
---
Created from AR-1772 full-gate evidence. The exact failing test is
`tool_discovery::tests::path_discovery_is_deterministic_and_bounded`: the
fixture expected Cargo version `null` with `version_probe_unavailable`, while
ambient PATH Cargo produced version `1.0` and no warning. Repair must isolate
or pin the probe without weakening bounded execution or privacy contracts.

- 2026-10-12T02:18:42+00:00: dependency AR-1762 verified done

- 2026-10-12T02:18:42+00:00: Claimed by ar1801-cargo-fixture-luna56.

- 2026-10-12T02:19:06+00:00: Recorded command exit 0; command argv SHA-256
  00012a491b2f6d8d01149d6c8eac49ac352e3bd6209aea0a6f1f1e7e0db1a44d.

- 2026-10-12T02:19:55+00:00: Recorded command exit 0; command argv SHA-256
  9c6a285edf453dc229e9fb68e995cf771df21be220af575e86a482d77b5089fd.
