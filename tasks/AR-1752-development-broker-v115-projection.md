---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-09T07:34:23+00:00",
  "depends_on": [
    "AR-1719"
  ],
  "id": "AR-1752",
  "next_action": "Commit the focused negotiated-version repair, build exact ASB/TUI candidates, and run the installed public install/status/bare/dynamic-catalog journey before PR publication.",
  "owner": "codex-ar1752-v115-projection-20261009",
  "plan": "../plans/AR-1752-development-broker-v115-projection.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1752.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Forward negotiated v1.15 provider-catalog projection through the read-only development broker so the installed public dynamic-catalog route works.",
  "task_revision": 23,
  "title": "Repair development broker v1.15 dynamic-catalog projection",
  "updated_at": "2026-10-09T03:59:03+00:00",
  "worktree_key": ""
}
---

AR-1721's implementation and paired asb-tui route are merged, but fresh
exact-head qualification found a product failure at the public installed
boundary. With ASB `69bf9029a4976f14739cf4c25949428ff2fe0bb7` and asb-tui
`60ab530dd1a09d6617514f9974217c9f08d48876`, `asb tui install`, `status`, and
bare `asb tui` succeed, while `asb tui dynamic-catalog` exits 4 with
`development_launch_failed`. The sanitized frontend diagnosis is
`dynamic_catalog_response_missing; network=unknown`.

The defect is in ASB, not the standalone TUI renderer. `RunnerBackend`
implements negotiated `execute_versioned` and projects a v1.15
`ProviderCatalog` result into `DynamicProviderCatalog`. The read-only
`DevelopmentBackend` delegates admitted calls through `inner.execute`, so the
negotiated wire version is discarded and a legacy catalog reaches a v1.15
frontend. Unit tests cover legacy direct execution and the full runner backend,
but not negotiated v1.15 execution through `DevelopmentBackend` or the public
installed route.

This repair is limited to version-preserving delegation through the ASB-owned
development broker and its tests/evidence. It must not add renderer, Ratatui,
terminal UI, navigation, or application-state code to ASB; all actual TUI work
remains in `asb-tui`. It must also preserve the development backend's read-only
authority boundary: configuration/auth/provider-profile/run/recording mutations
remain unavailable. Development authentication, signatures, and key management
remain explicit warning-only concerns and must not block this development path.
Explicit live/dynamic requests must still reject protocol, identity, stale,
unavailable, static, malformed, and transport failures without silent fallback.

Reproduction evidence is retained under the active AR-1721 qualification root
until this repair produces a reviewed current-main receipt. The eventual public
journey evidence must contain no credential value or raw provider payload.

- 2026-10-09T03:34:23+00:00: Claimed by codex-ar1752-v115-projection-20261009.

- 2026-10-09T03:35:16+00:00: Recorded command exit 0; command argv SHA-256
  0cfdba1bb7f3b56220c6a197e7721e065a7fa52691a568c597b93c32f8f0c83a.

- 2026-10-09T03:36:28+00:00: Recorded command exit 0; command argv SHA-256
  684caf244e8f06052e6279288bfeb8b91fa67be69ce9bc2eef2dd21d397e3501.

- 2026-10-09T03:38:13+00:00: Recorded command exit 0; command argv SHA-256
  be68d16a2ee75ab35884e181b700fbcb6039581940a01e4954a2e9ba57804a2d.

- 2026-10-09T03:40:22+00:00: Recorded command exit 1; command argv SHA-256
  aa60bc93fd5dfeeed3a45daadfe94e57e1b78fd30d9234e794433a70b3f81426.

- 2026-10-09T03:41:47+00:00: Recorded command exit 1; command argv SHA-256
  ddca6561d886a251eb25d0883a59e5f6defdae8ae0110126c5f94fe2b6d4f58e.

- 2026-10-09T03:42:25+00:00: Recorded command exit 1; command argv SHA-256
  2c1938a84a2949baba05c6783500c2f4de523aa77e45acd7d215c505c3d801b7.

- 2026-10-09T03:43:03+00:00: Recorded command exit 0; command argv SHA-256
  a73acaab8e40150e8f56d9145a3c4bd1fdfd280dad3744a25b8e4c011ac62007.

- 2026-10-09T03:43:35+00:00: Recorded command exit 0; command argv SHA-256
  0cfdba1bb7f3b56220c6a197e7721e065a7fa52691a568c597b93c32f8f0c83a.

- 2026-10-09T03:44:08+00:00: Recorded command exit 0; command argv SHA-256
  d0e01221a1e079c3b8f287f2dcc5fc9fce4c98fb697a8d2eb8af9a092014922a.

- 2026-10-09T03:44:53+00:00: Recorded command exit 0; command argv SHA-256
  5c3c74a1afb639150696d759e0f40c6ec72fc61c42d2a0b36c2ccb89a9855ea3.

- 2026-10-09T03:46:03+00:00: Recorded command exit 0; command argv SHA-256
  d19f226b1462ca3d6cc1e65e276f36477ee3fcb688518442b3ffae78efa568be.

- 2026-10-09T03:46:35+00:00: Recorded command exit 0; command argv SHA-256
  a8fe67aeaf03de63cc8dfb92067526a23fe853411844e1234d1498c149b4f01b.

- 2026-10-09T03:47:28+00:00: Recorded command exit 0; command argv SHA-256
  cdb31d861fb6aa7d6ed552f87aa919955646de4c1ae849a5b6af14856aa6f4f3.

- 2026-10-09T03:48:00+00:00: Recorded command exit 0; command argv SHA-256
  6542b09c224bbf128edd447bd4b51d5a4d0b39b96f8e64504cdc0244f1acec82.

- 2026-10-09T03:49:39+00:00: Recorded command exit 0; command argv SHA-256
  ce8a18b2194b786ad65cb4827a84b7154a8f731824bbd79e65642819aac0f075.

- 2026-10-09T03:50:17+00:00: Recorded command exit 0; command argv SHA-256
  a8fe67aeaf03de63cc8dfb92067526a23fe853411844e1234d1498c149b4f01b.

- 2026-10-09T03:50:52+00:00: Recorded command exit 0; command argv SHA-256
  cdb31d861fb6aa7d6ed552f87aa919955646de4c1ae849a5b6af14856aa6f4f3.

- 2026-10-09T03:51:27+00:00: Recorded command exit 0; command argv SHA-256
  6542b09c224bbf128edd447bd4b51d5a4d0b39b96f8e64504cdc0244f1acec82.

- 2026-10-09T03:52:14+00:00: Recorded command exit 0; command argv SHA-256
  4b48240ee0b5569ca7fab8614a2a30382d7805827e33fff38cc0cae0bcf27f23.

- 2026-10-09T03:58:56+00:00: Active isolated product worktree is agent-systems-benchmark-ar-1752 on
  branch repair/ar-1752-development-broker-v115-projection, synchronized to base
  f3840f351c9da1657ad44af594cf2b6ae8b419c9. Exact pre-repair installed ASB 69bf9029/TUI 60ab530d
  reproduction exits 4 with development_launch_failed and dynamic_catalog_response_missing; focused
  fmt, v1.14/v1.15 backend and private-socket tests, authority negatives, and focused Clippy pass.

- 2026-10-09T03:59:03+00:00: Recorded command exit 0; command argv SHA-256
  5505d6d58ed10296cbf385a0e04bd5e3da16b777251daad25d2e0270f3dc56f3.
