---
{
  "branch": "feature/measurement-selection-plan",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-11T06:32:03+00:00",
  "depends_on": [
    "AR-0104",
    "AR-1036"
  ],
  "id": "AR-1037",
  "next_action": "After AR-1036, add canonical measurement IDs to validated ASB plans and make collection honor them without any UI code.",
  "observed_branch": "feature/measurement-selection-plan",
  "observed_dirty": 0,
  "observed_head": "6ef815144b8c23f4d0937c15f72fdecd93cfd767",
  "owner": "codex-root-ar1037-selection-20260911",
  "plan": "../plans/AR-1037.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Carry catalog-backed measurement choices through ASB plan validation, collection and evidence.",
  "task_revision": 56,
  "title": "Add measurement selection to validated run plans",
  "updated_at": "2026-09-11T04:14:24+00:00",
  "worktree_key": "agent-systems-benchmark-measurement-selection-plan"
}
---
## AR-1037

Implement only the ASB runner/control semantics required to make measurement choices real: closed
plan fields, catalog validation, canonical hashing, source gating and evidence provenance. All
search, group tri-state behavior, selection/deselection controls, rendering and help remain
exclusively in `martin-beck/asb-tui` under AR-1014.

- 2026-09-11T03:31:52+00:00: Dependencies AR-0104 and AR-1036 are done; fully green protected-main
  descendant 1a19b692 qualifies the catalog control boundary. Promote ASB-only measurement selection
  semantics with no frontend implementation.

- 2026-09-11T03:32:03+00:00: Claimed by codex-root-ar1037-selection-20260911.

- 2026-09-11T03:32:25+00:00: Recorded command exit 0; command argv SHA-256
  e93ce83471cb6810cbe793116d30cf552be146bcaee414eb9dd68d1b35c47e90.

- 2026-09-11T03:40:05+00:00: Recorded command exit 101; command argv SHA-256
  f8f5cfd8b7ce540eefbcf1ed8593289dcea998c3c67ea623a330a2542845d0e8.

- 2026-09-11T03:40:29+00:00: Recorded command exit 0; command argv SHA-256
  dc4208b7165aebbd5611033bf943ec0ee209e69a0410bd55afd62e8f31008cbd.

- 2026-09-11T03:41:28+00:00: Recorded command exit 1; command argv SHA-256
  0ea6fe112897f4953580feb3bbd086ea218eaea05048e5dfabc08e70b91b8c71.

- 2026-09-11T03:41:41+00:00: Recorded command exit 0; command argv SHA-256
  09c15c70d984c743b03913b5a4a636b645d98c882e9c14f86f69af03ba63b252.

- 2026-09-11T03:41:59+00:00: Recorded command exit 0; command argv SHA-256
  9ccfcfa9c389668cf5c8f871d8115e0a1d8e06c78ef5b3135f5f0f79d08664ab.

- 2026-09-11T03:45:25+00:00: Recorded command exit 101; command argv SHA-256
  476105f72caa4cc95ff415ef324a9ee1e1a12507c57629e7848ad27364dad583.

- 2026-09-11T03:46:13+00:00: Recorded command exit 0; command argv SHA-256
  476105f72caa4cc95ff415ef324a9ee1e1a12507c57629e7848ad27364dad583.

- 2026-09-11T03:46:43+00:00: Recorded command exit 101; command argv SHA-256
  baf579661282d83e638b954ec98e02553246afabb34f1d5c8487dd77135c9272.

- 2026-09-11T03:47:42+00:00: Recorded command exit 0; command argv SHA-256
  09c15c70d984c743b03913b5a4a636b645d98c882e9c14f86f69af03ba63b252.

- 2026-09-11T03:48:05+00:00: Recorded command exit 0; command argv SHA-256
  baf579661282d83e638b954ec98e02553246afabb34f1d5c8487dd77135c9272.

- 2026-09-11T03:49:42+00:00: Recorded command exit 101; command argv SHA-256
  1a30159cf316e006bd585fb4c6ea47760f8381910b664cd68ee3eb97f0cfba26.

- 2026-09-11T03:50:08+00:00: Recorded command exit 0; command argv SHA-256
  3f6b94c7ee5251023b9777cd611070f333030f05751c7ff6efc759f69f112bb5.

- 2026-09-11T03:50:24+00:00: Recorded command exit 0; command argv SHA-256
  84735ce5b140a26f41287c5e9470022eb54e2354bb57b1dc53154eda2deac183.

- 2026-09-11T03:50:45+00:00: Recorded command exit 101; command argv SHA-256
  effb686fd5ddcae8042cee59da0779f82e1f6dac9272213feae15475372b7d48.

