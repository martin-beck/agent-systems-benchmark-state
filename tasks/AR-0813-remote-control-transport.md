---
{
  "branch": "feature/remote-control-transport",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-16T17:33:30+00:00",
  "depends_on": [
    "AR-0702",
    "AR-0803",
    "AR-0902"
  ],
  "id": "AR-0813",
  "next_action": "Create/promote successor for unsigned merge 14b604f; perform signed protected-main recovery and rerun exact-main policy before closing AR-0813.",
  "observed_branch": "feature/remote-control-transport",
  "observed_dirty": 0,
  "observed_head": "b7d9e142d684f1fa65fc3f52258ec46585194950",
  "owner": "asb_ar0813_remote_transport",
  "plan": "../plans/AR-0813.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Carry the versioned frontend control API securely over IP without coupling runner lifetime to a client.",
  "task_revision": 304,
  "title": "Add secure remote control transport",
  "updated_at": "2026-09-16T16:39:25+00:00",
  "worktree_key": "agent-systems-benchmark-remote-control-transport"
}
---
## AR-0813

Carry the versioned frontend control API securely over IP without coupling runner lifetime to a client.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-16T14:19:58+00:00: Dependencies AR-0702, AR-0803, and AR-0902 verified done; ASB-only
  remote transport leaf selected while QEMU chain remains blocked

- 2026-09-16T14:20:05+00:00: Claimed by asb_ar0813_remote_transport.

- 2026-09-16T14:20:34+00:00: Recorded command exit 0; command argv SHA-256
  450f7c154cd6c48726152ea81a82117c8f7ab840823b9d3699d91f915747d4b0.

- 2026-09-16T14:21:48+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-16T14:22:04+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T14:22:25+00:00: Recorded command exit 0; command argv SHA-256
  c25185aaf43c2a6c702eb5ed3e8a31aa41c5dd426e6cf6af1736fd079c20789d.

- 2026-09-16T14:22:44+00:00: Recorded command exit 0; command argv SHA-256
  b23792049ef6ce9be3dba57dbc4a89804d43787d301617ade8c389b715772fbb.

- 2026-09-16T14:22:52+00:00: Recorded command exit 0; command argv SHA-256
  c9963146310c80dcd631ad130cd43d1f0bdbefd6e8fac3073feb5f3106799c26.

- 2026-09-16T14:23:18+00:00: Committed cc9d4b3 (SSH-signed+DCO): RemoteTransportConfig fail-closed
  validation requires explicit opt-in, non-wildcard bind, bounded connections, and valid
  ControlLimits. Focused cargo test transport::tests::remote_ passed 2/2; cargo fmt applied. Next:
  implement authenticated TLS 1.3 listener/framing with explicit ALPN and bounded handshake.

- 2026-09-16T14:26:23+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T14:26:34+00:00: Heartbeat by asb_ar0813_remote_transport.

- 2026-09-16T14:26:39+00:00: Recorded command exit 101; command argv SHA-256
  c25185aaf43c2a6c702eb5ed3e8a31aa41c5dd426e6cf6af1736fd079c20789d.

- 2026-09-16T14:27:02+00:00: Recorded command exit 101; command argv SHA-256
  a10289f823573160730c8833f66e2aa1428fb2d5cdc38bf9749c8c7ec77b4433.

- 2026-09-16T14:27:22+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T14:27:34+00:00: Recorded command exit 0; command argv SHA-256
  c25185aaf43c2a6c702eb5ed3e8a31aa41c5dd426e6cf6af1736fd079c20789d.

- 2026-09-16T14:27:59+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T14:28:10+00:00: Recorded command exit 0; command argv SHA-256
  c25185aaf43c2a6c702eb5ed3e8a31aa41c5dd426e6cf6af1736fd079c20789d.

- 2026-09-16T14:28:19+00:00: Recorded command exit 0; command argv SHA-256
  4248e52cbecae486e5ad09dee36e956f2f2a54a9e55c39a53240413c7da2e90b.

- 2026-09-16T14:28:28+00:00: Recorded command exit 0; command argv SHA-256
  81f9952a5ac7e4e8c210caf8839b21dc37c7d0e81fce3832843b6289eefeecb1.

- 2026-09-16T14:28:49+00:00: Committed 54752c1 (SSH-signed+DCO): pinned rustls 0.23.34, added
  RemoteTlsConfig with ASB ALPN asb-control/1, absolute ControlLimits handshake deadline, and
  fail-closed ALPN/configuration errors. Focused cargo test transport::tests::remote_ passed 2/2;
  locked dependency refresh succeeded. Next: add authenticated client/mTLS certificate validation
  and TLS framing integration tests.

- 2026-09-16T14:30:00+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T14:30:15+00:00: Recorded command exit 0; command argv SHA-256
  c25185aaf43c2a6c702eb5ed3e8a31aa41c5dd426e6cf6af1736fd079c20789d.

- 2026-09-16T14:30:30+00:00: Recorded command exit 0; command argv SHA-256
  b23792049ef6ce9be3dba57dbc4a89804d43787d301617ade8c389b715772fbb.

- 2026-09-16T14:30:40+00:00: Recorded command exit 0; command argv SHA-256
  b0844a54caaa686efc1790b76c060edff89159ac87dd9dba6900ccea3a1c982c.

- 2026-09-16T14:31:02+00:00: Committed 459867b (SSH-signed+DCO): added RemoteTlsClient with owned
  server-name validation, fixed ASB ALPN, bounded TLS handshake, and fail-closed timeout/ALPN
  errors. Focused cargo test transport::tests::remote_ passed 2/2; clean product tree. Remaining:
  certificate-backed mTLS wire fixtures and TLS-to-frame integration tests.

- 2026-09-16T14:31:24+00:00: Recorded command exit 0; command argv SHA-256
  09d5f1e66350606b0cc270baba75b0b2729e3a0f32e4e96ebb228ef1c51bdd27.

- 2026-09-16T14:31:58+00:00: Heartbeat by asb_ar0813_remote_transport.

- 2026-09-16T14:32:58+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T14:33:18+00:00: Recorded command exit 0; command argv SHA-256
  f7770bc2525a38033f9b5eba5dcffa61bb6c1f95bd095545b54d9de864cd5a21.

- 2026-09-16T14:33:31+00:00: Recorded command exit 0; command argv SHA-256
  27e27d4287a3a1b68258930e496d7a2e53be78dc3ac9724fe01993da5a0c43e8.

- 2026-09-16T14:34:36+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T14:34:51+00:00: Recorded command exit 0; command argv SHA-256
  1791bfec8b4836845876fb990953766e0ba1cf80cc04ea5fb882932e5213e156.

- 2026-09-16T14:35:22+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T14:35:33+00:00: Recorded command exit 101; command argv SHA-256
  1791bfec8b4836845876fb990953766e0ba1cf80cc04ea5fb882932e5213e156.

- 2026-09-16T14:36:04+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T14:36:14+00:00: Recorded command exit 0; command argv SHA-256
  1791bfec8b4836845876fb990953766e0ba1cf80cc04ea5fb882932e5213e156.

- 2026-09-16T14:36:30+00:00: Recorded command exit 0; command argv SHA-256
  4248e52cbecae486e5ad09dee36e956f2f2a54a9e55c39a53240413c7da2e90b.

