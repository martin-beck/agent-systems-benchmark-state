---
{
  "branch": "feature/native-capacity-controller",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-09T15:11:42+00:00",
  "depends_on": [
    "AR-0701",
    "AR-0103"
  ],
  "id": "AR-0704",
  "next_action": "Add bounded CLI operations and lifecycle fixtures around the green atomic ledger, then run full applicable gates and prepare a focused signed candidate.",
  "observed_branch": "feature/native-capacity-controller",
  "observed_dirty": 2,
  "observed_head": "b6d04a8305ce6d49cc327e4e6d2d6fa42a88050b",
  "owner": "contracts_20260906",
  "plan": "../plans/AR-0704.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Control genuine native platform capacity lifecycle.",
  "task_revision": 25,
  "title": "Control native capacity lifecycle",
  "updated_at": "2026-09-09T12:40:47+00:00",
  "worktree_key": "agent-systems-benchmark-native-capacity-controller"
}
---
## AR-0704

Define the credential-isolated reservation/provision/teardown controller for genuine Debian and
openEuler native x86_64 cells on the authorized development host, including local resource
ceilings, availability, privacy, boot identity, and evidence. No emulation or container
substitution satisfies the native x86_64 claim. Native ARM64 is optional future evidence and
must not block this AR or its dependents.

- 2026-09-09T12:11:35+00:00: Explicit authorization received for development-host lifecycle control:
  use existing x86_64 development capacity and keep AArch64 portability under AR-0702; no external
  provider provisioning, emulated-native substitution, or cost-bearing capacity claim. Dependencies
  AR-0701 and AR-0103 are durably done and the control-policy paths are disjoint from active AR-0702
  qualification paths.

- 2026-09-09T12:11:42+00:00: Claimed by contracts_20260906.

- 2026-09-09T12:12:56+00:00: Recorded command exit 0; command argv SHA-256
  5345cd4b5f66285dc80cddfe59c0a95475263f9ff88d25d2639fce3c300aa4b9.

- 2026-09-09T12:13:04+00:00: Recorded command exit 0; command argv SHA-256
  c107569e774896d4dc2c977d011e1a56b9a47d6f8f4f9d1193cb71e139ba20f9.

- 2026-09-09T12:16:18+00:00: Recorded command exit 0; command argv SHA-256
  52fd83c7899d290fc71d2d2d53dd973b3a98a4458397bc437c2b928999700371.

- 2026-09-09T12:16:55+00:00: Recorded command exit 1; command argv SHA-256
  5fb36337b427a59e04ba695cfeb9b4c6f76b92b6a3b6b9d795eeb474b3425af5.

- 2026-09-09T12:17:13+00:00: Recorded command exit 0; command argv SHA-256
  cf516be0d775d0d75952f479dd98da416ebafb57c63cefd7cfc80c821c636266.

- 2026-09-09T12:17:20+00:00: Recorded command exit 1; command argv SHA-256
  12af6705f973a02e5cceba14c2de2e755a8df9d4cb99881a1b4773d29388d322.

- 2026-09-09T12:17:49+00:00: Recorded command exit 0; command argv SHA-256
  7d20d601fc0189bac8f849a131ad230afed7543e9c0ddb5015f6b5706586bbbb.

- 2026-09-09T12:17:56+00:00: Recorded command exit 1; command argv SHA-256
  12af6705f973a02e5cceba14c2de2e755a8df9d4cb99881a1b4773d29388d322.

- 2026-09-09T12:18:32+00:00: Recorded command exit 1; command argv SHA-256
  d66ecd27cb8a7c91fbebde4d22782e9ed4eb1878bdb8ed40e8e707d47e87951f.

- 2026-09-09T12:18:57+00:00: Recorded command exit 1; command argv SHA-256
  d66ecd27cb8a7c91fbebde4d22782e9ed4eb1878bdb8ed40e8e707d47e87951f.

- 2026-09-09T12:32:32+00:00: Recorded command exit 0; command argv SHA-256
  d66ecd27cb8a7c91fbebde4d22782e9ed4eb1878bdb8ed40e8e707d47e87951f.

- 2026-09-09T12:35:46+00:00: Recorded command exit 1; command argv SHA-256
  52fd83c7899d290fc71d2d2d53dd973b3a98a4458397bc437c2b928999700371.

- 2026-09-09T12:36:50+00:00: Recorded command exit 1; command argv SHA-256
  d66ecd27cb8a7c91fbebde4d22782e9ed4eb1878bdb8ed40e8e707d47e87951f.

- 2026-09-09T12:37:08+00:00: Recorded command exit 0; command argv SHA-256
  cf516be0d775d0d75952f479dd98da416ebafb57c63cefd7cfc80c821c636266.

- 2026-09-09T12:37:15+00:00: Recorded command exit 1; command argv SHA-256
  d66ecd27cb8a7c91fbebde4d22782e9ed4eb1878bdb8ed40e8e707d47e87951f.

- 2026-09-09T12:37:40+00:00: Recorded command exit 0; command argv SHA-256
  d66ecd27cb8a7c91fbebde4d22782e9ed4eb1878bdb8ed40e8e707d47e87951f.

- 2026-09-09T12:38:10+00:00: Implemented the provider-neutral persistent lifecycle core in two new
  AR-0704-only paths. The contract binds a sanitized x86_64 capacity pseudonym, trusted class, exact
  owner/revision/deadline, and zero external cost; expired or uncertain work requires positive
  reconciliation. The ledger enforces a private owner-only root, no-follow regular files,
  nonblocking exclusive lock, bounded canonical JSON, descriptor/path identity checks, fsync-backed
  atomic replacement, and fail-closed crash residue. Ten focused tests cover deterministic
  acquire/renew/release, stale/conflicting owner, expiry, cost/architecture/privacy bounds,
  uncertain recovery, corruption, symlink, lock contention, failed-transition atomicity, mid-read
  replacement, root modes, and stale temp state. Focused unittest 10/10, Ruff format/lint, strict
  mypy, and diff-check pass. Worktree remains dirty only in new tools/capacity and tests/capacity
  paths; AR-0702 and runner paths are untouched, and no private host identifier appears.

- 2026-09-09T12:40:21+00:00: Recorded command exit 1; command argv SHA-256
  12af6705f973a02e5cceba14c2de2e755a8df9d4cb99881a1b4773d29388d322.

- 2026-09-09T12:40:40+00:00: Recorded command exit 0; command argv SHA-256
  cf516be0d775d0d75952f479dd98da416ebafb57c63cefd7cfc80c821c636266.

- 2026-09-09T12:40:47+00:00: Recorded command exit 0; command argv SHA-256
  d66ecd27cb8a7c91fbebde4d22782e9ed4eb1878bdb8ed40e8e707d47e87951f.
