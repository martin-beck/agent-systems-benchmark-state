# AR-1771 plan: human status and quiet-output contract

1. Inventory every public command, alias, early parse/usage path, routed TUI
   lifecycle path, interactive route, and raw/protocol entrypoint; record which
   ones own human operational output.
2. Specify one configurable output router that owns every ASB human/result write,
   safe writer destination configuration, writer failure behavior, and default
   stdout/stderr routing. Extend project-init configuration to persist level
   `normal` and its default routing without overwriting a user choice.
3. Specify closed `quiet`, `normal`, `verbose`, and `debug` levels, their
   project-config/command-line precedence, `-q` equivalence, bounded privacy
   policy, and the distinction between human routing and JSON output.
4. Specify a closed fixed-width token vocabulary, severity/state transitions,
   color policy, terminal and redirected-stream rendering, accessibility
   wording, and one-line operation rule.
5. Specify global `-q` / `--quiet` parsing and precedence in every option
   position, including failures before normal dispatch; retain prompts required
   by explicitly interactive commands and do not suppress the actual TUI.
6. Specify the strict `--json` boundary: no status, update, spinner, or progress
   bytes on either stream, unchanged JSON schemas, and unchanged exit codes.
7. Add contract tests for each parser/command family, router destination, project
   default, level, token width, color/no-color, quiet, JSON silence, privacy,
   stream ownership, and compatibility.
8. Update the user-facing command-output documentation and contributor contract;
   obtain independent review and exact-head evidence.
