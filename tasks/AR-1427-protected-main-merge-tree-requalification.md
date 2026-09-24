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
  "observed_dirty": 0,
  "observed_head": "81f02d294dc51894a35c6b5273cacde2bb392ef3",
  "owner": "ar1427-merge-requal-luna56",
  "plan": "../plans/AR-1427-protected-main-merge-tree-requalification.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Repair exact protected-main merge-tree requalification after sequential tutorial merges.",
  "task_revision": 36,
  "title": "Protected-main merge-tree requalification repair",
  "updated_at": "2026-09-24T21:42:56+00:00",
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

- 2026-09-24T21:29:34+00:00: Recorded command exit 0; command argv SHA-256
  7c730eec3ea71bd24ffc5a9255bf7f542481bf601dba6c72bed6e00f6c2fab3c.

- 2026-09-24T21:29:49+00:00: Recorded command exit 0; command argv SHA-256
  8b8593044d3ca935d540ebaee28ce9b821aef8ae70cced56f790ac5640c72663.

- 2026-09-24T21:30:11+00:00: Recorded command exit 0; command argv SHA-256
  9f1650afbb3adb81004300430acf4764511525ff040a3ca32c8006d11484de61.

- 2026-09-24T21:30:36+00:00: Recorded command exit 0; command argv SHA-256
  ac99b772dd8bd62096364ead4849ecaefc960101488bf7324f352f35029df1f7.

- 2026-09-24T21:31:46+00:00: Recorded command exit 0; command argv SHA-256
  ae406dea0c3b651f5287170cb3a3c17b3f7bf1f1d4c507ee26c337ee8b9aa879.

- 2026-09-24T21:32:06+00:00: Recorded command exit 0; command argv SHA-256
  88c9dd0608200a51dbc41f39b119652d7e1ae7885546b06f9be2da49eaac69ea.

- 2026-09-24T21:32:29+00:00: Recorded command exit 0; command argv SHA-256
  2be1455e1fbb4d43f10a25c81d518869ac65da40d2a715539f0960a4d886c013.

- 2026-09-24T21:32:47+00:00: Recorded command exit 8; command argv SHA-256
  7e8254165b378afb5fd0c6618ea9cb8f955ef7007e5e305b80882360f77ee2a5.

- 2026-09-24T21:33:37+00:00: Recorded command exit 8; command argv SHA-256
  7e8254165b378afb5fd0c6618ea9cb8f955ef7007e5e305b80882360f77ee2a5.

- 2026-09-24T21:34:15+00:00: Recorded command exit 8; command argv SHA-256
  7e8254165b378afb5fd0c6618ea9cb8f955ef7007e5e305b80882360f77ee2a5.

- 2026-09-24T21:35:02+00:00: Recorded command exit 8; command argv SHA-256
  7e8254165b378afb5fd0c6618ea9cb8f955ef7007e5e305b80882360f77ee2a5.

- 2026-09-24T21:35:17+00:00: Recorded command exit 8; command argv SHA-256
  7e8254165b378afb5fd0c6618ea9cb8f955ef7007e5e305b80882360f77ee2a5.

- 2026-09-24T21:36:01+00:00: Recorded command exit 8; command argv SHA-256
  7e8254165b378afb5fd0c6618ea9cb8f955ef7007e5e305b80882360f77ee2a5.

- 2026-09-24T21:36:21+00:00: Recorded command exit 8; command argv SHA-256
  7e8254165b378afb5fd0c6618ea9cb8f955ef7007e5e305b80882360f77ee2a5.

- 2026-09-24T21:36:54+00:00: Recorded command exit 8; command argv SHA-256
  7e8254165b378afb5fd0c6618ea9cb8f955ef7007e5e305b80882360f77ee2a5.

- 2026-09-24T21:37:12+00:00: Recorded command exit 0; command argv SHA-256
  7f80731483bccd01223169821fab9cfd9845c83ace9e558f57bf56a97a849276.

- 2026-09-24T21:37:50+00:00: Recorded command exit 8; command argv SHA-256
  7e8254165b378afb5fd0c6618ea9cb8f955ef7007e5e305b80882360f77ee2a5.

- 2026-09-24T21:38:06+00:00: Recorded command exit 8; command argv SHA-256
  7e8254165b378afb5fd0c6618ea9cb8f955ef7007e5e305b80882360f77ee2a5.

- 2026-09-24T21:39:00+00:00: Recorded command exit 8; command argv SHA-256
  7e8254165b378afb5fd0c6618ea9cb8f955ef7007e5e305b80882360f77ee2a5.

- 2026-09-24T21:39:32+00:00: Recorded command exit 8; command argv SHA-256
  7e8254165b378afb5fd0c6618ea9cb8f955ef7007e5e305b80882360f77ee2a5.

- 2026-09-24T21:39:57+00:00: Recorded command exit 8; command argv SHA-256
  7e8254165b378afb5fd0c6618ea9cb8f955ef7007e5e305b80882360f77ee2a5.

- 2026-09-24T21:40:26+00:00: Recorded command exit 8; command argv SHA-256
  7e8254165b378afb5fd0c6618ea9cb8f955ef7007e5e305b80882360f77ee2a5.

- 2026-09-24T21:40:50+00:00: Recorded command exit 8; command argv SHA-256
  7e8254165b378afb5fd0c6618ea9cb8f955ef7007e5e305b80882360f77ee2a5.

- 2026-09-24T21:41:09+00:00: Recorded command exit 0; command argv SHA-256
  765c39026547401912d817152eeeb9ee57ef3aadbb88aae2e5aa267022bfef5b.

- 2026-09-24T21:42:03+00:00: Recorded command exit 0; command argv SHA-256
  765c39026547401912d817152eeeb9ee57ef3aadbb88aae2e5aa267022bfef5b.

- 2026-09-24T21:42:18+00:00: Recorded command exit 0; command argv SHA-256
  7e8254165b378afb5fd0c6618ea9cb8f955ef7007e5e305b80882360f77ee2a5.

- 2026-09-24T21:42:36+00:00: Recorded command exit 0; command argv SHA-256
  e6dd66fc904999f00789c01fb80080490621860052897383acc25b3235181cbe.

- 2026-09-24T21:42:56+00:00: Recorded command exit 0; command argv SHA-256
  64450c58d30932f1c4051195cf8eeb1a55404a98900d593f2016335009aeb2c4.
