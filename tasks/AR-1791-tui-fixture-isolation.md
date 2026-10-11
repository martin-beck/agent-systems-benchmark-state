---
{
  "branch": "codex/ar-1791-tui-fixture-isolation",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1770",
    "AR-1788",
    "AR-1789",
    "AR-1790"
  ],
  "id": "AR-1791",
  "next_action": "Inspect privacy/diff, then run another ordinary full workspace gate; release only if it passes and static/provenance gates remain green.",
  "observed_branch": "codex/ar-1791-tui-fixture-isolation",
  "observed_dirty": 0,
  "observed_head": "4dbf735db270be0faf25fa005104397d8a680eb3",
  "owner": "",
  "plan": "../plans/AR-1791-tui-fixture-isolation.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "hosted",
    "evidence_digest": "sha256:e040f3b3358077de6ffe7016069b6c9981c8ea0019ca5e9580b48ff25728d5b7",
    "evidence_ref": "quality/AR-1791-tui-fixture-isolation-postmerge-receipt.json",
    "spec_ref": "specs/AR-1791.json",
    "spec_revision": 1,
    "status": "pass"
  },
  "spec_ref": "specs/AR-1791.json",
  "spec_revision": 1,
  "status": "done",
  "summary": "Make the GCC descendant-marker and rustup descriptor-cleanup TUI fixtures deterministic under repeated ordinary workspace execution.",
  "task_revision": 54,
  "title": "Repair recurrent TUI fixture isolation failures",
  "updated_at": "2026-10-10T23:50:36+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1791-tui-fixture-isolation"
}
---

This development repair does not require a GitHub Reviews API approval object. Independent technical review, exact-head CI, signed DCO integration, and post-merge verification remain mandatory.

- 2026-10-10T23:10:24+00:00: Clean state worktree permits promotion; dependencies complete. Start
  fixture isolation repair under full development gates, with no GitHub Reviews API approval object.

- 2026-10-10T23:10:24+00:00: Claimed by codex-ar1791-fixture-repair.

- 2026-10-10T23:11:53+00:00: Recorded command exit 0; command argv SHA-256
  f702145443cf17b5bd0983f1c3ced4800ff6e06976fb9bd09c169e8a07d5d3a7.

- 2026-10-10T23:12:01+00:00: Recorded command exit 0; command argv SHA-256
  a2fae77c04bf5e8d1361baf666316f7853f3ad9af50c54ad10c944203b1b2729.

- 2026-10-10T23:12:08+00:00: Recorded command exit 0; command argv SHA-256
  624c5aaf590b985a6f9c95f86077477c7419196ec5757211325e6556e254af7e.

- 2026-10-10T23:13:16+00:00: Recorded command exit 101; command argv SHA-256
  faf12f611507a64478d0d52fc3eea6628859dc244467bf00ff18bb5e351e34d6.

- 2026-10-10T23:13:45+00:00: Recorded command exit 0; command argv SHA-256
  5ddcf8bdcd387c922a7307a3a41d861bf2137fd6e520254a210c5ae6a9619b8b.

- 2026-10-10T23:14:00+00:00: Recorded command exit 0; command argv SHA-256
  92621713b1a260197374ff82a6f74b2c6ebeb51ead07eadd5bef0690d6283cc5.

- 2026-10-10T23:14:28+00:00: Recorded command exit 0; command argv SHA-256
  5ddcf8bdcd387c922a7307a3a41d861bf2137fd6e520254a210c5ae6a9619b8b.

- 2026-10-10T23:14:41+00:00: Recorded command exit 0; command argv SHA-256
  1606f02a1f7d6bf1fa0c9882e9209228ad8af13ccc2534b98f3ea89bc139f823.

- 2026-10-10T23:14:49+00:00: Recorded command exit 0; command argv SHA-256
  e16a3a9426a494cc890c8c53da22acbc56e95a09ced4233c37795649cfe5d8a6.

- 2026-10-10T23:15:08+00:00: Candidate 4dbf735db270be0faf25fa005104397d8a680eb3 is SSH-signed and
  DCO-signed. Initial focused attempt exited 101 because I added a duplicate Scratch Drop
  implementation; source inspection found the existing RAII Drop later in the module, so I removed
  the duplicate. The committed repair adds a cleanup regression and changes the rustup post-close
  check from global /proc/self/fd/N nonexistence (racy under parallel FD reuse) to positive/negative
  original dev+inode identity checks. Corrected focused rustup and GCC hostile-descendant tests
  pass. No serialization, exclusion, publication, or merge.

- 2026-10-10T23:15:57+00:00: Recorded command exit 101; command argv SHA-256
  4c1dd549c7fa7cfa736b77e60908a5544d43021bd2f6ca805b8289eebb67feda.

