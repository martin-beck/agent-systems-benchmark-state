---
{
  "branch": "feature/ar-1338-guided-asb-command-wrapper",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-25T18:17:09+00:00",
  "depends_on": [
    "AR-1331",
    "AR-1442",
    "AR-1443",
    "AR-1446"
  ],
  "id": "AR-1338",
  "next_action": "PR #327 updated at exact head 76524a7 after focused/full CLI gates and independent review. Hosted exact-head checks and review remain pending. Guided setup now enforces catalog provider/model pairs and absolute non-traversal paths; plain CLI replay remains fail-closed until a runtime-owned authority acquisition successor is delivered. Do not merge until CI/review are green.",
  "observed_branch": "feature/ar-1338-guided-asb-command-wrapper",
  "observed_dirty": 0,
  "observed_head": "76524a7e081946391143b5225412f428bf73a5fc",
  "owner": "coordinator-ar1338",
  "plan": "../plans/AR-1338.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Add a catalog-driven friendly wrapper for setup, selection and benchmark workflows.",
  "task_revision": 50,
  "title": "Guided ASB command wrapper",
  "updated_at": "2026-09-25T16:40:10+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1338-guided-asb-command-wrapper"
}
---

Add a friendly `asb easy` command or equivalent in-tree wrapper that guides a
user through supported setup, provider/model selection, multi-agent plans and
benchmark/report workflows. It must derive all digests and generated files from
the authoritative ASB catalog and config contracts, preserve secret isolation,
and delegate execution to the normal ASB commands. It must not become a second
provider registry or bypass the runtime's fail-closed validation.

## Current development and CI qualification boundary

The mandatory development and CI qualification path for this AR is a deterministic
local provider/LLM mock (LiteLLM-compatible where practical), including hostile
negative tests and offline replay where applicable. External/live OpenRouter or
other provider reachability is optional supplementary evidence only; it is never a
completion, dependency-readiness, or CI gate. Production egress policy, credential
non-disclosure, runtime-owned authority, namespace/relay attestation, cancellation
and teardown, and fail-closed denial of unapproved external traffic remain required
contracts. Existing live-provider dependency edges describe production integration
ordering only and must not be used to block local qualification or to claim external
reachability.

- 2026-09-25T15:45:17+00:00: ASB-only wrapper dependencies AR-1442, AR-1443, and AR-1446 are done.
  Optional live capture and asb-tui remain separate; promote full catalog-driven wrapper
  implementation.

- 2026-09-25T15:45:20+00:00: Claimed by coordinator-ar1338.

- 2026-09-25T15:45:44+00:00: Recorded command exit 0; command argv SHA-256
  62cc414e2aff2ff6a6ecedac52ecb1c1bf9777c8f4628e29597d8cf0016bb0e2.

- 2026-09-25T15:53:33+00:00: Audit of protected merge 2872a31f: existing bounded easy
  run/sweep/record-campaign path is present and full CLI/customer gates are green, but the complete
  wrapper acceptance is not met because normal CLI replay still requires runtime-issued
  ReplayLaunchAuthority. AR-1448 now owns the missing runtime/control authority source; no wrapper
  mutation or authority weakening made.

- 2026-09-25T16:17:09+00:00: Claimed by coordinator-ar1338.

- 2026-09-25T16:17:23+00:00: Recorded command exit 0; command argv SHA-256
  ed516f6f0da731f7f0c8670680dc0151dbd38c6637e417bb47b211eb4c8699ca.

- 2026-09-25T16:17:40+00:00: Recorded command exit 0; command argv SHA-256
  91c481d4f1a058d3265e9102b0531d1eefe09cb45e5c1807ecda5e8c8b6b67d5.

- 2026-09-25T16:19:04+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-25T16:19:54+00:00: Recorded command exit 0; command argv SHA-256
  043e0e6a9bba4d73f28ba31a6981e405e5f5b0da9c785bd75eb12763d934cc10.

- 2026-09-25T16:22:33+00:00: Recorded command exit 0; command argv SHA-256
  043e0e6a9bba4d73f28ba31a6981e405e5f5b0da9c785bd75eb12763d934cc10.

- 2026-09-25T16:23:04+00:00: Recorded command exit 101; command argv SHA-256
  008f3a8824b64ae468ae900d7bbac2a871a8d29892d84aba5b02a0cc1c0aedff.

- 2026-09-25T16:23:41+00:00: Recorded command exit 0; command argv SHA-256
  62ca4bfbbe17bf0de52acb89c73dd6e5a583b98bbb557b81669134c23fa00448.

- 2026-09-25T16:24:06+00:00: Recorded command exit 0; command argv SHA-256
  008f3a8824b64ae468ae900d7bbac2a871a8d29892d84aba5b02a0cc1c0aedff.

