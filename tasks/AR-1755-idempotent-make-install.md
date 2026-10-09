---
{
  "branch": "fix/ar-1755-idempotent-make-install",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-09T11:33:25+00:00",
  "depends_on": [
    "AR-1745"
  ],
  "id": "AR-1755",
  "next_action": "Post the head-bound independent approval on PR #526, construct and publish the documented signed exact-tree merge for reviewed head 6ac109533612f827320f87bbf65f98694cee4e8d/tree 2bc351c195732261fb694e0d4c156a47daba04c0, then verify all exact-main hosted checks before release.",
  "observed_branch": "fix/ar-1755-idempotent-make-install",
  "observed_dirty": 0,
  "observed_head": "6ac109533612f827320f87bbf65f98694cee4e8d",
  "owner": "codex-asb-ar1755-install-20261009",
  "plan": "../plans/AR-1755-idempotent-make-install.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1755.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Repair the ASB Make install path so rerunning plain `make install` replaces its existing ASB binary without advertising an invalid Make option.",
  "task_revision": 43,
  "title": "Make ASB installation safely idempotent",
  "updated_at": "2026-10-09T10:07:21+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1755-idempotent-make-install"
}
---

On current protected ASB main, a first `make install` succeeds, but a second
install into the same prefix delegates to `cargo install` without Cargo's
overwrite flag. Cargo reports that the binary already exists and recommends
`--force`. Passing that text back as `make install --force` fails earlier because
GNU Make does not recognize `--force` as one of its options.

Restore the idempotent reinstall contract accepted by AR-1745. Plain
`make install` must safely replace the ASB-managed executable inside the already
validated prefix without requiring an additional user option. Preserve all
absolute-prefix, traversal, repository-root, filesystem-root, symlink-chain,
ownership-boundary, cleanup-marker, and out-of-prefix protections. Do not broaden
the change into TUI installation, release packaging, runtime installation, or
system-wide privilege handling.


- 2026-10-09T09:33:22+00:00: AR-1745 is done; exact ASB main reproduces the Cargo
  existing-destination failure and GNU Make rejects the suggested --force spelling.

- 2026-10-09T09:33:25+00:00: Claimed by codex-asb-ar1755-install-20261009.

- 2026-10-09T09:33:55+00:00: Recorded command exit 0; command argv SHA-256
  048c8e1fefac351386dd2444042d2e0c10f87c1379dbb29985451c5f4351ec1e.

- 2026-10-09T09:34:55+00:00: Recorded command exit 0; command argv SHA-256
  b1c2c9d69651561e32b970415591af09bcaa14d36b0791d31ae69d5ab57387c7.

- 2026-10-09T09:35:45+00:00: Recorded command exit 2; command argv SHA-256
  ff9297d17c0732874297929773bce1e7f679caddd77de7a11179d73b2a300879.

- 2026-10-09T09:36:10+00:00: Recorded command exit 2; command argv SHA-256
  1d5792ee8fc396e26989a595d13bd583bf7210c1a9512b742608f41ac2234fc6.

- 2026-10-09T09:36:34+00:00: Recorded command exit 0; command argv SHA-256
  814c0f4f77879374fe521c19226a8a37d6f6e49ceb311f438743896a1911e5a2.

- 2026-10-09T09:36:54+00:00: Recorded command exit 0; command argv SHA-256
  cc04621c43fbd45bb6f513eb7e57b111d06e969fe97f996e936ad21717131803.

- 2026-10-09T09:37:37+00:00: Recorded command exit 0; command argv SHA-256
  cc04621c43fbd45bb6f513eb7e57b111d06e969fe97f996e936ad21717131803.

- 2026-10-09T09:38:36+00:00: Recorded command exit 0; command argv SHA-256
  79edd2fa6ab3acc370a2014dfa8c343390f85f83495c162be8bddfd529fa42b6.

- 2026-10-09T09:39:09+00:00: Exact base 64eaad2215e4f08fe8e803022acb6e9146b95d94: GNU Make rejects
  make install --force with exit 2. Cargo 1.93 replaces a repeat install that it already owns, but
  the reported unmanaged/pre-existing destination case requires Cargo --force. Candidate now passes
  --force only at Cargo install after all existing prefix/symlink validation. Focused deterministic
  harness passes repeat default-HOME and explicit-prefix installs, replacement, unrelated-file
  preservation, fake no-force rejection, correct help, and
  empty/root/repository/traversal/non-directory/symlink negatives. A real Cargo run also replaced an
  unmanaged executable, completed a second plain reinstall, reported asb 0.1.0 twice, and preserved
  an unrelated file.

- 2026-10-09T09:39:56+00:00: Recorded command exit 101; command argv SHA-256
  35b562cfc3d5d2917f7408eb532221249fdcfef96ddf0544dcc1098f75cd0413.

- 2026-10-09T09:40:07+00:00: Recorded command exit 0; command argv SHA-256
  d458e247b20c6b9bd4b4bc538982e816f941a395d34d58281a0f8ba4ac58307c.

- 2026-10-09T09:45:54+00:00: Recorded command exit 0; command argv SHA-256
  c07ee61f8c00981eb93b9d88dfb9d733e130f84bd378f9a98766558b8e075c81.

- 2026-10-09T09:46:19+00:00: Recorded command exit 0; command argv SHA-256
  560ac8f08397034ba8938d9dd505587860021b80722d0931b522fd3ce62b8175.

