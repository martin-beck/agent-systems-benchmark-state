---
{
  "branch": "feature/ar-1327-openrouter-adapter-parity",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-23T09:10:13+00:00",
  "depends_on": [
    "AR-0315",
    "AR-1325",
    "AR-1326"
  ],
  "id": "AR-1327",
  "next_action": "Push rebased parity head 03749b620003f6737cc33ff2dec576a91221d4ca, wait exact-head CI, independently review PR #251, then merge through handoffctl only after all required checks green; post-merge verify and release AR-1327.",
  "observed_branch": "feature/ar-1327-openrouter-adapter-parity",
  "observed_dirty": 0,
  "observed_head": "bdb3bf028f0ab96a7a00ffd186fbb20bfae073b2",
  "owner": "codex-asb-ar1327-20260923",
  "plan": "../plans/AR-1327.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Wire the OpenRouter endpoint and model through every compatible agent adapter projection and prove parity with hostile conformance evidence.",
  "task_revision": 37,
  "title": "OpenRouter adapter projections and parity conformance",
  "updated_at": "2026-09-23T07:20:36+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1327-openrouter-adapter-parity"
}
---

The provider-aware launch boundary exports a fixed provider/model projection and
a per-agent credential target; the built-in projections currently pin the public
OpenAI endpoint and `OPENAI_API_KEY`. This AR wires the AR-1325 OpenRouter
profile through the adapter projections for every compatible agent, resolves the
secret through `OPENROUTER_API_KEY`, and proves cross-agent parity under the
AR-0315 conformance harness. The aider and mini-SWE adapters already list
`openrouter.ai` in their known-egress sets; any remaining adapter egress
allowance must be extended explicitly, never silently.

- 2026-09-23T07:09:33+00:00: Dependency AR-1326 is merged and released; all seven post-merge
  workflows are green. Promote OpenRouter adapter parity as next dependency-ready AR.

- 2026-09-23T07:10:13+00:00: Claimed by codex-asb-ar1327-20260923.

- 2026-09-23T07:10:25+00:00: Recorded command exit 0; command argv SHA-256
  53c501452a74c3b7ca470a2f29d1f418ac76768339297ba429a62b1248181e3a.

- 2026-09-23T07:10:42+00:00: Recorded command exit 0; command argv SHA-256
  1aa2de6aeb772b69263e2566f5b31a29341b462e35b9b38e1e88fdc86796965c.

- 2026-09-23T07:11:12+00:00: Recorded command exit 0; command argv SHA-256
  0597fa110f9d6cf57b619485fdae2a50f4ba82193adc6be0da8d303021675365.

- 2026-09-23T07:11:27+00:00: Recorded command exit 0; command argv SHA-256
  bb783db1d0a7aad50565669282359a993e83a0716c66b4b30c7364826c96da5f.

- 2026-09-23T07:11:49+00:00: Recorded command exit 0; command argv SHA-256
  3feb350d0913053f03e03b18ae5515534349e45ff20f6edd01e0daf3b3a1dbbd.

- 2026-09-23T07:12:03+00:00: Recorded command exit 0; command argv SHA-256
  d6c85d10c88fc31f9da06b79d83043458809171a9de55ceb3ab7ac48a8c294ed.

- 2026-09-23T07:12:23+00:00: Recorded command exit 101; command argv SHA-256
  770dc16bbb0746021c36cd4bcd0ed614078b0979762078535f91a4107d0238d5.

- 2026-09-23T07:12:48+00:00: Recorded command exit 0; command argv SHA-256
  c8abb949288692ccba550b4ea34d6817631666655480e4db5c97459e0a84c15c.

- 2026-09-23T07:13:17+00:00: Recorded command exit 0; command argv SHA-256
  90914b391c7ca82d3090af91adbb5aad6ce0bc9102a2368fe14cbd42fb1ddf25.

- 2026-09-23T07:14:00+00:00: Recorded failure repair: an initial handoffctl cargo test invocation
  exited 101 because execution starts in the state checkout and no Cargo.toml was present. No
  product mutation occurred. Re-ran the identical focused gate with --manifest-path
  /srv/data/projects/agent-systems-benchmark-ar-1327/Cargo.toml; provider parity 12/12 passed and
  full asb-agents tests passed (188 passed, 1 ignored plus integration suites). Rebased PR #251 onto
  protected main 8692729, preserving only AR-1327 delta; signed+DCO head is
  03749b620003f6737cc33ff2dec576a91221d4ca.

- 2026-09-23T07:14:09+00:00: Recorded command exit 0; command argv SHA-256
  127012eddafb0b76f965d87a974ac5c4d10952a2e569b269fcaa0ae92f8700ef.

- 2026-09-23T07:15:25+00:00: Recorded command exit 0; command argv SHA-256
  ac1f0f01a2564cb8382a77afe3b697a7f1c485a8be45a79e5ecd6e0ed2d04ba5.

- 2026-09-23T07:16:09+00:00: Recorded command exit 0; command argv SHA-256
  a2f58f74d70a6c9ea01fbbe90819a908ae1a2e0b8fa77d16a30eeffa43bdacc2.

- 2026-09-23T07:16:52+00:00: Recorded command exit 0; command argv SHA-256
  5345cd4b5f66285dc80cddfe59c0a95475263f9ff88d25d2639fce3c300aa4b9.

- 2026-09-23T07:17:16+00:00: Recorded command exit 1; command argv SHA-256
  c7e7b852ff3523dcc25f4a7acec723225eeee38c9bafe49ae71a0681109e39dc.

- 2026-09-23T07:17:47+00:00: Recorded command exit 0; command argv SHA-256
  0f93b9db78678600300f6f3774eb54d2e11c2fd2b7eab4c94d8e554c25b1ef64.

- 2026-09-23T07:18:00+00:00: Recorded command exit 0; command argv SHA-256
  e66a7a74179052c70e4427a0541f9fc25245cf458538127c7fc5cbd2365adba8.

- 2026-09-23T07:18:18+00:00: Recorded command exit 0; command argv SHA-256
  dcd53e50ec587cc45f6fea35e87acaf8b4ddc1b2073f7379a0794340b90eea2e.

- 2026-09-23T07:18:35+00:00: Recorded command exit 0; command argv SHA-256
  d017a50d6d9806b240315c9041641af2ae29b3317137aa0b78b7b66636899f2a.

- 2026-09-23T07:19:02+00:00: Recorded command exit 101; command argv SHA-256
  e961587d7451bb9ddb38c69c021eabdfdb039f9933ba4b63e793211666dcebb3.

- 2026-09-23T07:19:21+00:00: Recorded command exit 0; command argv SHA-256
  3e2088e20fa2dac2a969d8b0fcd2b31c01203b1833928e167ea3b26bb3a2eab7.

- 2026-09-23T07:19:43+00:00: Recorded command exit 0; command argv SHA-256
  0f93b9db78678600300f6f3774eb54d2e11c2fd2b7eab4c94d8e554c25b1ef64.

- 2026-09-23T07:19:58+00:00: Recorded command exit 0; command argv SHA-256
  8d5eae452c434232ed77ac32e3f55b474f59a8b10122c0694309a5c5d7c1ba0f.

- 2026-09-23T07:20:15+00:00: Recorded command exit 0; command argv SHA-256
  e961587d7451bb9ddb38c69c021eabdfdb039f9933ba4b63e793211666dcebb3.

- 2026-09-23T07:20:36+00:00: Recorded command exit 0; command argv SHA-256
  2264a4905a63dfdf25983e0e69c004f051ea442acac8a4f9f85c207b984716e5.
