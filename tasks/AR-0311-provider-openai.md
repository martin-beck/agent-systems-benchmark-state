---
{
  "branch": "feature/provider-openai",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-08T12:57:57+00:00",
  "depends_on": [
    "AR-0301",
    "AR-0302",
    "AR-0303",
    "AR-0304",
    "AR-0305",
    "AR-0306",
    "AR-0307",
    "AR-0308",
    "AR-0309",
    "AR-0310"
  ],
  "id": "AR-0311",
  "next_action": "Hold exact 05262805acc538a31c8f12ed152a71026294706e unpublished for independent immutable review; live credentialed provider/account journeys remain opt-in and were not run.",
  "observed_branch": "feature/provider-openai",
  "observed_dirty": 0,
  "observed_head": "1128595cd2f93988374be008fcecda07fef9fde4",
  "owner": "contracts_20260906",
  "plan": "../plans/AR-0311.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Apply one default OpenAI provider profile consistently to all supported agents.",
  "task_revision": 27,
  "title": "Support a shared OpenAI provider",
  "updated_at": "2026-09-08T10:21:02+00:00",
  "worktree_key": "agent-systems-benchmark-provider-openai"
}
---
## AR-0311

Apply one default OpenAI provider profile consistently to all supported agents.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-08T09:53:22+00:00: Promote shared OpenAI provider after all adapter dependencies are done
  and AR-0312 Ollama provider is released.

- 2026-09-08T09:53:27+00:00: Claimed by contracts_20260906.

- 2026-09-08T09:55:23+00:00: Recorded command exit 0; command argv SHA-256
  7e88ebced015075b888df28562157975bde6d6e50ea68961a5514a936f9ae278.

- 2026-09-08T09:56:20+00:00: Recorded command exit 0; command argv SHA-256
  4db8c8d9db82832ab21db53ddafd0eddd0af792f22d23605cd9d86a534c33562.

- 2026-09-08T09:57:57+00:00: Heartbeat by contracts_20260906.

- 2026-09-08T10:00:46+00:00: Recorded command exit 2; command argv SHA-256
  842b16cbde21e5f60688efe941941cb128c1eb34b282911637385be2c02c8350.

- 2026-09-08T10:05:02+00:00: Recorded command exit 0; command argv SHA-256
  e4e7b5d30b14991038bf41709ddde33a67e9ff498799346f925ff9c51d600257.

- 2026-09-08T10:05:40+00:00: Material first implementation checkpoint on exact base e5cdf97: dirty
  only crates/asb-agents/src/lib.rs plus new openai.rs and OPENAI.md. Added dated gpt-5.2-2025-12-11
  public-service profile, secret-reference-only credential provenance, eight adapter translations,
  Codex Responses versus Chat Completions routing, Gemini fail-closed rejection, and
  profile/credential/drift negatives. Focused OpenAI tests pass 3/3 after fmt. Two earlier exits 2
  were patch transport misuse only (apply_patch requires one argument, not stdin); neither changed
  product files; corrected external patch artifact applied through wrapper.

- 2026-09-08T10:07:44+00:00: Recorded command exit 1; command argv SHA-256
  e5be3f8df3b34e0a1bdec0247c3f6975eaa9dcf1d7d886959424968ab7b29b74.

- 2026-09-08T10:08:11+00:00: Recorded command exit 101; command argv SHA-256
  43fba63adb3e942ff90705d90b7aac4462a9ee0154db239001af5915e5f40c3f.

- 2026-09-08T10:08:46+00:00: Recorded command exit 0; command argv SHA-256
  ba2d71263105869493967af12277d8770abbc2e6670e73f4f523b8912bcf06e1.

- 2026-09-08T10:10:26+00:00: Recorded command exit 0; command argv SHA-256
  378c08c3c40bf465250ac73672127e4b4a2864bbed49368e721b3669903f29fd.

- 2026-09-08T10:11:50+00:00: Recorded command exit 0; command argv SHA-256
  ec916e38bb1fb459f63ae04d5e9340e7a187e47a42bc1b23102fd9f420c9988b.

- 2026-09-08T10:12:57+00:00: Recorded command exit 0; command argv SHA-256
  57d5720f446b3e91b02a1874d41cbf8463e3f6a8f161e3f68156b8029c16b6d9.

- 2026-09-08T10:13:22+00:00: Recorded command exit 0; command argv SHA-256
  c46c0b6397f3e414393c037de8dbbe09e5cbdec8d68e6b0a3dd6a23afb073691.

- 2026-09-08T10:16:21+00:00: Candidate 05262805acc538a31c8f12ed152a71026294706e tree
  4be6a6f17df4943dde94cf82bde9473bc3959e55 parent e5cdf97dd2954e5d097b1a6c872beafd724aa12f is clean,
  SSH-signed, exact DCO, and limited to crates/asb-agents/{OPENAI.md,src/lib.rs,src/openai.rs}.
  Exact-tree affected fmt, 5 OpenAI tests, clippy, policy, Gitleaks, and diff-check pass; preceding
  full workspace test/clippy/docs/release/deny/audit gates pass, with coverage 92.93% workspace and
  93.94% lines for openai.rs. Earlier exit 101 was compiler E0631 from a method-reference signature
  mismatch and was fixed with a closure; exit-2 apply_patch invocations were wrapper-argument misuse
  and caused no product mutation. Evidence validates bounded synthetic effective-request translation
  and negatives; it does not claim a live credentialed account journey.

- 2026-09-08T10:18:21+00:00: Recorded command exit 0; command argv SHA-256
  d71815e2039aeaf0e0ddaca9ce75e813a3b48b5a3da7fb5cfdee3c85ed20f507.

- 2026-09-08T10:18:43+00:00: Recorded command exit 0; command argv SHA-256
  a8fca044a9d2e30a317204f79f0dcd6de8f1a1b009f03632046c74e0a14b3ab4.

- 2026-09-08T10:19:11+00:00: Recorded command exit 127; command argv SHA-256
  3583fa50823f43f214d8c45de49fb9eb09eacd4a85c0036db754d154a4dedf93.

- 2026-09-08T10:19:47+00:00: Recorded command exit 101; command argv SHA-256
  8fe17495495c624d12237d4b7d257ee40a9fa64cd5b111b058b87ba46c5f4ac7.

- 2026-09-08T10:20:42+00:00: Recorded command exit 0; command argv SHA-256
  786c9134dc0e913041d93edb2fe9e8ef2b07d6d52ab69146eab4643230282fbf.

- 2026-09-08T10:21:02+00:00: Recorded command exit 0; command argv SHA-256
  f71cee7e91a56bd681223087a7a7d92cb490ca0da98f7d61d6407c5aadc87f9c.
