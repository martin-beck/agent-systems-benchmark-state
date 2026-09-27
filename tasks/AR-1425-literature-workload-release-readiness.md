---
{
  "branch": "",
  "checkpoint_commit": "6baa7acfb1cc3616c9737118a6345b1813b291f1",
  "claim_expires": "2026-09-27T11:27:47+00:00",
  "depends_on": [
    "AR-1424",
    "AR-1417",
    "AR-1418"
  ],
  "id": "AR-1425",
  "next_action": "Release done after independent audit; no successor required. Future native/official qualification remains separately gated.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "0000000000000000000000000000000000000000",
  "owner": "ar1332-record-replay-luna56",
  "plan": "../plans/AR-1425-literature-workload-release-readiness.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Independently verify release readiness of the complete built-in and literature workload surface.",
  "task_revision": 19,
  "title": "Literature workload release-readiness gate",
  "updated_at": "2026-09-27T09:29:26+00:00",
  "worktree_key": ""
}
---

This is a final audit and integration gate. It never requires live providers,
upstream dataset downloads, native hosts, or signed bundles for development
fixtures; those remain independently labeled evidence boundaries.

Its evidence table must cover the seven built-in software-engineering fixtures
plus SWE-bench Lite/Verified and Pro, Terminal-Bench, Aider Polyglot and
Exercism tracks, BigCodeBench, EvalPlus, LiveCodeBench, SWE-Lancer, SWE-rebench,
SWE-Perf, SWE-fficiency, CORE-Bench, AgentBench, tau-bench, and AgentDojo.
Harbor, Inspect AI, HAL, AgentOps, and HELM remain explicit non-workload
boundaries unless separately proven.

- 2026-09-27T09:17:19+00:00: AR-1424, AR-1417, and AR-1418 are done; promote independent full
  literature workload release-readiness audit.

- 2026-09-27T09:17:36+00:00: Claimed by ar1332-record-replay-luna56.

- 2026-09-27T09:19:00+00:00: Heartbeat by ar1332-record-replay-luna56.

- 2026-09-27T09:19:21+00:00: Recorded command exit 0; command argv SHA-256
  7f89bfbd11f4ca8df54390e7ebbe4b54efcbbc44076738596f5c512d5c85e617.

- 2026-09-27T09:19:49+00:00: Recorded command exit 0; command argv SHA-256
  bdaca9bf3f7580dbe5c50125ae88cde6aba63ba1a333ffb6bb5538b6d94f691a.

- 2026-09-27T09:20:20+00:00: Recorded command exit 0; command argv SHA-256
  d88aecf22363d9ceddca86ac049b6f237a73c3216d576b8c86506f6e3158e6c5.

- 2026-09-27T09:20:47+00:00: Recorded command exit 0; command argv SHA-256
  a177428c4fe8514d1cbc7d085999a18a0a93c3960cb4ff7b1b491797c2b901c9.

- 2026-09-27T09:21:20+00:00: Recorded command exit 0; command argv SHA-256
  e23eae41995c1a0fb986255cd1c8bf689586ddac91a975a346085a7d7253b6b3.

- 2026-09-27T09:21:44+00:00: Recorded command exit 0; command argv SHA-256
  cd9b53e4bb8e5a8622d366c3f21d6270b2c5ec3ad374fdee2956315fc976fe3d.

- 2026-09-27T09:22:41+00:00: Recorded command exit 0; command argv SHA-256
  5a5f232715fd709e348c52316be6c244f7efd7c17c53cc95f4b7252961468ad3.

- 2026-09-27T09:23:38+00:00: Heartbeat by ar1332-record-replay-luna56.

- 2026-09-27T09:24:29+00:00: Recorded command exit 0; command argv SHA-256
  6bd0d8281bee3e003b8663cf2e658388e747744550afddbfc33f003dff4cf1ec.

- 2026-09-27T09:25:22+00:00: Recorded command exit 0; command argv SHA-256
  024bf0e1493220c348b563cf32ab6e41d0dd0c558372bc17a6babb7a26881c84.

- 2026-09-27T09:26:31+00:00: Recorded command exit 0; command argv SHA-256
  31d007093a19582a7f04284e6885ec99dd3bad799dbf6f94e73c75dfc833600c.

- 2026-09-27T09:27:47+00:00: Heartbeat by ar1332-record-replay-luna56.

- 2026-09-27T09:28:09+00:00: Recorded command exit 0; command argv SHA-256
  661fbc98ac5efe6815800f9d378d9f67eca9a69134acc0bed93d9312816c0d6f.

- 2026-09-27T09:28:36+00:00: Recorded command exit 0; command argv SHA-256
  7494c67e63576e88249ee4e8dc156055ca13a4856ecdedef3573544d1703be88.

- 2026-09-27T09:29:26+00:00: Independent AR-1425 audit complete on clean isolated worktree exact
  origin/main 6baa7acfb1cc3616c9737118a6345b1813b291f1. Registry: 7 built-ins plus 22 external
  records; all documented families represented, methodology boundaries and unavailable reasons
  explicit, selectors fail closed. Focused Rust 35/35 asb-workloads lib + 4/4 public API; workload
  Python 36/36; catalog parity 5/5 and CLI parity passed; generated catalog SHA-256
  2ff05e9b06bc07bca986834b8213c19242c8efc557e76497280f5c21293108. Full serial workspace tests
  passed; fmt, clippy -D warnings, rustdoc -D warnings passed. Coverage passed: workspace 90.56%
  lines, critical asb-replay 96.52% and asb-core 99.61%, asb-workloads 93.44%. Privacy/redaction,
  strict replay, egress denial, negative paths and formal/release evidence covered by
  tests/current-main post-merge. AR-1424 current-main post-merge workflows green: Huawei 36308369609
  hosted 36308369648 credential-free 36308369573 fault 36308369579 formal 36308369594
  repository-quality 36308369618 Rust 36308369583 AArch64 36308369675. No
  product/asb-tui/live-provider change.