- 2026-10-09T09:46:49+00:00: Recorded command exit 0; command argv SHA-256
  0cfdba1bb7f3b56220c6a197e7721e065a7fa52691a568c597b93c32f8f0c83a.

- 2026-10-09T09:47:27+00:00: Recorded command exit 0; command argv SHA-256
  4d149b653f7d6b2966eac12006b142efbf6c4640436c325417b4999f9df6d87e.

- 2026-10-09T09:47:52+00:00: Recorded command exit 0; command argv SHA-256
  70a4163a40aef4dad4b9fa428484aaa0d9bb6ebf7e4a43888fa050ebdef69064.

- 2026-10-09T09:48:33+00:00: Recorded command exit 0; command argv SHA-256
  cc04621c43fbd45bb6f513eb7e57b111d06e969fe97f996e936ad21717131803.

- 2026-10-09T09:49:32+00:00: Recorded command exit 0; command argv SHA-256
  cc04621c43fbd45bb6f513eb7e57b111d06e969fe97f996e936ad21717131803.

- 2026-10-09T09:50:08+00:00: Recorded command exit 0; command argv SHA-256
  c09146aa0a8ddf9d21071001d7d6a3bc19a702a07ff65958300021469f0c9ac9.

- 2026-10-09T09:51:23+00:00: Recorded command exit 0; command argv SHA-256
  c07ee61f8c00981eb93b9d88dfb9d733e130f84bd378f9a98766558b8e075c81.

- 2026-10-09T09:51:47+00:00: Recorded command exit 0; command argv SHA-256
  79cbc6321afc046053b0bd525bf0c0c5ebd460fcbabe425cd25097d9d457f248.

- 2026-10-09T09:52:11+00:00: Recorded command exit 0; command argv SHA-256
  eaa1e186b29db36d5c3503e85273b238410490d27e35a8d1f9c68ac6a959310b.

- 2026-10-09T09:52:53+00:00: Independent review rejected superseded head
  e8d123ae790420c2fcac06c33fe79a6ef4fec98c because unconditional Cargo overwrite could replace an
  unmarked unrelated regular bin/asb. New signed+DCO head 909dae145e46c4e67de4d744f389a6011bc28330,
  tree 3c1be3e898aca2549f4bbcdb7bc48391d5ffa253, gates replacement on a safe regular Make ownership
  marker and regular non-symlink destination. Deterministic negatives prove unmarked binaries,
  non-regular destinations, symlink markers, and non-regular markers remain unchanged and Cargo is
  not invoked. Real Cargo proves first managed install plus repeat plain install succeeds and an
  unmarked binary remains byte-identical. Focused harness, fmt, Clippy, complete locked workspace
  tests, rustdoc, release build/CLI behavior, source-header policy/tests, ShellCheck, and diff
  checks pass. PR #526 now targets the repaired head; hosted checks are running.

- 2026-10-09T09:54:07+00:00: Recorded command exit 0; command argv SHA-256
  facf61688d3614a3b39febcd477d6131c84f8c3532bbfae6b55af4f66e6b8592.

- 2026-10-09T09:55:21+00:00: Recorded command exit 0; command argv SHA-256
  c07ee61f8c00981eb93b9d88dfb9d733e130f84bd378f9a98766558b8e075c81.

- 2026-10-09T09:55:44+00:00: Recorded command exit 0; command argv SHA-256
  4c6fce8a8e955a73da74acec413d9c6584df3fa05f5e3da51de5d882b5541dcb.

- 2026-10-09T09:56:01+00:00: Recorded command exit 0; command argv SHA-256
  eaa1e186b29db36d5c3503e85273b238410490d27e35a8d1f9c68ac6a959310b.

- 2026-10-09T09:56:10+00:00: Recorded command exit 0; command argv SHA-256
  a093358747429c07186377bda4237371fb9bd68bf927ae01ce7a8ca10a87279b.

- 2026-10-09T09:56:34+00:00: Independent review rejected superseded head
  909dae145e46c4e67de4d744f389a6011bc28330 because the focused shell harness used GNU-only find
  -printf. New signed+DCO head 6ac109533612f827320f87bbf65f98694cee4e8d replaces it with POSIX find
  -print. The harness passes under BusyBox sh with BusyBox find, and the complete documented local
  gate payload passes. The enclosing handoffctl command recorded a post-payload reconciliation error
  only because unrelated stale worktree metadata names missing /tmp/asb-ar1698-qual.fE5S7P; this
  does not invalidate the passing product tests but requires separate coordinator cleanup.

- 2026-10-09T09:57:35+00:00: Recorded command exit 0; command argv SHA-256
  a093358747429c07186377bda4237371fb9bd68bf927ae01ce7a8ca10a87279b.

- 2026-10-09T09:58:10+00:00: Recorded command exit 0; command argv SHA-256
  dad0ab377d0884f6c7b6a0a3e0ded6d87584c1094c292a50b9383f9c7e78314c.

- 2026-10-09T10:07:14+00:00: Recorded command exit 0; command argv SHA-256
  1a61b10878af15b1c21a44760e122297c6e523ff0bd4468bfb61d34166ab80f2.

- 2026-10-09T10:07:21+00:00: Final independent APPROVE-equivalent verdict reports no findings on
  exact head 6ac109533612f827320f87bbf65f98694cee4e8d/tree 2bc351c195732261fb694e0d4c156a47daba04c0.
  Reviewer verified remote identity, valid SSH signatures and DCO, marker-gated safe overwrite,
  portable BusyBox-compatible harness, clean tree, focused local gates, and all 15 of 15 hosted
  exact-head checks successful.
