---
{
  "branch": "fix/tmux-hosted-startup-readiness-recovery",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1064",
  "next_action": "Implement the bounded hosted-runner startup-readiness recovery in asb-tui tests/terminal_foundation.rs, then run exact Rust 1.93.0 gates and trusted-main.",
  "owner": "",
  "plan": "../plans/AR-1064.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Recover authenticated tmux startup observation on the hosted trusted runner without weakening authority or cleanup.",
  "task_revision": 1,
  "title": "Recover hosted tmux startup readiness",
  "updated_at": "2026-09-14T10:30:00+00:00",
  "worktree_key": "agent-systems-benchmark-asb-tui-tmux-hosted-startup-readiness-recovery"
}
---

The exact-main `asb-tui` Trusted-main run `34831918221` at `db612b6f` still fails five live tmux
fixtures during authenticated server observation (`socket_connect_rejected` /
`server_before_unavailable`). Local exact Rust 1.93.0 runs pass; a temporary uncommitted increase
from 100 to 500 bounded attempts made the local suite pass. This AR owns the smallest evidence-led
recovery and must prove it on the hosted runner.

- Repository: `martin-beck/asb-tui` only.
- Owned path: `tests/terminal_foundation.rs` only; no renderer, application, lifecycle protocol,
  dependency, release, workflow, or ASB source changes.
- Preserve socket ownership, peer credentials, process-generation checks, pane/TTY identity,
  revalidation, cleanup authority, closed error taxonomy, and zero-leak guarantees.
- Retry/readiness remains bounded and fail-closed; do not accept new error classes or weaken
  authentication. Add/adjust tests proving timeout bounds and hostile-path isolation.
- Acceptance requires exact signed DCO review, exact-head Repository quality and Trusted-main green,
  repeated local serial and parallel terminal suites, full Rust gates, privacy/schema/publication
  checks, and a clean worktree.

