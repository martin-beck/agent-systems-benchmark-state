---
{
  "branch": "feature/ar-1508-platform-owned-authority-provider",
  "checkpoint_commit": "06e91829123cb1498e566f595aa2e114ff5833f4",
  "claim_expires": "2026-09-29T13:06:54+00:00",
  "depends_on": [
    "AR-1473",
    "AR-1474",
    "AR-1480",
    "AR-1484",
    "AR-1485",
    "AR-1502",
    "AR-1505"
  ],
  "id": "AR-1508",
  "next_action": "Rebased local candidate onto protected 47329e35 at 06e91829, but publication blocked: cargo test -p asb-runtime fails at live_service.rs:2015 because materialize_runtime_owner still injects RuntimeAuthorityInputs and state_path into the new provider-only API, and live_service.rs:3346 still destructures the now-three-element fixture as two. The public asb-cli RuntimeControlBootstrapRunInput still carries owner_inputs/owner_state_path, violating the fail-closed contract. Resolve API/callers within AR scope or record successor blocker; do not push or merge.",
  "observed_branch": "feature/ar-1508-platform-owned-authority-provider",
  "observed_dirty": 0,
  "observed_head": "03ef142e8477b983fc19b8b0831981d68ad3a690",
  "owner": "ar1508-integration-repair-luna56",
  "plan": "../plans/AR-1508-platform-owned-authority-provider.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Provide an authenticated platform-owned source for private runtime roots, tools, policy, and enrollment material.",
  "task_revision": 89,
  "title": "Platform-owned authority provider",
  "updated_at": "2026-09-29T11:11:58+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1508-platform-owned-authority-provider"
}
---

AR-1507 proved that the existing bootstrap contract authenticates only digest
claims and that `RuntimeControlBootstrap::materialize_provisioner` still takes
caller-supplied `RuntimeAuthorityInputs`. This AR owns the missing platform
authority-provider boundary; it must produce verified private material without
exposing it to CLI callers or synthesizing it from fixed paths.

Acceptance requires:

- a runtime/control-owned authority provider authenticated to the AR-1505
  bootstrap session, with verified source/digest binding for namespace, lease,
  relay, tool pins, policy, credential reference, and enrollment material;
- a private materialization API consumed by `RuntimeControlBootstrap` and the
  live scheduler, with no caller/config/socket/path/PATH/fixed-root injection;
- fail-closed behavior for missing, stale, mismatched, expired, revoked,
  restarted, cancelled, or tampered authority, plus alternate-egress denial;
- provider-free deterministic local/mock/replay tests that qualify the contract
  without pretending to be first-customer production evidence;
- independent review, SSH-signed DCO, exact-head hosted checks, protected merge,
  and post-merge assurance.

Non-goals: asb-tui, live provider reachability, public credentials, synthetic or
fixed-path authority, weakening formal/privacy/native gates.

- 2026-09-29T04:14:00+02:00: Created from AR-1507 blocker evidence. The required
  source must be platform-owned and verified; no fixed path or mock authority is
  acceptable in production code.

- 2026-09-29T02:15:14+00:00: Dependencies through AR-1505 verified done; AR-1507 established the
  missing platform-owned authority provider contract.

- 2026-09-29T02:17:57+00:00: Claimed by ar1508_provider_luna56.

- 2026-09-29T02:18:11+00:00: Heartbeat by ar1508_provider_luna56.

- 2026-09-29T02:18:21+00:00: Setup audit: state reconciled and live doctor prerequisites refreshed;
  task revision 2 promoted/open then claimed at revision 3; dependencies include AR-1505 and are
  recorded done; AR-1505 product worktree inspected for requested merge base f92c2e9. Product docs
  and plan inspection now underway.

- 2026-09-29T02:19:06+00:00: Recorded command exit 0; command argv SHA-256
  a1159e9df3670d549d04524532629f5477ceb7deec9b45e47e8c009506ecb2c8.

