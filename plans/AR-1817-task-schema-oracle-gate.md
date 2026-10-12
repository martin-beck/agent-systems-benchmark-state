# AR-1817 implementation plan

## Scope

1. Compare `schema/task-schema.json` with the supported `oracle_gate` contract
   in `schema/task-record.schema.json`, `tools/oracle_lifecycle.py`, and
   `tools/handoffctl.py`.
2. Add a bounded, explicit `oracle_gate` definition to the project task
   schema, including required fields, stage/event limits, artifact/event
   structure, and the optional human-session contract. Retain
   `additionalProperties: false` at every newly defined object boundary.
3. Add positive validation fixtures for the real AR-1811 and AR-1813 records
   and negative fixtures for unknown gate fields, malformed events, and
   unbounded event lists.
4. Update public contract documentation if the project schema is the
   downstream contract owner. Do not edit generated views directly.

## Validation and boundaries

- Run `uv run --frozen --offline python tests/validate_schema.py` and the
  focused schema/oracle tests, then the applicable full coordinator quality
  suite.
- Preserve exact unknown-field rejection, DCO/SSH signing, privacy checks,
  and generated-view consistency.
- This AR owns only state-schema compatibility. It must not modify AR-1816,
  product code, workflow gate requirements, or formal/TLC policy.
- Publish through the normal reviewed PR, exact-head CI, signed local
  integration, and post-merge doctor/reconciliation path.
