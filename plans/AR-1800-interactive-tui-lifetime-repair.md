# AR-1800 plan: interactive TUI lifetime and terminal restoration

1. Reproduce the installed development route in a disposable controlling PTY
   from exact ASB and asb-tui heads. Record only public-safe timing, typed
   outcome, process-group, and terminal-restoration observations.
2. Separate admission/handshake deadlines from the lifetime of an admitted
   interactive child. A healthy child remains foreground until it exits or an
   explicit cancellation/signal path terminates its private process group.
3. Preserve the AR-1727 foreground-group transfer/revalidation/restore and
   descendant teardown behavior. Do not weaken process identity, descriptor,
   broker-root cleanup, or terminal capability checks.
4. Make human and JSON diagnostics distinguish admission timeout, child exit,
   child lifetime cancellation, control failure, and terminal restoration
   failure. Never copy child stderr, credentials, prompts, or terminal
   transcripts into durable state.
5. Add deterministic controlling-PTY regressions: the route survives beyond
   15 seconds, accepts normal wizard input, exits on `q`, restores the caller
   foreground group/mode, and retains bounded hostile handshake, failed child,
   cancellation, and descendant-cleanup cases.
6. Run focused and full applicable ASB gates; require independent exact-head
   review, signed-DCO protected merge, exact-main CI, and a post-merge real
   installed-entrypoint PTY qualification before release.
