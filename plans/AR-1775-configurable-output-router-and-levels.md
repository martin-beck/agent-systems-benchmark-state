# AR-1775 plan: configurable output router and levels

1. Define typed output destination, logical stream, level, and mode types with
   explicit safe defaults and no direct writer access outside the router.
2. Extend the project configuration schema and `project init` generation to
   write `output.level = "normal"` plus default stdout/stderr routes; preserve
   explicit user configuration on repeat initialization and validate bad targets.
3. Implement configuration/CLI precedence, `-q` as quiet, and normal/verbose/
   debug filtering without changing command effects, JSON schemas, or exits.
4. Replace every existing ASB-owned user-visible write with the router, including
   early command errors and lifecycle adapters; retain required prompts and TUI
   process ownership.
5. Implement granular writer-destination diagnostics and safe writer failure
   behavior; ensure debug/detail data remains privacy-safe.
6. Add configuration migration, default, override, all-level, every-command,
   destination failure, stream, quiet, JSON-silence, and redaction tests; obtain
   independent exact-head review and hosted qualification.
