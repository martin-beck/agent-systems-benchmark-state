---
{
  "branch": "codex/ar-1421-protected-main-race",
  "checkpoint_commit": "10b16186c8424f53f6d6d8c2797d785dea10c53b",
  "claim_expires": "2026-09-24T22:05:02+00:00",
  "depends_on": [
    "AR-1416",
    "AR-1398"
  ],
  "id": "AR-1421",
  "next_action": "PR #308 merged as 10b16186. Monitor exact-main post-merge workflow IDs 36052764434,36052764446,36052764452,36052764458,36052764507,36052764675,36052764433 to terminal SUCCESS; then verify merged tree/signature/DCO and release.",
  "observed_branch": "codex/ar-1421-protected-main-race",
  "observed_dirty": 0,
  "observed_head": "28e35608a2a87f53afa70732ca1b51aa57aa360b",
  "owner": "ar1421-protected-main-race-luna56",
  "plan": "../plans/AR-1421.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Repair protected-main merge-tree requalification after a literature PR merges onto an advanced main.",
  "task_revision": 71,
  "title": "Protected-main literature merge race repair",
  "updated_at": "2026-09-24T20:16:19+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1421"
}
---

The failed post-merge Repository Quality result is preserved as evidence. This AR
must not waive the exact-tree check, add a commit-specific exception, or classify
the merge released before fresh exact-main evidence succeeds.

- 2026-09-24T19:36:35+00:00: Incident evidence recorded in AR-1417; completed AR-1416 and AR-1398
  permit this independent repair while AR-1417 remains open.

- 2026-09-24T19:37:03+00:00: Claimed by ar1421-protected-main-race-luna56.

- 2026-09-24T19:37:29+00:00: Heartbeat by ar1421-protected-main-race-luna56.

- 2026-09-24T19:37:51+00:00: Heartbeat by ar1421-protected-main-race-luna56.

- 2026-09-24T19:44:24+00:00: Heartbeat by ar1421-protected-main-race-luna56.

- 2026-09-24T19:44:27+00:00: Recorded command exit 0; command argv SHA-256
  ff6d1fa7a7185010f75fcfafe4bdc1bdd5b9804d8c2b3e7abdd8a1b96cd81c63.

- 2026-09-24T19:44:52+00:00: Recorded command exit 0; command argv SHA-256
  2a6a5eca83c9f6060f288863588c33f1bbe35a8c6ac82db701c4ff8d4945b470.

- 2026-09-24T19:45:09+00:00: Recorded command exit 0; command argv SHA-256
  f9da2774b0df6431e804390585d848213c1e084b6f27b387a9a56d0be3fc4244.

- 2026-09-24T19:45:23+00:00: Recorded command exit 0; command argv SHA-256
  37c422c5bbac4dcd43eb3d0efafdb22cff608963502aeae8ac7e01b35af4809a.

- 2026-09-24T19:45:42+00:00: Recorded command exit 0; command argv SHA-256
  81651cc4c7f4ab1eb97b677d5d71989a56646776147d75eb43936ade3ec75a46.

- 2026-09-24T19:46:08+00:00: Recorded command exit 0; command argv SHA-256
  e5107e4d1283679910bc2ca2dfc677d1fd756367e9fd1b0ba3bfc5a917329bbe.

- 2026-09-24T19:46:30+00:00: Recorded command exit 0; command argv SHA-256
  377d90cefb534c83f4e4c93fc8d9b8969fdeadc9665c7668d3b61fccdfe87005.

- 2026-09-24T19:46:48+00:00: Recorded command exit 0; command argv SHA-256
  bb352b8e6baaddb9d3de402a3dca1a4aa0b06e91398cb92d40b2064099f0a696.

- 2026-09-24T19:47:05+00:00: Recorded command exit 0; command argv SHA-256
  a36cec07c42242108d530dc4de4a288507e9548109c0918e6f0160654ffc253d.

- 2026-09-24T19:47:19+00:00: Recorded command exit 0; command argv SHA-256
  453ec73d1508d8ad13f8ad10dd3b1dd19b1d5365c8ec56b6add85677253d9b5c.

