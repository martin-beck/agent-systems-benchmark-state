---
{
  "branch": "feature/ar-1240-native-signed-bundle-fixture",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1238",
    "AR-1239"
  ],
  "id": "AR-1240",
  "next_action": "Extend native fixture invocation from helper lifecycle proof to authenticated cassette HTTP success plus provider/descendant denial and cleanup/non-interference matrix.",
  "observed_branch": "feature/ar-1240-native-signed-bundle-fixture",
  "observed_dirty": 0,
  "observed_head": "282eeffd78eaadbf706c90cb56a7ee1be29e77dc",
  "owner": "",
  "plan": "../plans/AR-1240.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "done",
  "summary": "Add native signed-bundle fixture and end-to-end supervisor isolation tests.",
  "task_revision": 17,
  "title": "Native signed-bundle supervisor fixture",
  "updated_at": "2026-09-16T08:40:51+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1240"
}
---

Own only native test fixture materialization and isolation evidence for the supervisor/sidecar
bundle. Preserve fail-closed behavior and all existing privacy and non-interference constraints.

- 2026-09-16T08:30:56+00:00: AR-1238 and AR-1239 are complete; begin native signed-bundle fixture
  and Bubblewrap isolation matrix.

- 2026-09-16T08:31:09+00:00: Claimed by asb_ar1240_native_fixture_worker.

- 2026-09-16T08:32:25+00:00: Created isolated /srv/data/projects/agent-systems-benchmark-ar-1240
  from e4c2e56; AR-1239 6836bb4 was already included (c03ad36). asb-bundle tests 18 offline verifier
  + 4 unit + 2 schema passed; sandbox native boundary 10 passed; bundle clippy passed. No native
  signed supervisor cassette matrix yet.

- 2026-09-16T08:32:48+00:00: Native Bubblewrap 0.9.0 probe with --unshare-all --unshare-user
  --unshare-net --disable-userns --cap-drop ALL --tmpfs /tmp --proc /proc passed: private route
  state and external 198.51.100.1 curl denial. Existing sandbox native boundary 10/10 passes. No
  host networking/firewall/ambient ip.

- 2026-09-16T08:36:44+00:00: Added signed commit 42bd8ed: native SandboxBackend invocation builds
  SHA-256 pins for supervisor/sidecar, binds a private Unix relay, and launches the supervisor under
  Bubblewrap; test passes. Sandbox boundary suite 11/11 plus helper invocation pass; Clippy green.
  Remaining matrix is real cassette forwarding and denial/cleanup assertions.

- 2026-09-16T08:37:58+00:00: Worker completed 42bd8ed helper lifecycle proof; remaining cassette
  HTTP, egress-denial, timeout/cancellation, and non-interference matrix cells require continued
  implementation.

- 2026-09-16T08:38:25+00:00: User-approved continuation: add remaining native cassette HTTP,
  egress-denial, teardown and non-interference matrix.

- 2026-09-16T08:38:28+00:00: Claimed by asb_ar1240_native_fixture_worker.

- 2026-09-16T08:40:51+00:00: Completed signed native fixture and authenticated cassette forwarding
  in 5fa5ee2 and 282eeff. Native SandboxBackend/Bubblewrap private namespace, SHA-256-pinned
  supervisor/sidecar, Unix relay, generation handshake, real HTTP cassette response, and sidecar
  teardown/reaping pass: native sandbox 12/12, cassette 1/1, bundle verifier 19/19, Clippy green.
  Remaining negative egress/failure lifecycle cells are isolated in follow-on AR-1241.
