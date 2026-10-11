---
{
  "branch": "codex/ar-1449-current-main",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1443",
    "AR-1448"
  ],
  "id": "AR-1449",
  "next_action": "Requalify the current protected-main runtime-owned replay provisioner against generated cassettes; repair any strict offline authority failure, then independently review and run exact-head CI.",
  "observed_branch": "codex/ar-1449-current-main",
  "observed_dirty": 0,
  "observed_head": "59cfd9cf6f068ff8945eb093a04f0bbb0c7bb7c1",
  "owner": "",
  "plan": "../plans/AR-1449.md",
  "priority": "P1",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "quality",
    "evidence_digest": "sha256:5b93d20e8910a526b16ffc3502389e5c939fd6b66bbe5f66decdfd25b11e150e",
    "evidence_ref": "quality/AR-1449-current-main-requalification.json",
    "spec_ref": "specs/AR-1449.json",
    "spec_revision": 1,
    "status": "pass"
  },
  "spec_ref": "specs/AR-1449.json",
  "spec_revision": 1,
  "status": "done",
  "summary": "Provide fail-closed runtime-owned local replay authority for the guided CLI wrapper.",
  "task_revision": 35,
  "title": "Runtime-owned local replay CLI authority",
  "updated_at": "2026-10-10T23:13:13+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1449-current-main"
}
---
AR-1338 exposes the guided replay route, but the normal argument-only CLI intentionally receives no ReplayLaunchAuthority. This successor must provide a runtime-owned local deterministic replay acquisition boundary using the existing AR-1448 source and AR-1443 replay contracts.

Requirements:
- derive cassette identity from the validated cassette before any authority issuance;
- acquire bounded private relay, benchmark lease, network-denied sandbox input and runtime attestation inside the runtime boundary;
- inject one-shot authority into the ordinary CLI without accepting caller-built authority or secret bytes;
- preserve strict replay, cancellation, teardown, path confinement, offline operation and direct or alternate egress denial;
- provide positive and hostile tests for stale, copied, mismatched and unavailable authority;
- use local deterministic fixtures or LiteLLM-compatible mocks only; external providers and native hosts are not required.

Do not weaken AR-1448 or make live provider reachability a prerequisite.

- 2026-09-25T16:55:07+00:00: Claimed by ar1449-replay-luna56.

- 2026-09-25T16:56:36+00:00: Independent audit: AR-1448 ReplayAuthoritySource::issue requires
  caller-built SandboxLaunchInput, benchmark ResourceLease, SandboxBackend and relay attestation;
  ordinary CLI cannot safely acquire these. Promote a runtime-owned local replay acquisition factory
  successor; no product changes made.

- 2026-10-10T22:58:00+00:00: Dependencies AR-1443 and AR-1448 are complete. Promote runtime-owned
  local replay authority repair to unblock AR-1698; local/mock fixtures are sufficient and no GitHub
  Reviews API approval object is required.

- 2026-10-10T22:59:56+00:00: Claimed by codex-ar1449-runtime-replay-20261011.

- 2026-10-10T23:01:02+00:00: Recorded command exit 1; command argv SHA-256
  ebdb48c305bb702bc79c10e4a2331535c714ba52d210160e798693a9184f5d73.

- 2026-10-10T23:01:13+00:00: Recorded command exit 0; command argv SHA-256
  c89423b254146cbfb809f17acb09745c0d3b147e4b8e52b9bdc18a181394fc84.

- 2026-10-10T23:01:16+00:00: Recorded command exit 0; command argv SHA-256
  2b245f3f633ccd5d4e76b46865b4c38975ea764a922263c5a2cb4b711d4b3167.

- 2026-10-10T23:01:25+00:00: Recorded command exit 0; command argv SHA-256
  9e77938986d4d8c61d283d8de879bbdcfb3764435aa5a0b61dfb57124ce2cf7f.

- 2026-10-10T23:01:35+00:00: Recorded command exit 1; command argv SHA-256
  b7c438686581cf292b6cd41497ceabb3af42dfed57e04dfd6cc89efed8e2d15b.

- 2026-10-10T23:02:14+00:00: Terminal blocker: declared
  feature/ar-1449-runtime-owned-local-replay-cli is an unrelated-history stale branch (HEAD
  f03d9e484d6ca73eacdbd5476980bf33ca737540; origin/main 59cfd9cf6f068ff8945eb093a04f0bbb0c7bb7c1). A
  handoffctl-wrapped rebase onto origin/main stopped at commit 2579362d with hundreds of add/add
  conflicts across the repository; minimal git rebase --abort recovery restored clean declared
  worktree. No product mutation was published. Current protected origin/main already contains
  runtime-owned LocalReplayProvisioner/development_fixture acquisition and guided replay wiring
  (03d98ac7 and descendants), so cherry-picking onto this unrelated branch is unsafe. Requires
  coordinator rebind/rebase successor; preserve AR-1791 unrelated dirty state.

