---
{
  "branch": "feature/ar-1775-configurable-output-router-and-levels",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-12T02:11:02+00:00",
  "depends_on": [
    "AR-1771"
  ],
  "id": "AR-1775",
  "next_action": "Implement the sole configurable output router, generated project output defaults, and four-level selection after the output contract is accepted.",
  "observed_branch": "feature/ar-1775-configurable-output-router-and-levels",
  "observed_dirty": 0,
  "observed_head": "6b5040e9366ac8f22db5a9fac84e634ff3ad0be4",
  "owner": "ar1775_output_router_luna56",
  "plan": "../plans/AR-1775-configurable-output-router-and-levels.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "contract-test",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1775.json",
    "spec_revision": 1,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1775.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Implement the mandatory configurable output router and project-configured quiet, normal, verbose, and debug levels.",
  "task_revision": 19,
  "title": "Configurable output router and levels",
  "updated_at": "2026-10-12T00:11:02+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1775-configurable-output-router-and-levels"
}
---

Implement the AR-1771 output contract before progress reporting. Add one typed,
injectable output router which is the mandatory path for all ASB-owned
user-visible output. It must route ordinary human result output and operational
diagnostic/status output to independently configurable safe writers, with stdout
and stderr respectively as the default. Project initialization generates and
persists the `output` configuration with `level = "normal"`; repeated project
initialization preserves an explicit user selection.

Implement the closed levels `quiet`, `normal`, `verbose`, and `debug`, their
documented project configuration and CLI override precedence, and `-q` as a
quiet-level override. Every writer implementation must apply the same level
filter and privacy rules. `debug` is development detail, never credential or
private-host disclosure. Error handling for an unavailable/unwritable configured
destination must be specific, use the AR-1766 diagnostic catalog, and preserve
the original command outcome where safe to do so.

Route all pre-existing ASB output through this router before adding new progress
behavior. JSON is not a configurable human writer: `--json` retains its exact
stdout envelope and silences all human/operational output on both streams.

- 2026-10-12T00:06:27+00:00: dependencies verified for AR-1771 output contract

- 2026-10-12T00:06:29+00:00: Claimed by ar1775_output_router_luna56.

- 2026-10-12T00:07:07+00:00: Recorded command exit 0; command argv SHA-256
  ff6d1fa7a7185010f75fcfafe4bdc1bdd5b9804d8c2b3e7abdd8a1b96cd81c63.

- 2026-10-12T00:07:16+00:00: Recorded command exit 0; command argv SHA-256
  6f52ce0c7898b7e55e2d170cf661b7d44de400623508709ffdb62da5ad64b573.

- 2026-10-12T00:07:41+00:00: Recorded command exit 0; command argv SHA-256
  02cc591d56e3010939553991eebb118f82c0e8914f17192b90f686fd06bea06e.

- 2026-10-12T00:07:53+00:00: Recorded command exit 0; command argv SHA-256
  b521e7adb975a1d0486e66f44a9d2815068ba644d4a4f2d1bd49e22614cf731f.

- 2026-10-12T00:10:01+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-12T00:10:12+00:00: Recorded command exit 0; command argv SHA-256
  4f646e73349b74d4faf9a332be2199303b571a9c860d080e8cfc68a8c14f526f.

- 2026-10-12T00:10:22+00:00: Recorded command exit 0; command argv SHA-256
  5dd93d8ec3ad6a09e07905badfbaf11feb36b0db03188443fd962a63b531cfda.

- 2026-10-12T00:10:32+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-12T00:10:39+00:00: Recorded command exit 0; command argv SHA-256
  77d0770c1a49ff91d840819deaee69c4dc8cfe61a3d8fc2453ceb16c91392360.

- 2026-10-12T00:10:43+00:00: Recorded command exit 0; command argv SHA-256
  efc4fd4dc5b2b8ae439ba62765b898592f7e600627a069c89a73f3068d8c3ad7.

- 2026-10-12T00:10:53+00:00: Recorded command exit 0; command argv SHA-256
  4d2c5b9c7612b59b9a4f7108fce19e037a51e255fb403ad31785375c7e40a45b.

- 2026-10-12T00:11:02+00:00: Heartbeat by ar1775_output_router_luna56.
