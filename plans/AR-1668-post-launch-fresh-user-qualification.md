# AR-1668 — post-launch fresh-user journey qualification

Run the complete exact-head install-to-analysis journey after AR-1667: install
the default `dev` channel, configure OpenRouter through the TUI wizard, select
opencode/opendesk and compatible models, persist shared defaults, benchmark,
record selected/all workloads, deny the network, replay offline, compare,
rollback, and remove. Record command transcripts, JSON and human output,
network-denial evidence, paired SHAs, and cleanup.

The asb-tui PR253 combined qualification runner is a candidate implementation
and evidence source only. Keep this AR planned until that PR has passed hosted
checks and merged, then rerun the receipt at the resulting exact ASB/TUI heads.
Development-only missing authentication, signatures, and key management are
explicit warnings and must never block this prototype journey.
