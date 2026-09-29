# AR-1521 plan: formal AR-1307/1308 capacity repair

1. Read AR-1307, AR-1308, AR-1309, AR-1518 and AR-1520 completely and record
   the AR-1309 decision before modifying product code or runner scripts.
2. Implement only the selected, separately named capacity/model contract in an
   isolated product worktree. Never widen the original AR-1307 envelope or
   substitute the reduced development profile for full qualification.
3. Keep source, model/config, TLC/JDK, runner and profile digests exact; keep
   execution offline, networkless and host-mount-free with bounded process
   groups, admission fencing, cancellation and cleanup.
4. Add contract tests covering successful terminal evidence and fail-closed
   handling for missing/altered/stale inputs, Java OOM, timeout, disk pressure,
   concurrent admission, cleanup failure and full-vs-reduced claim mismatch.
5. Run focused tests, full state/formal/privacy gates, exact-head CI and an
   independent diff review. Publish and merge only from a clean exact head with
   signed+DCO commits; record all failures and next actions durably.

Exit evidence is an exact implementation commit and green required checks. A
nonterminal run remains a blocker for AR-1522 and cannot qualify AR-1307.
