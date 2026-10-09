# AR-1772 plan: unified human step-progress reporter

1. Design a small structured step API covering begin, work-total declaration,
   incremental update, message/detail update, warning/partial, success, failure,
   cancellation, and drop/interruption finalization.
2. Implement the one-second delayed renderer using an injectable monotonic clock
   and bounded refresh scheduler. It must avoid a transient line for sub-second
   steps and keep rendering live for longer steps even when a backend pauses.
3. Derive remaining-time estimates only from actual total/completed/rate data;
   use an explicit indeterminate bar plus elapsed time where no ETA is honest.
4. Implement fixed-width token/color output, terminal-width clipping, ANSI-safe
   redraw cleanup, redirected append-only lines, Unicode/control handling, writer
   failure behavior, and nested/sequential ordering.
5. Enforce construction only through the AR-1775 output router in human
   non-quiet/non-JSON mode and make JSON and quiet sinks no-op without spawning
   timers or emitting bytes.
6. Add deterministic fake-clock/unit tests and PTY/non-TTY tests for threshold,
   refresh, ETA, completion, failure, cancellation, unknown totals, width,
   color, privacy, and stream boundaries; document the mandatory API.
