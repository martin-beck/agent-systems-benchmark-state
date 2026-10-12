---
{
  "branch": "feature/ar-1779-default-usable-tool-install-command",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1777",
    "AR-1778",
    "AR-1784"
  ],
  "id": "AR-1779",
  "next_action": "Independent review and exact-head CI for PR #583 at 7c08cfb0; source-only fallback remains to be resolved before merge.",
  "observed_branch": "feature/ar-1779-default-usable-tool-install-command",
  "observed_dirty": 0,
  "observed_head": "daf2d3ee9750b24adb2a33d113a7096acd961e93",
  "owner": "",
  "plan": "../plans/AR-1779-default-usable-tool-install-command.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "environmental",
    "evidence_digest": "sha256:eb4b75b18b5b7ea8304c10949634963b29e25f6b1f205408c8da21b93979478b",
    "evidence_ref": "evidence/AR-1779-post-merge-receipt.txt",
    "spec_ref": "specs/AR-1779.json",
    "spec_revision": 1,
    "status": "pass"
  },
  "spec_ref": "specs/AR-1779.json",
  "spec_revision": 1,
  "status": "done",
  "summary": "Make default asb tool install produce and verify a usable project-local supported executable tool without manual source copying.",
  "task_revision": 60,
  "title": "Default usable tool-install command",
  "updated_at": "2026-10-11T21:05:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1779-default-usable-tool-install-command"
}
---

Change the public experience to `asb tool install <supported-id> [--project PATH]`.
It resolves the catalog, reuses a compatible verified local binary when one is
available, otherwise retrieves a verified official prebuilt artifact, otherwise
uses the pinned source-build/dependency fallback. A success is valid only after
an executable smoke check proves the installed entrypoint can be used
by the target ASB adapter. Persist the complete receipt and active usable state
only after that check passes.

Keep explicit local-file or fixture installation as a clearly labelled
development/import mode rather than the default supported-user flow. Offer
`status`, `repair`, `update`, and `remove` semantics that expose current
catalog/source/digest/platform/build state without downloading on read-only
commands. Human output must explain selection, downloads/builds, reused versus
created dependencies, result location, and next action; JSON retains its stable
machine contract and never includes secrets. The command must not silently use a
wrong binary, silently fall back to an unrelated tool, or claim installation when
the adapter smoke check failed.

- 2026-10-11T13:53:29+00:00: Promote dependency-safe AR-1779 now that AR-1777, AR-1778, and AR-1784
  are durably done.

- 2026-10-11T13:54:34+00:00: Claimed by luna56-ar1779.

- 2026-10-11T13:55:27+00:00: Recorded command exit 0; command argv SHA-256
  ff6d1fa7a7185010f75fcfafe4bdc1bdd5b9804d8c2b3e7abdd8a1b96cd81c63.

- 2026-10-11T13:57:08+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-10-11T13:57:59+00:00: Recorded command exit 0; command argv SHA-256
  a15cc58cd42c65980b3f718472d4802c1ccec6ff105530e3f2089168c16c493a.

- 2026-10-11T13:58:50+00:00: Recorded command exit 0; command argv SHA-256
  a15cc58cd42c65980b3f718472d4802c1ccec6ff105530e3f2089168c16c493a.

- 2026-10-11T13:59:14+00:00: Recorded command exit 0; command argv SHA-256
  e274074a17e0682b5edf79b5caca577a41520ed9ca8daf9342f0433b678582a1.

- 2026-10-11T13:59:42+00:00: Recorded command exit 0; command argv SHA-256
  66f996973c66b1dc6463c1cf5f3af22fc2e3038ab84de35cb406f119798f0306.

- 2026-10-11T14:00:27+00:00: Recorded command exit 101; command argv SHA-256
  10a701b2424e5ed226b0455eb01ce19376ff98a24fb81ec0200c779f16f8a3dc.

- 2026-10-11T14:00:55+00:00: Recorded command exit 0; command argv SHA-256
  245e3b0fff1646dc3984ec302e56aa0b1995e88266374bb46e25680733a6a143.

