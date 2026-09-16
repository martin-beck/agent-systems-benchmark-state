---
{
  "branch": "feature/remote-control-transport",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-16T16:20:05+00:00",
  "depends_on": [
    "AR-0702",
    "AR-0803",
    "AR-0902"
  ],
  "id": "AR-0813",
  "next_action": "Specify and implement an explicitly enabled authenticated remote transport for the frontend control API.",
  "observed_branch": "feature/remote-control-transport",
  "observed_dirty": 2,
  "observed_head": "cc9d4b3221c184c5e323a697ae1abce77d1413c3",
  "owner": "asb_ar0813_remote_transport",
  "plan": "../plans/AR-0813.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Carry the versioned frontend control API securely over IP without coupling runner lifetime to a client.",
  "task_revision": 15,
  "title": "Add secure remote control transport",
  "updated_at": "2026-09-16T14:26:30+00:00",
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
