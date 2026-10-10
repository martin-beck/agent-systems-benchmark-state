---
{
  "branch": "feature/ar-1771-human-status-and-quiet-contract",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-10T12:55:32+00:00",
  "depends_on": [
    "AR-1768"
  ],
  "id": "AR-1771",
  "next_action": "AR-1763 is merged at protected main 5e08ddadff5a716bcce844ed8ed5e1bc1868d02f. Rebase preserved AR-1771 output-contract patch onto that exact head, reconcile catalog/shared config seams without touching AR-1764 project_run ownership, then complete contract gates.",
  "observed_branch": "feature/ar-1771-human-status-and-quiet-contract",
  "observed_dirty": 13,
  "observed_head": "5e08ddadff5a716bcce844ed8ed5e1bc1868d02f",
  "owner": "ar1771-output-contract-terra",
  "plan": "../plans/AR-1771-human-status-and-quiet-contract.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "contract-test",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1771.json",
    "spec_revision": 2,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1771.json",
  "spec_revision": 2,
  "status": "in_progress",
  "summary": "Define one routed human-output vocabulary, levels, writers, and quiet contract without changing JSON or exit behavior.",
  "task_revision": 86,
  "title": "Human output, status, and quiet contract",
  "updated_at": "2026-10-10T11:01:07+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1771-human-status-and-quiet-contract"
}
---

Define the public operational-output contract for every ASB command before
implementing progress rendering. Add a global `-q` / `--quiet` option accepted in
every option position and command family. In human mode it suppresses all ASB
status, update, progress, warning, success, and failure presentation; it does
not change the command's effects, exit status, or structured result. Interactive
input needed to complete an explicitly interactive command and the launched TUI
application itself are not silently disabled; quiet only suppresses ASB's
lifecycle wrapper messages around that application.

Define one configurable output router and require every ASB-owned user-visible
result, diagnostic, status, update, warning, and progress write to use it. The
generated project configuration must persist an `output` section with level
`normal` by default and the default writer routing of ordinary result output to
stdout and human operational/diagnostic output to stderr. The configuration and
the router must support explicit safe writer destinations without allowing a
human output route to accidentally corrupt the machine-result stream. Define
documented precedence between project configuration and command-line overrides;
the output router remains the sole path regardless of the selected destination.

Define closed output levels `quiet`, `normal`, `verbose`, and `debug`. `quiet`
is the level selected by `-q`; `normal` is the generated-project default;
`verbose` adds useful non-sensitive operational detail; and `debug` adds bounded
development diagnostics without credentials, raw provider bodies, prompts, or
private host paths. Level selection must never alter command effects, result
schemas, or exit codes.

Every non-quiet human operational line must start with a fixed-width state marker:
`[ OK ]`, `[ERR ]`, `[WARN]`, `[WAIT]`, or another closed, documented four-cell
state. Green represents success, red errors/failures, yellow warnings/partial
states, and a sensible neutral/in-progress style represents waiting. ANSI styling
is used only when the human stream is a supported terminal; redirected output is
plain text with the same marker and wording. Lines remain concise, one logical
operation per line, accessible without color, and never disclose authentication material,
private paths, prompts, or provider payloads.

`--json` is a silent machine-output mode. It emits no human status lines, updates,
or progress bars on stdout or stderr, regardless of terminal detection or
configured human writers; stdout retains the existing versioned JSON contract
exactly. `-q --json` is valid and equivalent for operational output. Preserve
existing exit meanings, raw protocol commands, interactive prompts, and TUI
terminal ownership.

- 2026-10-10T09:29:30+00:00: AR-1768 is done with exact-head review and hosted evidence; promote
  output contract in parallel with catalog work.

- 2026-10-10T09:30:15+00:00: Claimed by ar1771-output-contract-terra.

- 2026-10-10T09:30:41+00:00: Recorded command exit 0; command argv SHA-256
  ff6d1fa7a7185010f75fcfafe4bdc1bdd5b9804d8c2b3e7abdd8a1b96cd81c63.

- 2026-10-10T09:30:50+00:00: Recorded command exit 0; command argv SHA-256
  22e8959654c0611947b6779be4c91bd3912ef67d0baea66d067a0c7acde50b69.

- 2026-10-10T09:31:29+00:00: AR-1768 is done; implementation is active in the declared worktree.

- 2026-10-10T09:31:32+00:00: Heartbeat by ar1771-output-contract-terra.

- 2026-10-10T09:34:33+00:00: Coordinator identified AR-1763 ownership overlap; no conflicting schema
  commit will be made.

- 2026-10-10T09:34:37+00:00: Heartbeat by ar1771-output-contract-terra.

- 2026-10-10T09:35:53+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-10-10T09:36:10+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-10T09:36:25+00:00: Recorded command exit 0; command argv SHA-256
  a62eac268a262b916bd76f885d2f1bc42037e4f49a237048da7e300ae129419e.

- 2026-10-10T09:37:04+00:00: Recorded command exit 101; command argv SHA-256
  434ba6f96c6ffe18116f45c4c43ce6f988135f2d706c438789163f67f218fbe4.

