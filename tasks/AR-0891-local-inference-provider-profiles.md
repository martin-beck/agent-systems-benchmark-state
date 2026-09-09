---
{
  "branch": "feat/local-inference-provider-profiles",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-0879",
    "AR-0312",
    "AR-0313",
    "AR-0315"
  ],
  "id": "AR-0891",
  "next_action": "Qualify grouped Ollama, llama.cpp, vLLM, and LocalAI profiles with exact engine, model, hardware, protocol, isolation, and reproducibility evidence.",
  "owner": "",
  "plan": "../plans/AR-0891.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "open",
  "summary": "Extend ASB local inference through evidence-backed profiles rather than one speculative adapter task per server.",
  "task_revision": 2,
  "title": "Qualify local inference provider profiles",
  "updated_at": "2026-09-09T08:33:38+00:00",
  "worktree_key": "agent-systems-benchmark-local-inference-provider-profiles"
}
---
## AR-0891

Use exact Ollama, llama.cpp, vLLM and LocalAI sources in `docs/LOCAL_LLM_TESTING_RECOMMENDATIONS.md`; qualify only profiles filling an ASB need.

- 2026-09-09T08:33:38+00:00: Dependencies AR-0879, AR-0312, AR-0313, and AR-0315 are released done;
  promote grouped local inference provider profiles. AR-0890 remains unclaimable until AR-0888
  selects a qualifying executable candidate.
