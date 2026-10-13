# AR-1850 plan: development TUI interactive lifetime

1. Read the ASB and coordinator development documentation, claim an isolated
   exact-main worktree, and reproduce `asb tui` through the development
   broker on a disposable PTY for longer than the present 15-second deadline.
2. Separate bounded broker admission from normal interactive session lifetime.
   Retain finite timeouts for endpoint admission and failed startup, but keep a
   healthy foreground TUI alive until explicit quit, terminal signal, or a
   real control failure.
3. Preserve process-group ownership and cleanup. On explicit quit, error, or
   signal, reap the child and all broker workers without leaked sockets,
   descriptors, terminals, or processes.
4. Add deterministic positive PTY coverage that exceeds 15 seconds before a
   deliberate quit and negative coverage for startup/admission failure,
   unexpected child exit, signal cleanup, and broker-worker failure.
5. Run focused and workspace checks, exact paired TUI qualification, formatting,
   lint, privacy and process-cleanup checks. Obtain independent exact-head
   review, signed-DCO integration, required CI, merge, and post-merge PTY
   validation.

Done requires a healthy development TUI to remain interactive beyond the old
deadline and exit only by an explicit/real terminal lifecycle event, with no
leaked runtime artifacts.
