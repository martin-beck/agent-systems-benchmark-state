# Public contract inventory

This inventory names tracked contracts that downstream projects may consume. Each entry is
strictly versioned and must reject unknown fields before a caller treats it as valid.

| Contract | Schema | Validator | Evidence |
| --- | --- | --- | --- |
| Coordinator role | `schema/role.schema.json` | `tools/role_registry.py` | `tests/test_role_registry.py` |
| Coordinator role registry | `schema/role-registry.schema.json` | `tools/role_registry.py` | `tests/test_role_registry.py` |
| Coordinator role assignment | `schema/role-assignment.schema.json` | `tools/role_assignment.py` | `tests/test_role_assignment.py` |
| Task specification | `schema/task-spec.schema.json` | `tools/task_spec.py` | `tests/test_task_spec.py` |
| Project task-spec evidence policy | `schema/task-spec-policy.schema.json` | `tools/task_spec.py` | `tests/test_task_spec.py`, `tests/test_handoffctl.py`, and `tests/test_sqlite_storage.py` |
| Human TUI gate session | `schema/task-record.schema.json#/$defs/humanSession` | `tools.oracle_lifecycle.py` | `tests/test_oracle_lifecycle.py`, `tests/test_handoffctl.py`, and `formal/oracle/OracleInteractionGates.tla` |
| Capability matrix formal contract | `formal/roles/CapabilityMatrix.tla` and `formal/roles/CapabilityMatrix.cfg` | `tools/capability_matrix_correspondence.py` | `tests/test_capability_matrix_formal.py` |

The role registry is descriptive authorization input. It does not itself authorize a mutation,
release, rollback, or Dispatch operation; those decisions remain owned by the Coordinator
runtime and its durable state.

The task-spec evidence policy is an optional, tracked file at the bound state repository root.
It can add bounded evidence-class names but cannot remove or reinterpret Coordinator's built-in
classes. The runtime captures one policy identity for each operation. Invalid, removed, dirty, or
racing policy input rejects before authority changes; the lifecycle model therefore observes the
same stuttering rejection as every other failed preflight guard.
