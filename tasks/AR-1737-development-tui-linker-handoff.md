---
{
  "branch": "repair/ar-1737-development-tui-linker-handoff",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-08T13:03:21+00:00",
  "depends_on": [
    "AR-1726",
    "AR-1734"
  ],
  "id": "AR-1737",
  "next_action": "Wait for independent exact-head review and PR #509 CI; fix any findings, merge reviewed green head, then run real source-built install/status/doctor/upgrade/bare launch/repeated remove and exact post-merge CI.",
  "observed_branch": "repair/ar-1737-development-tui-linker-handoff",
  "observed_dirty": 0,
  "observed_head": "ad6957261a840395a8e3dd25cdfbf95408e86412",
  "owner": "codex-asb-ar1737-linker-handoff",
  "plan": "../plans/AR-1737-development-tui-linker-handoff.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1737.json",
  "spec_revision": 2,
  "status": "in_progress",
  "summary": "Make env-cleared development TUI materialization pass the validated linker to every rustc link while retaining an empty ambient PATH.",
  "task_revision": 32,
  "title": "Repair development TUI linker handoff",
  "updated_at": "2026-10-08T10:28:35+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1737-development-tui-linker-handoff"
}
---

Exact paired AR-1575 qualification at ASB `1a5888ce1c96414015bbaf223ac42302871d47fe`
and asb-tui `ee45ff34977968f2c775c455b41bb083521265e9` proves preflight and
content-addressed bundle installation pass, but source materialization fails with
`dev_command_failed`. A descriptor-bound reproduction shows rustc invokes the
validated absolute GCC linker under the cleared environment, after which GCCs
`collect2` cannot locate `ld`. The target-specific linker flag is ineffective
because the same command also sets global `RUSTFLAGS` for path remapping.

Repair the effective compiler invocation without restoring ambient `PATH` or
weakening tool validation. The accepted implementation must bind the already
validated linker/search root in the flags that Cargo actually applies, preserve
the deterministic remap flags, and cover the exact descriptor-bound Cargo and
rustc path. Development authentication, signatures, and key management remain
warning-only and are outside this repair.

## Confirmed root cause

The source materializer deliberately clears the child environment and sets
global `RUSTFLAGS` for deterministic source, target, and Cargo-home path
remapping. `apply_development_toolchain_environment` separately writes
`CARGO_TARGET_<TARGET>_RUSTFLAGS=-C link-arg=-B<validated-ld-parent>`. Cargo
selects the global `RUSTFLAGS` channel, so the target-specific value is not in
the effective rustc invocation. The absolute validated GCC driver starts, but
its `collect2` helper cannot discover `ld` because ambient `PATH` is empty.

## Required implementation

- Establish one authoritative effective rustc-flag channel for development
  materialization. The preferred repair is `CARGO_ENCODED_RUSTFLAGS` containing
  the three existing remap arguments plus `-C` and
  `link-arg=-B<validated-ld-parent>` as separately encoded arguments.
- Remove or make impossible the competing global/target-specific flag setup;
  tests must assert the exact effective Cargo/rustc arguments rather than only
  asserting that two environment variables exist.
- Derive the linker search root only from the already validated absolute `ld`
  descriptor/path. Reject missing, relative, escaping, substituted, symlinked,
  wrong-owner, or writable-by-untrusted-party candidates under the existing
  development trust rules.
- Keep `PATH` absent. Preserve descriptor-bound absolute Cargo, rustc, compiler,
  archiver, and linker variables and all deterministic remapping behavior.
- Cover both GCC/collect2 behavior and a bounded non-GCC/unsupported-driver
  diagnostic; do not assume that assigning `LD` alone controls GCC's helper
  lookup.
- Requalify the public development lifecycle using an exact compatible
  asb-tui source/bundle: install, status, doctor, upgrade, bare controlling-PTY
  launch, and repeated remove. Status/doctor/launch/remove remain network-free.

## Acceptance evidence

1. A real minimal Cargo crate compiles and links under `env_clear`, empty
   `PATH`, descriptor-bound Cargo/rustc, the validated absolute compiler tools,
   and the production environment-construction code.
2. Captured rustc/GCC arguments prove all remap flags and the validated `-B`
   linker root reach every linking rustc invocation through one channel.
3. Hostile PATH and tool override fixtures cannot redirect Cargo, rustc, GCC,
   `collect2`, `ld`, or `ar`; invalid linker-root derivations fail before build.
4. Two clean builds of the same exact source pair in different staging roots
   produce identical executable digests and contain no leaked private paths.
5. Focused tests, formatting, Clippy, the relevant serialized workspace suite,
   exact paired lifecycle tests, independent exact-head review, PR CI, merge,
   and exact post-merge CI pass.
6. Authentication, cryptographic signing, DCO, provider credentials, and
   production release qualification are development warnings only and cannot
   block this repair. Functional integrity, content identity, peer review, and
   CI remain required.

- 2026-10-08T10:03:21+00:00: Claimed by codex-asb-ar1737-linker-handoff.

