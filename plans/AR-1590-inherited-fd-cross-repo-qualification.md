# AR-1590 — inherited-fd cross-repository qualification

Finish the ASB side of the real development broker journey after the
asb-tui PTY handoff seam is available. Launch the exact pinned asb-tui binary
through ASB's `launch_development_broker` path, capture and decode its actual
wire frames, and assert negotiation, ordered bootstrap/status calls, runner
identity, generation/revision/digest continuity, stale rejection, and all
failure cleanup paths.

The producer-side initial handoff must match the released TUI contract: the
frontend adopts an initial success packet carrying exactly one SCM_RIGHTS
control stream before it enters terminal setup. If the existing ASB router
waits for a descriptor-free child request, add a narrow typed producer-side
initial-generation seam in `asb-control` and test the parent-first packet
direction; do not bypass `BrokerState`, identity binding, or generation checks.

Keep the development route non-blocking for missing production credentials,
signatures, and key management; separately retain stable/production
fail-closed negatives. Every child, broker worker, socket, PTY, and temporary
root must have bounded cleanup.

Acceptance requires full immutable ASB/asb-tui source and tree identities,
non-ignored hosted execution, independent review, exact-head CI, and a
post-merge receipt. Do not accept an ASB-only client fixture as substitute
evidence.
