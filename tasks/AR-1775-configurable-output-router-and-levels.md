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
  "observed_head": "abe813338a1044a2497d8e7bd963651e26e8cf32",
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
  "task_revision": 49,
  "title": "Configurable output router and levels",
  "updated_at": "2026-10-12T00:16:28+00:00",
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

- 2026-10-12T00:11:48+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-12T00:11:58+00:00: Recorded command exit 0; command argv SHA-256
  f4520b357d6bfd4234077af14e37c2a6586e1467cc6d47d40c8247c1abe0094b.

- 2026-10-12T00:12:05+00:00: Recorded command exit 0; command argv SHA-256
  ac4700c11e22a6684072acc77b8e4e6a0a19aff604585310fd8a7b08d0329b08.

- 2026-10-12T00:12:10+00:00: Recorded command exit 0; command argv SHA-256
  7c3d026792488a1c316592919bf914e9005a149eb04c8de8a01edb5ef638ae62.

- 2026-10-12T00:12:14+00:00: Recorded command exit 0; command argv SHA-256
  582bb5233ca9e730842d6db1229c7c45304d57c065753cc5719653051c20b27b.

- 2026-10-12T00:12:21+00:00: Recorded command exit 0; command argv SHA-256
  77b31111479cace2f5afd7030468652263006fcb25c2f7d5fd5ff09d9c13498a.

- 2026-10-12T00:12:29+00:00: Recorded command exit 0; command argv SHA-256
  c2b8a89f6f2f4b09f24347be45d6f2dea1b1e2b6944a8e04727255bad37a27a8.

- 2026-10-12T00:12:36+00:00: Recorded command exit 8; command argv SHA-256
  45da4d961af9fbf5b24caaaf5d80af8c87aa7c1a83931c2d445d4486e51095d7.

- 2026-10-12T00:12:45+00:00: Recorded command exit 1; command argv SHA-256
  45da4d961af9fbf5b24caaaf5d80af8c87aa7c1a83931c2d445d4486e51095d7.

- 2026-10-12T00:12:52+00:00: Recorded command exit 0; command argv SHA-256
  4a1bbc018faaf407e480ced368ec0368f59059c0d963dddb52cb13a3c63398d6.

- 2026-10-12T00:13:00+00:00: Recorded command exit 0; command argv SHA-256
  321c534968b9c456a64caf5e6d09b63780c507f97548057d2bfe31edcfd73ff4.

- 2026-10-12T00:13:08+00:00: Recorded command exit 0; command argv SHA-256
  cd6b33e3f720979d83056e1a49b2146eb535e8df9d4d684c683e62453432edc0.

- 2026-10-12T00:13:15+00:00: Recorded command exit 1; command argv SHA-256
  427bb3b6ddcfa105221e2957627d3573c59c4ed1015b92ef9746d5403ff3e892.

- 2026-10-12T00:13:53+00:00: Recorded command exit 101; command argv SHA-256
  05c37d18f00754b5698295ca3bcf711ab28697a94b4c754da5c83c3e93af0f95.

- 2026-10-12T00:14:03+00:00: Recorded command exit 0; command argv SHA-256
  c9f46d9b132b62a71a13780302b72aaf184a013f66c4b0c05bf3799adedaaa38.

- 2026-10-12T00:14:04+00:00: Recorded command exit 101; command argv SHA-256
  d73b15a2495f19f934a37a5749ca6434845245f67ee6cbde94d0dd2f2dddc926.

- 2026-10-12T00:14:35+00:00: Recorded command exit 0; command argv SHA-256
  8307de8775d1c6087c63d267f5bb846d2fbf1524de6c1a24a39e09be91c71f39.

- 2026-10-12T00:14:42+00:00: Recorded command exit 101; command argv SHA-256
  c7d8e590f8ef999fa2490be403111205996be0057695dbc35d0ce2aa8e3de8cf.

- 2026-10-12T00:14:56+00:00: Recorded command exit 101; command argv SHA-256
  6f563bdb330330e731c7336858a58ee4dd81dea7b65c873357ce203593878f36.

- 2026-10-12T00:15:18+00:00: Recorded command exit 101; command argv SHA-256
  05c37d18f00754b5698295ca3bcf711ab28697a94b4c754da5c83c3e93af0f95.

- 2026-10-12T00:15:31+00:00: Recorded command exit 0; command argv SHA-256
  61f0ac545a7623e44605082d0271e645a293b32abded0fa007581e2b0c9830ce.

- 2026-10-12T00:15:41+00:00: Recorded command exit 101; command argv SHA-256
  05c37d18f00754b5698295ca3bcf711ab28697a94b4c754da5c83c3e93af0f95.

- 2026-10-12T00:15:48+00:00: Recorded command exit 0; command argv SHA-256
  e2a97165c2c516deb6bf2c8e0030f49b5ac28f2fec75ed32dbb8622048bc79fe.

- 2026-10-12T00:16:17+00:00: Recorded command exit 101; command argv SHA-256
  d91c2649c524d82675e801e0e44707c8fe1d61ac2fa191c5a5c1006f1c7e6d37.

- 2026-10-12T00:16:28+00:00: Recorded command exit 0; command argv SHA-256
  f9198eaeeff480fed15c18e9abdda0a05e31515024b2f0b35392ef12fc376354.
