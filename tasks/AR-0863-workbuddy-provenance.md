---
{
  "branch": "feature/workbuddy-provenance",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-0101",
    "AR-0102",
    "AR-0103",
    "AR-0310",
    "AR-0315",
    "AR-0317",
    "AR-0503",
    "AR-0855"
  ],
  "id": "AR-0863",
  "next_action": "Pin official source, package, dependency closure, license, executable digest, protocol mode, and supported platform before any adapter claim.",
  "observed_branch": "feature/workbuddy-provenance",
  "observed_dirty": 0,
  "observed_head": "9aad1317bdcaabcec2e62a856ff6d0b3ac757f46",
  "owner": "",
  "plan": "../plans/AR-0863.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "blocked",
  "summary": "Pin WorkBuddy source, package, and license provenance.",
  "task_revision": 10,
  "title": "Pin WorkBuddy source, package, and license provenance",
  "updated_at": "2026-09-09T03:18:06+00:00",
  "worktree_key": "agent-systems-benchmark-workbuddy-provenance"
}
---
## AR-0863

Pin official source, package, dependency closure, license, executable digest, protocol mode, and supported platform before any adapter claim.

This phase cannot claim support from mocks, parser fixtures, source inspection, compilation, or mutable artifacts. If its executable evidence is unavailable, leave this child blocked with exact provenance evidence while the sibling agent series proceeds.

- 2026-09-09T03:14:56+00:00: All eight dependencies are done; promote WorkBuddy provenance as the
  next highest-priority dependency-ready provider track.

- 2026-09-09T03:14:59+00:00: Claimed by replay_20260909.

- 2026-09-09T03:15:01+00:00: Heartbeat by replay_20260909.

- 2026-09-09T03:15:25+00:00: Recorded command exit 0; command argv SHA-256
  0fd9374bae63847b1da633949f37b96fc52dcb33464ba84b001b496d6e7c03b3.

- 2026-09-09T03:15:53+00:00: Recorded command exit 0; command argv SHA-256
  e3545c7eb677bc2c5c258732bf86746a830f4ddf71cd2993ca1adf6935bbcad4.

- 2026-09-09T03:16:28+00:00: Recorded command exit 0; command argv SHA-256
  22600a3995212b0adcf1edae445ea941e2d8a751506bf9e92e18980eb4228aed.

- 2026-09-09T03:17:13+00:00: Recorded command exit 1; command argv SHA-256
  7f86ac116c4b310a833a163050deb6af78cde960e72f11131ba72b3c4fa5f201.

- 2026-09-09T03:18:06+00:00: Blocked with exact evidence: official WorkBuddy pages
  https://www.workbuddy.ai/ and https://copilot.tencent.com/work/ expose dynamically served
  macOS/Windows installers and account-backed service only; official installation docs state Windows
  10+ and macOS 12+ but publish no immutable artifact URL, checksum, signature, source repository,
  dependency lock, or noninteractive protocol. GitHub search found Tencent/workbuddy-bench
  (benchmark only) and third-party mirrors/proxies, none authoritative executable provenance. No
  product files changed; clean declared worktree preserved. Next action: obtain an authorized
  immutable Tencent WorkBuddy installer/source publication with SHA-256/signature, license and
  dependency closure, plus a credential-free protocol test boundary; do not substitute mirrors,
  proxies, or private artifacts.
