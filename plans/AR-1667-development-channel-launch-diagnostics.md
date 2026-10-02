# AR-1667 — development-channel launch diagnostics repair

Repair the ASB TUI launch dispatch so an active development channel remains
visible in pre-spawn errors when the user omits `--channel`. Add a real
subprocess regression for unsafe environment roots and verify explicit channel
selection, unavailable-channel negatives, PTY launch, and JSON/human output.
Run the full ASB quality and hosted checks at the exact signed head.
