---
{
  "branch": "feature/remote-control-transport",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-16T16:43:22+00:00",
  "depends_on": [
    "AR-0702",
    "AR-0803",
    "AR-0902"
  ],
  "id": "AR-0813",
  "next_action": "Close remaining AR-0813 transport scope before publication: implement listener lifecycle with actual max-connection admission, bounded backpressure/keepalive/idle/rate/drain controls, reconnect revision/event replay without gaps or duplicate mutations, and fault tests for malformed/truncated/slow/half-open/reorder/packet-loss/reconnect/protocol-skew/IPv4/IPv6/partition cases; rerun full workspace gate after unrelated asb-metrics mismatch is repaired or explicitly qualified.",
  "observed_branch": "feature/remote-control-transport",
  "observed_dirty": 1,
  "observed_head": "f5a0ef0342aee6d5b1a368b9703b5b2fb2e8dca7",
  "owner": "asb_ar0813_remote_transport",
  "plan": "../plans/AR-0813.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Carry the versioned frontend control API securely over IP without coupling runner lifetime to a client.",
  "task_revision": 106,
  "title": "Add secure remote control transport",
  "updated_at": "2026-09-16T14:54:00+00:00",
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
