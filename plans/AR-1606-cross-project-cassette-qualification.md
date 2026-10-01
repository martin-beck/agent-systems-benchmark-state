# AR-1606 — cross-project cassette lifecycle qualification

Extend the existing ASB development ControlServer/PTY qualification harness
to exercise the paired TUI lifecycle against released ASB AR-1605: seed or
record and seal a cassette, close and reopen the backend, fetch the digest-only
catalog, select a cassette through the TUI route, dispatch strict offline
replay with provider egress denied, and feed the resulting run into comparison.

The fixture must bind runner, generation, campaign, provider profile, agent,
workload, cassette digest, and `offline_only`; malformed and stale selections
must return typed failures, and temporary resources must be cleaned up. It may
use the development backend's generated local authority and backend-seeded
cassette fixture, but must label that boundary as development-only and never
block on missing production authentication or key management.

Record exact ASB/TUI heads, binary/tree digests, commands, network-denial
evidence, comparison output, and cleanup evidence. This is a qualification
fixture, not a production security-hardening change.
