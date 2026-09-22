---
{
  "branch": "feature/ar-1327-openrouter-adapter-parity",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-0315",
    "AR-1325",
    "AR-1326"
  ],
  "id": "AR-1327",
  "next_action": "Translate the OpenRouter profile through every compatible agent adapter projection, point the credential target at OPENROUTER_API_KEY, verify egress allowances, and run hostile parity conformance with exact evidence.",
  "owner": "",
  "plan": "../plans/AR-1327.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Wire the OpenRouter endpoint and model through every compatible agent adapter projection and prove parity with hostile conformance evidence.",
  "task_revision": 1,
  "title": "OpenRouter adapter projections and parity conformance",
  "updated_at": "2026-09-22T09:54:42+00:00",
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
