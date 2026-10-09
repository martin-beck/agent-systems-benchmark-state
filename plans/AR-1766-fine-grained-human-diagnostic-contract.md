# AR-1766 plan: fine-grained human diagnostic contract

1. Inventory the exact current-main public command families, every `CliError`
   construction, backend-to-CLI mapping, TUI lifecycle code, result warning,
   filesystem operation, provider/transport failure, and partial outcome. Record
   current class/message, known cause, affected subject, mutation state, and
   recovery without copying private runtime data.
2. Define closed severity and cause enums. Keep `error` for rejected input or a
   command that could not begin, `failure` for an attempted operation that did
   not complete, and `warning` for a completed/continuing command with an
   important limitation. Preserve exit codes independently of wording.
3. Model fine-grained causes rather than broad buckets. Include typed resource
   roles and bounded safe context for user-facing paths/options/identities,
   operation phase, state change, and optional validated remediation.
4. Map filesystem, configuration, store, runtime, provider, control, tool,
   catalog, and TUI failures without discarding a known lower-level cause.
   Explicitly document where an unknown-cause fallback is unavoidable.
5. Keep machine JSON schemas and redaction stable. Human-only local context may
   identify a user-supplied or implicit destination, but must not enter public
   receipts, logs, or machine output unless its schema already permits it.
6. Add exhaustive enum/mapping, structured-context, severity/exit, and privacy
   tests before enabling downstream prose.

