---
{
  "branch": "feature/ar-1762-tool-discovery",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-09T18:40:34+00:00",
  "depends_on": [
    "AR-1759",
    "AR-1760"
  ],
  "id": "AR-1762",
  "next_action": "Add public API documentation to discovery module, rerun focused tests, then full gates.",
  "observed_branch": "feature/ar-1762-tool-discovery",
  "observed_dirty": 5,
  "observed_head": "ea5e52bfe843969c493f22146f66ccfa2415159a",
  "owner": "codex-asb-ar1762-tool-discovery-20261009",
  "plan": "../plans/AR-1762-tool-discovery.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "contract-test",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1762.json",
    "spec_revision": 1,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1762.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Auto-detect system-installed and project-configured ASB tools with deterministic diagnostics.",
  "task_revision": 41,
  "title": "Discover system and project ASB tools",
  "updated_at": "2026-10-09T15:50:46+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1762-tool-discovery"
}
---

Add a discovery command/API that scans configured project roots and system PATH
locations for known agents, harnesses, benchmarks, workloads, and support tools,
then merges them with project records. Report canonical path, kind, version,
capabilities, digest/availability, and a reason when unavailable. Discovery
must be deterministic, bounded, symlink/path safe, and must not overwrite the
configuration authority; live probes are allowlisted and warning-only when
development authentication/signatures/keys are absent.

- 2026-10-09T15:40:31+00:00: AR-1759 and AR-1760 accepted/released; dependencies verified for
  deterministic tool discovery

- 2026-10-09T15:40:34+00:00: Claimed by codex-asb-ar1762-tool-discovery-20261009.

- 2026-10-09T15:40:42+00:00: Recorded command exit 128; command argv SHA-256
  2b8452adb1cbcc0952c2f41b8b70232a83047aa768bbd7488006338526dde2ed.

- 2026-10-09T15:40:52+00:00: Recorded command exit 0; command argv SHA-256
  5345cd4b5f66285dc80cddfe59c0a95475263f9ff88d25d2639fce3c300aa4b9.

- 2026-10-09T15:41:07+00:00: Recorded command exit 0; command argv SHA-256
  156749639bcb11d86ef75ad637b668e71f48e845c32368d2c361047aafb3757e.

- 2026-10-09T15:41:18+00:00: Recorded command exit 0; command argv SHA-256
  2b8452adb1cbcc0952c2f41b8b70232a83047aa768bbd7488006338526dde2ed.

- 2026-10-09T15:41:23+00:00: Recorded command exit 0; command argv SHA-256
  bf795ab4a4e7de6c388d3af04e25fd72922ec79e8f19a28042f403ef2ef76d3b.

- 2026-10-09T15:41:32+00:00: Recorded command exit 0; command argv SHA-256
  628f1ff23cfb64b925600497c95e19845877dbe4b74cb107bdeeff9a68d6d055.

- 2026-10-09T15:43:30+00:00: Recorded command exit 1; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-09T15:43:43+00:00: Recorded command exit 0; command argv SHA-256
  27cc9c3bd0c4b3c18fe49e5dc258038875e791793f69b05c221ffabfac2d0776.

- 2026-10-09T15:43:54+00:00: Recorded command exit 101; command argv SHA-256
  ddc93c361d7a760463e5c5f2bf3d58c5587b3df1a23e9082b47dac26ddf72818.

- 2026-10-09T15:44:38+00:00: Recorded command exit 101; command argv SHA-256
  5719b1305347319cb9670126dde5b8aefd936841ab34dc44dd40df59a7e9e38a.

- 2026-10-09T15:44:49+00:00: Failure recorded: focused cargo test exited 101 because discovery had
  unused imports, DiscoverySource lacked Ord for deterministic sorting, and tool_discovery passed
  u64 where read_bounded_json requires usize. Patched all four issues; retry through handoffctl.

- 2026-10-09T15:44:56+00:00: Recorded command exit 0; command argv SHA-256
  27cc9c3bd0c4b3c18fe49e5dc258038875e791793f69b05c221ffabfac2d0776.

- 2026-10-09T15:45:10+00:00: Recorded command exit 101; command argv SHA-256
  5719b1305347319cb9670126dde5b8aefd936841ab34dc44dd40df59a7e9e38a.

