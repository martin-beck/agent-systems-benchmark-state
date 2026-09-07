---
{"branch":"feature/emulated-aarch64-portability","checkpoint_commit":"","claim_expires":"","depends_on":["AR-0701","AR-0103"],"id":"AR-0707","next_action":"Provide a reproducible x86_64-hosted aarch64 VM/emulation lane for userspace portability and negative qualification only.","owner":"","plan":"../plans/AR-0707.md","priority":"P1","schema_version":1,"status":"planned","summary":"Add explicit emulated-aarch64 portability qualification without claiming native support.","task_revision":1,"title":"Qualify emulated aarch64 portability","updated_at":"2026-09-07T00:00:00+00:00","worktree_key":"agent-systems-benchmark-emulated-aarch64-portability"}
---
## AR-0707

Provide a reproducible x86_64-hosted aarch64 VM/emulation lane for userspace, protocol, adapter,
packaging, replay, and failure-path portability scenarios. Label every result `emulated-aarch64`.
Do not claim native kernel, timing, contention, architecture performance, openEuler/Debian boot,
or native hardware support. Keep native aarch64 capacity as future AR-0703 work with no dependency
from this AR.

Acceptance criteria:

- Pin emulator/VM, guest image, architecture, kernel, and toolchain provenance.
- Run bounded offline smoke, protocol, replay, packaging, and negative tests with deterministic cleanup.
- Prove host/guest distinction and fail closed when a native claim is requested.
- Publish a support matrix that separates emulated from native evidence and cost/latency limits.
