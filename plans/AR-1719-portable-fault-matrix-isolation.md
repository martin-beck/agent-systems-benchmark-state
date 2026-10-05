# AR-1719 — portable fault-matrix network isolation repair

This is the durable AR for PR #487 after AR-1718 was concurrently reused for
an unrelated OpenRouter catalog task.

The worker must preserve the closed backend abstraction, loopback/external
network preflight, bounded process/output/workspace cleanup, typed unavailable
behavior, and redacted backend receipt. Direct `unshare --net` remains first;
approved equivalents are `systemd-run --user` with `PrivateNetwork=yes` and
`bwrap --unshare-net --die-with-parent`. No host-network fallback is allowed.

Verification is: focused tests; five-case matrix through bubblewrap or systemd
on this EPERM host; signed+DCO PR #487; independent review; exact-head hosted
checks; protected merge; post-merge checks; and an AR-1596 matrix-linked receipt.
