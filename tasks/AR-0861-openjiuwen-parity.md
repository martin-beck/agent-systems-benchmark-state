---
{
  "branch": "feature/openjiuwen-parity",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-0860"
  ],
  "id": "AR-0861",
  "next_action": "Extend exact provider parity and the platform support matrix only for executable-qualified OpenJiuwen combinations under a serialized shared-path fence.",
  "observed_branch": "feature/openjiuwen-parity",
  "observed_dirty": 0,
  "observed_head": "3e8d58994eb2b3faeda9449e4186498cf86eeb86",
  "owner": "",
  "plan": "../plans/AR-0861.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "blocked",
  "summary": "Add OpenJiuwen provider parity and support matrix evidence.",
  "task_revision": 8,
  "title": "Add OpenJiuwen provider parity and support matrix evidence",
  "updated_at": "2026-09-16T12:20:51+00:00",
  "worktree_key": "agent-systems-benchmark-openjiuwen-parity"
}
---
## AR-0861

Extend exact provider parity and the platform support matrix only for executable-qualified OpenJiuwen combinations under a serialized shared-path fence.

This phase cannot claim support from mocks, parser fixtures, source inspection, compilation, or mutable artifacts. If its executable evidence is unavailable, leave this child blocked with exact provenance evidence while the sibling agent series proceeds.

- 2026-09-16T12:18:40+00:00: Dependency AR-0860 is complete; promote OpenJiuwen parity/support
  matrix child for implementation.

- 2026-09-16T12:18:43+00:00: Claimed by asb_ar1024_lifecycle_router.

- 2026-09-16T12:20:04+00:00: Heartbeat by asb_ar1024_lifecycle_router.

- 2026-09-16T12:20:19+00:00: Recorded command exit 0; command argv SHA-256
  694058a07c30311c499b513da6eda6f4b0f17629a2e608d034924311c76b17eb.

- 2026-09-16T12:20:30+00:00: Recorded command exit 101; command argv SHA-256
  ab97a5f6db73481cf378a483b8cea89dfc61e7580766ace7bd856205c056cdf4.

- 2026-09-16T12:20:51+00:00: Focused provider_parity passed 5/5 (OpenAI/Ollama profile parity,
  atomic unsupported route, replay/live exact binding, corrupt cassette/no-fallback). Required
  executable-qualified OpenJiuwen gate was run with cargo test -p asb-agents --test real_openjiuwen
  --locked --offline -- --ignored and failed 8/8 before execution: pinned wheel test panicked at
  real_openjiuwen.rs:406 missing ASB_OPENJIUWEN_WHEEL; seven live tests failed at line 345 because
  ASB_OPENJIUWEN_LOOPBACK_ONLY was absent (Err(NotPresent), expected Ok("1")). No pinned
  executable/wheel/interpreter, immutable runtime closure, or loopback-only namespace evidence is
  available. Plan forbids claiming support from mocks, parser fixtures, compilation, or replay;
  preserve clean origin/main head 3e8d589 and resume only with exact immutable artifacts plus
  serialized shared-path live evidence.
