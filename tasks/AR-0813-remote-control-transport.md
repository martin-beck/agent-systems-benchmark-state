---
{
  "branch": "feature/remote-control-transport",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-16T15:01:58+00:00",
  "depends_on": [
    "AR-0702",
    "AR-0803",
    "AR-0902"
  ],
  "id": "AR-0813",
  "next_action": "Specify and implement an explicitly enabled authenticated remote transport for the frontend control API.",
  "observed_branch": "feature/remote-control-transport",
  "observed_dirty": 3,
  "observed_head": "459867b0bd8b9ab97239fc11f9ee929f04f1c575",
  "owner": "asb_ar0813_remote_transport",
  "plan": "../plans/AR-0813.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Carry the versioned frontend control API securely over IP without coupling runner lifetime to a client.",
  "task_revision": 44,
  "title": "Add secure remote control transport",
  "updated_at": "2026-09-16T14:35:22+00:00",
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