- 2026-10-11T14:01:23+00:00: Recorded command exit 0; command argv SHA-256
  3ce7e7052283f0a20f77e43c8d9a7bbdd6c377538c05e7f56ee034002add5ad6.

- 2026-10-11T14:02:37+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-11T14:03:07+00:00: Recorded command exit 0; command argv SHA-256
  e274074a17e0682b5edf79b5caca577a41520ed9ca8daf9342f0433b678582a1.

- 2026-10-11T14:03:33+00:00: Recorded command exit 0; command argv SHA-256
  9bee9533393737c3f6f9394ca04410e19296da8940afaf99aaad5895237504ef.

- 2026-10-11T14:03:58+00:00: Recorded command exit 0; command argv SHA-256
  f18ad62f9c9d9a6760e09d95ece99cc58b831e4016946fa857d41e1688516b8c.

- 2026-10-11T14:04:44+00:00: Recorded command exit 0; command argv SHA-256
  cab79174958809e6e46c45ff4e7953c404de8b4e7dcba8de94d226f3ce8d4ac8.

- 2026-10-11T14:05:22+00:00: Rustfmt repair 32cb692a pushed. Full cargo test -p asb-cli passed
  before repair; repair is formatting-only. PR #583 exact head updated.

- 2026-10-11T14:08:25+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-11T14:09:07+00:00: Recorded command exit 0; command argv SHA-256
  e274074a17e0682b5edf79b5caca577a41520ed9ca8daf9342f0433b678582a1.

- 2026-10-11T14:09:29+00:00: Recorded command exit 0; command argv SHA-256
  f6b6f842c448a90c56fe8c665d4f473b301b67152ad8b1849254c6ae566946c2.

- 2026-10-11T14:09:54+00:00: Recorded command exit 0; command argv SHA-256
  f18ad62f9c9d9a6760e09d95ece99cc58b831e4016946fa857d41e1688516b8c.

- 2026-10-11T14:10:16+00:00: Pushed signed repair 7c08cfb0. Added explicit lifecycle repair/update
  installed-ID validation, transactional rerun behavior, and human/machine
  selection/source/build/reuse/path/next fields. Focused parser test passes.

- 2026-10-11T14:10:32+00:00: Heartbeat by luna56-ar1779.

- 2026-10-11T14:11:42+00:00: Recorded command exit 0; command argv SHA-256
  a3fcf50559681de15238986360c1d4702b78883aa98c68d9afd55eca44a0b8e2.

- 2026-10-11T14:11:53+00:00: Recorded command exit 0; command argv SHA-256
  5cf7ef1b33d2d66d11d63bbe78d94081f0cb3366cd0a77c841993395ec8f82a9.

- 2026-10-11T19:29:04+00:00: Recovered expired claim formerly owned by luna56-ar1779. Coordinator
  recovery: lease expired; preserve PR #583 head and recorded next action.

- 2026-10-11T20:52:07+00:00: Claimed by ar1779-review-merge-luna56.

- 2026-10-11T20:52:10+00:00: Recorded command exit 0; command argv SHA-256
  17a35505ebdb797ffbaba7bbdde53d009e26b289b62293d5e1e4d0aabfa8ca1d.

- 2026-10-11T20:52:25+00:00: Recorded command exit 0; command argv SHA-256
  4d42d72e4864f264baf15a25ba06db5f2547c25cbf8a8c7708e7da2ae34b8999.

- 2026-10-11T20:52:38+00:00: Recorded command exit 0; command argv SHA-256
  30c5f7dfcd1a0ea6eb72f5f24ce2f479ec87dc913db56ab828b92c5686bd597b.

- 2026-10-11T20:52:42+00:00: Recorded command exit 0; command argv SHA-256
  24285fcfaf98d0efa54dff3fb037cf77e6d303dfb81beb490d23d427e15ffb48.

- 2026-10-11T20:53:01+00:00: Recorded command exit 0; command argv SHA-256
  1221ba4ddc514d57554bb1db2da9561f7c6a3fd1a66d78595d7b268c0a4e9a8e.

