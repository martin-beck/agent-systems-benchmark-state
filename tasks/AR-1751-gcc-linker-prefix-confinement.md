---
{
  "branch": "repair/ar-1751-gcc-linker-prefix-confinement",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-09T02:16:21+00:00",
  "depends_on": [
    "AR-1737"
  ],
  "id": "AR-1751",
  "next_action": "Constrain development Cargo linker handoff so a validated ld cannot widen GCC helper or library trust through -B; add adversarial collect2/library regressions, independent exact-head review, signed reviewed-tree merge, and exact-main post-merge verification.",
  "observed_branch": "repair/ar-1751-gcc-linker-prefix-confinement",
  "observed_dirty": 0,
  "observed_head": "31ca7a481fca8b79bfbff126b92db6c6118beb7c",
  "owner": "codex-asb-ar1751-linker-confinement-20261009",
  "plan": "../plans/AR-1751-gcc-linker-prefix-confinement.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1751.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Confine the PATH-free development linker handoff to validated linker material without trusting sibling GCC helpers or libraries.",
  "task_revision": 5,
  "title": "Confine GCC linker-prefix trust after AR-1737",
  "updated_at": "2026-10-09T00:17:09+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1751-gcc-linker-prefix-confinement"
}
---

AR-1737 repaired env-cleared TUI source materialization by preserving one
`CARGO_ENCODED_RUSTFLAGS` channel and passing `-B<validated-ld-parent>` to the
validated GCC driver. PR #509 merged that repair as signed reviewed-tree commit
`9aeea48c40417108b95c0a2743b2d4b3220f56bd`; its exact post-merge workflows
are green and the original `collect2: cannot find ld` failure is resolved.

Independent follow-up review found that the accepted trust claim is broader
than the implementation proves. GCC treats `-B` as a general program and
library prefix, not an `ld`-only locator. When `ASB_DEV_LD` names an otherwise
valid current-user-owned private `ld`, an unvalidated sibling `collect2`,
compiler helper, startup object, or library may be selected from the same
directory. A bounded `cc -### -B<private-root>` reproduction selected a sibling
`collect2` and added the directory to `COMPILER_PATH`, `LIBRARY_PATH`, and
linker `-L` inputs. Existing AR-1737 tests reject malformed or untrusted `ld`
paths but do not exercise a trusted `ld` with hostile siblings.

This successor owns only that trust-confinement defect. It must preserve the
successful PATH-free materialization, absolute descriptor-bound Cargo/rustc/
compiler/archiver selection, deterministic remap flags, content-addressed
installation, and typed unsupported-driver behavior. Development
authentication, production signing, provider credentials, and release
qualification remain visible warning-only concerns and are not blockers.

The repair must not trust or execute a directory merely because one file in it
passed validation. Acceptable designs include a private materialized linker
tool directory whose complete executable and library closure is explicitly
validated and descriptor-bound, or a compiler/linker invocation that selects
the validated linker without introducing a general GCC prefix. The worker must
measure the real GCC invocation and prove the selected design, rather than
assuming `LD`, `-fuse-ld`, or a wrapper has narrower semantics.

- 2026-10-09T00:12:29+00:00: AR-1737 is done; independent follow-up reproduced GCC -B trust widening
  to unvalidated helper and library siblings, so this P0 repair is dependency-ready.

- 2026-10-09T00:16:21+00:00: Claimed by codex-asb-ar1751-linker-confinement-20261009.

- 2026-10-09T00:16:48+00:00: Recorded command exit 0; command argv SHA-256
  20d576e89aa897f3a625489c98c4d7b6954cbd9822989ab00bde278518c51dad.
