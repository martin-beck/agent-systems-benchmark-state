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
  "task_revision": 32,
  "title": "Propagate validated development tools to installed TUI",
  "updated_at": "2026-10-08T02:05:15+00:00",
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

- 2026-10-08T01:48:54+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-08T01:49:37+00:00: Recorded command exit 0; command argv SHA-256
  82fba3ffee0a29793f76427ab377e730473bc6fd33811ecdc0a51de40f76cd27.

- 2026-10-08T01:50:06+00:00: Recorded command exit 101; command argv SHA-256
  e39d977690fe97611b2341f71e9f6d8866cdb42b6a991dffbdc54b5b85b9a8a8.

- 2026-10-08T01:50:58+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-08T01:51:20+00:00: Recorded command exit 101; command argv SHA-256
  e39d977690fe97611b2341f71e9f6d8866cdb42b6a991dffbdc54b5b85b9a8a8.

- 2026-10-08T01:51:46+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-08T01:52:08+00:00: Recorded command exit 101; command argv SHA-256
  e2d38c280b8d8c46b7371c37ae0d25e6d25a007cb8c10c2b14a9989c33fda35f.

- 2026-10-08T01:52:34+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-08T01:53:07+00:00: Recorded command exit 101; command argv SHA-256
  e2d38c280b8d8c46b7371c37ae0d25e6d25a007cb8c10c2b14a9989c33fda35f.

- 2026-10-08T01:53:58+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-08T01:54:31+00:00: Recorded command exit 0; command argv SHA-256
  e2d38c280b8d8c46b7371c37ae0d25e6d25a007cb8c10c2b14a9989c33fda35f.

- 2026-10-08T01:56:47+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-10-08T01:57:26+00:00: Recorded command exit 101; command argv SHA-256
  2ddd222d5ab3dbbc5824e8367ff0d1151a6168041a569b52fb97c11e3c8515c1.

- 2026-10-08T01:57:56+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-10-08T01:58:28+00:00: Recorded command exit 0; command argv SHA-256
  2cd6e91752974ac59b48671237ddf930cad2e53bff9f153193c794b07e985545.

- 2026-10-08T01:59:25+00:00: Recorded command exit 0; command argv SHA-256
  95395ce61f1b783b8ea272706ba78c152183c6b4f42018c61c38fbc22692c0de.

- 2026-10-08T02:00:33+00:00: Recorded command exit 0; command argv SHA-256
  f2e590bbecafd942675030c8632cddabd4d88498a2a3e9a4e48bbf81f69aa4e3.

- 2026-10-08T02:01:17+00:00: Recorded command exit 0; command argv SHA-256
  95395ce61f1b783b8ea272706ba78c152183c6b4f42018c61c38fbc22692c0de.

- 2026-10-08T02:02:26+00:00: Recorded command exit 4; command argv SHA-256
  61e0bf2f1bd07b014e0770582eefe6d8deddc8e7c0271a513c36cb69bab4e0b0.

- 2026-10-08T02:03:19+00:00: Recorded command exit 0; command argv SHA-256
  dddf947698aee5c7251b09fe1bcf75337f5d16145d0143887d81ecb361bc8e99.

- 2026-10-08T02:04:06+00:00: Recorded command exit 1; command argv SHA-256
  2e6d8ddc1232121b3bc5fc13375c90ef4475eca14d86d9cdfd6c2c45169d31c1.

- 2026-10-08T02:04:41+00:00: Recorded command exit 0; command argv SHA-256
  3003ffad7a32a97d8164c80a3cbe79b8fb35cc4d05e8368f355f953afd824ac8.

- 2026-10-08T02:05:15+00:00: Recorded command exit 0; command argv SHA-256
  58f415d37d50ac31f03d42027dc7b759e4b6c435d34c29c5cff23cdff32b44d4.