- 2026-10-11T20:53:05+00:00: Recorded command exit 0; command argv SHA-256
  35ec55c3e234f7a18afaf73a93beadfd28fb9cf9f04f531f103d5be6ecb2848c.

- 2026-10-11T20:53:57+00:00: Recorded command exit 101; command argv SHA-256
  22fc19d872be75a975891ff0abd53f1c305974a409b50c49c5df5d842d033e81.

- 2026-10-11T20:54:18+00:00: Recorded command exit 1; command argv SHA-256
  8da9301c3b436d1d2430be4cf7a9ec902b7262bb7e8f28de6f839d0fd0e2560c.

- 2026-10-11T20:54:29+00:00: Recorded command exit 0; command argv SHA-256
  e0049c285cc38207c4c5fcabb1fc5a59394e952ca231c49896756236a92890d8.

- 2026-10-11T20:55:14+00:00: Recorded command exit 0; command argv SHA-256
  e274074a17e0682b5edf79b5caca577a41520ed9ca8daf9342f0433b678582a1.

- 2026-10-11T20:55:34+00:00: Recorded command exit 0; command argv SHA-256
  7f8e954103b2fb839f013ebb12d6e4c66ce6a8064251e44031ba2c4ebc11debf.

- 2026-10-11T20:56:46+00:00: Recorded command exit 0; command argv SHA-256
  d21ee7f3c43d56d4497abd9f493e766257107bd28a98eef79e57ad4028072ea5.

- 2026-10-11T20:56:55+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-10-11T20:57:39+00:00: Recorded command exit 0; command argv SHA-256
  1024fc1e6cefa31b078f0b5d2ed85c7ea4586897b388bf1e308f62db58574461.

- 2026-10-11T20:58:49+00:00: Recorded command exit 0; command argv SHA-256
  534f8613e1c316db8f0f46dd989e44e14a8ca74304a94791b4e4a1c59b2fbb1d.

- 2026-10-11T20:59:59+00:00: Review worker stopped after no active AR process; preserve PR #583
  exact head daf2d3ee and source-only fallback concern for a replacement worker.

- 2026-10-11T21:00:49+00:00: Claimed by ar1779-review-merge-luna56.

- 2026-10-11T21:00:51+00:00: Recorded command exit 0; command argv SHA-256
  17a35505ebdb797ffbaba7bbdde53d009e26b289b62293d5e1e4d0aabfa8ca1d.

- 2026-10-11T21:01:27+00:00: Recorded command exit 101; command argv SHA-256
  3ebf9b919ee1fcc9f22a059c364358193ba08869b997c9f174fafd823eaccd87.

- 2026-10-11T21:02:02+00:00: Recorded command exit 0; command argv SHA-256
  851292e15ad2a20e0ee2f1c4e5ede7eabf5c03fbe5bee71b38a36f5ff33c4814.

- 2026-10-11T21:04:17+00:00: Recorded command exit 0; command argv SHA-256
  beb2864b3de0321ab097a65ee43cecf5286e02a499cc32a7944044b263271823.

- 2026-10-11T21:04:34+00:00: Recorded command exit 0; command argv SHA-256
  891ba707f01eeb14266821397a2c576d7390b60187f13cccfdc5f86ca77ef248.

- 2026-10-11T21:04:39+00:00: Recorded command exit 0; command argv SHA-256
  c0d77ac0e85c0cdfde7b135154c2d8c78d3fa912790a07aa30a26f6e9a11c20a.

- 2026-10-11T21:04:44+00:00: Recorded command exit 0; command argv SHA-256
  8662a565deeeba67d44e00559c68165429b3e59d16ce0b0c285de916da75a82f.

- 2026-10-11T21:04:58+00:00: Exact-main acceptance: implementation is present via merged PR #585,
  all 15 required checks are green, focused CLI/install lifecycle tests pass, and superseded PR #583
  is closed without merge.

- 2026-10-11T21:05:00+00:00: Default usable tool installation is on exact protected main via PR #585
  merge 24cb72d; all 15 required checks and focused lifecycle tests passed; PR #583 closed as
  empty/superseded; acceptance receipt recorded.