- 2026-09-24T19:47:38+00:00: Recorded command exit 0; command argv SHA-256
  5666b0a050fc97aa1b3fb26da72b4058350b85ff0e5081b15c12b7ef21d4e3f3.

- 2026-09-24T19:47:53+00:00: Recorded command exit 0; command argv SHA-256
  f407f0389c6d949f3e23f14e21f6a17725297cde91e83383fd75e298011832ce.

- 2026-09-24T19:48:07+00:00: Recorded command exit 0; command argv SHA-256
  3c752766688dda4842b1f16d9fb5e7700ea8a524ad7178c582386c727bd898d0.

- 2026-09-24T19:48:21+00:00: Recorded command exit 0; command argv SHA-256
  7ca3f8d61e2724c7888011b1b015c9a61f815ada816215c678cf52a474d1c159.

- 2026-09-24T19:48:35+00:00: Recorded command exit 0; command argv SHA-256
  5c700772f4437bb137c3c4cf213e01722448be53f7a262c3178f666f972b3f0c.

- 2026-09-24T19:49:05+00:00: Recorded command exit 0; command argv SHA-256
  37c945926dce37d768e534841d48c838be363f6e73478e6ce54e0b688c1c0b06.

- 2026-09-24T19:49:33+00:00: Recorded command exit 0; command argv SHA-256
  777a80a312429ffa170d3c0e8e2bad0aa71faa1921d85504ceb3f95fdf87417b.

- 2026-09-24T19:50:35+00:00: Recorded command exit 2; command argv SHA-256
  48458d4adcbc2714c4ae60f17ec39d916357031118af6e75d9a5cd826c73f20e.

- 2026-09-24T19:51:14+00:00: Recorded command exit 2; command argv SHA-256
  bee40bf64c130e3c330871e64c32e88a5867ff88fc19d4edaa346166fc6a272f.

- 2026-09-24T19:52:10+00:00: Recorded command exit 0; command argv SHA-256
  228192cc7894e8b9c93b36bdb07fa5be1c74657147d75c44e1e2f9a822bddae6.

- 2026-09-24T19:52:33+00:00: Recorded command exit 1; command argv SHA-256
  ac99b772dd8bd62096364ead4849ecaefc960101488bf7324f352f35029df1f7.

- 2026-09-24T19:52:52+00:00: Recorded command exit 0; command argv SHA-256
  ac99b772dd8bd62096364ead4849ecaefc960101488bf7324f352f35029df1f7.

- 2026-09-24T19:53:13+00:00: Recorded command exit 1; command argv SHA-256
  0adf6bcefc164948aa25e5c4a875ca3167953ccdfdc8cb4f761e6ad872b2c2f7.

- 2026-09-24T19:53:27+00:00: Recorded command exit 0; command argv SHA-256
  d74bb0eea616bc82160c5f72a87056d033b00b3033e14b6c91cb6936963f4394.

- 2026-09-24T19:53:45+00:00: Diagnosis and repair in progress: PR #307 merge 5ddac12 has first
  parent a2a6414 while reviewed topic was based on 0dcc717; protected-main policy correctly rejected
  reviewed-tree versus merge-tree mismatch. merge_pr.py now explicitly requalifies target/PR refs
  after fetch and immediately before publication, failing closed with fresh exact-main qualification
  required. Added hostile fetch-race regression. First focused rerun had one stale expected-message
  assertion; corrected, then python3 -m unittest tools.integration.test_merge_pr passed 12/12. A
  combined command also failed before tests due nonexistent module
  tools.quality.test_repository_policy (ModuleNotFoundError); merge tests in that combined command
  ran 12 tests but overall exit 1. This is recorded as command/setup error, not product failure.

- 2026-09-24T19:54:01+00:00: Recorded command exit 0; command argv SHA-256
  db1892a26ddeb0bf09f8f135a5a66192b83eddf4ad93b00787dafa3e67ca7980.

