---
{
  "branch": "feature/csb-execution-assurance",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-07T11:44:22+00:00",
  "depends_on": [
    "AR-0101",
    "AR-0102",
    "AR-0103",
    "AR-0104"
  ],
  "id": "AR-0603",
  "next_action": "After explicit Cargo fence handoff, rebase the two signed commits onto exact main, add only asb-csb-runner membership/runtime/store dependencies and implement durable sandboxed process/artifact/cancellation/recovery tests including a real pinned offline x86_64 fixture.",
  "observed_branch": "feature/csb-execution-assurance",
  "observed_dirty": 3,
  "observed_head": "ec4a1d28baca4426b17bc20cffee036d1d3eff23",
  "owner": "contracts-20260906",
  "plan": "../plans/AR-0603.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Pin and audit CSB provenance and prove a bounded sandboxed execution, cancellation, recovery, artifact, and privacy boundary.",
  "task_revision": 66,
  "title": "Establish pinned CSB execution and conformance boundary",
  "updated_at": "2026-09-07T09:10:58+00:00",
  "worktree_key": "agent-systems-benchmark-csb-execution-assurance"
}
---
## AR-0603

Pin and license-audit one exact public CSB revision and build graph, expose only a bounded
version-negotiated subprocess protocol, and prove containment, cancellation, recovery, artifact,
path, and privacy behavior before ASB may invoke CSB.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-07T06:07:58+00:00: Coordinator verified AR-0603 dependencies, ownership isolation, and
  user authorization; promote for contracts worker.

- 2026-09-07T06:08:42+00:00: Claimed by contracts-20260906.

- 2026-09-07T06:09:03+00:00: Recorded command exit 0; command argv SHA-256
  456777cb1fc425f81a3c32ba739ecc38b8819118384de19f77b6dbf74d105241.

- 2026-09-07T06:09:47+00:00: Recorded command exit 0; command argv SHA-256
  dbd573af68275a803470007808b024658cc936b348b7eaa681f44480393da696.

- 2026-09-07T06:10:24+00:00: Recorded command exit 0; command argv SHA-256
  ab3f40c0f399fa2c95c83f81150268c71c39dd4fc742b49a5ddd8efb0011ca87.

- 2026-09-07T06:11:04+00:00: Released before product mutation so the newly authorized runner
  activation can take priority. Preserved external research clone
  /srv/data/projects/.asb-local/csb-ar0603-source at official https://github.com/martin-beck/CSB.git
  commit d577c5249501b29e33a87524a677a101477d5579, tree 97d08b39026f7c7d3e6f748b26a20e819a92184f,
  release message v0.4.0, root MIT license, and declared submodule commits 41fee1f9 FlameGraph,
  cebe6d15 benchkit, 49741843 inferno, 44df4dbc syzkaller (not initialized yet). requirements.txt
  remains incompletely pinned, so offline reproducibility is unproven. One checkout attempt used an
  invalid relative handoffctl path and caused no mutation; the absolute wrapped retry succeeded.
  Declared product worktree remains clean at base 814397f with no AR-0603 files. Next action:
  re-claim, initialize and license-audit the complete source graph, then implement the bounded
  version-negotiated subprocess contract under the existing Cargo/schema fence.

- 2026-09-07T06:12:01+00:00: Claimed by contracts-20260906.

- 2026-09-07T06:13:08+00:00: Recorded command exit 0; command argv SHA-256
  8f6d165f368e612e351299eb362c6e5d00629ad90b3554116d933dffd379caae.

- 2026-09-07T06:13:13+00:00: Recorded command exit 0; command argv SHA-256
  de1523e77860b7acb15de2a930a1be5dba0af31cea316857117658c58edcbac3.

