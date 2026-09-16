---
{
  "branch": "fix/shellcheck-fail-closed",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-16T10:21:05+00:00",
  "depends_on": [
    "AR-0003",
    "AR-0897",
    "AR-1008"
  ],
  "id": "AR-0898",
  "next_action": "Pin ShellCheck and prove actionlint cannot silently disable its delegated shell analysis.",
  "observed_branch": "fix/shellcheck-fail-closed",
  "observed_dirty": 0,
  "observed_head": "c261af069c5ce7ecb84b2acfc56f12d2a4cb116a",
  "owner": "asb_ar0898_shellcheck",
  "plan": "../plans/AR-0898.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Resolve GitHub issue 117 by installing and explicitly enforcing a digest-pinned ShellCheck.",
  "task_revision": 9,
  "title": "Make ShellCheck fail closed",
  "updated_at": "2026-09-16T08:23:06+00:00",
  "worktree_key": "agent-systems-benchmark-shellcheck-fail-closed"
}
---
## AR-0898

Resolve [product issue 117](https://github.com/martin-beck/agent-systems-benchmark/issues/117).

Live reproduction confirmed that actionlint 1.7.12 exits successfully while reporting its ShellCheck rule disabled when the binary is absent. Explicit ShellCheck 0.11.0 found no current workflow defect.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-16T08:21:03+00:00: Dependencies AR-0003, AR-0897 and AR-1008 are complete; promote
  ShellCheck fail-closed implementation.

- 2026-09-16T08:21:05+00:00: Claimed by asb_ar0898_shellcheck.

- 2026-09-16T08:21:21+00:00: Recorded command exit 0; command argv SHA-256
  4bd44964fb5c0d94c2efa184bce60cf7708fb428d20ae043e7e3cb902f3ee645.

- 2026-09-16T08:22:05+00:00: Recorded command exit 0; command argv SHA-256
  0bfdd83929bfac7702b79ce4198d3831d6a73a134a70f4b47a6dda15b708f3ab.

- 2026-09-16T08:22:33+00:00: Recorded command exit 0; command argv SHA-256
  94f634820438bfe2655edc21ac06dd11389920a7738c42674b994ee6aae69872.

- 2026-09-16T08:22:49+00:00: Recorded command exit 2; command argv SHA-256
  44fb12f55485790b321a695d51fed8e0c4be4818359353ee7c9d7e502f7ba8db.

- 2026-09-16T08:23:06+00:00: Recorded command exit 0; command argv SHA-256
  fb7023fc57d490ca69459fa64f34339f84c53b020434dc40264232662731acff.
