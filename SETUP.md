# Coordinator setup

Requires Python 3.12+, Git, GitHub CLI and the pinned uv quality environment.
Use a shared checkout for local worker locking. All workers use their own product
worktrees under the configured project root. The runtime config is ignored.

Create .runtime/config.json with private values for projects_root (absolute parent),
product_worktree (agent-systems-benchmark), github_repository
(martin-beck/agent-systems-benchmark), and push_enabled (true).
Set its directory mode to 0700 and file mode to 0600. Configure the Git name,
gmx.de email and SSH signing key locally; handoffctl commits with -S -s.

The product must have an origin/main before live reconciliation.
Run tools/handoffctl reconcile --commit --push, snapshot, then doctor --live.
Do not configure another project or its coordination service to use this database.

## Validation

```sh
uv sync --locked --only-group quality
uv run ruff format --check tools tests
uv run ruff check --no-fix tools tests
uv run mypy tools/handoffctl.py tools/status_renderer.py tests
uv run coverage run --branch -m unittest discover -s tests -p 'test_*.py'
uv run coverage report --fail-under=95
uv run python tests/validate_schema.py
tools/handoffctl render-status --check
tools/handoffctl doctor
```