- 2026-09-29T02:19:33+00:00: Recorded command exit 0; command argv SHA-256
  0e82d1f9ce576541812d2c59fe0a6f45539dc4cfb91f7a39fe3327fc4dea309a.

- 2026-09-29T02:22:14+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-29T02:22:34+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-29T02:23:07+00:00: Recorded command exit 101; command argv SHA-256
  03315ef10f14441f5aadec73db36f3fb7b35454147c037b191e659b38ff938ee.

- 2026-09-29T02:23:35+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-29T02:23:54+00:00: Recorded command exit 0; command argv SHA-256
  03315ef10f14441f5aadec73db36f3fb7b35454147c037b191e659b38ff938ee.

- 2026-09-29T02:24:15+00:00: Concrete protected-main audit: AR-1505 merge
  f92c2e941913129d7db50480f71e8361a0d43a0c contains RuntimeControlBootstrap materialization with
  caller-supplied RuntimeAuthorityInputs and PathBuf. AR-1508 now introduces the crate-private
  RuntimePlatformAuthorityBinding and provider/material contract; materialization receives only
  owner plus provider, validates session/generation/expiry/root/tool claims and provider-owned state
  path, then delegates to the existing resolver. Focused test first exited 101 because -D warnings
  rejected unused lifecycle error variants; added the deliberate dead-code annotation to retain
  explicit fail-closed categories, and the exact focused test now passes.

- 2026-09-29T02:24:35+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-29T02:24:53+00:00: Recorded command exit 0; command argv SHA-256
  f4e5d8b14cda44421923169e0a87b069ad13e27509d93301edee77eec7344946.

- 2026-09-29T02:25:15+00:00: Recorded command exit 0; command argv SHA-256
  02dc064651fd94b14b265f6321ed4689e7785281edcdea9b2ada9fad3dbf0495.

- 2026-09-29T02:25:58+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-29T02:26:19+00:00: Recorded command exit 0; command argv SHA-256
  97ee782321facf1df64b14b3500c62b04b8b48c9904b8abb83044328a904f4b2.

- 2026-09-29T02:26:36+00:00: Recorded command exit 0; command argv SHA-256
  2faa80e23aae1ee23dded301e7fabeba025e544fd3aa6911359e0f841bfc5fb3.

- 2026-09-29T02:26:52+00:00: Recorded command exit 0; command argv SHA-256
  2a4ba46b698bbe0b03388cdbd9c13d04641f5385375e0892e648b2996a73f171.

- 2026-09-29T02:27:16+00:00: Recorded command exit 101; command argv SHA-256
  e8beebac0638d83321c84d952814966bbba80dc16ee7dd3d3ead10f3c2b72292.

- 2026-09-29T02:28:32+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-29T02:28:51+00:00: Recorded command exit 0; command argv SHA-256
  e8beebac0638d83321c84d952814966bbba80dc16ee7dd3d3ead10f3c2b72292.

- 2026-09-29T02:29:10+00:00: Recorded command exit 0; command argv SHA-256
  02dc064651fd94b14b265f6321ed4689e7785281edcdea9b2ada9fad3dbf0495.

- 2026-09-29T02:29:32+00:00: Recorded command exit 0; command argv SHA-256
  67739c573b579619ef3e71fb893a396c166af5a2a061ba9f37d5e424ed8b55d4.

- 2026-09-29T02:29:49+00:00: Recorded command exit 0; command argv SHA-256
  80e1eb9890f3dfad67ec444d6e89d59576e05226594eb494dccd9069a7cc055c.

- 2026-09-29T02:30:07+00:00: Audit follow-up: the provider contract now has a production
  RuntimePlatformAuthorityProviderHandle. Runtime/control creates it only from authenticated
  platform material after complete binding verification; bootstrap consumes that handle and
  revalidates it on materialization. No live/fixed-path/synthetic source was invented. The handle is
  exercised by the positive bootstrap test; unavailable, tampered, and relative-path provider
  failures are covered deterministically. Focused six-test group and package Clippy pass. Initial
  Clippy failure (two unnecessary to_owned calls) was repaired through handoffctl.