- 2026-10-10T23:16:49+00:00: Recorded command exit 0; command argv SHA-256
  955dfd54f7432b57d0e6cee4f15baadfe05d190309a35de135483691a7cdaf8e.

- 2026-10-10T23:17:02+00:00: First full workspace gate at 4dbf735d exited 101 in the bounded
  coordinator record, although the visible stream included both target TUI tests passing; runner
  evidence intentionally retains no subprocess output. Narrowed ordinary parallel cargo test
  --locked -p asb-cli --lib then passed all 341 tests, including GCC descendant-marker, rustup
  path-replacement, and new Scratch cleanup coverage. Therefore do not claim the target fixtures are
  still failing or the candidate is qualified: repeat the full workspace gate to distinguish another
  crate/cross-crate failure from transient infrastructure before release.

- 2026-10-10T23:17:52+00:00: Recorded command exit 0; command argv SHA-256
  4c1dd549c7fa7cfa736b77e60908a5544d43021bd2f6ca805b8289eebb67feda.

- 2026-10-10T23:18:20+00:00: Heartbeat by codex-ar1791-fixture-repair.

- 2026-10-10T23:18:47+00:00: Recorded command exit 0; command argv SHA-256
  eb9c7de77390563c861de43544be355b873e8917cabc15a3f74da088d4bb66a6.

- 2026-10-10T23:19:12+00:00: Recorded command exit 0; command argv SHA-256
  81f4fb6cedf77ea22c37645ce2d41aa634a8f7ccdb83e74a6f1d134eb3537a9e.

- 2026-10-10T23:19:29+00:00: Recorded command exit 0; command argv SHA-256
  68f43c76b69fa3d2475ad33d90a36afe6c23b8066b9dbfe2d2d3fe5e760b4372.

- 2026-10-10T23:19:38+00:00: Recorded command exit 128; command argv SHA-256
  375abd39b3e80fb57d64d65b224ff7da3da1d84026d4a428377c702d1e8bd9e7.

- 2026-10-10T23:19:50+00:00: Recorded command exit 0; command argv SHA-256
  6a7b7f8c955a1ac481bfcc4f11c8f27181eddb4dcdfd447436a54e378b5d8854.

- 2026-10-10T23:19:57+00:00: Recorded command exit 0; command argv SHA-256
  76a7c9a82626e506c233f334bcac5a41bb15e42cd2c6d26a4516c9718dca27ec.

- 2026-10-10T23:20:05+00:00: Recorded command exit 0; command argv SHA-256
  88416ef4db0f5102fe87b682cf45630aee60fb359ce416aeb53144aaf4ef4746.

- 2026-10-10T23:20:15+00:00: Recorded command exit 0; command argv SHA-256
  dde51f6432f8cbc7e95d3c77421fd1355c1d5cc331e2c7393464d5590d460485.

- 2026-10-10T23:20:33+00:00: Classified quality command exit 128 at 23:19:38: git diff --check
  received a stale/truncated base SHA and failed before inspecting the tree. Actual merge base is
  59cfd9cf; rerun diff --check 59cfd9cf..4dbf735d exited 0. This is operator-input evidence, not a
  product/test failure and not a passing gate. The attempted unsupported handoffctl note subcommand
  was also a CLI usage error only; durable update follows.

- 2026-10-10T23:20:40+00:00: Recorded command exit 0; command argv SHA-256
  08c4b90bc238fea378d62bab8df8b6a161ad683257a10e94780f61d6e12247a0.

- 2026-10-10T23:21:55+00:00: Recorded command exit 0; command argv SHA-256
  4c1dd549c7fa7cfa736b77e60908a5544d43021bd2f6ca805b8289eebb67feda.

- 2026-10-10T23:22:30+00:00: Candidate 4dbf735db270be0faf25fa005104397d8a680eb3 is released only for
  independent exact-head review; it is SSH-signed and carries matching DCO. Repair adds a positive
  Scratch uniqueness/removal regression and replaces the racy global /proc/self/fd/N post-close
  assertion with positive/negative dev+inode identity checks, so parallel FD-number reuse cannot be
  mistaken for a leaked original descriptor. Focused rustup path-replacement and GCC
  descendant-marker tests pass; ordinary parallel asb-cli lib run passed 341/341. First workspace
  command exited 101 without retained subprocess output; narrowed run then passed and the two
  following ordinary cargo +1.93.0 test --locked --workspace runs exited 0 (23:17:52 and 23:21:55).
  fmt --check, clippy --workspace --all-targets -D warnings, rustdoc -D warnings --workspace
  --no-deps, corrected-base diff --check, signature verification, and privacy diff inspection pass.
  The stale-base diff exit 128 and attempted unsupported note CLI error are recorded as operator
  errors, not product evidence. No serial-only bypass, exclusion, merge, or GitHub Reviews API
  approval object. Reviewer must independently inspect exact head and rerun applicable gates.

