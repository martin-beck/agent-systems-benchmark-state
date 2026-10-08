---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1726", "AR-1734"],
  "id": "AR-1737",
  "next_action": "Reproduce the exact env-cleared development materializer failure, bind the validated linker search root in the effective Cargo/rustc flags, and requalify source-built install, upgrade, and bare launch without widening PATH.",
  "owner": "",
  "plan": "../plans/AR-1737-development-tui-linker-handoff.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1737.json",
  "spec_revision": 1,
  "status": "open",
  "summary": "Make env-cleared development TUI materialization pass the validated linker to every rustc link while retaining an empty ambient PATH.",
  "task_revision": 1,
  "title": "Repair development TUI linker handoff",
  "updated_at": "2026-10-08T04:19:50+00:00",
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