- 2026-10-10T23:03:44+00:00: Claimed by codex-ar1449-rebind.

- 2026-10-10T23:03:47+00:00: Recorded command exit 0; command argv SHA-256
  74dcd1cb28fa2fad4b01a1261e8fa21822af4c19bc8a7c826b6f4129e8f8ca8b.

- 2026-10-10T23:03:54+00:00: Recorded command exit 1; command argv SHA-256
  a1971ccc85a0b7970f0999a449d90195e58b810afb183deea60b803f531af2af.

- 2026-10-10T23:04:02+00:00: Recorded command exit 0; command argv SHA-256
  7a147ab4419597fad6c3452d0c44b3d91672c596be6055fbca205ab54b9c1dbd.

- 2026-10-10T23:04:09+00:00: Rebound stale AR-1449 metadata to current protected-main
  branch/worktree; worker may now requalify the existing runtime-owned replay provisioner.

- 2026-10-10T23:04:16+00:00: Claimed by codex-ar1449-runtime-replay-20261011.

- 2026-10-10T23:04:48+00:00: Recorded command exit 0; command argv SHA-256
  d601e73c1529f9a94970e083ddb746e882265236602e0e36210f94a43091d277.

- 2026-10-10T23:04:57+00:00: Recorded command exit 0; command argv SHA-256
  566ece1ae4fb36cae1b47bba5a6bdd814700d6910d2c20f379c36b87d1d354f5.

- 2026-10-10T23:05:10+00:00: Recorded command exit 0; command argv SHA-256
  a706c985e5e58974dfcc39900f77a6ac866f9ed84272aa11209f30c82d44bef9.

- 2026-10-10T23:06:03+00:00: Recorded command exit 0; command argv SHA-256
  6163502e0cc7ce887e4607b2a38eb2e4c876907e62dbda1046460cc780b76888.

- 2026-10-10T23:06:13+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-10-10T23:06:27+00:00: AR-1449 exact-head requalification is terminally green but done
  admission is blocked by coordinator gate: spec_acceptance is incomplete or unknown. Evidence:
  protected current-main 59cfd9cf6f068ff8945eb093a04f0bbb0c7bb7c1 in isolated worktree
  /srv/data/projects/agent-systems-benchmark-ar-1449-current-main; SSH signature good (ED25519
  SHA256:a36V6yPvRZyxnQ2113tiA/MlHt7mPfJEXAGByBXVkuE), Signed-off-by matches; focused CLI
  guided_local_replay_uses_runtime_owned_fixture_seam 1 passed; focused runtime launch_factory 21
  passed/1 ignored native bwrap; exact-head cargo test --workspace --all-targets passed with only
  explicit unavailable native/external ignores; cargo fmt check passed; worktree clean and no
  product diff required because runtime-owned LocalReplayProvisioner/development_fixture and guided
  replay integration are already on protected head. Coordinator must complete spec_acceptance or
  accept no-op requalification; no merge/API approval object was needed.

- 2026-10-10T23:12:33+00:00: Spec and privacy-safe exact-main receipt are now present;
  requalification is terminal green. Admit the existing runtime-owned replay implementation without
  a PR or GitHub Reviews API approval object.

- 2026-10-10T23:12:36+00:00: Claimed by codex-ar1449-final.

- 2026-10-10T23:12:47+00:00: Recorded command exit 0; command argv SHA-256
  74dcd1cb28fa2fad4b01a1261e8fa21822af4c19bc8a7c826b6f4129e8f8ca8b.

- 2026-10-10T23:12:54+00:00: Recorded command exit 1; command argv SHA-256
  ea46d009fa95347762ef8ec0148e1e47b0d5dd359d2b3f9e65357ffd30552339.

- 2026-10-10T23:13:10+00:00: Exact-main requalification passed guided replay, launch-factory, full
  workspace, fmt, signatures/DCO, privacy, and clean-diff gates; implementation is already
  integrated and no API approval object is required.

- 2026-10-10T23:13:13+00:00: AR-1449 complete via exact-main requalification; no product diff, PR,
  merge, provider traffic, or GitHub Reviews API approval was required.