- 2026-09-11T03:52:06+00:00: Recorded command exit 0; command argv SHA-256
  09c15c70d984c743b03913b5a4a636b645d98c882e9c14f86f69af03ba63b252.

- 2026-09-11T03:52:25+00:00: Recorded command exit 101; command argv SHA-256
  effb686fd5ddcae8042cee59da0779f82e1f6dac9272213feae15475372b7d48.

- 2026-09-11T03:54:43+00:00: Recorded command exit 0; command argv SHA-256
  09c15c70d984c743b03913b5a4a636b645d98c882e9c14f86f69af03ba63b252.

- 2026-09-11T03:54:59+00:00: Recorded command exit 0; command argv SHA-256
  66b605b717c5a7e0669e4c3b56b03e3292b60b93599cb2aac180bc48b4807143.

- 2026-09-11T03:56:53+00:00: Recorded command exit 101; command argv SHA-256
  090b850845d3902400b8dba91f08d8fd0686ea1771d7e661c10a4475f2c78c9d.

- 2026-09-11T03:57:37+00:00: Recorded command exit 0; command argv SHA-256
  090b850845d3902400b8dba91f08d8fd0686ea1771d7e661c10a4475f2c78c9d.

- 2026-09-11T03:59:42+00:00: Recorded command exit 0; command argv SHA-256
  2ae237e8bf230a319428216a20d8d44a784760418ac276e5456c7ba8a40e7b62.

- 2026-09-11T04:00:22+00:00: Recorded command exit 0; command argv SHA-256
  b261f2db642db5afa1636ea290ff223389d8206813eea15fee65fe9f83827b97.

- 2026-09-11T04:05:25+00:00: Recorded command exit 0; command argv SHA-256
  09c15c70d984c743b03913b5a4a636b645d98c882e9c14f86f69af03ba63b252.

- 2026-09-11T04:05:41+00:00: Recorded command exit 101; command argv SHA-256
  ab5db4159478c7bb637151e6412eb5eb2f80528493a4950e3d63fa25aaae3b50.

- 2026-09-11T04:06:01+00:00: Recorded command exit 101; command argv SHA-256
  ab5db4159478c7bb637151e6412eb5eb2f80528493a4950e3d63fa25aaae3b50.

- 2026-09-11T04:07:02+00:00: Recorded command exit 0; command argv SHA-256
  09c15c70d984c743b03913b5a4a636b645d98c882e9c14f86f69af03ba63b252.

- 2026-09-11T04:07:28+00:00: Recorded command exit 0; command argv SHA-256
  ab5db4159478c7bb637151e6412eb5eb2f80528493a4950e3d63fa25aaae3b50.

- 2026-09-11T04:07:50+00:00: Recorded command exit 101; command argv SHA-256
  effb686fd5ddcae8042cee59da0779f82e1f6dac9272213feae15475372b7d48.

- 2026-09-11T04:09:41+00:00: Recorded command exit 0; command argv SHA-256
  7a423e08b2040b2558c8d3853534387da26cd917d95acf109bb9ffd1f074085f.

- 2026-09-11T04:11:13+00:00: Recorded command exit 101; command argv SHA-256
  effb686fd5ddcae8042cee59da0779f82e1f6dac9272213feae15475372b7d48.

- 2026-09-11T04:12:14+00:00: Recorded command exit 0; command argv SHA-256
  09c15c70d984c743b03913b5a4a636b645d98c882e9c14f86f69af03ba63b252.

- 2026-09-11T04:12:45+00:00: Recorded command exit 101; command argv SHA-256
  effb686fd5ddcae8042cee59da0779f82e1f6dac9272213feae15475372b7d48.

- 2026-09-11T04:13:07+00:00: Recorded command exit 0; command argv SHA-256
  dc4208b7165aebbd5611033bf943ec0ee209e69a0410bd55afd62e8f31008cbd.

- 2026-09-11T04:13:29+00:00: Recorded command exit 0; command argv SHA-256
  3b7d06ce0619f0624c1733d6f57d0ca676bc5d886e1fee3b81496810a6408148.

- 2026-09-11T04:13:49+00:00: Recorded command exit 0; command argv SHA-256
  053f1638aa53c5bfb58c4b51315447c9fdf9a78d5d33c6434abc748067e78835.

- 2026-09-11T04:14:04+00:00: Recorded command exit 0; command argv SHA-256
  31d4ced0013afeccc0a324eed65c1f743d315f3888be3187f310d251d812d7a1.

- 2026-09-11T04:14:24+00:00: Recorded command exit 0; command argv SHA-256
  60a46a7cb90a6c7a92e02edcd2458c9019671d40611d3eb5f3dc6577cf91b660.
