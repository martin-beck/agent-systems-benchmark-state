---
{
  "branch": "feature/ar-1771-human-status-and-quiet-contract",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1768"
  ],
  "id": "AR-1771",
  "next_action": "After AR-1768 is done, define the closed human status, output-router, level, quiet, stream, and compatibility contract for every ASB command.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
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
  "status": "open",
  "summary": "Define one routed human-output vocabulary, levels, writers, and quiet contract without changing JSON or exit behavior.",
  "task_revision": 3,
  "title": "Human output, status, and quiet contract",
  "updated_at": "2026-10-10T09:29:30+00:00",
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
