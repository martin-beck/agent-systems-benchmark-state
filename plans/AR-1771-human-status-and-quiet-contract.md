# AR-1771 plan: human status and quiet-output contract

1. Inventory every public command, alias, early parse/usage path, routed TUI
   lifecycle path, interactive route, and raw/protocol entrypoint; record which
   ones own human operational output.
2. Specify a closed fixed-width token vocabulary, severity/state transitions,
   color policy, terminal and redirected-stream rendering, accessibility
   wording, and one-line operation rule.
3. Specify global `-q` / `--quiet` parsing and precedence in every option
   position, including failures before normal dispatch; retain prompts required
   by explicitly interactive commands and do not suppress the actual TUI.
4. Specify the strict `--json` boundary: no status, update, spinner, or progress
   bytes on either stream, unchanged JSON schemas, and unchanged exit codes.
5. Add contract tests for each parser/command family, token width, color/no-color,
   quiet, JSON silence, privacy, stream ownership, and compatibility.
6. Update the user-facing command-output documentation and contributor contract;
   obtain independent review and exact-head evidence.