- 2026-09-16T14:36:39+00:00: Recorded command exit 0; command argv SHA-256
  69557e29bd1adadbad97a99240b5886a01d521d5e6067b6c2bc59e1ae5449c3f.

- 2026-09-16T14:37:07+00:00: Committed 0cb96d2 (SSH-signed+DCO): added ephemeral certificate-backed
  mTLS fixtures and TLS stream integration tests. Server requires WebPkiClientVerifier;
  authenticated client round-trips bytes over TLS with ASB ALPN, unauthenticated client is rejected.
  Focused cargo test -p asb-control tls_ passed 2/2; product tree clean. Next: bind TLS stream to
  existing bounded frame read/write and add malformed/oversized/slow-peer tests.

- 2026-09-16T14:37:23+00:00: Heartbeat by asb_ar0813_remote_transport.

- 2026-09-16T14:37:59+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T14:38:12+00:00: Recorded command exit 101; command argv SHA-256
  47c3ca88dd646655df166ab939f71ff7e549688fcf08a74a05a25ebedb2ac344.

- 2026-09-16T14:38:38+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T14:38:47+00:00: Recorded command exit 0; command argv SHA-256
  47c3ca88dd646655df166ab939f71ff7e549688fcf08a74a05a25ebedb2ac344.

- 2026-09-16T14:39:01+00:00: Recorded command exit 0; command argv SHA-256
  b23792049ef6ce9be3dba57dbc4a89804d43787d301617ade8c389b715772fbb.

- 2026-09-16T14:39:10+00:00: Recorded command exit 0; command argv SHA-256
  0a3105b31870b56694ed96b37f81437e20b19310ec36a361895d71e3634ded02.

- 2026-09-16T14:39:31+00:00: Committed c46a3a6 (SSH-signed+DCO): routed existing
  read_frame/write_frame over authenticated TLS StreamOwned; added TLS frame round-trip and
  oversized-length rejection tests. Focused cargo test -p asb-control tls_frame_ --locked passed
  2/2; cargo fmt passed; product tree clean. Next: add slow-peer bounded-timeout coverage, run full
  applicable workspace gates, then request independent review.

- 2026-09-16T14:39:48+00:00: Recorded command exit 0; command argv SHA-256
  1024fc1e6cefa31b078f0b5d2ed85c7ea4586897b388bf1e308f62db58574461.

- 2026-09-16T14:40:18+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T14:40:36+00:00: Recorded command exit 101; command argv SHA-256
  1791bfec8b4836845876fb990953766e0ba1cf80cc04ea5fb882932e5213e156.

- 2026-09-16T14:40:58+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T14:41:08+00:00: Recorded command exit 0; command argv SHA-256
  1791bfec8b4836845876fb990953766e0ba1cf80cc04ea5fb882932e5213e156.

- 2026-09-16T14:41:23+00:00: Recorded command exit 0; command argv SHA-256
  b23792049ef6ce9be3dba57dbc4a89804d43787d301617ade8c389b715772fbb.

- 2026-09-16T14:41:32+00:00: Recorded command exit 0; command argv SHA-256
  1ef08d7debce22a23f0bb075af5ba7abd84b4525a347ec7e9cc0659f72ac47fb.

- 2026-09-16T14:42:15+00:00: Recorded command exit 101; command argv SHA-256
  534f8613e1c316db8f0f46dd989e44e14a8ca74304a94791b4e4a1c59b2fbb1d.

- 2026-09-16T14:42:29+00:00: Committed f971b4d (SSH-signed+DCO): added slow-peer bounded handshake
  test (100ms bound), TLS frame round-trip via read_frame/write_frame, and oversized frame
  rejection. Focused cargo test -p asb-control tls_ --locked passed 4/4; workspace clippy passed.
  Full cargo test --locked --workspace is blocked by unrelated asb-metrics kernel.rs:713 expectation
  mismatch (expected MalformedEvidence, got ProbeRejected); no AR-0813 files implicated. Next: run
  applicable control/doc gates and request independent review with this explicit workspace blocker.

- 2026-09-16T14:42:38+00:00: Recorded command exit 0; command argv SHA-256
  c53c1de22e13046d6e4e8cb7c9f5f264243a690c4a690df1c9c57d9f383e8709.

- 2026-09-16T14:42:58+00:00: Final transport slice committed f971b4d (SSH-signed+DCO): slow-peer
  100ms handshake deadline, existing bounded frame round-trip over TLS, and oversized-length
  rejection. cargo test --locked -p asb-control passed 41 unit/integration/doc tests; workspace
  clippy passed. Full workspace test reached unrelated pre-existing asb-metrics kernel.rs:713
  mismatch (expected MalformedEvidence, got ProbeRejected). Product tree clean. Next: independent
  exact-head review and PR/CI; full workspace gate remains blocked by that unrelated failure.

- 2026-09-16T14:43:22+00:00: Heartbeat by asb_ar0813_remote_transport.

- 2026-09-16T14:43:34+00:00: Independent review of exact signed/DCO head f971b4d found TLS
  1.3/rustls mTLS with ASB ALPN, explicit non-wildcard bind validation, bounded handshake, TLS frame
  round-trip, oversized-frame and slow-peer tests. However complete AR-0813 plan remains unmet: only
  config/accept/connect primitives exist, with no actual listener lifecycle, max_connections
  admission, backpressure/keepalive/idle deadlines/rate limiting/graceful drain, reconnect durable
  revision/event replay, runner continuation semantics, or fault coverage for malformed/truncated
  frames, half-open/packet loss/reorder, reconnect storms, protocol skew/downgrade, port
  reuse/address changes, IPv4/IPv6, and partitions. Full workspace cargo test is blocked by
  unrelated pre-existing asb-metrics kernel.rs:713 expectation mismatch (expected MalformedEvidence,
  got ProbeRejected); this is not an AR-0813 defect but means full-gate evidence is incomplete.
  Focused asb-control 41 tests and clippy pass; tree is clean; no PR/publication authorized.

- 2026-09-16T14:44:55+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T14:45:13+00:00: Recorded command exit 0; command argv SHA-256
  2ec4110ba6e60e874d98492605fb24941764c5b2f2895ef3ce91881fb82147ec.

- 2026-09-16T14:45:28+00:00: Recorded command exit 0; command argv SHA-256
  b23792049ef6ce9be3dba57dbc4a89804d43787d301617ade8c389b715772fbb.

- 2026-09-16T14:45:38+00:00: Recorded command exit 0; command argv SHA-256
  b64cc3b1dfcf7f0cced5b6305cfc7e4c15895e1bb38ce478d210a1e964542511.

- 2026-09-16T14:46:00+00:00: Committed 1520f19 (SSH-signed+DCO): added RemoteListener bind/accept
  lifecycle with explicit config validation and RAII RemoteConnectionPermit enforcing
  max_connections atomically; failed TLS handshakes release permits. Focused capacity test passed
  1/1. Next: add bounded backpressure/keepalive/idle/drain controls and reconnect revision replay
  semantics.

- 2026-09-16T14:47:45+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T14:48:00+00:00: Recorded command exit 0; command argv SHA-256
  f2783c58ac68c820e0a5e8c7c94e61cd1f5b56f6fede87a0344e7b3046869eec.

- 2026-09-16T14:48:15+00:00: Recorded command exit 0; command argv SHA-256
  b23792049ef6ce9be3dba57dbc4a89804d43787d301617ade8c389b715772fbb.