- 2026-09-25T16:24:30+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-25T16:25:11+00:00: Recorded command exit 0; command argv SHA-256
  1024fc1e6cefa31b078f0b5d2ed85c7ea4586897b388bf1e308f62db58574461.

- 2026-09-25T16:25:46+00:00: Recorded command exit 0; command argv SHA-256
  3d4b9cb65499215dee0b8a0fbc639dc04e4742feb81d5d8a8a75457f378e698a.

- 2026-09-25T16:26:01+00:00: Recorded command exit 0; command argv SHA-256
  c5a6adb98fee17e9dcbed784e785ee2fec922af16dd8ce5a51b6601459c2ff7f.

- 2026-09-25T16:26:19+00:00: Recorded command exit 0; command argv SHA-256
  486041c3ec0b604a209ad09e256ea791b8661a595ff1e1847631491ee6f946dc.

- 2026-09-25T16:26:43+00:00: Recorded command exit 0; command argv SHA-256
  04e4b7c0db0cbe9be2bec51a6a8ca205c906d59c43b326859833312e9a124028.

- 2026-09-25T16:27:05+00:00: Recorded command exit 0; command argv SHA-256
  fcaf31bb45a6c34ff662160c77874c1e9d525a90a214781d91eafee104db140a.

- 2026-09-25T16:28:07+00:00: Recorded command exit 8; command argv SHA-256
  b2524a2bfd053eeff28aa529f064980f98ccaa0deb56a6d3e19bf174d24173cd.

- 2026-09-25T16:29:09+00:00: Recorded command exit 8; command argv SHA-256
  b2524a2bfd053eeff28aa529f064980f98ccaa0deb56a6d3e19bf174d24173cd.

- 2026-09-25T16:29:58+00:00: Recorded command exit 8; command argv SHA-256
  b2524a2bfd053eeff28aa529f064980f98ccaa0deb56a6d3e19bf174d24173cd.

- 2026-09-25T16:31:34+00:00: Recorded command exit 0; command argv SHA-256
  91c31a03f8990d8bb18b7b0422ccda9d38e51731cace8bb643b4444b35d76f13.

- 2026-09-25T16:31:49+00:00: Recorded command exit 0; command argv SHA-256
  91c31a03f8990d8bb18b7b0422ccda9d38e51731cace8bb643b4444b35d76f13.

- 2026-09-25T16:32:32+00:00: Recorded command exit 0; command argv SHA-256
  81c792d36a65dc0b2ca3a5171548872eb32ce2771368f5d72773d690104abf25.

- 2026-09-25T16:33:54+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-25T16:34:17+00:00: Recorded command exit 101; command argv SHA-256
  043e0e6a9bba4d73f28ba31a6981e405e5f5b0da9c785bd75eb12763d934cc10.

- 2026-09-25T16:34:43+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-25T16:35:02+00:00: Recorded command exit 0; command argv SHA-256
  043e0e6a9bba4d73f28ba31a6981e405e5f5b0da9c785bd75eb12763d934cc10.

- 2026-09-25T16:35:29+00:00: Recorded command exit 0; command argv SHA-256
  7552d1a65dcfdd4111fbc25267fda3a9e73566a0aca4c2597dfc536441bf70d4.

- 2026-09-25T16:36:01+00:00: Recorded command exit 0; command argv SHA-256
  008f3a8824b64ae468ae900d7bbac2a871a8d29892d84aba5b02a0cc1c0aedff.

- 2026-09-25T16:36:21+00:00: Recorded command exit 0; command argv SHA-256
  1024fc1e6cefa31b078f0b5d2ed85c7ea4586897b388bf1e308f62db58574461.

- 2026-09-25T16:36:45+00:00: Recorded command exit 0; command argv SHA-256
  3d4b9cb65499215dee0b8a0fbc639dc04e4742feb81d5d8a8a75457f378e698a.

- 2026-09-25T16:37:01+00:00: Recorded command exit 0; command argv SHA-256
  fd6ba813de27c527d63e3a4bba8aca5722cf6473f8ad5555f5dcc72fced251d3.

- 2026-09-25T16:37:17+00:00: Recorded command exit 0; command argv SHA-256
  486041c3ec0b604a209ad09e256ea791b8661a595ff1e1847631491ee6f946dc.

- 2026-09-25T16:37:42+00:00: Recorded implementation and review follow-up evidence.

- 2026-09-25T16:37:52+00:00: Recorded command exit 0; command argv SHA-256
  a4b4c039d5b97fca478387464285223fbc6f00bfd60131ff60ae3465577d0082.

- 2026-09-25T16:39:03+00:00: Recorded command exit 8; command argv SHA-256
  b2524a2bfd053eeff28aa529f064980f98ccaa0deb56a6d3e19bf174d24173cd.

- 2026-09-25T16:40:10+00:00: Recorded command exit 8; command argv SHA-256
  b2524a2bfd053eeff28aa529f064980f98ccaa0deb56a6d3e19bf174d24173cd.
