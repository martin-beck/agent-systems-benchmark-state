# AR-1588 — ASB development-channel command surface

Complete the ASB-side user-facing channel selection contract after the channel
and materialization primitives. `dev` is the default for a fresh development
installation; an explicit channel remains selectable, and unsupported
stable/nightly/experimental channels fail with a clear typed response until
their contracts exist. Apply the same selection consistently to install,
status, launch, upgrade, remove, doctor, and help/JSON output without
silently changing an existing installation's channel.

Development mode may use generated local identity and signatures and must not
block on missing authentication, signature validation, or key management.
Stable/production paths remain fail-closed and unchanged.

Acceptance requires parser/help/JSON tests, fresh-state default tests,
existing-install preservation tests, unavailable-channel negatives, and exact
post-merge verification with signed provenance.