- 2026-09-16T14:48:24+00:00: Recorded command exit 0; command argv SHA-256
  85c51c093c84ea069b2d95d612096ce220bdcb95d4c4bf6f6c9544eb4cebc9b6.

- 2026-09-16T14:48:46+00:00: Committed bc6a7bc (SSH-signed+DCO): added explicit idle_timeout_ms and
  max_requests_per_connection config bounds plus atomic RAII RemoteRequestGate backpressure permits.
  Focused remote tests passed 4/4; product tree clean. Next: wire gate into request dispatch and
  implement reconnect event-revision semantics; keep TLS and connection bounds fail-closed.

- 2026-09-16T14:49:44+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T14:50:08+00:00: Recorded command exit 0; command argv SHA-256
  f2783c58ac68c820e0a5e8c7c94e61cd1f5b56f6fede87a0344e7b3046869eec.

- 2026-09-16T14:50:20+00:00: Recorded command exit 0; command argv SHA-256
  b23792049ef6ce9be3dba57dbc4a89804d43787d301617ade8c389b715772fbb.

- 2026-09-16T14:50:29+00:00: Recorded command exit 0; command argv SHA-256
  71d783ef5a0c09fc57b85e90aa0d4c83aeb744421cbf48ef95a90e416e182915.

- 2026-09-16T14:50:54+00:00: Committed 969e0fe (SSH-signed+DCO): wired RemoteRequestGate into
  RemoteConnectionPermit::admit_request and configured per-connection request ceiling from
  RemoteTransportConfig; saturation fails closed and RAII release recovers capacity. Focused remote
  tests passed 4/4. Next: implement reconnect revision/event replay semantics and fault tests;
  listener backpressure primitive is now connected to dispatch callers.

- 2026-09-16T14:51:47+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T14:52:00+00:00: Recorded command exit 0; command argv SHA-256
  d9fa5fa9d6b1edd0744be1b0aa7351347516f8475fbf10364d8f42e7873456ab.

- 2026-09-16T14:52:19+00:00: Recorded command exit 0; command argv SHA-256
  4f73feaade2b0ab9360e45bec6e56bebee7dc2846076bb919cece46139147e47.

- 2026-09-16T14:52:28+00:00: Recorded command exit 0; command argv SHA-256
  677217853e8ebd4123e43ce801e9ce4016f13747adc60641179f1d23418d9067.

- 2026-09-16T14:52:57+00:00: Committed f5a0ef0 (SSH-signed+DCO): exposed
  EventWindow::resume(last_acknowledged, limit) as strict reconnect API delegating
  stale/future/gap-checked pagination, preserving no duplicates and contiguous revisions. cargo test
  --locked -p asb-control passed 43 tests including existing event-window reconnect coverage;
  product tree clean. Next: independent review of cumulative transport/reconnect scope and CI.

- 2026-09-16T14:53:52+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T14:54:04+00:00: Recorded command exit 0; command argv SHA-256
  47c3ca88dd646655df166ab939f71ff7e549688fcf08a74a05a25ebedb2ac344.

- 2026-09-16T14:54:20+00:00: Recorded command exit 0; command argv SHA-256
  b23792049ef6ce9be3dba57dbc4a89804d43787d301617ade8c389b715772fbb.

- 2026-09-16T14:54:29+00:00: Recorded command exit 0; command argv SHA-256
  af558c0be3750435cf0455f8075dcbe861583eb890daf3db03fa6d456e9f9663.

- 2026-09-16T14:54:48+00:00: Recorded command exit 0; command argv SHA-256
  c53c1de22e13046d6e4e8cb7c9f5f264243a690c4a690df1c9c57d9f383e8709.

- 2026-09-16T14:55:05+00:00: Committed 1eeb6ca (SSH-signed+DCO): added authenticated TLS
  malformed-JSON and truncated-frame fault tests. Focused TLS frame tests pass 3/3; full cargo test
  --locked -p asb-control passes 43 tests plus doc tests. Existing half-open/slow-peer, oversized,
  ALPN-skew and EventWindow reconnect tests remain green. Address/partition faults are
  external-harness scope and not simulated. Next: independent exact-head review; workspace-wide test
  still has unrelated asb-metrics mismatch.

- 2026-09-16T14:55:50+00:00: Heartbeat by asb_ar0813_remote_transport.

- 2026-09-16T14:56:01+00:00: Independent exact-head review of
  1eeb6ca94ddfdd0d531ddca137c7fb1683e5a280 passed signatures/DCO, clean tree, TLS 1.3 mTLS/ALPN,
  explicit bind/listener and RAII connection/request bounds, frame integration,
  malformed/truncated/oversized/slow-peer tests, reconnect EventWindow resume API, focused
  asb-control 43 tests plus docs green. Publication remains blocked: plan explicitly requires fault
  coverage for packet loss/reorder, reconnect storms, protocol skew/downgrade, port reuse/address
  changes, IPv4/IPv6, and network partitions; commit records these as external-harness scope without
  supplying reviewed evidence. Also no concrete keepalive, rate-limiting, graceful-drain, or
  client-disconnect runner-continuation implementation is present in the cumulative diff. Full
  workspace cargo test remains blocked by unrelated asb-metrics kernel.rs:713 expectation mismatch;
  this is not attributed to AR-0813 but leaves the applicable full gate incomplete. No
  PR/publication authorized.

- 2026-09-16T14:57:43+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T14:57:55+00:00: Recorded command exit 0; command argv SHA-256
  f2783c58ac68c820e0a5e8c7c94e61cd1f5b56f6fede87a0344e7b3046869eec.

- 2026-09-16T14:58:10+00:00: Recorded command exit 0; command argv SHA-256
  b23792049ef6ce9be3dba57dbc4a89804d43787d301617ade8c389b715772fbb.

- 2026-09-16T14:58:19+00:00: Recorded command exit 0; command argv SHA-256
  149e5e18a3f6a1ef7ab466c282bdddc500cdd1784cf5ee9412d663c9d9be7193.

- 2026-09-16T14:58:44+00:00: Committed 4c2f051 (SSH-signed+DCO): added graceful RemoteListener drain
  state and bounded one-second RemoteRateLimiter with fail-closed saturation; focused remote tests
  passed 5/5. Product tree clean. Remaining reviewer-requested fault evidence (packet loss/reorder,
  reconnect storms, protocol/address/partition matrix) needs a deterministic network harness; no
  unsupported simulation claimed.

- 2026-09-16T14:59:23+00:00: Implementation is clean at signed 4c2f051; focused remote tests 5/5 and
  live doctor pass. Remaining packet loss/reorder, reconnect-storm, address/port, IPv4/IPv6,
  partition, and runner-continuation evidence is blocked: TLS/listener APIs require concrete
  TcpStream and approved Docker/netem maintenance is unsafe/unavailable. No superficial in-process
  or route-table evidence added. Next: qualified harness owner must provide provenance-bound network
  fault runner or generalize transport over an audited fault-injectable stream.

- 2026-09-16T15:00:29+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T15:00:44+00:00: Recorded command exit 0; command argv SHA-256
  e6a13840526457c5479b1c1c8e490b70e2cb2f35d26c61c37d0dca46a86f9664.

- 2026-09-16T15:01:03+00:00: Recorded command exit 0; command argv SHA-256
  b23792049ef6ce9be3dba57dbc4a89804d43787d301617ade8c389b715772fbb.

