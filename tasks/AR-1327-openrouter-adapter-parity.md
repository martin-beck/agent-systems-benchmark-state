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
  "next_action": "Translate the OpenRouter profile through every compatible agent adapter projection, point the credential target at OPENROUTER_API_KEY, verify egress allowances, and run hostile parity conformance with exact evidence.",
  "observed_branch": "feature/ar-1327-openrouter-adapter-parity",
  "observed_dirty": 4,
  "observed_head": "a4934fca0b528ac90d09fb537936584f5af0f75e",
  "owner": "codex-asb-ar1327-20260923",
  "plan": "../plans/AR-1327.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Wire the OpenRouter endpoint and model through every compatible agent adapter projection and prove parity with hostile conformance evidence.",
  "task_revision": 10,
  "title": "OpenRouter adapter projections and parity conformance",
  "updated_at": "2026-09-23T07:11:49+00:00",
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