- 2026-10-10T09:37:07+00:00: Recorded command exit 101; command argv SHA-256
  434ba6f96c6ffe18116f45c4c43ce6f988135f2d706c438789163f67f218fbe4.

- 2026-10-10T09:38:23+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-10T09:38:32+00:00: Recorded command exit 101; command argv SHA-256
  434ba6f96c6ffe18116f45c4c43ce6f988135f2d706c438789163f67f218fbe4.

- 2026-10-10T09:39:12+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-10-10T09:39:22+00:00: Recorded command exit 101; command argv SHA-256
  434ba6f96c6ffe18116f45c4c43ce6f988135f2d706c438789163f67f218fbe4.

- 2026-10-10T09:39:57+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-10-10T09:40:13+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-10T09:40:26+00:00: Recorded command exit 101; command argv SHA-256
  434ba6f96c6ffe18116f45c4c43ce6f988135f2d706c438789163f67f218fbe4.

- 2026-10-10T09:41:30+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-10T09:41:41+00:00: Recorded command exit 101; command argv SHA-256
  434ba6f96c6ffe18116f45c4c43ce6f988135f2d706c438789163f67f218fbe4.

- 2026-10-10T09:42:13+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-10T09:42:27+00:00: Recorded command exit 0; command argv SHA-256
  db4328e27c4e71453a524b2b46fd887ce3d74885daa5fff869f7708c8439aebf.

- 2026-10-10T09:42:41+00:00: Recorded command exit 101; command argv SHA-256
  f50c979e144ca5e48ea4a01b55f1849d728c878f109ddd4cf943ebc93ad5aa8e.

- 2026-10-10T09:43:06+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-10T09:43:15+00:00: Recorded command exit 0; command argv SHA-256
  434ba6f96c6ffe18116f45c4c43ce6f988135f2d706c438789163f67f218fbe4.

- 2026-10-10T09:43:50+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-10T09:44:03+00:00: Recorded command exit 101; command argv SHA-256
  a2b72999f264a1723535f52fad41e050b63be478df1e76d49a0a6afdefae3692.

- 2026-10-10T09:44:26+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-10-10T09:44:39+00:00: Recorded command exit 0; command argv SHA-256
  a2b72999f264a1723535f52fad41e050b63be478df1e76d49a0a6afdefae3692.

- 2026-10-10T09:44:48+00:00: Heartbeat by ar1771-output-contract-terra.

- 2026-10-10T09:45:11+00:00: Coordinator reported new AR-1763 overlap in CLI human presentation;
  focused AR-1771 tests are green, but integration must serialize.

- 2026-10-10T10:41:06+00:00: Heartbeat by ar1771-output-contract-terra.

- 2026-10-10T10:42:14+00:00: Recorded command exit 0; command argv SHA-256
  aa54729ab7f6458b3779170ee3a4e3160e8b545c7527f0a5418de3e4f44a9f8a.

- 2026-10-10T10:42:50+00:00: Heartbeat by ar1771-output-contract-terra.

- 2026-10-10T10:43:17+00:00: Recovered preserved patch after AR-1763 merge; serialization condition
  is resolved.

- 2026-10-10T10:44:07+00:00: Recorded command exit 0; command argv SHA-256
  ed516f6f0da731f7f0c8670680dc0151dbd38c6637e417bb47b211eb4c8699ca.

- 2026-10-10T10:44:40+00:00: Recorded command exit 0; command argv SHA-256
  b7c438686581cf292b6cd41497ceabb3af42dfed57e04dfd6cc89efed8e2d15b.

- 2026-10-10T10:45:02+00:00: Recorded command exit 0; command argv SHA-256
  6b0340b78e00b5e8d62e9973b7e72f6c6de22448e8636894d4001797a91460ec.

- 2026-10-10T10:45:43+00:00: Recorded command exit 0; command argv SHA-256
  31a05f46a65b4172cfcc5ef4e1ed2b4ddd54c042ac56eff6dc51f4205a4051b1.

- 2026-10-10T10:46:24+00:00: Recorded command exit 0; command argv SHA-256
  434ba6f96c6ffe18116f45c4c43ce6f988135f2d706c438789163f67f218fbe4.

- 2026-10-10T10:47:59+00:00: Recorded command exit 101; command argv SHA-256
  d32df0a8f7802e39b9a6743613fff16ac35e4dddba3905aa783a204f77a7e43f.

- 2026-10-10T10:48:58+00:00: Recorded command exit 1; command argv SHA-256
  b3f0e639efd1d94eb044d52fa97ed3d450ffd3c292b4130d91ea1147571986da.

- 2026-10-10T10:49:11+00:00: Recorded command exit 1; command argv SHA-256
  4cf65f85b7da6f74f7445aa03ad27b7586fb991692419f90f3c7967b1e1d545a.

- 2026-10-10T10:49:25+00:00: Recorded command exit 1; command argv SHA-256
  ed49abd8d0d0c83096d221b22a5b1d2f0e484e7fcf05fd41adeaf44bc6227844.