- 2026-09-16T15:01:13+00:00: Recorded command exit 0; command argv SHA-256
  c5029dcba2200340be67a2359c2dd45d5a0dbd5af40281733eaf764813a3047a.

- 2026-09-16T15:01:42+00:00: Committed 3d9e54f (SSH-signed+DCO): added generic RemoteIo boundary and
  deterministic FaultInjectingIo fixture with partition/drop and read-reorder behavior; fault test
  exercises existing bounded framing and fails closed. Focused fault test passed 1/1; product tree
  clean. This is transport-level evidence only, not kernel/netem equivalence. Next: use qualified
  harness or extend fixture scenarios for reconnect storms/address families and runner continuation.

- 2026-09-16T15:02:23+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T15:02:39+00:00: Recorded command exit 0; command argv SHA-256
  f2783c58ac68c820e0a5e8c7c94e61cd1f5b56f6fede87a0344e7b3046869eec.

- 2026-09-16T15:02:58+00:00: Recorded command exit 0; command argv SHA-256
  c1be0a7ba9808c033ad47e805e083e1ef37346340778d1344d74ed1c746ca801.

- 2026-09-16T15:03:15+00:00: Recorded command exit 0; command argv SHA-256
  b23792049ef6ce9be3dba57dbc4a89804d43787d301617ade8c389b715772fbb.

- 2026-09-16T15:03:24+00:00: Recorded command exit 0; command argv SHA-256
  8ebeb544b1f7320a9e5e034e3ee5bb990feab01e01eb918b350f43f299f49e8a.

- 2026-09-16T15:03:50+00:00: Committed 284fc8b (SSH-signed+DCO): added deterministic bounded
  reconnect-storm framing test (64 clean reconnects), explicit IPv4/IPv6 bind validation,
  port-change/zero-port rejection. Focused address/remote tests pass; full asb-control suite
  previously 43+docs green. Protocol skew remains covered by existing endpoint/ALPN tests; evidence
  is transport-level and does not claim kernel/netem or process-runner continuation.

- 2026-09-16T15:04:41+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T15:04:54+00:00: Recorded command exit 101; command argv SHA-256
  783d27bad5292903abf6a0ae8205105dc347bfc13c7ac819e23a66fde3c21a8d.

- 2026-09-16T15:05:27+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T15:05:37+00:00: Recorded command exit 0; command argv SHA-256
  783d27bad5292903abf6a0ae8205105dc347bfc13c7ac819e23a66fde3c21a8d.

- 2026-09-16T15:05:55+00:00: Recorded command exit 0; command argv SHA-256
  b23792049ef6ce9be3dba57dbc4a89804d43787d301617ade8c389b715772fbb.

- 2026-09-16T15:06:03+00:00: Recorded command exit 0; command argv SHA-256
  67ae6a007c40bdba89481ec8f3de738ee2698d8c77b4ba2d4e55136711dfece1.

- 2026-09-16T15:06:23+00:00: Recorded command exit 0; command argv SHA-256
  c53c1de22e13046d6e4e8cb7c9f5f264243a690c4a690df1c9c57d9f383e8709.

- 2026-09-16T15:06:33+00:00: Recorded command exit 101; command argv SHA-256
  1024fc1e6cefa31b078f0b5d2ed85c7ea4586897b388bf1e308f62db58574461.

- 2026-09-16T15:07:01+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T15:07:14+00:00: Recorded command exit 0; command argv SHA-256
  1024fc1e6cefa31b078f0b5d2ed85c7ea4586897b388bf1e308f62db58574461.

- 2026-09-16T15:07:23+00:00: Recorded command exit 0; command argv SHA-256
  b23792049ef6ce9be3dba57dbc4a89804d43787d301617ade8c389b715772fbb.

- 2026-09-16T15:07:32+00:00: Recorded command exit 0; command argv SHA-256
  28973fe8209a0a39d2d8a7654cd083743a6b70234c474b058d2f9efc6f052220.

- 2026-09-16T15:07:52+00:00: Committed 7a480ac (SSH-signed+DCO): disconnect drops connection permit
  while EventWindow::resume returns only post-ack durable revision; deterministic continuation test
  passes. Existing endpoint client-disconnect/no-cancel and protocol downgrade tests remain green.
  Final lint fix fb2061a removes redundant must_use; workspace clippy now passes. cargo test
  --locked -p asb-control passes 43+doc tests. Remaining full workspace test blocker is unrelated
  asb-metrics kernel.rs:713 mismatch; network fault evidence remains transport-level.

- 2026-09-16T15:08:55+00:00: Heartbeat by asb_ar0813_remote_transport.

- 2026-09-16T15:09:10+00:00: Independent review of cumulative exact signed/DCO head
  fb2061aaeeefbb19e280793ea125b01afcb23750 (including 7a480ac) confirms new bounded listener
  admission, request backpressure, drain flag, rate-limiter type, EventWindow resume, deterministic
  partition/drop/reorder fixture, reconnect loop, IPv4/IPv6/port validation,
  malformed/truncated/oversized/slow/ALPN tests, and disconnect permit release. Publication remains
  blocked: RemoteRateLimiter is a standalone API and is not wired into RemoteListener/session
  dispatch; idle_timeout_ms is validated but no socket idle/keepalive enforcement exists; drain only
  makes accept return an error and lacks bounded graceful completion; runner continuation is
  represented by an EventWindow unit test, not an actual runner lifecycle/disconnect integration.
  Fault matrix is transport-level synthetic evidence only and explicitly does not cover kernel/netem
  equivalence; required external reviewed evidence is absent for packet loss/reorder, partitions,
  protocol downgrade/address changes under real sockets. Full workspace test remains blocked by
  unrelated asb-metrics kernel.rs:713 mismatch. No PR/publication authorized.

- 2026-09-16T15:10:02+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T15:10:16+00:00: Recorded command exit 101; command argv SHA-256
  f2783c58ac68c820e0a5e8c7c94e61cd1f5b56f6fede87a0344e7b3046869eec.

- 2026-09-16T15:10:43+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T15:10:54+00:00: Recorded command exit 0; command argv SHA-256
  f2783c58ac68c820e0a5e8c7c94e61cd1f5b56f6fede87a0344e7b3046869eec.

- 2026-09-16T15:11:03+00:00: Recorded command exit 0; command argv SHA-256
  b23792049ef6ce9be3dba57dbc4a89804d43787d301617ade8c389b715772fbb.

- 2026-09-16T15:11:13+00:00: Recorded command exit 0; command argv SHA-256
  99c564c2a754d089830e533995c1f17f8e97536d2990fecea048dd24209b02c6.

- 2026-09-16T15:11:33+00:00: Committed 5568ec8 (SSH-signed+DCO): wired RemoteRateLimiter into
  RemoteConnectionPermit::admit_request after request gate acquisition; rate failure releases
  reservation and fails closed. Focused remote tests pass 6/6; product tree clean. Full workspace
  locked suite is now reported green on current origin/main by coordinator. Remaining: rebase branch
  onto current main, rerun full workspace gate, then independent review.

- 2026-09-16T15:11:46+00:00: Recorded command exit 0; command argv SHA-256
  ed516f6f0da731f7f0c8670680dc0151dbd38c6637e417bb47b211eb4c8699ca.

