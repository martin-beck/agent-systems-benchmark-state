# AR-1727 — Development broker foreground-terminal repair

Repair the ASB development broker launch so its private child process group is
also the foreground group of the caller's controlling terminal for the full
interactive lifetime.

## Scope

- Capture and validate the caller's controlling terminal and exact foreground
  process group before spawning the development frontend.
- Spawn the frontend in its existing ASB-owned private process group, transfer
  foreground terminal ownership to that group, and restore the exact prior
  group after success, timeout, handshake failure, server failure, spawn
  failure, or cancellation.
- Keep descendant/process-group termination, child reaping, server joining,
  broker-root cleanup, identity binding, and stable launch behavior intact.
- Use audited safe library interfaces only; `unsafe` remains forbidden.
- Return typed development terminal/launch failures when foreground ownership
  cannot be established or restored. Never silently run an interactive child
  as a background terminal group.

## Required regression

Create a real session with a controlling PTY, invoke the actual
`launch_development_broker_with_backend` path, and prove all of the following:

1. the spawned development frontend's private process group becomes the PTY's
   foreground process group before interactive terminal I/O;
2. broker admission still completes through the real development path;
3. the prior foreground group is restored after the frontend exits;
4. failure/timeout cleanup still kills and reaps the private group and its
   descendants without signalling the caller's restored group.

The existing stable candidate-launch test and the asb-tui qualification
runner's synthetic non-controlling PTY do not satisfy this regression.

## Integration

Base the worktree on exact ASB `origin/main` and modify only the ASB product.
Do not absorb the separate asb-tui zero-size/controlling-PTY runner repair.
Require exact-head independent review, all applicable hosted checks, signed
merge integrity, post-merge CI, and then notify the asb-tui AR-1654 owner to
rerun the paired installed launch journey.