- 2026-10-10T10:49:36+00:00: Recorded command exit 0; command argv SHA-256
  80d2b922509f2ed6f9075ff951fda51ddc951a2c53de13886e8a410664224c82.

- 2026-10-10T10:49:52+00:00: Recorded command exit 101; command argv SHA-256
  d32df0a8f7802e39b9a6743613fff16ac35e4dddba3905aa783a204f77a7e43f.

- 2026-10-10T10:50:18+00:00: Recorded command exit 0; command argv SHA-256
  d32df0a8f7802e39b9a6743613fff16ac35e4dddba3905aa783a204f77a7e43f.

- 2026-10-10T10:50:39+00:00: Recorded command exit 101; command argv SHA-256
  22fc19d872be75a975891ff0abd53f1c305974a409b50c49c5df5d842d033e81.

- 2026-10-10T10:51:09+00:00: Recorded command exit 1; command argv SHA-256
  cf7f4cc1fb4d9d796f30af2c52f75e8a82e3cefa4830ad8fb285879a621001da.

- 2026-10-10T10:51:26+00:00: Recorded command exit 101; command argv SHA-256
  3d4cc54827fa0ae5c402321266e4a8e9a84a69a17f7ff27b7a0f0c858d454784.

- 2026-10-10T10:51:46+00:00: Recorded command exit 101; command argv SHA-256
  3d4cc54827fa0ae5c402321266e4a8e9a84a69a17f7ff27b7a0f0c858d454784.

- 2026-10-10T10:52:09+00:00: Recorded command exit 0; command argv SHA-256
  3d4cc54827fa0ae5c402321266e4a8e9a84a69a17f7ff27b7a0f0c858d454784.

- 2026-10-10T10:53:00+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-10T10:53:23+00:00: Recorded command exit 101; command argv SHA-256
  3a69ab8fb4986af8a09c7cfe1d37c5b47d21f6612c17d4a2c292cf56ed320fff.

- 2026-10-10T10:53:43+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-10-10T10:53:58+00:00: Recorded command exit 101; command argv SHA-256
  3a69ab8fb4986af8a09c7cfe1d37c5b47d21f6612c17d4a2c292cf56ed320fff.

- 2026-10-10T10:54:25+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-10-10T10:54:45+00:00: Recorded command exit 101; command argv SHA-256
  3a69ab8fb4986af8a09c7cfe1d37c5b47d21f6612c17d4a2c292cf56ed320fff.

- 2026-10-10T10:55:06+00:00: Recorded command exit 0; command argv SHA-256
  3a69ab8fb4986af8a09c7cfe1d37c5b47d21f6612c17d4a2c292cf56ed320fff.

- 2026-10-10T10:55:32+00:00: Heartbeat by ar1771-output-contract-terra.

- 2026-10-10T10:56:11+00:00: Recorded command exit 101; command argv SHA-256
  534f8613e1c316db8f0f46dd989e44e14a8ca74304a94791b4e4a1c59b2fbb1d.

- 2026-10-10T10:56:20+00:00: Recorded command exit 0; command argv SHA-256
  b36d15881eb65027724bc584f1b04db05666cd79896b100806e528307c04b65c.

- 2026-10-10T10:57:09+00:00: Recorded command exit 0; command argv SHA-256
  b49a90ee600c1023cee9ee9f9e8a4f9a06c53eef8c48d3932d88e482126c7c01.

- 2026-10-10T10:57:25+00:00: Recorded command exit 101; command argv SHA-256
  d880b562ab316782bc754e3e5d4bb3f7fc72d58c88e73c7de4f3f09bf1e9dbe4.

- 2026-10-10T10:57:42+00:00: Recorded command exit 0; command argv SHA-256
  3d4cc54827fa0ae5c402321266e4a8e9a84a69a17f7ff27b7a0f0c858d454784.

- 2026-10-10T10:58:22+00:00: Recorded command exit 0; command argv SHA-256
  3d4cc54827fa0ae5c402321266e4a8e9a84a69a17f7ff27b7a0f0c858d454784.

- 2026-10-10T10:58:34+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-10-10T10:59:02+00:00: Recorded command exit 101; command argv SHA-256
  534f8613e1c316db8f0f46dd989e44e14a8ca74304a94791b4e4a1c59b2fbb1d.

- 2026-10-10T10:59:19+00:00: Recorded command exit 0; command argv SHA-256
  bebe50790cfd409aeecd081e27469feeff22ba0c42d18f547f896c530479f8b6.

- 2026-10-10T10:59:46+00:00: Recorded command exit 101; command argv SHA-256
  534f8613e1c316db8f0f46dd989e44e14a8ca74304a94791b4e4a1c59b2fbb1d.

- 2026-10-10T11:00:32+00:00: Recorded command exit 101; command argv SHA-256
  dc3864fced58547ee9a95596c9bf3e6ba705c4ee879ebbf0dd2b4df3d35ab8bf.

- 2026-10-10T11:00:49+00:00: Recorded command exit 101; command argv SHA-256
  dc3864fced58547ee9a95596c9bf3e6ba705c4ee879ebbf0dd2b4df3d35ab8bf.

- 2026-10-10T11:01:07+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.
