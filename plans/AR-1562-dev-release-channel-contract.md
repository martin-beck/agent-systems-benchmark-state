# AR-1562 implementation plan

Own the ASB-side channel enum, defaulting, CLI help, response metadata, and
fail-closed channel selection. Do not clone or build sources in this AR.

Acceptance: exact parser/output tests for every channel, default `dev`, explicit
unavailable-channel errors, and unchanged signed-channel behavior.