- 2026-09-07T06:13:40+00:00: Priority switch to authorized AR-0830 runner repair before product
  mutation. Preserved fully initialized official CSB graph at
  /srv/data/projects/.asb-local/csb-ar0603-source: root d577c524/tree 97d08b39; FlameGraph
  41fee1f9/tree 85d36fd0; benchkit cebe6d15/tree d82f2d7c; inferno 49741843/tree 3e271fe6; nested
  FlameGraph 57207afb/tree 32a15a83; syzkaller 44df4dbc/tree 9586b54e. Root, benchkit, inferno and
  syzkaller licenses located; FlameGraph license provenance still requires inspection. Root
  requirements remain mostly floating and offline reproducibility unproven. Wrapped submodule
  command completed, while its evidence push reported a stale expected ref although remote already
  contained the exact commit; reconcile reached a8a440c5. Declared product worktree remains clean at
  814397f. Next action: license/dependency inventory and bounded subprocess contract after reclaim.

- 2026-09-07T06:23:46+00:00: Claimed by contracts-20260906.

- 2026-09-07T06:24:56+00:00: Recorded command exit 0; command argv SHA-256
  4226ddb9a5b88305eb975651b62ce3d098b097e328110b2d7188fa7316fef92e.

- 2026-09-07T06:25:13+00:00: Recorded command exit 0; command argv SHA-256
  bc57e757e58aa8a5f5e403d2558066455b858407d0af4b48abd9e629b743801d.

- 2026-09-07T06:25:25+00:00: Recorded command exit 0; command argv SHA-256
  fd2f55682c2f04b841eeda5027efdce47197620ef0c8d3575c76d7150f100d20.

- 2026-09-07T06:25:35+00:00: Recorded command exit 0; command argv SHA-256
  1c179dfa6d247d855d7a5c8ff781ca6f74ebe65dc5de89ff6a30b94a58c198df.

- 2026-09-07T06:25:51+00:00: Signed+DCO product checkpoint 939c35c5ee64c9f9685cec471efc03cb620643c2
  records official CSB d577c524/tree 97d08b39 and the complete initialized submodule commit/tree
  graph, license boundaries, floating Python dependency limitation, unsupported
  generator/syzkaller/monitor/platform claims, and four bounded JSON-RPC fixture envelopes.
  Wrapper-run jq parsing, 64 KiB fixture cap, diff/privacy checks passed; worktree is clean. No
  offline reproducible upstream Python environment or executable digest is claimed yet.

- 2026-09-07T06:26:10+00:00: Release after signed+DCO CSB provenance checkpoint 939c35c; switch
  worker to authorized AR-0830 repair and online canary.

- 2026-09-07T06:31:31+00:00: Claimed by contracts-20260906.

- 2026-09-07T06:34:17+00:00: Recorded command exit 128; command argv SHA-256
  afa18a275766dd40e288b86f30721db3d0f8ea218fa55df6a198f9080403a6d8.

- 2026-09-07T06:34:54+00:00: First isolated crate patch application failed before product mutation
  because its generated unified-diff hunk counts were incorrect (git apply reported a corrupt
  patch). Product worktree remains clean at 939c35c. The scratch patch was inspected and corrected
  to exact 17/18/296-line hunk counts; next action is git apply --check followed by one wrapped
  apply, not a blind replay.

- 2026-09-07T06:35:10+00:00: Recorded command exit 0; command argv SHA-256
  afa18a275766dd40e288b86f30721db3d0f8ea218fa55df6a198f9080403a6d8.

- 2026-09-07T06:35:26+00:00: Recorded command exit 1; command argv SHA-256
  f1f9ddeeb35a7a2a0e36bd4138e2d897dba6d44b3558046fe6ffda086f7dc7cd.

- 2026-09-07T06:35:36+00:00: Recorded command exit 1; command argv SHA-256
  391271fde14b43153d72996ebb6e7762ebae2d15fe3d3b7ad84115b055bb4ea1.

- 2026-09-07T06:35:42+00:00: Coordinator elevates authorized AR-0830 runner startup repair and
  online canary; preserve CSB checkpoint and return to it after runner evidence.

- 2026-09-07T08:44:22+00:00: Claimed by contracts-20260906.

