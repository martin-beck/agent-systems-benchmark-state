---
{
  "branch": "feature/live-provider-capture",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-0102", "AR-0502", "AR-0503", "AR-0314", "AR-1200"],
  "id": "AR-1201",
  "next_action": "Define the capture sidecar contract, implement ProviderCapture::capture for a real launch, and wire asb record live mode with redaction, replay-verification before seal, and mandatory cost/network acknowledgement.",
  "owner": "",
  "plan": "../plans/AR-1201.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Implement the runtime-owned capture path so asb record launches a real attempt against the pinned provider, intercepts provider-bound traffic, redacts and seals a cassette, and replay-verifies it before any durable write.",
  "task_revision": 1,
  "title": "Implement live provider capture (record) seam",
  "updated_at": "2026-09-22T09:39:55+00:00",
  "worktree_key": "agent-systems-benchmark-live-capture"
}
---
Implement the concrete runtime-owned capture path replacing `UnavailableProviderCapture`: a capture
sidecar (reverse of `loopback_sidecar.rs`) proxies provider-bound traffic, records semantic request/
response fields into `CassetteContents`, applies the redaction policy, seals the cassette, and runs
it once through `StrictReplayService` (network denied) before returning the digest. `asb record`
gains a live mode with mandatory cost/network acknowledgement. Repository:
`martin-beck/agent-systems-benchmark`.

- 2026-09-22T09:39:55+00:00: Defined from the record/replay/benchmark integration proposal.
  Depends on the process runtime (AR-0102), cassette and strict replay (AR-0502/AR-0503), source
  choice (AR-0314), and the pinned OpenRouter profile (AR-1200). The existing envelope-seal path
  must keep working.
