# AR-1757 plan: human-first ASB command output

## Outcome

Make the default `asb` command-line experience self-explanatory. A person should
understand the outcome, the few facts that matter, and the next action without
knowing ASB's JSON schema or internal state vocabulary. Preserve explicit JSON as
the complete stable automation interface.

## Design and implementation

1. Inventory every public command and meaningful outcome on exact current main,
   including help/version, doctor, setup, easy, capabilities and catalogs, plan,
   run, sweep, live benchmark, report, compare, recording/replay, completion,
   serve, and `asb tui` lifecycle routing. Record success, partial-result,
   warning, usage error, host limitation, product failure, and unavailable
   dependency cases. Add an exhaustiveness test so a new command or outcome
   cannot silently fall back to a raw object dump.
2. Define one presentation model separate from command execution and structured
   result types. It must carry a short outcome sentence, command-relevant facts,
   bounded warnings, and zero or one primary next action with an exact safe
   command. Renderers must not infer success from missing fields or reconstruct
   business decisions already owned by the typed result.
3. Replace the recursive JSON-to-`key: value` default renderer with command-aware
   presentations. Use plain language and stable layout: outcome first, relevant
   details second only when useful, and `Next: <command>` last only when action
   is required. Do not print `schema_version`, `ok`, `classification`,
   `development_only`, raw transport/network fields, internal digests, empty
   values, or repeated status labels unless the current command makes them
   directly useful.
4. Make failures actionable. State what failed and why, whether any state or
   artifacts changed, and the safest next command. Translate stable error codes
   into meaningful sentences while retaining the code in explicit JSON and,
   where useful, an opt-in verbose/details mode. Never suggest a command ASB does
   not implement, leak a credential into argv, or instruct a user to paste a
   secret.
5. Preserve automation and composability. `--json` and `--format json` retain
   schema, field semantics, ordering guarantees where documented, exit codes,
   stdout/stderr boundaries, and secret redaction. Non-interactive human output
   remains bounded and readable without color; optional terminal styling must
   respect `NO_COLOR`, redirection, and narrow terminals.
6. Update `--help`, quickstart, and command examples so every documented journey
   shows the expected concise outcome and the next command. Document how to get
   JSON and verbose diagnostic details without presenting those modes as the
   ordinary human path.

## Required tests

- Golden and semantic tests for every command family's representative success,
  warning, partial, usage, host, dependency, and product-failure outcomes.
- Assertions that required outcome/cause/next-action content is present and
  irrelevant envelope fields are absent from default output.
- Exact-command tests proving suggested commands parse and address the reported
  condition; terminal successes and non-actionable failures must not fabricate
  suggestions.
- Exhaustiveness coverage that fails when a new public command or result variant
  lacks an explicit human presentation.
- JSON byte/semantic compatibility tests, exit-code tests, stdout/stderr tests,
  redaction tests, bounded-output tests, redirected-output and `NO_COLOR` tests,
  plus representative terminal-width snapshots.
- A clean-install user journey through setup, selection, plan, local/mock run,
  report, compare, and TUI lifecycle routing in which each step explains the
  next supported command without exposing internal-only status.

## Integration

Use one isolated product worktree and signed+DCO commits. Require independent
review of the exact effective diff, all applicable exact-head hosted checks, the
documented signed reviewed-tree merge, all exact-main checks, and a privacy-safe
receipt containing before/after output examples without credentials or private
host paths.