- 2026-09-24T19:54:22+00:00: Recorded command exit 0; command argv SHA-256
  7c730eec3ea71bd24ffc5a9255bf7f542481bf601dba6c72bed6e00f6c2fab3c.

- 2026-09-24T19:54:37+00:00: Recorded command exit 0; command argv SHA-256
  5882166f925a7392d5afbac44f9caa6cb1c5885b57088e8b68d4974019d14058.

- 2026-09-24T19:54:51+00:00: Recorded command exit 0; command argv SHA-256
  3a2ca948c4df58faec478ffd99748b9739808c1ab15efc6e30d4032564ef809b.

- 2026-09-24T19:55:24+00:00: Recorded command exit 0; command argv SHA-256
  db1892a26ddeb0bf09f8f135a5a66192b83eddf4ad93b00787dafa3e67ca7980.

- 2026-09-24T19:55:45+00:00: Recorded command exit 0; command argv SHA-256
  7c730eec3ea71bd24ffc5a9255bf7f542481bf601dba6c72bed6e00f6c2fab3c.

- 2026-09-24T19:56:00+00:00: Recorded command exit 0; command argv SHA-256
  ff6d1fa7a7185010f75fcfafe4bdc1bdd5b9804d8c2b3e7abdd8a1b96cd81c63.

- 2026-09-24T19:56:14+00:00: Recorded command exit 0; command argv SHA-256
  5882166f925a7392d5afbac44f9caa6cb1c5885b57088e8b68d4974019d14058.

- 2026-09-24T19:56:29+00:00: Recorded command exit 0; command argv SHA-256
  ff6d1fa7a7185010f75fcfafe4bdc1bdd5b9804d8c2b3e7abdd8a1b96cd81c63.

- 2026-09-24T19:56:50+00:00: Recorded command exit 1; command argv SHA-256
  e105ad747bd56145bae904ede22e1de97f273e0d16aca8550853d3eeab31b23b.

- 2026-09-24T19:57:11+00:00: Recorded command exit 0; command argv SHA-256
  0fe9b68d93bfcb357ef70168e6c8dbc3062b7db80a51afbb9f2e0aa9c1614b8f.

- 2026-09-24T19:57:37+00:00: Recorded command exit 0; command argv SHA-256
  e105ad747bd56145bae904ede22e1de97f273e0d16aca8550853d3eeab31b23b.

- 2026-09-24T19:57:56+00:00: Recorded command exit 0; command argv SHA-256
  19c387515001d3fabbbaf98bd7c5aaca205f3c0e2d025aa0df986ff5be9ea33c.

- 2026-09-24T19:58:22+00:00: Signed+DCO commit 28e3560 is clean and independently reviewed. It adds
  explicit remote target/PR requalification after fetch and immediately before publication, with
  exact ancestry/tree checks; fetch-target-race hostile regression; docs and repository-policy
  integrity fragment updated. Focused integration + signature-policy suite passed 28 tests. Earlier
  combined test command recorded ModuleNotFoundError for nonexistent
  tools.quality.test_repository_policy and was corrected.

- 2026-09-24T19:58:31+00:00: Recorded command exit 0; command argv SHA-256
  0c90409569fda4472a940e0740cdba311915d2704eca7c7ff38445375e528496.

- 2026-09-24T19:59:01+00:00: Recorded command exit 0; command argv SHA-256
  96131db4dd263a9e70ef0258efec9249ba463ea9373d1c487fe9b2744d578f32.

- 2026-09-24T19:59:28+00:00: Recorded command exit 0; command argv SHA-256
  af61552e610431e14f1cc5ff5c84e8f4d6aeb74fe3e4aa6e82c1a08788204727.

- 2026-09-24T19:59:42+00:00: PR #308 opened from exact base 5ddac12 to signed+DCO head
  28e35608a2a87f53afa70732ca1b51aa57aa360b. Initial check snapshot: AWQ and headers SUCCESS;
  remaining required checks in progress. Product push succeeded. Automatic state reconcile push
  failed non-fast-forward because remote state main advanced from expected d5d97d8 to 7238fca; this
  is recorded and does not affect product branch.

