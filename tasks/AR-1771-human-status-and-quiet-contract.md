---
{
  "branch": "feature/ar-1771-human-status-and-quiet-contract",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-10T11:34:37+00:00",
  "depends_on": [
    "AR-1768"
  ],
  "id": "AR-1771",
  "next_action": "AR-1771 output config seam is preserved uncommitted in crates/asb-config/src/lib.rs and schema/v1/project-config.schema.json; wait for AR-1763 exact config head, then rebase/merge the additive output section before committing. Continue isolated CLI/human routing tests only.",
  "observed_branch": "feature/ar-1771-human-status-and-quiet-contract",
  "observed_dirty": 4,
  "observed_head": "772bc46537b0574008635ebfc27d6b147c12c805",
  "owner": "ar1771-output-contract-terra",
  "plan": "../plans/AR-1771-human-status-and-quiet-contract.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "contract-test",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1771.json",
    "spec_revision": 2,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1771.json",
  "spec_revision": 2,
  "status": "in_progress",
  "summary": "Define one routed human-output vocabulary, levels, writers, and quiet contract without changing JSON or exit behavior.",
  "task_revision": 21,
  "title": "Human output, status, and quiet contract",
  "updated_at": "2026-10-10T09:39:22+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1771-human-status-and-quiet-contract"
}
---

Define the public operational-output contract for every ASB command before
implementing progress rendering. Add a global `-q` / `--quiet` option accepted in
every option position and command family. In human mode it suppresses all ASB
status, update, progress, warning, success, and failure presentation; it does
not change the command's effects, exit status, or structured result. Interactive
input needed to complete an explicitly interactive command and the launched TUI
application itself are not silently disabled; quiet only suppresses ASB's
lifecycle wrapper messages around that application.

Define one configurable output router and require every ASB-owned user-visible
result, diagnostic, status, update, warning, and progress write to use it. The
generated project configuration must persist an `output` section with level
`normal` by default and the default writer routing of ordinary result output to
stdout and human operational/diagnostic output to stderr. The configuration and
the router must support explicit safe writer destinations without allowing a
human output route to accidentally corrupt the machine-result stream. Define
documented precedence between project configuration and command-line overrides;
the output router remains the sole path regardless of the selected destination.

Define closed output levels `quiet`, `normal`, `verbose`, and `debug`. `quiet`
is the level selected by `-q`; `normal` is the generated-project default;
`verbose` adds useful non-sensitive operational detail; and `debug` adds bounded
development diagnostics without credentials, raw provider bodies, prompts, or
private host paths. Level selection must never alter command effects, result
schemas, or exit codes.

Every non-quiet human operational line must start with a fixed-width state marker:
`[ OK ]`, `[ERR ]`, `[WARN]`, `[WAIT]`, or another closed, documented four-cell
state. Green represents success, red errors/failures, yellow warnings/partial
states, and a sensible neutral/in-progress style represents waiting. ANSI styling
is used only when the human stream is a supported terminal; redirected output is
plain text with the same marker and wording. Lines remain concise, one logical
operation per line, accessible without color, and never disclose authentication material,
private paths, prompts, or provider payloads.

`--json` is a silent machine-output mode. It emits no human status lines, updates,
or progress bars on stdout or stderr, regardless of terminal detection or
configured human writers; stdout retains the existing versioned JSON contract
exactly. `-q --json` is valid and equivalent for operational output. Preserve
existing exit meanings, raw protocol commands, interactive prompts, and TUI
terminal ownership.

- 2026-10-10T09:29:30+00:00: AR-1768 is done with exact-head review and hosted evidence; promote
  output contract in parallel with catalog work.

- 2026-10-10T09:30:15+00:00: Claimed by ar1771-output-contract-terra.

- 2026-10-10T09:30:41+00:00: Recorded command exit 0; command argv SHA-256
  ff6d1fa7a7185010f75fcfafe4bdc1bdd5b9804d8c2b3e7abdd8a1b96cd81c63.

- 2026-10-10T09:30:50+00:00: Recorded command exit 0; command argv SHA-256
  22e8959654c0611947b6779be4c91bd3912ef67d0baea66d067a0c7acde50b69.

- 2026-10-10T09:31:29+00:00: AR-1768 is done; implementation is active in the declared worktree.

- 2026-10-10T09:31:32+00:00: Heartbeat by ar1771-output-contract-terra.

- 2026-10-10T09:34:33+00:00: Coordinator identified AR-1763 ownership overlap; no conflicting schema
  commit will be made.

- 2026-10-10T09:34:37+00:00: Heartbeat by ar1771-output-contract-terra.

- 2026-10-10T09:35:53+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-10-10T09:36:10+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-10T09:36:25+00:00: Recorded command exit 0; command argv SHA-256
  a62eac268a262b916bd76f885d2f1bc42037e4f49a237048da7e300ae129419e.

- 2026-10-10T09:37:04+00:00: Recorded command exit 101; command argv SHA-256
  434ba6f96c6ffe18116f45c4c43ce6f988135f2d706c438789163f67f218fbe4.

- 2026-10-10T09:37:07+00:00: Recorded command exit 101; command argv SHA-256
  434ba6f96c6ffe18116f45c4c43ce6f988135f2d706c438789163f67f218fbe4.

- 2026-10-10T09:38:23+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-10T09:38:32+00:00: Recorded command exit 101; command argv SHA-256
  434ba6f96c6ffe18116f45c4c43ce6f988135f2d706c438789163f67f218fbe4.

- 2026-10-10T09:39:12+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-10-10T09:39:22+00:00: Recorded command exit 101; command argv SHA-256
  434ba6f96c6ffe18116f45c4c43ce6f988135f2d706c438789163f67f218fbe4.
