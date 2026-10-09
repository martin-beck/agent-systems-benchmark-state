---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-09T07:34:23+00:00",
  "depends_on": [
    "AR-1719"
  ],
  "id": "AR-1752",
  "next_action": "Claim in an isolated ASB worktree; reproduce the exact installed asb tui dynamic-catalog failure, repair DevelopmentBackend negotiated-version forwarding, and qualify the public install-to-route journey.",
  "owner": "codex-ar1752-v115-projection-20261009",
  "plan": "../plans/AR-1752-development-broker-v115-projection.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1752.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Forward negotiated v1.15 provider-catalog projection through the read-only development broker so the installed public dynamic-catalog route works.",
  "task_revision": 8,
  "title": "Repair development broker v1.15 dynamic-catalog projection",
  "updated_at": "2026-10-09T03:42:25+00:00",
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