- 2026-09-24T19:59:56+00:00: Recorded command exit 0; command argv SHA-256
  88532e8a191f9d191580c7bc7b4c86a81bfa044cf03c478e7ab6c09f16090fe3.

- 2026-09-24T20:00:20+00:00: Recorded command exit 0; command argv SHA-256
  88532e8a191f9d191580c7bc7b4c86a81bfa044cf03c478e7ab6c09f16090fe3.

- 2026-09-24T20:01:13+00:00: Recorded command exit 0; command argv SHA-256
  88532e8a191f9d191580c7bc7b4c86a81bfa044cf03c478e7ab6c09f16090fe3.

- 2026-09-24T20:01:31+00:00: Recorded command exit 0; command argv SHA-256
  7d3b9205c9a719a9ffb49ba701b83d8e4c4d9dbdf0265bd8d428fe8293cf2387.

- 2026-09-24T20:02:24+00:00: Recorded command exit 0; command argv SHA-256
  88532e8a191f9d191580c7bc7b4c86a81bfa044cf03c478e7ab6c09f16090fe3.

- 2026-09-24T20:02:39+00:00: Recorded command exit 0; command argv SHA-256
  88532e8a191f9d191580c7bc7b4c86a81bfa044cf03c478e7ab6c09f16090fe3.

- 2026-09-24T20:03:30+00:00: Recorded command exit 0; command argv SHA-256
  88532e8a191f9d191580c7bc7b4c86a81bfa044cf03c478e7ab6c09f16090fe3.

- 2026-09-24T20:03:51+00:00: Recorded command exit 0; command argv SHA-256
  88532e8a191f9d191580c7bc7b4c86a81bfa044cf03c478e7ab6c09f16090fe3.

- 2026-09-24T20:04:33+00:00: Recorded command exit 0; command argv SHA-256
  88532e8a191f9d191580c7bc7b4c86a81bfa044cf03c478e7ab6c09f16090fe3.

- 2026-09-24T20:05:02+00:00: Heartbeat by ar1421-protected-main-race-luna56.

- 2026-09-24T20:05:06+00:00: Recorded command exit 0; command argv SHA-256
  88532e8a191f9d191580c7bc7b4c86a81bfa044cf03c478e7ab6c09f16090fe3.

- 2026-09-24T20:08:44+00:00: Recorded command exit 0; command argv SHA-256
  71a9dfb59630a682d82029f84b04d44188ab5a7f5b662df3e4b754ca5ac1469f.

- 2026-09-24T20:09:18+00:00: PR #308 merged after all 12 required checks terminal SUCCESS. Exact
  merge 10b16186c8424f53f6d6d8c2797d785dea10c53b is now the post-merge evidence target. Seven push
  workflows observed: Repository quality 36052764434, Rust 36052764446, aarch64 36052764452, Fault
  assurance 36052764458, hosted portability 36052764507, Formal assurance 36052764675, MIT headers
  36052764433 (already SUCCESS). Merge command finalization initially hit LOCK_TIMEOUT; fresh query
  confirmed MERGED.

- 2026-09-24T20:09:36+00:00: Recorded command exit 0; command argv SHA-256
  a3590b7d997947e3afc251cecf38d22bf5830971d224aae2cb387b3c49ec1bdb.

- 2026-09-24T20:11:57+00:00: Recorded command exit 0; command argv SHA-256
  a3590b7d997947e3afc251cecf38d22bf5830971d224aae2cb387b3c49ec1bdb.

- 2026-09-24T20:14:15+00:00: Recorded command exit 0; command argv SHA-256
  a3590b7d997947e3afc251cecf38d22bf5830971d224aae2cb387b3c49ec1bdb.

- 2026-09-24T20:16:19+00:00: Recorded command exit 0; command argv SHA-256
  a3590b7d997947e3afc251cecf38d22bf5830971d224aae2cb387b3c49ec1bdb.
