---
{
  "branch": "feature/ar-1745-user-local-install-prefix",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-08T15:06:58+00:00",
  "depends_on": [
    "AR-1740"
  ],
  "id": "AR-1745",
  "next_action": "Record completion receipt, release AR-1745 done, and reconcile live state.",
  "observed_branch": "feature/ar-1745-user-local-install-prefix",
  "observed_dirty": 0,
  "observed_head": "250ef6658e0cdaa3d8cea53bb009a0bbd88787d4",
  "owner": "codex-ar1745-install",
  "plan": "../plans/AR-1745-user-local-install-prefix.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "contract-test",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1745.json",
    "spec_revision": 1,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1745.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Make ASB development installation place the asb executable at the invoking user's $HOME/.local/bin/asb by default, with a safe explicit prefix override.",
  "task_revision": 25,
  "title": "Install ASB into the invoking user's local bin",
  "updated_at": "2026-10-08T13:48:45+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1745-user-local-install-prefix"
}
---

The current Make install workflow must be easy for a fresh user and must not
assume root access or place a user's development binary in a system prefix.
By default, `make install` (and any ASB command implementing the same install
contract) shall install `asb` at `$HOME/.local/bin/asb` for the user performing
the install. A caller may provide an explicit safe prefix for packaging or CI.

The implementation must not silently write outside the selected prefix, must
not alter unrelated TUI/runtime installation semantics, and must provide
clear PATH guidance when `$HOME/.local/bin` is not already on PATH.

- 2026-10-08T13:06:55+00:00: Promote high-priority user-local install-prefix AR after dependency
  audit; AR-1740 is done and exact current main shows repository-local .make/install default.

- 2026-10-08T13:06:58+00:00: Claimed by codex-ar1745-install.

- 2026-10-08T13:16:35+00:00: Recorded command exit 0; command argv SHA-256
  68b1e285b99377f1949df050e1627e23e2da5bfead27496d90d8802ed77c0ef7.

- 2026-10-08T13:17:43+00:00: Recorded command exit 0; command argv SHA-256
  68b1e285b99377f1949df050e1627e23e2da5bfead27496d90d8802ed77c0ef7.

- 2026-10-08T13:18:17+00:00: Recorded command exit 0; command argv SHA-256
  77538cc8cd1f66303ff8c9157cf959d2a4f0871db47d4ea873814d834700e7f3.

- 2026-10-08T13:18:51+00:00: Recorded command exit 0; command argv SHA-256
  44784fdedea78ea85acbf5061372cfb59a2221a33950ccc933153571fa62ff31.

- 2026-10-08T13:20:46+00:00: Recorded command exit 2; command argv SHA-256
  3fc122cf075789d0bc02db7fd32de1be63709d388a5a8cb44f03ddbc0ae0dfb6.

- 2026-10-08T13:21:55+00:00: Recorded command exit 0; command argv SHA-256
  68b1e285b99377f1949df050e1627e23e2da5bfead27496d90d8802ed77c0ef7.

- 2026-10-08T13:22:30+00:00: Recorded command exit 0; command argv SHA-256
  e0625d493101da8b6bf211fff8be801b798bee0a8bcd7018ae8ac48f319ddd78.

- 2026-10-08T13:23:21+00:00: Recorded command exit 0; command argv SHA-256
  31615385e59695400741f4436f46d12a893be41c3c5e31931fa259bd475f9229.

- 2026-10-08T13:24:23+00:00: Recorded command exit 0; command argv SHA-256
  68b1e285b99377f1949df050e1627e23e2da5bfead27496d90d8802ed77c0ef7.

- 2026-10-08T13:24:57+00:00: Recorded command exit 0; command argv SHA-256
  7615bfc80d34a9418ffec2e6c81474e464a5880faebcbb8c633d99829db4866d.

- 2026-10-08T13:25:39+00:00: Recorded command exit 0; command argv SHA-256
  31615385e59695400741f4436f46d12a893be41c3c5e31931fa259bd475f9229.

- 2026-10-08T13:26:42+00:00: Independent review approved exact head
  250ef6658e0cdaa3d8cea53bb009a0bbd88787d4. Focused tests and diff-check pass; symlink install and
  cleanup escapes are covered.

- 2026-10-08T13:26:53+00:00: Recorded command exit 0; command argv SHA-256
  593d8ebfb614a13bcdfbdf7a15f2caa65ab5a02ce8e848adfabfb0f7eeef9134.

- 2026-10-08T13:37:22+00:00: Recorded command exit 0; command argv SHA-256
  e54079976049d8b5a885a7fca1ad256ce7620a590256c4a86487f95aef8f9d65.

- 2026-10-08T13:48:45+00:00: PR #512 merged as signed protected-main merge 1ab175c3. Exact
  tree/parents, signature/DCO, local policy, focused tests, independent review, and all nine
  post-merge workflows passed.