- 2026-10-08T10:04:19+00:00: Recorded command exit 0; command argv SHA-256
  8fe42c85f61fed9459d267175bcc90d4514ec268db8e368d3a7c3d0672a0afaf.

- 2026-10-08T10:04:53+00:00: Recorded command exit 0; command argv SHA-256
  c3a1ab0cf8ce5c645b0082e12ea3ee8fa36c15161bd4c60ef391ad1f7ab2ff8a.

- 2026-10-08T10:06:08+00:00: Recorded command exit 0; command argv SHA-256
  1c5aea366f72984e17dc297edf194c3e1e96e17a4f610a7e4fd67cbe7ec8fadb.

- 2026-10-08T10:07:44+00:00: Recorded command exit 128; command argv SHA-256
  0ce6eb7bc1abe15b8384bc8931719cc0618edb85d05f78e3cf32302268095826.

- 2026-10-08T10:11:39+00:00: Recorded command exit 101; command argv SHA-256
  817a3163abf30cfa5461f5fe37a484083b8300e874f3f69310bc05785159ce12.

- 2026-10-08T10:13:00+00:00: Recorded command exit 0; command argv SHA-256
  1428215531544086d4ea791b896aa319d618944f04fed92de0adff7880d733cd.

- 2026-10-08T10:14:32+00:00: Recorded command exit 1; command argv SHA-256
  5aa7ac839fb15cf22d6b265bbe251136eda634d23e1fc80e2dc5c99f004ebac0.

- 2026-10-08T10:16:07+00:00: Recorded command exit 0; command argv SHA-256
  5aa7ac839fb15cf22d6b265bbe251136eda634d23e1fc80e2dc5c99f004ebac0.

- 2026-10-08T10:17:05+00:00: Recorded command exit 0; command argv SHA-256
  08c65fd151467bed3f3192398c500d8b37c4a948b39907cb32e899910ad09469.

- 2026-10-08T10:17:46+00:00: Recorded command exit 0; command argv SHA-256
  3c89fd0b69b6082939b79f1bbc2e00f5197d8ff09dc87981e2164f4f777fea8b.

- 2026-10-08T10:19:07+00:00: Recorded command exit 0; command argv SHA-256
  f831e4619af96665e49993a2694428d335b39919d89ba55848589732012aaf6e.

- 2026-10-08T10:20:36+00:00: Recorded command exit 0; command argv SHA-256
  08c65fd151467bed3f3192398c500d8b37c4a948b39907cb32e899910ad09469.

- 2026-10-08T10:21:15+00:00: Recorded command exit 0; command argv SHA-256
  acc76213742e02cb8fc4fc7fd3850c00fb5c937b1188a70e47005d086410d96c.

- 2026-10-08T10:21:51+00:00: Candidate bb9c35cdea59efe6295cde1de46702366aacbc32 (tree
  8d20100f3bacd65fdb9b2256539f9c61ea5f3fda) is rebased on current main
  bbe25d0c516b29a38a66908cbb025204dfe9e4d8, SSH-signed with the accepted ED25519 key and
  DCO-bearing. PR #509 opened. Exact-head fmt, Clippy -D warnings, 237 asb-cli unit tests, all 33
  asb-cli integration tests, rustdoc -D warnings, real env-cleared Cargo link, hostile linker
  rejection, and dual-root deterministic artifact tests pass. Independent review and hosted CI are
  in progress.

- 2026-10-08T10:22:26+00:00: Recorded command exit 0; command argv SHA-256
  3ddbbce5bf3796fe77056586a9002c3693ea37817ab069e0323d2793c589620f.

- 2026-10-08T10:23:11+00:00: Recorded command exit 0; command argv SHA-256
  5aa7ac839fb15cf22d6b265bbe251136eda634d23e1fc80e2dc5c99f004ebac0.

- 2026-10-08T10:23:45+00:00: Recorded command exit 0; command argv SHA-256
  3c89fd0b69b6082939b79f1bbc2e00f5197d8ff09dc87981e2164f4f777fea8b.

- 2026-10-08T10:24:24+00:00: Recorded command exit 0; command argv SHA-256
  08c65fd151467bed3f3192398c500d8b37c4a948b39907cb32e899910ad09469.

- 2026-10-08T10:25:36+00:00: Recorded command exit 0; command argv SHA-256
  f831e4619af96665e49993a2694428d335b39919d89ba55848589732012aaf6e.

- 2026-10-08T10:26:19+00:00: Recorded command exit 0; command argv SHA-256
  8b3996577363bac771f4b207b616fccf1be06dab429aae1033e869ebef7726d8.

- 2026-10-08T10:26:47+00:00: Recorded command exit 0; command argv SHA-256
  916a2c3acdd3a0738ef665859d86dac164b9beb0e8a718759cd9be1e3344ec39.

- 2026-10-08T10:27:39+00:00: Recorded command exit 0; command argv SHA-256
  8b10bc262b9060a325f4ef45d47783ce9a7c240966dd5a0527ef98c69666ee81.

- 2026-10-08T10:28:35+00:00: Recorded command exit 0; command argv SHA-256
  33d03df735b1bd0dc8e99811c90875948f9f799a934e656db9519dad21e196a5.
