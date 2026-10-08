# AR-1737 plan: development TUI linker handoff

1. Reproduce the development materializer build with an empty ambient `PATH`,
   descriptor-bound Cargo and rustc, validated absolute compiler/linker tools,
   and the exact reproducibility flags.
2. Ensure the effective rustc flags retain deterministic path remapping and
   direct the validated GCC driver to the validated linker search root; do not
   add an ambient or user-controlled `PATH`.
3. Add positive descriptor-bound build coverage and hostile override/path
   negatives, then run focused TUI lifecycle and serialized workspace gates.
4. Requalify exact paired source-built `asb tui install`, offline status/doctor,
   upgrade, bare controlling-PTY launch, and removal. Require independent
   review, signed+DCO integration, and terminal-green exact-main CI.