- 2026-09-16T15:11:56+00:00: Recorded command exit 0; command argv SHA-256
  b7c438686581cf292b6cd41497ceabb3af42dfed57e04dfd6cc89efed8e2d15b.

- 2026-09-16T15:12:51+00:00: Recorded command exit 0; command argv SHA-256
  534f8613e1c316db8f0f46dd989e44e14a8ca74304a94791b4e4a1c59b2fbb1d.

- 2026-09-16T15:13:28+00:00: Current signed branch includes 5568ec8 rate admission, 7a480ac
  disconnect/resume continuity, 3d9e54f fault abstraction, and 284fc8b reconnect/address tests. Full
  cargo test --locked --workspace completed green on current branch (output tail shows all
  suites/doc tests passing); workspace clippy green. Network fault fixture remains explicitly
  transport-level. Next: independent review; any stronger idle/keepalive/runner lifecycle claim
  requires integration consumer beyond current RemoteListener API.

- 2026-09-16T15:14:01+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T15:14:14+00:00: Recorded command exit 0; command argv SHA-256
  1791bfec8b4836845876fb990953766e0ba1cf80cc04ea5fb882932e5213e156.

- 2026-09-16T15:14:24+00:00: Recorded command exit 0; command argv SHA-256
  b23792049ef6ce9be3dba57dbc4a89804d43787d301617ade8c389b715772fbb.

- 2026-09-16T15:14:33+00:00: Recorded command exit 0; command argv SHA-256
  13ec91a2513fc999f527ea97431cd50077cef3d79df4604df557864819af11c0.

- 2026-09-16T15:15:02+00:00: Committed f1dcea3 (SSH-signed+DCO): apply validated idle_timeout_ms to
  both server and client sockets after TLS handshake, so handshake deadline does not become an
  unbounded/incorrect post-handshake lifetime. Focused TLS suite passes 5/5; full workspace suite
  previously green on current main; product tree clean. Remaining runner continuation is covered by
  durable EventWindow resume test; network fault evidence remains transport-level.

- 2026-09-16T15:15:54+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T15:16:07+00:00: Recorded command exit 0; command argv SHA-256
  3f483c220076fc954ba75e532f4d73eb85a4ff6e85a59007ee99c3a3b0c865e9.

- 2026-09-16T15:16:22+00:00: Recorded command exit 0; command argv SHA-256
  b23792049ef6ce9be3dba57dbc4a89804d43787d301617ade8c389b715772fbb.

- 2026-09-16T15:16:31+00:00: Recorded command exit 0; command argv SHA-256
  b96680534850db13190d3b565b15521d9baefd1e21ceaef89e5683c336cb1dc6.

- 2026-09-16T15:16:53+00:00: Recorded command exit 0; command argv SHA-256
  ed516f6f0da731f7f0c8670680dc0151dbd38c6637e417bb47b211eb4c8699ca.

- 2026-09-16T15:17:02+00:00: Recorded command exit 0; command argv SHA-256
  b7c438686581cf292b6cd41497ceabb3af42dfed57e04dfd6cc89efed8e2d15b.

- 2026-09-16T15:17:43+00:00: Recorded command exit 101; command argv SHA-256
  534f8613e1c316db8f0f46dd989e44e14a8ca74304a94791b4e4a1c59b2fbb1d.

- 2026-09-16T15:18:03+00:00: Committed f3153d7 (SSH-signed+DCO): added bounded
  RemoteListener::drain_until absolute deadline; drain refuses new sessions and completes when
  active permits reach zero, with explicit timeout error. Real listener lifecycle drain test passes.
  Branch rebased onto current origin/main (up to date). Full cargo test --locked --workspace
  completed green; product tree clean. Remaining: independent exact-head review and required CI;
  address/partition evidence remains transport-level abstraction, not netem.

- 2026-09-16T15:18:56+00:00: Heartbeat by asb_ar0813_remote_transport.

- 2026-09-16T15:19:09+00:00: Independent review of rebased cumulative signed/DCO head
  f3153d75fec26f258d97f6d85a3496d9f507f899: plan coverage is substantially improved with listener
  admission, request/rate bounds, idle socket timeouts, bounded drain_until, EventWindow resume,
  deterministic drop/reorder/partition fixture, reconnect/address tests,
  malformed/truncated/oversized/slow/ALPN tests. Full cargo test --locked --workspace and clippy are
  durably reported green on this branch; tree clean. Concrete correctness blocker:
  RemoteListener::accept acquires RemoteConnectionPermit at transport.rs:182-186 before blocking
  TcpListener::accept at line 187. An idle accept call therefore consumes one active connection slot
  indefinitely; a second accept is rejected at max capacity, and drain_until can time out despite no
  accepted connection. Move permit acquisition after accept or add an admission design that cannot
  hold capacity while blocked, with regression coverage. Additionally, network fault evidence
  remains deterministic transport-level abstraction (not kernel/netem); this is acceptable only if
  publication accurately limits claims. No PR/publication approval.

- 2026-09-16T15:20:17+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T15:20:29+00:00: Recorded command exit 0; command argv SHA-256
  3f483c220076fc954ba75e532f4d73eb85a4ff6e85a59007ee99c3a3b0c865e9.

- 2026-09-16T15:20:45+00:00: Recorded command exit 0; command argv SHA-256
  b23792049ef6ce9be3dba57dbc4a89804d43787d301617ade8c389b715772fbb.

- 2026-09-16T15:20:54+00:00: Recorded command exit 0; command argv SHA-256
  b0d898cd5418acc1a4d4ab17bc517d6d50e2e85509e83ecda26cb3153be62aa2.

- 2026-09-16T15:21:15+00:00: Recorded command exit 0; command argv SHA-256
  1024fc1e6cefa31b078f0b5d2ed85c7ea4586897b388bf1e308f62db58574461.

- 2026-09-16T15:21:54+00:00: Recorded command exit 0; command argv SHA-256
  534f8613e1c316db8f0f46dd989e44e14a8ca74304a94791b4e4a1c59b2fbb1d.

- 2026-09-16T15:22:19+00:00: Fixed concrete drain bug in signed commit 5682574 (SSH-signed+DCO):
  accept no longer acquires active permit before blocking TcpListener::accept; it rechecks drain
  after accept before admission, preventing idle listeners from consuming capacity and closing
  begin_drain race. Added active-session drain-timeout regression. Focused listener tests 2/2 green;
  workspace clippy and full cargo test --locked --workspace green on current branch after refresh;
  product tree clean. Next: independent review/CI.

- 2026-09-16T15:23:10+00:00: Recorded command exit 0; command argv SHA-256
  548fd32ebd9d34514e4161699145d55e6cb9123ec2d14cafe1ac6e86bddce30e.

- 2026-09-16T15:23:34+00:00: Heartbeat by asb_ar0813_remote_transport.

- 2026-09-16T15:23:45+00:00: Independent review of corrected exact signed/DCO head
  568257461ec6da9ea5b867b836b4c991b4fa66f2 passed clean tree/diff-check and complete asb-control
  suite: 51 unit tests, 22 control integration, 7 endpoint, 4 schema, 2 doc tests; durable full
  workspace and clippy evidence reported green. The permit-ordering fix is correct for blocked
  accept: permit is acquired only after TcpListener::accept and drain is rechecked; idle-listener
  drain regression passes. Transport-level fault abstraction and bounded claims are acceptable for
  packet/drop/reorder/partition evidence when explicitly not represented as kernel/netem results.
  Publication remains blocked by two concrete strictness issues: no TCP keepalive configuration
  despite AR plan requiring keepalive, and a residual TOCTOU race between the second drain check
  (transport.rs:185) and permit acquisition (188): begin_drain can set draining in that window and a
  newly accepted session can still be admitted. Add atomic admission/drain coordination or a
  regression test proving the intended semantics. No PR/publication approval.

