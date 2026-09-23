---
{
  "branch": "feature/ar-1328-openrouter-free-model-config",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-23T09:31:24+00:00",
  "depends_on": [
    "AR-1325",
    "AR-1326",
    "AR-1100"
  ],
  "id": "AR-1328",
  "next_action": "Persist a per-user OpenRouter selection with a pinned free-model identity and enroll the OPENROUTER_API_KEY reference through the credential-free asb-config AuthEnrollment boundary, then wire --use-config into the CLI.",
  "observed_branch": "feature/ar-1328-openrouter-free-model-config",
  "observed_dirty": 0,
  "observed_head": "5207ce478986cdf1687207967cdf517129f85624",
  "owner": "codex-asb-ar1328-20260923",
  "plan": "../plans/AR-1328.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Persist the per-user OpenRouter free-model configuration and credential-free key enrollment.",
  "task_revision": 6,
  "title": "OpenRouter free-model user configuration and key enrollment",
  "updated_at": "2026-09-23T07:35:02+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1328-openrouter-free-model-config"
}
---

The AR-1325/AR-1326 work makes the OpenRouter profile selectable through the
CLI catalog, but the selection and its credential still live only in process
memory or shell state: the AR-1100 `asb-config` crate owns the
credential-free `AuthEnrollment` and `CredentialReference` boundary, yet the CLI
has no `--use-config` wiring and no way to persist a pinned free-model OpenRouter
selection. This AR defines the durable per-user configuration that names the
exact free model, binds the credential reference digest to the
`OPENROUTER_API_KEY` environment channel, and loads it through the CLI without
ever writing a secret to disk. Unsupported, stale, or credential-bearing
configurations fail closed.

- 2026-09-23T07:30:47+00:00: Dependencies AR-1325 and AR-1326 are released; AR-1100 is done. Promote
  next OpenRouter user-configuration AR while AR-1327 post-merge verification continues.

- 2026-09-23T07:31:24+00:00: Claimed by codex-asb-ar1328-20260923.

- 2026-09-23T07:31:58+00:00: Recorded command exit 0; command argv SHA-256
  d7eb8d802ae6845423749ce62fb86178fe290e3c7376ab62af304a8b5f5ba983.

- 2026-09-23T07:35:02+00:00: Recorded command exit 101; command argv SHA-256
  31a05f46a65b4172cfcc5ef4e1ed2b4ddd54c042ac56eff6dc51f4205a4051b1.
