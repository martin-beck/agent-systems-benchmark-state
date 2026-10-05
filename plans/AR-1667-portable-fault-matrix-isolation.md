# AR-1667 — portable fault-matrix network isolation

## Scope

Repair the ASB development fault-matrix runner so AR-1596 can execute on a
host where `unshare --net` is denied. This is test infrastructure only. The
runner must preserve fail-closed behavior and may not silently use the host
network.

## Implementation

1. Read the local development instructions and claim AR-1667 with one worker.
2. Refactor `tools/fault-matrix/run.py` around a closed isolation-backend
   enum. Keep direct `unshare --net` as the first backend.
3. Add an explicit `systemd-run --user --pipe --wait --collect` backend using
   `PrivateNetwork=yes` and `NoNewPrivileges=yes`, with a bounded unit name,
   private working directory, inherited exit status, and descendant cleanup.
4. Add an explicit bubblewrap backend using `--unshare-net` and
   `--die-with-parent`. Bind only the executable/runtime paths and the case
   workspace needed by the test; do not bind a writable host root or expose
   ambient HOME credentials.
5. Add a preflight for each backend that verifies a live loopback interface,
   rejects an external connection, and reports a typed unavailable result on
   failure. Backend selection must not accept arbitrary argv or shell syntax.
6. Preserve all existing timeout, output, workspace, process-group, cleanup,
   and typed classification behavior. Add receipt fields for backend and
   preflight evidence while keeping paths and environment values redacted.

## Verification

1. Run formatting, Python type/lint checks, and focused fault-matrix tests.
2. Run the five-case manifest with direct `unshare` where available.
3. Run the same manifest through an approved equivalent backend on a host where
   direct unshare returns EPERM; prove external network denial and cleanup.
4. Test explicit backend denial, malformed backend selection, timeout, output
   limit, workspace limit, descendant cleanup, and receipt redaction.
5. Commit signed and DCO-certified changes, open a PR, obtain independent
   review, wait for exact-head Repository Quality/AWQ checks, merge protected,
   and verify post-merge checks.
6. Attach the exact-head receipt to AR-1667 and use it to rerun AR-1596.

## Non-goals

- Do not disable user-namespace restrictions globally.
- Do not use `--network=host`, ambient host sockets, or an implicit fallback.
- Do not change ASB production runtime sandbox policy.
- Do not modify asb-tui source.