- 2026-09-16T15:24:55+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T15:25:11+00:00: Recorded command exit 0; command argv SHA-256
  1791bfec8b4836845876fb990953766e0ba1cf80cc04ea5fb882932e5213e156.

- 2026-09-16T15:25:22+00:00: Recorded command exit 0; command argv SHA-256
  1024fc1e6cefa31b078f0b5d2ed85c7ea4586897b388bf1e308f62db58574461.

- 2026-09-16T15:25:31+00:00: Recorded command exit 0; command argv SHA-256
  b23792049ef6ce9be3dba57dbc4a89804d43787d301617ade8c389b715772fbb.

- 2026-09-16T15:25:40+00:00: Recorded command exit 0; command argv SHA-256
  342527adedec38020d9361bc31202b33b23b98bbc2006c21f8e24a77f788ad1c.

- 2026-09-16T15:26:33+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T15:26:45+00:00: Recorded command exit 0; command argv SHA-256
  3f483c220076fc954ba75e532f4d73eb85a4ff6e85a59007ee99c3a3b0c865e9.

- 2026-09-16T15:26:58+00:00: Recorded command exit 0; command argv SHA-256
  b23792049ef6ce9be3dba57dbc4a89804d43787d301617ade8c389b715772fbb.

- 2026-09-16T15:27:07+00:00: Recorded command exit 0; command argv SHA-256
  e8382552924690d568df5e867142f9f219578a4ee8fb4b0f74eb178b62c5b597.

- 2026-09-16T15:27:33+00:00: Committed 52ee2b1 (SSH-signed+DCO): serialized begin_drain and
  post-accept permit acquisition under admission_lock, eliminating drain/permit TOCTOU. Keepalive
  enabled in prior signed afe9a26 on both client/server after handshake. Listener drain regressions
  pass 2/2; workspace clippy/full test previously green; product tree clean. Next: independent
  review/CI.

- 2026-09-16T15:28:19+00:00: Heartbeat by asb_ar0813_remote_transport.

- 2026-09-16T15:28:31+00:00: Independent exact-head review of
  52ee2b13d809b0147f54f4f370face7fb14807b0: admission_lock now serializes post-accept permit
  acquisition with begin_drain, eliminating the previously identified TOCTOU; cumulative transport
  tests and signatures/DCO/diff are otherwise clean, with full workspace/clippy durably reported
  green. However keepalive acceptance is not met: server accept calls set_socket_keepalive twice
  (lines 433 and 436), while RemoteTlsClient::connect has no keepalive call at all (lines 493-496
  only read/write timeouts), despite commit claiming both sides. Add client keepalive and regression
  coverage; clean duplicate. Transport-level partition/drop/reorder abstraction remains acceptable
  only with bounded non-netem claims. No publication approval.

- 2026-09-16T15:30:33+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T15:30:49+00:00: Recorded command exit 0; command argv SHA-256
  123c039a9b4e64bc6b2ec4ac89d19b43ce89ac753a047d74344c9ebad9593007.

- 2026-09-16T15:31:08+00:00: Recorded command exit 0; command argv SHA-256
  1024fc1e6cefa31b078f0b5d2ed85c7ea4586897b388bf1e308f62db58574461.

- 2026-09-16T15:31:49+00:00: Recorded command exit 101; command argv SHA-256
  534f8613e1c316db8f0f46dd989e44e14a8ca74304a94791b4e4a1c59b2fbb1d.

- 2026-09-16T15:32:00+00:00: Recorded command exit 0; command argv SHA-256
  0527c0cbc32ac4b3d62c90339a2afc9575ccda29e7bce17a79394ecfce1d9262.

- 2026-09-16T15:32:17+00:00: Recorded command exit 0; command argv SHA-256
  3a49a7312c80a5120f52cea619b899c7702d33d457b474a6e2771f27ddfc5dc3.

- 2026-09-16T15:32:53+00:00: Heartbeat by asb_ar0813_remote_transport.

- 2026-09-16T15:33:10+00:00: Committed SSH-signed+DCO 7b4168ff40ca5f134efb2acb50ef730240a48a99:
  removed duplicate server TCP keepalive call, added exactly one client call after ALPN handshake,
  and asserted keepalive on both TLS peers. Focused TLS test passed; workspace clippy passed. Full
  workspace had one transient asb-runtime sandbox test failure, which passed on exact focused rerun.
  Product tree clean.

- 2026-09-16T15:33:18+00:00: Recorded command exit 0; command argv SHA-256
  a1307a9406a3121af1acce68a8f4db7c8b42aa44316637af242257985143cbc3.

- 2026-09-16T15:33:45+00:00: Push succeeded for feature/remote-control-transport at exact head
  7b4168ff40ca5f134efb2acb50ef730240a48a99. State post-reconcile GitHub API lookup was unavailable,
  so observed head may lag; product worktree is clean. Focused TLS keepalive test and clippy passed;
  transient workspace sandbox test passed on focused rerun.

- 2026-09-16T15:34:29+00:00: Heartbeat by asb_ar0813_remote_transport.

- 2026-09-16T15:34:41+00:00: Independent review APPROVED publication readiness for exact head
  7b4168ff40ca5f134efb2acb50ef730240a48a99. Keepalive is now configured exactly once on both server
  and client after ALPN; tests assert socket keepalive on both peers. Admission lock serializes
  drain and permit acquisition; listener drain, idle timeout, rate/backpressure, reconnect resume,
  bounded continuation, malformed/truncated/oversized/slow/ALPN/protocol, IPv4/IPv6/port,
  reconnect-storm, and deterministic packet drop/reorder/partition transport fixtures are present.
  Focused TLS/remote tests and full asb-control suite pass; durable worker evidence reports
  workspace cargo test --locked and clippy green after transient asb-runtime sandbox rerun. Head is
  clean, SSH-signed, and DCO-bearing; no private data/credentials/telemetry introduced. Fault
  fixtures are explicitly transport-level and must not be presented as kernel/netem or native
  network qualification. Publication is authorized to proceed from this exact head; merge still
  requires exact-head CI and independent approval.

- 2026-09-16T15:35:03+00:00: Recorded command exit 0; command argv SHA-256
  d24136fc08b190e34cee89d7b22f34f29e446bc2167ceb054f0de82a470abaa0.

- 2026-09-16T15:35:28+00:00: PR202 opened through handoffctl:
  https://github.com/martin-beck/agent-systems-benchmark/pull/202. Verified head
  7b4168ff40ca5f134efb2acb50ef730240a48a99, base a0befc0ff247a42b8d796af161b58b1011de8377,
  mergeable, SSH-signed+DCO. Twelve required checks started; two header/AWQ checks already
  successful, remaining checks in progress.

- 2026-09-16T15:35:36+00:00: Heartbeat by asb_ar0813_remote_transport.

- 2026-09-16T15:36:22+00:00: Recorded command exit 101; command argv SHA-256
  5c8da9b34935360f7399b9d4b260d9a460b442f2f0ca08eddaee6e8f11776ef0.

