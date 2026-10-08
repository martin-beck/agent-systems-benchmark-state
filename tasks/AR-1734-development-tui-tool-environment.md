---
{
  "branch": "repair/ar-1734-development-tui-tool-environment",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-08T04:41:07+00:00",
  "depends_on": [
    "AR-1726",
    "AR-1727"
  ],
  "id": "AR-1734",
  "next_action": "Claim in an isolated ASB worktree; reproduce the AR-1713 installed-launch failure, then pass only validated development tool identities across the scrubbed broker environment with hostile replacement tests.",
  "observed_branch": "repair/ar-1734-development-tui-tool-environment",
  "observed_dirty": 1,
  "observed_head": "736a65cd8904b8f4a6f1715fc86ae1c854fe2232",
  "owner": "codex-ar1734-tool-environment",
  "plan": "../plans/AR-1734-development-tui-tool-environment.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1734.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Provide the installed development TUI a minimal validated tool environment without inheriting ambient PATH or weakening stable launch.",
  "task_revision": 9,
  "title": "Propagate validated development tools to installed TUI",
  "updated_at": "2026-10-08T01:47:59+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1734-development-tui-tool-environment"
}
---

AR-1713 proved that development bundle installation and status succeed, while
bare launch, dynamic catalog, and live-provider routes fail before provider
dispatch because ASB clears the standalone frontend environment without
reconstructing the bounded tool environment required by its preflight.

Repair the ASB development broker boundary only. Preserve `env_clear`, reuse
the exact validated development tools and descriptor-bound rustup selection,
and pass a minimal environment that cannot be redirected by an ambient PATH or
post-validation pathname swap. Development warnings remain nonblocking; stable
and production policy remains fail closed and unchanged.


- 2026-10-08T01:36:35+00:00: Claimed by codex-ar1734-planning.

- 2026-10-08T01:36:43+00:00: Recorded command exit 0; command argv SHA-256
  a0a5101c89c1881d8ddb910a6fd38534f58d1c35f702171439b1c42e63920303.

- 2026-10-08T01:37:20+00:00: Published detailed P0 dependency for the bounded validated tool
  environment required by installed ASB-TUI launch; ready for an isolated ASB implementation worker
  after current TUI review/repair capacity permits.

- 2026-10-08T01:41:07+00:00: Claimed by codex-ar1734-tool-environment.

- 2026-10-08T01:41:15+00:00: Recorded command exit 0; command argv SHA-256
  5345cd4b5f66285dc80cddfe59c0a95475263f9ff88d25d2639fce3c300aa4b9.

- 2026-10-08T01:41:47+00:00: Recorded command exit 0; command argv SHA-256
  a5118f9a2a9d79ac48d8faac3ac684782a5c24e73c2d9f509e3b43c2c10db367.

- 2026-10-08T01:47:59+00:00: Recorded command exit 0; command argv SHA-256
  462f99fb6c13a94edf35bcd2beffd9d7ab45129bbf1e6a663c89769c174d0be5.