- 2026-10-09T15:45:29+00:00: Retry failure recorded: Rust E0382 because configured.insert consumed
  the deterministic key before selected.insert. Clone the key at insertion; rerun through
  handoffctl.

- 2026-10-09T15:45:43+00:00: Recorded command exit 0; command argv SHA-256
  27cc9c3bd0c4b3c18fe49e5dc258038875e791793f69b05c221ffabfac2d0776.

- 2026-10-09T15:45:56+00:00: Recorded command exit 101; command argv SHA-256
  5719b1305347319cb9670126dde5b8aefd936841ab34dc44dd40df59a7e9e38a.

- 2026-10-09T15:46:11+00:00: Recorded command exit 0; command argv SHA-256
  27cc9c3bd0c4b3c18fe49e5dc258038875e791793f69b05c221ffabfac2d0776.

- 2026-10-09T15:46:36+00:00: Recorded command exit 0; command argv SHA-256
  5719b1305347319cb9670126dde5b8aefd936841ab34dc44dd40df59a7e9e38a.

- 2026-10-09T15:47:06+00:00: Recorded command exit 0; command argv SHA-256
  22cc58d2e0195269ed622987b99eb25451090f956bfdef5910e91d2445725e49.

- 2026-10-09T15:47:31+00:00: Recorded command exit 0; command argv SHA-256
  27cc9c3bd0c4b3c18fe49e5dc258038875e791793f69b05c221ffabfac2d0776.

- 2026-10-09T15:47:44+00:00: Recorded command exit 0; command argv SHA-256
  5719b1305347319cb9670126dde5b8aefd936841ab34dc44dd40df59a7e9e38a.

- 2026-10-09T15:48:14+00:00: Recorded command exit 0; command argv SHA-256
  27cc9c3bd0c4b3c18fe49e5dc258038875e791793f69b05c221ffabfac2d0776.

- 2026-10-09T15:48:38+00:00: Recorded command exit 101; command argv SHA-256
  2c773d075c9455062a72d0991af91dece7d496ef558436fc7e7ec9d898047b31.

- 2026-10-09T15:48:50+00:00: Full asb-cli test gate reached 254 passing tests but failed one
  unrelated control lifecycle test: control state root already owned at control.rs:7398.
  Discovery-specific tests passed. Classify by serial rerun before calling regression.

- 2026-10-09T15:48:55+00:00: Recorded command exit 0; command argv SHA-256
  b45c83268660fd13a393b0f63396bc006930e794a37c6011340f930ea2be0f71.

- 2026-10-09T15:49:09+00:00: Recorded command exit 0; command argv SHA-256
  832d375717d2abd9bc693482b0371f7f5842663c885ec9bbc6697c784fbf610f.

- 2026-10-09T15:49:39+00:00: Recorded command exit 0; command argv SHA-256
  27cc9c3bd0c4b3c18fe49e5dc258038875e791793f69b05c221ffabfac2d0776.

- 2026-10-09T15:49:46+00:00: Recorded command exit 1; command argv SHA-256
  ab1f7c499e6e269445892bbd708a6228559c89a99df0bd050ac3b894bfab6926.

- 2026-10-09T15:50:00+00:00: Test invocation failed with cargo usage exit 1 because two TESTNAME
  filters were supplied. No product failure; rerun each focused filter separately.

- 2026-10-09T15:50:09+00:00: Recorded command exit 101; command argv SHA-256
  62ef8d684d2d242b4241eec9f870d2300b4e9f4577ec87169e464167da61d100.

- 2026-10-09T15:50:27+00:00: Focused test retry stopped at compile gate: public discovery API lacked
  required rustdoc under workspace missing-docs policy (23 diagnostics). Added documentation for
  schema, source enum, report/entry fields, and discover function; no behavioral failure.

- 2026-10-09T15:50:34+00:00: Recorded command exit 0; command argv SHA-256
  27cc9c3bd0c4b3c18fe49e5dc258038875e791793f69b05c221ffabfac2d0776.

- 2026-10-09T15:50:46+00:00: Recorded command exit 101; command argv SHA-256
  62ef8d684d2d242b4241eec9f870d2300b4e9f4577ec87169e464167da61d100.
