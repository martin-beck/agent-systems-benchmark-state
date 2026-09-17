---
{
  "branch": "repair/ar-1298-narrow-metadata-repair",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-17T07:35:28+00:00",
  "depends_on": [],
  "id": "AR-1298",
  "next_action": "Restore unrelated task files to pre-AR-1297 bytes, retain only evidence-backed schema-failure repairs, regenerate views, and rerun all gates.",
  "observed_branch": "repair/ar-1298-narrow-metadata-repair",
  "observed_dirty": 0,
  "observed_head": "9adb1a2d57435549dec57e49b6f0d24c9ed9ad6b",
  "owner": "asb-ar1298-scope-cleanup",
  "plan": "../plans/AR-1298.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Narrow AR-1297 metadata changes to the exact evidence-backed schema repairs.",
  "task_revision": 9,
  "title": "Narrow task metadata repair scope",
  "updated_at": "2026-09-17T05:37:23+00:00",
  "worktree_key": "agent-systems-benchmark-state-ar-1298-metadata-cleanup"
}
---

## AR-1298

AR-1297 passed all validators but its commit normalized unrelated task files.
This cleanup owns only restoration of incidental changes and preservation of
the exact reported schema repairs. It must not rewrite history, weaken schema,
or touch product, asb-tui, handoffctl, or formal implementation.

- 2026-09-17T05:35:13+00:00: Independent review found incidental task rewrites in AR-1297; narrow
  scope before finalizing metadata publication.

- 2026-09-17T05:35:28+00:00: Claimed by asb-ar1298-scope-cleanup.

- 2026-09-17T05:36:02+00:00: Recorded command exit 0; command argv SHA-256
  4755b81c79c8c3fa0ba3f6c859150436a42939b626baebc3076c10ca774040b4.

- 2026-09-17T05:36:33+00:00: Recorded command exit 0; command argv SHA-256
  c0e0742c558335d140db75756ca0b79832921d337396da85ba2a5660214e9851.

- 2026-09-17T05:36:42+00:00: Recorded command exit 0; command argv SHA-256
  34245c7206030d623f05de34f1c76f5df72cfdeb4b474007c35c354ef3f109f9.

- 2026-09-17T05:37:05+00:00: Recorded command exit 0; command argv SHA-256
  d2cdb60471c075e3acd8081631efe002ca9588c5c19e65d6b238477910a36f5e.

- 2026-09-17T05:37:14+00:00: Recorded command exit 0; command argv SHA-256
  9d64a4d6dd09f2894fa926add0a692ed82209393811d4fd14bae6632bdcd1dc3.

- 2026-09-17T05:37:23+00:00: Recorded command exit 0; command argv SHA-256
  6f2870f75f529d7a08d42a8d3f215d99ef25ed31d169338429ce04e42a4cfbc6.