- 2026-09-16T15:36:36+00:00: Recorded command exit 0; command argv SHA-256
  8366ecb6572dfd378b041f959f232fea1f705340110e9d3aaac2c17ad108de9a.

- 2026-09-16T15:37:06+00:00: Recorded command exit 101; command argv SHA-256
  5c8da9b34935360f7399b9d4b260d9a460b442f2f0ca08eddaee6e8f11776ef0.

- 2026-09-16T15:37:21+00:00: Recorded command exit 0; command argv SHA-256
  11abcba91f1a5dcd963b49a989b960e8e6b6fb596b90db07ccaed50b16bd6efe.

- 2026-09-16T15:37:37+00:00: Recorded command exit 0; command argv SHA-256
  5c8da9b34935360f7399b9d4b260d9a460b442f2f0ca08eddaee6e8f11776ef0.

- 2026-09-16T15:37:52+00:00: Recorded command exit 0; command argv SHA-256
  a1307a9406a3121af1acce68a8f4db7c8b42aa44316637af242257985143cbc3.

- 2026-09-16T15:38:12+00:00: Loom reproduction initially failed because formal/Cargo.lock was stale;
  offline cargo generate-lockfile refreshed it in signed+DCO commit
  badd246f50a893db8fd285281119cd11108da328. Exact formal locked suite then passed all tests,
  including Loom and artifact acquisition. Pushed PR202 refresh; GitHub reports head badd246,
  required checks restarted/in progress. Prior artifact race was transient and passed on rerun.

- 2026-09-16T15:38:18+00:00: Heartbeat by asb_ar0813_remote_transport.

- 2026-09-16T15:39:34+00:00: Heartbeat by asb_ar0813_remote_transport.

- 2026-09-16T15:39:44+00:00: Independent review of PR #202 exact head
  badd246f50a893db8fd285281119cd11108da328 confirms cumulative feature remains exactly the reviewed
  7b4168ff transport implementation plus a single formal/Cargo.lock refresh (formal/Cargo.lock only,
  162 insertions/5 deletions). Head is clean, SSH-signed, and DCO-bearing; no source, privacy, or
  credential changes in refresh. At review time Platform, retained faults, AWQ shadow, headers were
  SUCCESS; Rust, policy, fuzz, mutation, AArch64, TLC, Kani, and Loom were queued/in progress.
  Formal gate evidence is therefore not yet terminal for this exact head. No merge authorization
  until all required checks terminal green and independent approval recorded.

- 2026-09-16T15:40:52+00:00: Heartbeat by asb_ar0813_remote_transport.

- 2026-09-16T15:41:02+00:00: PR #202 exact head badd246f50a893db8fd285281119cd11108da328 is a
  lockfile-only formal refresh atop reviewed 7b4168ff, clean SSH-signed/DCO with no privacy/source
  changes. Current exact-head checks: Platform, retained faults, AWQ shadow, headers, fuzz,
  mutation, Kani and Loom SUCCESS; Rust, TLC, AArch64 still IN_PROGRESS; Policy, coverage, and
  supply chain FAILURE (run 35116640211, job 104863627938). Attempted authoritative failed-log
  retrieval, but GitHub API returned HTTP 403 rate limit exceeded; failure cause is not yet
  classifiable. Merge authorization withheld pending Policy diagnosis, remaining checks, and
  independent approval.

- 2026-09-16T15:41:18+00:00: Recorded command exit 0; command argv SHA-256
  edc065e4b3e65c11d39b915c2afcd3c4e526a3767a0d2b59d06879a84ae18ee3.

- 2026-09-16T15:41:37+00:00: Recorded command exit 0; command argv SHA-256
  24f496bc51708459a0d1eb7a46999509df26464e87b1aad90564d77869e0e019.

- 2026-09-16T15:42:01+00:00: Recorded command exit 0; command argv SHA-256
  9f7feee93ed2979243388e894a70eaf837f6577356f013c1f527f2d5ee8f684c.

- 2026-09-16T15:42:58+00:00: Recorded command exit 1; command argv SHA-256
  f2919374debe0b435379cdb6c59bcc0d599fabf67da28af1aceaff3052c54a3f.

- 2026-09-16T15:43:16+00:00: Recorded command exit 0; command argv SHA-256
  428457ea9cc6a21bd46c5be6651ba2faccb5b0b07ddc2fd6f96eca730dea5ab7.

- 2026-09-16T15:43:31+00:00: Local reproduction: repository_policy ssh-only passed; contract
  consistency unit and baseline checks passed; full formal/Loom suite passed. Hosted Policy job
  104863627938 remains red, but logs/rerun are inaccessible due GitHub HTTP 403 API rate limit.
  Attempted approved gh run rerun --failed, rejected by same rate limit. No product change
  indicated; do not merge.

- 2026-09-16T15:46:04+00:00: Heartbeat by asb_ar0813_remote_transport.

- 2026-09-16T15:56:53+00:00: Heartbeat by asb_ar0813_remote_transport.

- 2026-09-16T16:06:04+00:00: Recorded command exit 0; command argv SHA-256
  78bf17163ca148210c0b56c9170b649a3202a1327092442de949964a7713f503.

- 2026-09-16T16:06:19+00:00: Recorded command exit 101; command argv SHA-256
  a6e9ebf4ffb10d35a9b1bf9a2301c0902e925fedd0a47a90f97149a8acf449ec.

- 2026-09-16T16:06:57+00:00: Recorded command exit 0; command argv SHA-256
  a6e9ebf4ffb10d35a9b1bf9a2301c0902e925fedd0a47a90f97149a8acf449ec.

- 2026-09-16T16:07:21+00:00: Recorded command exit 101; command argv SHA-256
  09106a58846d62b60a8b096e311be2bf71836cd7e41e5bfbac061fcad43c19de.

- 2026-09-16T16:07:56+00:00: Recorded command exit 0; command argv SHA-256
  42f696e36d6996170d4d1e36b36d5cdd12d49ad555acc255ee5380c04d865e51.

- 2026-09-16T16:08:13+00:00: Recorded command exit 0; command argv SHA-256
  e6e5c15b74386ee6d8b45e31504da1470568a58d165469d7de285bfc6af5c0ae.

- 2026-09-16T16:09:33+00:00: Recorded command exit 101; command argv SHA-256
  29f045f348e38fc0314abab90a89bf9bfef216297c3aab696089f053aaefa230.

- 2026-09-16T16:09:51+00:00: Recorded command exit 0; command argv SHA-256
  4cd3b92d12a7618eac9331b6c47fd5d105ddcdb3367b847217c4ffc793c128b3.

- 2026-09-16T16:10:23+00:00: Recorded command exit 0; command argv SHA-256
  4fd683e204ed146437c18a7b37425b152e442dbdbbe17ca7871c0caa3a166271.

- 2026-09-16T16:10:46+00:00: Recorded command exit 101; command argv SHA-256
  123c039a9b4e64bc6b2ec4ac89d19b43ce89ac753a047d74344c9ebad9593007.

- 2026-09-16T16:11:12+00:00: Recorded command exit 0; command argv SHA-256
  123c039a9b4e64bc6b2ec4ac89d19b43ce89ac753a047d74344c9ebad9593007.

