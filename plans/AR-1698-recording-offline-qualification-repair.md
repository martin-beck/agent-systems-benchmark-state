# AR-1698 current-head recording and strict offline qualification repair

Audit the existing ASB recording implementation at exact main
`ad43609b67825f7f422b371f5d8104e0a5b20f2e` and publish state evidence for the
planned AR-1652. Use only deterministic local fixtures and no provider
credentials.

The matrix must cover selected workload capture, all-workload campaign
expansion, redaction and content-addressed sealing, incomplete/duplicate or
mismatched capture rejection, durable publication/cleanup, strict offline
replay with network denied, human output, and explicit `--json` output. The
receipt must bind provider profile, agent, workload, scorer, cassette and
execution identities while exposing only opaque IDs and typed diagnostics.

If any predicate fails, report the exact backend gap and leave AR-1652
planned. If all predicates pass, accept AR-1698 and then reconcile AR-1652
through handoffctl using the digest-bound receipt; do not directly edit task
JSON or weaken replay/network gates.
