# AR-1372: Protected merge topology repair

## Objective

Repair the protected-main merge topology after AR-1371's squash merge produced
a one-parent commit, while changing no product behavior. Create a signed,
DCO-bearing no-op topology repair merge from the current protected `main` so
the Repository quality policy sees the required two-parent merge shape.

## Constraints

- Depend on the already merged AR-1371 content currently on protected main.
- Do not alter product files, gates, thresholds, or evidence policy.
- Use only the established handoffctl publication and protected merge workflow.
- Verify exact-head CI and all seven post-merge workflows before release.

## Acceptance

- Clean isolated worktree at current protected main.
- A signed+DCO topology-only repair commit/merge with no product diff.
- Repository quality and every required exact-head check green.
- Seven post-merge workflows for the repair merge terminal success.
- Durable evidence records the one-parent failure and repaired two-parent merge.