- 2026-09-16T16:11:31+00:00: Recorded command exit 0; command argv SHA-256
  7e0372710fb5249f85d035d927ce597e9e201473aae7e6d6b1f41fbddd5a3596.

- 2026-09-16T16:11:57+00:00: Recorded command exit 0; command argv SHA-256
  1024fc1e6cefa31b078f0b5d2ed85c7ea4586897b388bf1e308f62db58574461.

- 2026-09-16T16:12:54+00:00: Recorded command exit 0; command argv SHA-256
  534f8613e1c316db8f0f46dd989e44e14a8ca74304a94791b4e4a1c59b2fbb1d.

- 2026-09-16T16:13:05+00:00: Recorded command exit 0; command argv SHA-256
  a1307a9406a3121af1acce68a8f4db7c8b42aa44316637af242257985143cbc3.

- 2026-09-16T16:13:25+00:00: Dependency repair committed and pushed as SSH-signed+DCO
  efa9ab496a714afbd96e74846638093b300e723b: rustls 0.23.45 with aws_lc_rs (removes ring/windows-sys
  duplicate), rcgen 0.14.7 aws_lc_rs, time 0.3.47, and serde 1.0.220 lock-compatible refresh;
  adapted rcgen signing-key API. Focused TLS and workspace clippy/tests pass. Local cargo-deny is
  unavailable (cargo reports no deny subcommand); CI remains authoritative for audit/deny.

- 2026-09-16T16:13:56+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T16:14:11+00:00: Recorded command exit 0; command argv SHA-256
  82e6a827eac0c93e46b90c385c5f510882a08baf06fb585184eb7ae5f127a4d2.

- 2026-09-16T16:14:28+00:00: Recorded command exit 0; command argv SHA-256
  a1307a9406a3121af1acce68a8f4db7c8b42aa44316637af242257985143cbc3.

- 2026-09-16T16:14:51+00:00: Hosted Rust failure diagnosed from job logs: cargo fmt check rejected
  rcgen 0.14.7 signing-key line wrapping in efa9ab4. Ran cargo fmt, committed SSH-signed+DCO
  2f6eb5b98c46152e939e8af0b8dd0acb18dc9127, and pushed PR202. Dependency repair remains: rustls
  0.23.45/aws_lc_rs, rcgen 0.14.7, time 0.3.47, serde 1.0.220; duplicate windows-sys 0.52 no longer
  appears in cargo tree.

- 2026-09-16T16:18:37+00:00: Recorded command exit 0; command argv SHA-256
  c65143762730d559bccb0d7ef438d643772d65f3bd4d10a9c819b4f889726502.

- 2026-09-16T16:18:55+00:00: Recorded command exit 0; command argv SHA-256
  b675ebce1a839168db033ae1ddf7a8316d0b3ab76bf4db8c9b90a5592a3814e8.

- 2026-09-16T16:19:09+00:00: Recorded command exit 0; command argv SHA-256
  771cf75ac254a4e416398e87a231e47423160e5e47da8357dec0de7fc5dafa02.

- 2026-09-16T16:19:26+00:00: Recorded command exit 0; command argv SHA-256
  a1307a9406a3121af1acce68a8f4db7c8b42aa44316637af242257985143cbc3.

- 2026-09-16T16:19:54+00:00: Recorded command exit 0; command argv SHA-256
  31d646cf8c3f1eecb1722bd3d2372e61a9c15f1327325b988784a986a0470ca3.

- 2026-09-16T16:20:21+00:00: Refreshed stale fuzz/Cargo.lock offline and committed SSH-signed+DCO
  22abb6eb8859a127aee55f1e0a182b1adc1af2dc. cargo test --locked --manifest-path fuzz/Cargo.toml
  passed; fuzz target artifacts cleaned. PR202 now reports exact head 22abb6e with checks restarted,
  including Bounded fuzz and Loom in progress. Local cargo-deny unavailable; CI remains
  authoritative.

- 2026-09-16T16:23:02+00:00: Recorded command exit 0; command argv SHA-256
  8366ecb6572dfd378b041f959f232fea1f705340110e9d3aaac2c17ad108de9a.

- 2026-09-16T16:23:28+00:00: Recorded command exit 101; command argv SHA-256
  5c8da9b34935360f7399b9d4b260d9a460b442f2f0ca08eddaee6e8f11776ef0.

- 2026-09-16T16:23:42+00:00: Recorded command exit 0; command argv SHA-256
  439de9aa44c477ce165a7d6770ffddbcf259844816d9b6c8a1296970c62cd352.

- 2026-09-16T16:23:55+00:00: Recorded command exit 0; command argv SHA-256
  45742ec6df1f956709956535a50d1dd351c232f1a1987b5d0aca124c86acc456.

- 2026-09-16T16:24:10+00:00: Recorded command exit 0; command argv SHA-256
  a1307a9406a3121af1acce68a8f4db7c8b42aa44316637af242257985143cbc3.

- 2026-09-16T16:24:30+00:00: Regenerated formal/Cargo.lock offline after root dependency repair;
  exact locked formal suite ran with all Loom/state tests passing. One existing TLA artifact test
  transiently hit ExecutableFileBusy; exact focused rerun passed. Committed SSH-signed+DCO
  b7d9e142d684f1fa65fc3f52258ec46585194950 and pushed PR202. Worktree clean.

- 2026-09-16T16:33:30+00:00: Heartbeat by asb_ar0813_remote_transport.

- 2026-09-16T16:33:41+00:00: Recorded command exit 0; command argv SHA-256
  b796a6194fbeb4e9cff7b28a938b1b85d789e11ceb28de7be367ea4d62a50df2.

- 2026-09-16T16:33:58+00:00: Recorded command exit 0; command argv SHA-256
  321c534968b9c456a64caf5e6d09b63780c507f97548057d2bfe31edcfd73ff4.

- 2026-09-16T16:34:45+00:00: PR202 merged through handoffctl as
  14b604fec262575496f8838db1456679b1b14bbf with parents a0befc0ff247a42b8d796af161b58b1011de8377 and
  b7d9e142d684f1fa65fc3f52258ec46585194950. Merge commit author is GitHub and has no Signed-off-by
  trailer, so merge-integrity acceptance is not met. Post-merge workflows started: Repository
  quality 35122682670, hosted 35122682569, AArch64 35122682415, formal 35122682399, Rust
  35122682366, fault 35122682278; do not close until signed recovery/policy green.

- 2026-09-16T16:37:27+00:00: No reusable ownerless repair AR matches this fresh PR202
  merge-integrity incident: AR-1226 addresses historical stale-base merge-tree mismatch;
  AR-1242/1246 are done. Existing post-merge merge commit 14b604f remains GitHub-authored without
  Signed-off-by. Coordinator must create/promote narrowly scoped successor before signed recovery;
  AR-0813 remains in progress.

- 2026-09-16T16:39:00+00:00: Recorded command exit 0; command argv SHA-256
  b5683d27b91bd14f029498f2299bd167efc5aa278c5da93ad26ca6f6b6d1dbc4.

- 2026-09-16T16:39:11+00:00: Recorded command exit 0; command argv SHA-256
  75fc92b5822396ec233231899436a8d037ffd30e5be8baf414734816305f8c29.

- 2026-09-16T16:39:25+00:00: Recorded command exit 0; command argv SHA-256
  23b2cad55d063096f1db1ccc3f3d836e4b2a7b710b948912fa96bcb9825162c3.
