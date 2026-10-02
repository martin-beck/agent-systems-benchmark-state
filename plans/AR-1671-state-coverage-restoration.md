# AR-1671 — ASB state strict coverage restoration

After AR-1670, run the complete state test suite and identify uncovered
behavior. Add deterministic tests for the restored authority, role, lifecycle,
rollback, handoff, oracle, and upgrade seams. Keep the configured 95% gate and
branch coverage unchanged, run all static/schema/source checks, and attach
independent review plus hosted evidence.
