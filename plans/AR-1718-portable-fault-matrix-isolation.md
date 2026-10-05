# AR-1718 — portable fault-matrix network isolation

## Scope

Repair the ASB development fault-matrix runner so AR-1596 can execute on a
host where `unshare --net` is denied. This is test infrastructure only; the
runner remains fail-closed and never silently uses the host network.

## Implementation

1. Claim AR-1718 with one worker after reading the development instructions.
2. Refactor `tools/fault-matrix/run.py` around a closed isolation-backend enum,
   retaining direct `unshare --net` as the first backend.
3. Add an explicit `systemd-run --user --pipe --wait --collect` backend with
   `PrivateNetwork=yes`, `NoNewPrivileges=yes`, bounded working directory and
   inherited exit status/cleanup.
4. Add an explicit bubblewrap backend with `--unshare-net` and
   `--die-with-parent`, binding only required runtime paths and the case
   workspace; never bind a writable host root or ambient HOME credentials.
5. Add a bounded preflight proving loopback exists and an external connection
   is denied. Reject arbitrary argv or shell syntax in backend selection.
6. Preserve timeout, output, workspace, process-group, cleanup, and typed
   classification behavior. Add backend/preflight fields to redacted receipts.

## Verification and integration

1. Run formatting, Python type/lint checks, and focused fault-matrix tests.
2. Run all five cases with direct `unshare` where available.
3. Run all five through an approved equivalent backend where direct unshare is
   EPERM, proving external denial and cleanup.
4. Test malformed backend selection, unavailable backends, timeout/output/
   workspace limits, descendant cleanup, and receipt redaction.
5. Commit signed+DCO, open a PR, obtain independent review, wait for exact-head
   Repository Quality/AWQ, merge protected, and verify post-merge checks.
6. Attach the exact-head receipt to AR-1718 and rerun AR-1596.

## Non-goals

- Do not globally disable user-namespace restrictions.
- Do not use `--network=host`, ambient host sockets, or implicit fallback.
- Do not change ASB production runtime sandbox policy or asb-tui source.
