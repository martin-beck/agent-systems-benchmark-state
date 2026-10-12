---
{
  "branch": "repair/ar-1800-interactive-tui-lifetime",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1577", "AR-1727"],
  "id": "AR-1800",
  "next_action": "Promote and claim the reproduced installed-entrypoint repair; keep broker admission bounded while removing the interactive-child lifetime deadline.",
  "owner": "",
  "plan": "../plans/AR-1800-interactive-tui-lifetime-repair.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1800.json",
  "spec_revision": 1,
  "status": "planned",
  "summary": "Repair `asb tui` so a successful development broker session remains interactive until the user exits and always restores the terminal.",
  "task_revision": 1,
  "title": "Repair ASB interactive TUI session lifetime and terminal restoration",
  "updated_at": "2026-10-12T13:45:44+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1800-interactive-tui-lifetime"
}
---

The installed `asb tui` route opens the development TUI, then forcibly
terminates it after the broker's 15-second child deadline and reports a
generic terminal-interface launch failure. This is a regression of the
AR-1577 session-lifetime contract, not a provider or authentication failure.

Repair only the ASB launcher/broker boundary. Bounded deadlines remain valid
for setup, authenticated control admission, handshake, cancellation, and
cleanup; they must not bound a healthy interactive session. Preserve the
foreground-process-group and descendant-cleanup guarantees from AR-1727.
Classify child, broker, timeout, and terminal-restoration failures distinctly
in human and JSON output without exposing private child output.

The repair must exercise the real installed `asb tui` route in a controlling
PTY: keep it alive beyond the former deadline, perform a normal user exit, and
prove that the caller terminal is restored. Failure, cancellation, handshake,
and cleanup paths remain bounded and isolated.
