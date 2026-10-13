# Task-record schema vocabulary

`schema/task-record.schema.json` is the strict public record contract used by the coordinator.
Standard task metadata uses bounded identifiers, revisions, timestamps, branch/worktree
references, integer dirty-entry observations, and confined plan/spec references. Execution
reservations/results and retry-circuit records retain bounded digests, revisions, command classes,
and finite attempt histories.

Unknown fields are rejected at every execution, retry, and nested metadata boundary. Positive and
hostile examples are covered by `tests/test_task_record_schema.py`; this contract is data-only and
does not authorize subprocess execution or external side effects.
