# ASB task schema extensions

The ASB state repository extends the coordinator task record with an optional,
strict `oracle_gate` field. The field is used by the existing lifecycle records
and is validated by `schema/task-schema.json`.

An oracle gate requires `required: true`, `open_stage`, `completed`, and
`events`. Stage names and lifecycle dispositions are enumerated; event lists,
artifact references, and discussion rounds are bounded. Artifact references
contain only a public-safe reference and a SHA-256 digest. The optional
`human_session` object is bounded and requires a close timestamp when its
status is resolved or clarification is requested.

Every object in this extension rejects unknown fields. Use
`tools/oracle_lifecycle.py` for lifecycle semantics; do not loosen the schema
to accept unrecognized gate or event data.