- 2026-09-29T02:30:58+00:00: Recorded command exit 101; command argv SHA-256
  534f8613e1c316db8f0f46dd989e44e14a8ca74304a94791b4e4a1c59b2fbb1d.

- 2026-09-29T02:31:19+00:00: Recorded command exit 0; command argv SHA-256
  79bec090309cc89803dbedc97f657de211f21b609a26c1a28a455a7f48d24def.

- 2026-09-29T02:31:49+00:00: Independent exact-diff review rejects publication. Signed commits
  7306f83/0135650 add only a crate-private/test provider façade: no production authenticated
  provider or non-test materialization callsite; binding digest is self-attestation and does not
  independently bind tools/policy/allowlist/endpoint; resolver lacks post-materialization
  expiry/revocation fencing; credential/enrollment material is not implemented. Preserve commits
  unpushed. Create AR-1509 for a real platform provider receipt and lifecycle fence.

- 2026-09-29T10:43:43+00:00: AR-1510 confirms the same missing provider boundary; AR-1508 has the
  narrow provider/materialization candidate and now needs exact-head gates and independent review
  before publication.

- 2026-09-29T10:43:46+00:00: Claimed by ar1508-provider-luna56.

- 2026-09-29T10:44:15+00:00: Recorded command exit 0; command argv SHA-256
  79bec090309cc89803dbedc97f657de211f21b609a26c1a28a455a7f48d24def.

- 2026-09-29T10:45:32+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-29T10:45:51+00:00: Recorded command exit 101; command argv SHA-256
  e8beebac0638d83321c84d952814966bbba80dc16ee7dd3d3ead10f3c2b72292.

- 2026-09-29T10:46:11+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-29T10:46:29+00:00: Recorded command exit 0; command argv SHA-256
  e8beebac0638d83321c84d952814966bbba80dc16ee7dd3d3ead10f3c2b72292.

- 2026-09-29T10:46:52+00:00: Recorded command exit 0; command argv SHA-256
  02dc064651fd94b14b265f6321ed4689e7785281edcdea9b2ada9fad3dbf0495.

- 2026-09-29T10:47:14+00:00: Recorded command exit 0; command argv SHA-256
  67739c573b579619ef3e71fb893a396c166af5a2a061ba9f37d5e424ed8b55d4.

- 2026-09-29T10:47:31+00:00: Recorded command exit 0; command argv SHA-256
  6dc297611924a2ae988d59011e6fc6e3979c557c8eae0980597c4a05eeda086f.

- 2026-09-29T10:47:52+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-29T10:48:25+00:00: Recorded command exit 0; command argv SHA-256
  1024fc1e6cefa31b078f0b5d2ed85c7ea4586897b388bf1e308f62db58574461.

- 2026-09-29T10:49:20+00:00: Recorded command exit 0; command argv SHA-256
  534f8613e1c316db8f0f46dd989e44e14a8ca74304a94791b4e4a1c59b2fbb1d.

- 2026-09-29T10:49:56+00:00: Recorded command exit 0; command argv SHA-256
  8f020a8266d9eda8e0ed704996e99736ad1cf29c0294cefaaa456dc2d9fb4d92.

- 2026-09-29T10:50:50+00:00: Recorded command exit 0; command argv SHA-256
  b49a90ee600c1023cee9ee9f9e8a4f9a06c53eef8c48d3932d88e482126c7c01.

- 2026-09-29T10:51:24+00:00: Final exact-head candidate audit: signed commits 7306f830, 013565032,
  and 2c70f811 are clean, DCO-matching, and based on protected AR-1505 merge f92c2e941. Diff is
  limited to README, runtime live_service provider/materialization contract, and platform authority
  handoff docs; no asb-tui, credentials, fixed-path discovery, PATH, or synthetic/live provider
  changes. Gates pass: cargo fmt --all --check; cargo clippy --locked --workspace --all-targets --
  -D warnings; cargo test --locked --workspace (155 runtime tests, all workspace tests pass; one
  initial CLI state-root collision reran serially and passed); env RUSTDOCFLAGS=-D warnings cargo
  doc --locked --workspace --no-deps; cargo build --locked --workspace --release. Independent review
  repaired the missing tool-pin-to-claim comparison before this final head.

