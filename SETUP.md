# Coordinator setup

Requires Python 3.12+, Git, GitHub CLI and the pinned uv quality environment.
Use a shared checkout for local worker locking. All workers use their own product
worktrees under the configured project root. The runtime config is ignored.

The coordinator is pinned to signed upstream release v0.1.3. Run
`python tools/handoffctl_vendor.py verify --target .` before operating or upgrading it, and read
`docs/agent-workflow-coordinator.md` for the complete vendor workflow. `.handoffctl.json` and
`coordinator.binding.json` were created by the one-time initialization and must remain paired. The
tool fails closed if their immutable project UUIDs or repository identities differ, or if it is
called outside this state checkout and the configured product checkout. There is no supported
rebind operation.

Create .runtime/config.json with private values for projects_root (absolute parent),
product_worktree (agent-systems-benchmark), github_repository
(martin-beck/agent-systems-benchmark), and push_enabled (true).
Set its directory mode to 0700 and file mode to 0600. Configure the Git name,
gmx.de email and SSH signing key locally; handoffctl commits with -S -s.

The product must have an origin/main before live reconciliation.
Run tools/handoffctl reconcile --commit --push, snapshot, then doctor --live.
Do not configure another project or its coordination service to use this database.

Planned work is opened only after dependency and path review:

    tools/handoffctl promote AR-NNNN --expected-revision REVISION --note "dependencies and paths verified"

The command requires a clean, valid state checkout and atomically updates the task, CURRENT.md,
and graphical STATUS.md. After an ambiguous interruption, inspect the signed local commit and
remote ref before retrying; preserve a durable local transition and reconcile its replication.

## Validation

```sh
uv sync --locked --only-group quality
uv run ruff format --check tools tests
python tools/handoffctl_vendor.py verify --target .
uv run ruff check --no-fix tools tests
uv run mypy tools/handoffctl.py tools/status_renderer.py tests
uv run coverage run --branch -m unittest discover -s tests -p 'test_*.py'
uv run coverage report --fail-under=95
uv run python tests/validate_schema.py
tools/handoffctl render-status --check
tools/handoffctl doctor
```
