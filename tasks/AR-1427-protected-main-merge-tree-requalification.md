---
{
  "branch": "codex/ar-1427-merge-requal",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-24T23:25:50+00:00",
  "depends_on": [
    "AR-1421"
  ],
  "id": "AR-1427",
  "next_action": "Promote and reproduce PR #310 merge f511645 versus reviewed topic 9d97e168; repair exact protected-main merge-tree requalification, then rerun AR-1215 post-merge evidence.",
  "observed_branch": "codex/ar-1427-merge-requal",
  "observed_dirty": 3,
  "observed_head": "f51164569bf4da67a0759328b4be280385abe9a4",
  "owner": "ar1427-merge-requal-luna56",
  "plan": "../plans/AR-1427-protected-main-merge-tree-requalification.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Repair exact protected-main merge-tree requalification after sequential tutorial merges.",
  "task_revision": 7,
  "title": "Protected-main merge-tree requalification repair",
  "updated_at": "2026-09-24T21:29:20+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1427-merge-requal"
}
---

This repair preserves the exact-tree policy while making sequential protected
main merges safe. The AR-1215 failure run `36060277237` remains immutable
incident evidence; no gate is waived.

- 2026-09-24: Added after Repository Quality rejected merge `f511645` because
  the protected merge tree differed from reviewed topic tree `9d97e168`.

- 2026-09-24T21:23:49+00:00: Promote protected-main merge-tree requalification repair after AR-1215
  post-merge policy failure 36060277237.

- 2026-09-24T21:25:50+00:00: Claimed by ar1427-merge-requal-luna56.

- 2026-09-24T21:26:10+00:00: Recorded command exit 0; command argv SHA-256
  88d86267fcba4a31b51d75f493d4981ee26856992977a659070356289f7bc042.

- 2026-09-24T21:27:32+00:00: Recorded command exit 1; command argv SHA-256
  ac99b772dd8bd62096364ead4849ecaefc960101488bf7324f352f35029df1f7.

- 2026-09-24T21:29:20+00:00: Recorded command exit 0; command argv SHA-256
  ff6d1fa7a7185010f75fcfafe4bdc1bdd5b9804d8c2b3e7abdd8a1b96cd81c63.
