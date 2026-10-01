# AR-1590 — inherited-fd cross-repository qualification

Finish the ASB side of the real development broker journey after the
asb-tui PTY handoff seam is available. Launch the exact pinned asb-tui binary
through ASB's `launch_development_broker` path, capture and decode its actual
wire frames, and assert negotiation, ordered bootstrap/status calls, runner
identity, generation/revision/digest continuity, stale rejection, and all
failure cleanup paths.

Keep the development route non-blocking for missing production credentials,
signatures, and key management; separately retain stable/production
fail-closed negatives. Every child, broker worker, socket, PTY, and temporary
root must have bounded cleanup.

Acceptance requires full immutable ASB/asb-tui source and tree identities,
non-ignored hosted execution, independent review, exact-head CI, and a
post-merge receipt. Do not accept an ASB-only client fixture as substitute
evidence.