- 2026-09-07T08:45:51+00:00: Fresh audit at claimed revision 31 found exact head 939c35c with three
  untracked asb-csb-runner files and no live CSB process. The already-applied boundary patch has
  SHA-256 2c9214895a70c1c4ca399a71d705dd1aa44c02dfcc7e783044ddb3b285fdb182; git apply --check
  rejects it because all target files already exist, so it must not be replayed. The saved
  completion patch SHA-256 6b2778635ea8200b7cdc5b1de3ec9ecf0103bf9c31e449063a90611a01091b is still
  corrupt at line 42, and src/lib.rs is truncated at line 296 inside the environment negative.
  Preserve the existing effect and reconstruct only the intended missing test tail before isolated
  validation. Root Cargo/lock/schema remain fenced.

- 2026-09-07T08:46:36+00:00: Recorded command exit 0; command argv SHA-256
  1788d9ca4ddaaa55f5f304aeb782043fd81db97061a782ec721ee81b7d2d48f2.

- 2026-09-07T08:49:07+00:00: Recorded command exit 127; command argv SHA-256
  e6e82f56418c7ecc3f13fae8ecad5435beeb90d722c3b75c8284e74d4b5aee7a.

- 2026-09-07T08:49:22+00:00: Isolated mirror test command exited 127 before compilation because
  cargo was absent from the wrapped PATH. Product worktree content did not change; disposable mirror
  remains under /srv/data/projects/.asb-local. Retry once with explicit
  /srv/data/projects/.asb-local/cargo/bin/cargo and pinned CARGO_HOME/RUSTUP_HOME.

- 2026-09-07T08:49:39+00:00: Recorded command exit 101; command argv SHA-256
  5119c32d316a7bda8d1d4c1f81377e487e3b29b09545a943bf2ddd7c33043957.

- 2026-09-07T08:49:54+00:00: Pinned Cargo invocation reached dependency resolution but --locked
  correctly refused because the disposable mirror's copied lock does not yet include the new
  workspace member. It attempted only the public crates.io index and did not compile or mutate the
  product worktree. Generate the mirror-only lock offline from the pinned cache, then run locked
  tests; root Cargo.toml/Cargo.lock remain fenced.

- 2026-09-07T08:50:20+00:00: Recorded command exit 101; command argv SHA-256
  02b40a9de082559413ce0a1c92ea6e157f10b4abf8cfb1981cbbbdc476bdcfaf.

- 2026-09-07T08:51:13+00:00: Mirror compilation exposed an unclosed delimiter at src/lib.rs:325.
  Audit showed the preserved completion patch header declared 34 new lines although the hunk
  contains 36; git apply had accepted only through the final assertion and omitted the
  function/module closing braces. Product worktree remains an uncommitted scaffold. Apply only a
  two-line closing-delimiter patch, refresh the mirror, and rerun locked offline tests.

- 2026-09-07T08:51:39+00:00: Recorded command exit 0; command argv SHA-256
  7e9cc4e0071bcb150caa86da3ec3872a92a4af4ebf7b0518baf3bd3ca6e9b2ed.

- 2026-09-07T08:54:46+00:00: Recorded command exit 128; command argv SHA-256
  b51ad9d4acf6a9b06611f304679fce6017aaea4d3f3019de40fae2c648ba5063.

- 2026-09-07T08:55:47+00:00: Recorded command exit 0; command argv SHA-256
  b51ad9d4acf6a9b06611f304679fce6017aaea4d3f3019de40fae2c648ba5063.

- 2026-09-07T08:56:07+00:00: Recorded command exit 1; command argv SHA-256
  b7703ce76f5cdd41a09ed979882f1e040de580ff7441a11ac5172c634e0cd288.

- 2026-09-07T08:56:24+00:00: Recorded command exit 0; command argv SHA-256
  71ab8858219553f87e63619e7932e17bc4e94053ea388f5a8e0edd978b0bfbba.

- 2026-09-07T08:56:49+00:00: Recorded command exit 0; command argv SHA-256
  b7703ce76f5cdd41a09ed979882f1e040de580ff7441a11ac5172c634e0cd288.

