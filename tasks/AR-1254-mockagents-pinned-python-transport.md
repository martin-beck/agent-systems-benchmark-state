---
{
  "branch": "feature/ar-1254-mockagents-pinned-python-transport",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-16T15:50:56+00:00",
  "depends_on": [
    "AR-1252",
    "AR-1253"
  ],
  "id": "AR-1254",
  "next_action": "Add arm64 artifact selection/provenance and runner-proven network-none denial; request independent review after full gates.",
  "observed_branch": "feature/ar-1254-mockagents-pinned-python-transport",
  "observed_dirty": 2,
  "observed_head": "ce5452c2104d6101f5bdfb35bb4d817e48a713cd",
  "owner": "asb_ar1254_mockagents_transport",
  "plan": "../plans/AR-1254.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Qualify MockAgents through the pinned Python sandbox.",
  "task_revision": 26,
  "title": "Qualify MockAgents through pinned Python transport",
  "updated_at": "2026-09-16T13:53:36+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1254"
}
---

Implement only the linked AR-1254 plan using ASB development documentation and handoffctl.
Keep fixtures, runtimes, caches, and evidence under `/srv/data/projects`.

- 2026-09-16T13:44:21+00:00: AR-1252 and AR-1253 completed with immutable runner/runtime evidence;
  promote corrected MockAgents transport successor.

- 2026-09-16T13:44:29+00:00: Claimed by asb_ar1254_mockagents_transport.

- 2026-09-16T13:44:37+00:00: Recorded command exit 0; command argv SHA-256
  009884615fa8662c9070d8ce2e9b138e54961ba8bda6bec5fb2208ed2d342059.

- 2026-09-16T13:46:14+00:00: Recorded command exit 0; command argv SHA-256
  f5a3ba9d11814bbbe44f849c4f7a2378093bf0786167c2243b194ffb2b797278.

- 2026-09-16T13:46:34+00:00: Recorded command exit 0; command argv SHA-256
  38f975f54c027fa02bb9f8ae9b9b33491472c6c87674b438df1840ed7ebc2724.

- 2026-09-16T13:47:06+00:00: Recorded command exit 0; command argv SHA-256
  f2931e03b4545fe2406f19d24954795339f90a1317c7f1a62160f0a3fb5cd28f.

- 2026-09-16T13:47:31+00:00: Signed+DCO commit 8b07428 pushed. Added bounded transport_fixture.py
  with real authenticated loopback HTTP event ordering, bounded response body, cancellation and
  process cleanup, plus explicit non-loopback connection attempt classified unavailable outside
  isolation. Positive/negative tests pass; full llm-double-spike suite 19/19 and py_compile/diff
  checks pass. This is a transport fixture foundation; actual MockAgents executable invocation and
  runner-proven outbound denial remain required before completion.

- 2026-09-16T13:47:33+00:00: Heartbeat by asb_ar1254_mockagents_transport.

- 2026-09-16T13:48:23+00:00: Heartbeat by asb_ar1254_mockagents_transport.

- 2026-09-16T13:48:35+00:00: Independent review of exact signed head 8b074286 found publication
  blockers against complete AR-1254 acceptance. transport_fixture.py only serves a synthetic
  loopback HTTP response and never invokes the real pinned MockAgents executable or run_isolated.py;
  README explicitly says network denial remains unpromoted. Outbound probe merely catches
  OSError/timeout and labels unavailable-outside-isolation, so it is not actual network-none denial
  evidence. Request body length is checked but body read/JSON/malformed input contract is not
  validated. cancellation_cleanup terminates one direct Python child; no descendant process-tree
  cleanup or bounded backpressure/cancellation terminal-state evidence. No repeat-clean-state,
  amd64/arm64 artifact selection/digest provenance, pinned runtime/runner invocation, or malformed
  input negatives. Existing tests cover only synthetic ordering/cleanup and non-executable README
  rejection. Commit 8b074286 is SSH-signed/DCO and diff-clean, but head is not review-ready; no
  PR/merge authorized.

- 2026-09-16T13:49:40+00:00: Recorded command exit 0; command argv SHA-256
  124618df5c7d6d69866a1e2bdd93941abdab91e1f4701499547dba8bf0372494.

- 2026-09-16T13:50:02+00:00: Recorded command exit 0; command argv SHA-256
  1deadcda507b9205b77f7e96f074c3d0637c16dac9226b64769c51d3989bc634.

- 2026-09-16T13:50:26+00:00: Recorded command exit 0; command argv SHA-256
  6b7b34d3706b12235bfb3cf3735c327b3fd33382dce3f672e2d95e3f09aa7f34.

- 2026-09-16T13:50:53+00:00: Signed+DCO commit ce5452c pushed. Transport fixture now invokes the
  approved run_isolated.py with Python digest and pinned MockAgents executable artifact; live
  invocation returned mockagents_runner=pinned-version-verified. Real loopback tool-result ordering,
  repeated clean-state, process-group cancellation/cleanup and bounded body checks pass. Full
  llm-double-spike suite 19/19, transport focused 2/2, py_compile/diff checks pass. Non-loopback
  attempt remains explicitly unavailable-outside-isolation until network-none runner evidence; arm64
  artifact selection/provenance remains.

- 2026-09-16T13:50:56+00:00: Heartbeat by asb_ar1254_mockagents_transport.

- 2026-09-16T13:52:24+00:00: Recorded command exit 0; command argv SHA-256
  38f975f54c027fa02bb9f8ae9b9b33491472c6c87674b438df1840ed7ebc2724.

- 2026-09-16T13:52:44+00:00: Recorded command exit 1; command argv SHA-256
  fceed76d6da8d335aab663462782d1ae5b648123eeb47126bc732feda35ff2e1.

- 2026-09-16T13:53:14+00:00: Recorded command exit 0; command argv SHA-256
  fceed76d6da8d335aab663462782d1ae5b648123eeb47126bc732feda35ff2e1.

- 2026-09-16T13:53:36+00:00: Recorded command exit 0; command argv SHA-256
  95204edb19267a70de0891d5f1bfdfda7e1009ecf544aa1e6f91661f054c22fe.
