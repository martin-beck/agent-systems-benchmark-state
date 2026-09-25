---
{
  "branch": "feature/ar-1358-runtime-enrollment-cli-dispatch",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1357"
  ],
  "id": "AR-1358",
  "next_action": "Promote after AR-1357 is done, then wire asb run/sweep through runtime-attested enrollment records with fail-closed positive and negative tests.",
  "observed_branch": "feature/ar-1358-runtime-enrollment-cli-dispatch",
  "observed_dirty": 0,
  "observed_head": "7862e3bb90a777e86e30d23b6af9639935671efe",
  "owner": "",
  "plan": "../plans/AR-1358-runtime-enrollment-cli-dispatch.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "blocked",
  "summary": "Consume runtime-attested enrollment records in asb run and sweep without exposing authority.",
  "task_revision": 10,
  "title": "Runtime enrollment CLI dispatch",
  "updated_at": "2026-09-23T22:28:09+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1358-runtime-enrollment-cli-dispatch"
}
---

Coordinator-created consumer repair for AR-1329 after AR-1357 delivered the
runtime-owned record transport. Do not touch asb-tui or weaken replay/offline
gates.

- 2026-09-24T00:30:00+00:00: Created because AR-1329's remaining dispatch gap is
  distinct from the completed runtime transport primitive.

- 2026-09-23T22:26:02+00:00: AR-1357 is done with merge and post-merge evidence; promote the
  runtime-owned CLI dispatch consumer repair.

- 2026-09-23T22:26:05+00:00: Claimed by codex-asb-runtime-attested-enrollment-luna56.

- 2026-09-23T22:26:12+00:00: Recorded command exit 0; command argv SHA-256
  1068daf3aa96ce8739897a79927707a44394caf77b7b575a00fed63e8d9a446d.

- 2026-09-23T22:26:27+00:00: Recorded command exit 0; command argv SHA-256
  321c534968b9c456a64caf5e6d09b63780c507f97548057d2bfe31edcfd73ff4.

- 2026-09-23T22:26:40+00:00: Recorded command exit 0; command argv SHA-256
  b7c438686581cf292b6cd41497ceabb3af42dfed57e04dfd6cc89efed8e2d15b.

- 2026-09-23T22:27:23+00:00: Recorded command exit 0; command argv SHA-256
  d9968b12c7f956de92f539f058a63496b4c6e90159a690bd701323c4d5bba02c.

- 2026-09-23T22:28:09+00:00: Blocked by exact cross-crate architecture gap: AR-1357 provides
  runtime-private record validation and acquire_from_record, but asb-cli has no safe authenticated
  source. asb-control cannot depend on asb-runtime; attestation/bootstrap constructors are
  intentionally private, so CLI cannot mint or fabricate authority. Existing run/sweep APIs require
  injected opaque LiveProviderAttemptFactory and cannot consume records. Created successor
  AR-1359-runtime-control-bridge (planned, depends on AR-1357) to implement the missing
  runtime-owned bridge. AR-1329 remains fail-closed.

## Current development and CI qualification boundary

The mandatory development and CI qualification path for this AR is a deterministic
local provider/LLM mock (LiteLLM-compatible where practical), including hostile
negative tests and offline replay where applicable. External/live OpenRouter or
other provider reachability is optional supplementary evidence only; it is never a
completion, dependency-readiness, or CI gate. Production egress policy, credential
non-disclosure, runtime-owned authority, namespace/relay attestation, cancellation
and teardown, and fail-closed denial of unapproved external traffic remain required
contracts. Existing live-provider dependency edges describe production integration
ordering only and must not be used to block local qualification or to claim external
reachability.