- 2026-10-10T23:22:53+00:00: Claimed by codex-ar1791-independent-review.

- 2026-10-10T23:23:26+00:00: Recorded command exit 0; command argv SHA-256
  1ce788985e7531bb7af842fe6ab17af2d34b14fb0189968ccbd92387f2f5900f.

- 2026-10-10T23:23:33+00:00: Recorded command exit 0; command argv SHA-256
  085d666b8479697639890e9505cf6a87f605d589717295f502778430358d971e.

- 2026-10-10T23:23:37+00:00: Recorded command exit 0; command argv SHA-256
  89ceb5d3e85a7e7aec0f3fe665d95cec7045581bf6558291822387c3138e4146.

- 2026-10-10T23:24:33+00:00: Recorded command exit 0; command argv SHA-256
  0a80e5fef7a7fd1f9619dda5154f8e236f7046b2d753e8434f5dc84d2c1342d8.

- 2026-10-10T23:24:41+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-10-10T23:24:50+00:00: Independent review clean for exact candidate
  4dbf735db270be0faf25fa005104397d8a680eb3. Complete diff is one file (crates/asb-cli/src/tui.rs,
  +42/-2): adds Scratch RAII cleanup regression and changes rustup descriptor teardown assertions to
  compare original dev+inode identity, removing a parallel-FD reuse race. git diff --check passed;
  no secrets, credentials, private paths, serialization/publication changes, or network behavior.
  Candidate commit is SSH-signed with ED25519 SHA256:a36V6yPvRZyxnQ2113tiA/MlHt7mPfJEXAGByBXVkuE and
  matching Signed-off-by. Focused tests passed: scratch_roots_are_unique_and_removed_on_drop,
  development_rustup_tools_execute_validated_objects_after_path_replacement,
  development_gcc_probe_kills_stdout_descendant_and_restores_cloexec. Repeated ordinary cargo test
  --locked --workspace --all-targets passed; cargo fmt --all -- --check passed. No GitHub Reviews
  API approval object required. Released for integration; reviewer did not accept or merge.

- 2026-10-10T23:25:07+00:00: Claimed by codex-ar1791-integration.

- 2026-10-10T23:25:14+00:00: Recorded command exit 0; command argv SHA-256
  74e37ada69cdee5a2df2868f52bad2b102f3f305d6209ee652e7e5a3e83cec2a.

- 2026-10-10T23:25:26+00:00: Recorded command exit 0; command argv SHA-256
  17f9f65a6bae21a93d1f223a1deba04f38677b43abf4450ba2e208af72875f91.

- 2026-10-10T23:25:38+00:00: Recorded command exit 0; command argv SHA-256
  fcb958044598a581f53c21cf70a51fda31123653141450573b52bd4f322c286f.

- 2026-10-10T23:26:20+00:00: Recorded command exit 8; command argv SHA-256
  e5d48d51a2848f051ba3c00120e327a538c7dc105ec5eb53d9243acb4203c247.

- 2026-10-10T23:27:10+00:00: Recorded command exit 0; command argv SHA-256
  c9c037b558ea3e6248dfb24efcfb6506fdb925faac8263ea1a6be7d4c99868f4.

- 2026-10-10T23:36:58+00:00: Recorded command exit 0; command argv SHA-256
  69c59a7a35107865e4aaa4f83f3994f09e416bbbc0ec1772a18d681341f8f6ea.

- 2026-10-10T23:37:33+00:00: Recorded command exit 0; command argv SHA-256
  08fdd1ef8aff6a85a0e0e8311d8bae6faf04cfcd2447fc48f1e5afb0727668f0.

- 2026-10-10T23:38:24+00:00: Recorded command exit 0; command argv SHA-256
  147209cc161ad4f9df3655b648ccd652d8c328cf5d646c45140a971211c08315.

- 2026-10-10T23:48:47+00:00: Recorded command exit 0; command argv SHA-256
  f2348c027e23c899826d35c9226bf12c6db1ee09ec62c0b7cb2026bc27d4038b.

- 2026-10-10T23:49:08+00:00: Recorded command exit 0; command argv SHA-256
  06a9efb22937837cb7abacb85b975e02ca50417414c28ba9c6fffc8037fe8784.

- 2026-10-10T23:49:29+00:00: Recorded command exit 0; command argv SHA-256
  1bc174af6136366bb3c9fec24877914bc23d694207020af38ec109bb356e9f37.

- 2026-10-10T23:50:23+00:00: Accepted exact reviewed candidate 4dbf735, signed merge 16d8512, all
  exact-head and exact-main checks green; no GitHub Reviews API approval object required.

- 2026-10-10T23:50:36+00:00: AR-1791 complete: exact reviewed merge 16d8512, post-merge workflows
  terminal green, durable receipt accepted.
