# AR-1614 — immutable development-channel bundle and installability

Provide and qualify the immutable TUI bundle consumed by the ASB `dev`
channel. The ASB install/router must resolve the channel manifest to an exact
published TUI source/binary, reject unavailable or mismatched artifacts with a
typed next action, and preserve the current configuration on upgrade,
rollback, and removal. A clean machine must be able to install the current
development channel without a pre-existing checkout.

Development mode may use generated local identities and a visible
development-only warning; missing production authentication, signatures, or
key-management services must never block this prototype path. Production
publication remains fail-closed on missing or mismatched immutable evidence.

Required evidence: immutable manifest and digest, clean-machine clone/build or
bundle install, current-head and version handoff, upgrade/rollback/remove
negatives, no-secret output, independent review, hosted checks, and exact-main
post-merge verification in both repositories.