- 2026-09-07T08:57:13+00:00: Recorded command exit 101; command argv SHA-256
  a2aff4439721207ceeca6d51acbfe33750c54ff03d7bd398f2088e2cf1e79134.

- 2026-09-07T08:57:55+00:00: Recorded command exit 0; command argv SHA-256
  1c943e7e0e04bbe34ab45048f2de069c0e1bf68b3e3bcec5c6e5a96ae5354f1b.

- 2026-09-07T08:58:17+00:00: Recorded command exit 0; command argv SHA-256
  c98acca73d3217974cf79334ede91a5a601afa6ab49f87890b6f3df59ceae047.

- 2026-09-07T09:00:13+00:00: Recorded command exit 0; command argv SHA-256
  85fde7eacc44b2d420d84812ebec1d743936fb4bef4ea5f230d6826192e5c1d5.

- 2026-09-07T09:00:35+00:00: Recorded command exit 0; command argv SHA-256
  e85637054673fde70c8639c4932bc838d7559f6a3e43afd3a7f68a58d3788982.

- 2026-09-07T09:00:59+00:00: Recorded command exit 2; command argv SHA-256
  e19585636533e0d955f6502aeb4f9c0936fc634030aa057f55ac930018558071.

- 2026-09-07T09:01:27+00:00: Recorded command exit 128; command argv SHA-256
  feae5cb7320d53e83333613e5b155b0e997c6d9b3c0d6ac9818e86dac87c8443.

- 2026-09-07T09:02:03+00:00: Recorded command exit 0; command argv SHA-256
  feae5cb7320d53e83333613e5b155b0e997c6d9b3c0d6ac9818e86dac87c8443.

- 2026-09-07T09:02:44+00:00: Signed+DCO product checkpoint efa8f9636741d65786293067d82d7454c86bd2ef
  adds only crates/asb-csb-runner/{Cargo.toml,README.md,src/lib.rs} atop provenance checkpoint
  939c35c. It enforces v1 negotiation-first admission, strict peer-limit intersection, non-forgeable
  validated requests, bounded arguments/environment/artifact paths/frame size,
  duplicate/stale/unknown causal fencing, negotiated in-flight capacity, and a 4096-operation
  lifetime ceiling. Disposable offline mirror under /srv/data/projects passed stable fmt, Clippy -D
  warnings, 15 unit tests, doctests, rustdoc -D warnings; pinned nightly branch coverage is 98.48%
  (99.75% lines). Worktree is clean; root Cargo/lock/schema unchanged. This is a partial checkpoint
  only: no subprocess, durable intent, sandbox, artifact, cancellation, recovery, or native platform
  claim yet.

- 2026-09-07T09:05:48+00:00: Recorded command exit 0; command argv SHA-256
  8a7bae044a6c4fc25a6ec1d30a4f205b8340f6aca7e47e1f2c938f4321efec44.

- 2026-09-07T09:06:32+00:00: Recorded command exit 0; command argv SHA-256
  a544d753ee288265b71d8cdc6f82a50cb15bf06948446690a746d524e7711a18.

- 2026-09-07T09:08:18+00:00: Recorded command exit 0; command argv SHA-256
  01879949a94d2260f32ece699abed918e9d35c407351c700a211d84c9450d05e.

- 2026-09-07T09:08:58+00:00: Recorded command exit 0; command argv SHA-256
  df9737dab5a6f17cb74b887df76705a894a1eddc7b943119aea5be22f482d82b.

- 2026-09-07T09:09:53+00:00: Recorded command exit 0; command argv SHA-256
  c0a2df1a6a86ecc8f5f64c523979034bddbf2c6b308c664b8797485acd4d5efd.

- 2026-09-07T09:10:58+00:00: Recorded command exit 0; command argv SHA-256
  82b53fb1f8e055207f4fa119742a22bbb57f3029f4bde2da31769d62e3e98699.
