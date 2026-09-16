---
{
  "branch": "feature/ar-1254-mockagents-pinned-python-transport",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-16T15:55:14+00:00",
  "depends_on": [
    "AR-1252",
    "AR-1253"
  ],
  "id": "AR-1254",
  "next_action": "Implement real executable transport qualification before publication: invoke the pinned MockAgents artifact through run_isolated.py on amd64 and QEMU arm64; bind exact lock source/tag/commit/license/checksums and platform digests; add malformed/oversized body negatives, ordered tool-result/backpressure/cancellation terminal tests, descendant cleanup proof, actual outbound-denial probe inside network-none, and repeat-clean-state evidence.",
  "observed_branch": "feature/ar-1254-mockagents-pinned-python-transport",
  "observed_dirty": 0,
  "observed_head": "154a34549784bd3bba0a5fa47d046a237897980a",
  "owner": "asb_ar1254_mockagents_transport",
  "plan": "../plans/AR-1254.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Qualify MockAgents through the pinned Python sandbox.",
  "task_revision": 31,
  "title": "Qualify MockAgents through pinned Python transport",
  "updated_at": "2026-09-16T13:55:28+00:00",
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

- 2026-09-16T13:54:02+00:00: Signed+DCO commit 154a345 pushed. Added closed lock-based amd64/arm64
  artifact digest selection and rejected digest drift; arm64 archive runner network probe now passes
  with network=none-verified. Real fixture repeats loopback tool-result ordering, process-group
  cancellation/descendant cleanup and bounded body checks; executable mode invokes pinned MockAgents
  through run_isolated and returns pinned-version-verified. Full llm-double-spike suite 20/20,
  py_compile and diff checks pass. Host outbound remains labeled unavailable-outside-isolation; only
  runner network-none evidence is promoted.

- 2026-09-16T13:54:05+00:00: Heartbeat by asb_ar1254_mockagents_transport.

- 2026-09-16T13:55:14+00:00: Heartbeat by asb_ar1254_mockagents_transport.

- 2026-09-16T13:55:28+00:00: Independent review of signed exact head 154a345497 found prior gaps
  only partially addressed. It adds lock digest selection, repeat loopback, a runner call, and
  network-probe mode, but invoke_runner only asks run_isolated.py to execute /input/artifact
  --version and does not prove the real MockAgents transport/event scenarios; --executable is merely
  an is_file/executable-bit check and is not passed to the runner. The network probe checks
  /proc/net/route rather than attempting an outbound connection inside the isolated container; host
  outbound_attempt remains outside isolation. platform selection changes only lock key while
  run_isolated always uses amd64 Python image and no QEMU/arm64 execution is performed. HTTP handler
  accepts any body, does not parse/validate malformed input, and has no oversized/malformed negative
  tests. cancellation_cleanup checks only direct parent termination and never asserts descendant
  absence; no backpressure terminal-state test. Lock fields/source/license/checksums are not
  validated as a closed reviewed provenance contract. Current unit tests 3/3 pass but do not
  establish AR acceptance. Head is signed/DCO and diff-clean; no PR/merge authorized.
