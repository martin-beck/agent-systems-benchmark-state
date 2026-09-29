# AR-1524 plan: live-dispatch graph repair

1. Read AR-1374, AR-1375, AR-1453 and AR-1523 completely and verify the
   dependency cycle against the current generated graph.
2. Use handoffctl state transitions to supersede AR-1375 as an obsolete
   duplicate and update AR-1374's next action to route through AR-1523.
3. Do not alter product code, claims, gates, leases, or historical evidence.
4. Reconcile, render-status check, and run live doctor. Record the exact state
   revision and the resulting acyclic routing.