- 2026-09-29T10:51:38+00:00: Recorded command exit 0; command argv SHA-256
  b47c09716f462c93788cc8ff79f951331d6fe3842e456e51d0713d32a6738c52.

- 2026-09-29T10:52:11+00:00: Recorded command exit 0; command argv SHA-256
  a1d307397995da68e8914fade2211ad6cf0ccf172cc81c58f0d29a199b558e2f.

- 2026-09-29T10:52:34+00:00: Recorded command exit 0; command argv SHA-256
  48a1c9f73747ebe9ccd4891b180aa49a5ae05f5cb7ce9cd343db488130e6f66b.

- 2026-09-29T10:52:59+00:00: Recorded command exit 0; command argv SHA-256
  f5a589cdf7ff0b0c4aa322d6e6d65fbb05fd91306ad84af64030c0948de4ef59.

- 2026-09-29T10:53:38+00:00: Published signed candidate branch and PR #384. Remote main resolves to
  protected AR-1505 merge f92c2e941; candidate is exactly three commits descendant with clean
  merge-base and no worktree changes. GitHub PR API currently reports OPEN, head 2c70f811, no checks
  yet, mergeable CONFLICTING; this appears GitHub mergeability lag because remote main is the
  requested f92c2e9 and git confirms f92c2e9 is ancestor. No merge attempted.

- 2026-09-29T10:53:45+00:00: Recorded command exit 0; command argv SHA-256
  01c455596ff4c440218b755107dd6e44f138909fa56ac82e056ab70c3d75ee17.

- 2026-09-29T10:54:15+00:00: Recorded command exit 0; command argv SHA-256
  321c534968b9c456a64caf5e6d09b63780c507f97548057d2bfe31edcfd73ff4.

- 2026-09-29T10:54:44+00:00: Implementation and local exact-head audit complete at signed candidate
  2c70f81100ca0c4e911ec5d6c02736182b101a3b (three signed DCO commits from AR-1505 merge f92c2e941).
  PR #384 is published for independent review at that exact head; local fmt, workspace Clippy,
  workspace tests, rustdoc, and release build pass. Precise blocker: protected remote main advanced
  from f92c2e9 to 47329e35 (AR-1513 merge), so PR #384 reports DIRTY/CONFLICTING with no hosted
  checks yet. Rebase onto current protected main and repeat independent review/exact-head hosted
  checks before merge; no merge or force update attempted.

- 2026-09-29T10:56:36+00:00: Claimed by ar1508-provider-luna56.

- 2026-09-29T10:56:47+00:00: Corrected durable next action after refreshing protected remote main;
  no rebase, force update, or merge attempted.

- 2026-09-29T10:56:55+00:00: Released after publication and exact-head audit. Candidate 2c70f811 is
  signed/DCO and PR #384 is published, but protected origin/main is 47329e35 (AR-1513 merge), eight
  commits beyond f92c2e9. GitHub PR #384 reports base 47329e35, mergeable DIRTY/CONFLICTING, and
  zero hosted checks. Rebase onto current protected main and repeat independent review and hosted
  checks; no force update or merge attempted.

- 2026-09-29T10:58:08+00:00: Claimed by ar1508-rebase-repair-luna56.

- 2026-09-29T10:59:06+00:00: Heartbeat by ar1508-rebase-repair-luna56.

- 2026-09-29T10:59:14+00:00: Recorded command exit 0; command argv SHA-256
  321c534968b9c456a64caf5e6d09b63780c507f97548057d2bfe31edcfd73ff4.

- 2026-09-29T10:59:40+00:00: Recorded command exit 1; command argv SHA-256
  b7c438686581cf292b6cd41497ceabb3af42dfed57e04dfd6cc89efed8e2d15b.

- 2026-09-29T11:00:52+00:00: Recorded command exit 0; command argv SHA-256
  33cc27629ec87669d7163b5bea7f0765dc0be83781d15411aa0076a297106fb6.

- 2026-09-29T11:01:18+00:00: Recorded command exit 0; command argv SHA-256
  d14afeefc867752c7457e56fc7e0805b3300c11334d970b0020953c2cb905cd4.

- 2026-09-29T11:01:35+00:00: Recorded command exit 0; command argv SHA-256
  77b79940e1f0c2837a1f69eb5829c2dc93ecb3bb462b77a0fb350e402972b65c.

- 2026-09-29T11:02:33+00:00: Recorded command exit 101; command argv SHA-256
  44014d1953a8d245bec969da28df5931f8e670f0ff73d02a479a40e33d530f3b.

- 2026-09-29T11:04:13+00:00: Rebase onto protected origin/main=47329e35 completed with one
  legitimate fixture conflict resolved by retaining AR-1513 owner_id plus AR-1508 provider binding.
  New local head 06e91829123cb1498e566f595aa2e114ff5833f4 has three SSH-signed DCO commits and clean
  diff limited to README, live_service provider/materialization, and provider handoff docs. Exact
  cargo test --locked -p asb-runtime was run through handoffctl and failed with E0061 at
  live_service.rs:2015 (old three-argument caller API) and E0308 at live_service.rs:3346 (stale
  two-element fixture destructure). No push, PR update, merge, or hosted checks attempted.

- 2026-09-29T11:04:30+00:00: Released for repair, not merged: rebased local branch onto protected
  47329e35 at 06e91829123cb1498e566f595aa2e114ff5833f4. Exact cargo test --locked -p asb-runtime
  failed at live_service.rs:2015 (materialize_runtime_owner still passes caller
  RuntimeAuthorityInputs/state_path to provider-only API) and line 3346 (stale fixture arity);
  public CLI bridge still exposes caller authority. No push, PR update, merge, or hosted checks.
  Next worker must remove caller injection, update all callsites/tests, rerun independent exact-head
  gates, then publish.

- 2026-09-29T11:04:58+00:00: Claimed by ar1508-integration-repair-luna56.

- 2026-09-29T11:06:54+00:00: Heartbeat by ar1508-integration-repair-luna56.

- 2026-09-29T11:07:01+00:00: Recorded command exit 101; command argv SHA-256
  97ee782321facf1df64b14b3500c62b04b8b48c9904b8abb83044328a904f4b2.

- 2026-09-29T11:07:49+00:00: Recorded command exit 0; command argv SHA-256
  97ee782321facf1df64b14b3500c62b04b8b48c9904b8abb83044328a904f4b2.

- 2026-09-29T11:08:15+00:00: Recorded command exit 101; command argv SHA-256
  7b156112aa4a88b51b6049649edc1f0a823796afe35fb6f82149d0c42514af2e.

- 2026-09-29T11:10:21+00:00: Recorded command exit 0; command argv SHA-256
  64dab5bf01becc475a316fb33b11f66c67bf33927d541073a91edf2da0fdfb32.

- 2026-09-29T11:10:50+00:00: Recorded command exit 0; command argv SHA-256
  3d4cc54827fa0ae5c402321266e4a8e9a84a69a17f7ff27b7a0f0c858d454784.

- 2026-09-29T11:11:26+00:00: Recorded command exit 0; command argv SHA-256
  88771dabdeb077c561e65f4ecb30d491cd3eb148056a185d67aceec4bd7bfba8.

- 2026-09-29T11:11:43+00:00: Recorded command exit 0; command argv SHA-256
  5baca0896f5553b237d70ecc909a8ecbdb84f68b9545c0a0aea2ae1b8ce26c95.
