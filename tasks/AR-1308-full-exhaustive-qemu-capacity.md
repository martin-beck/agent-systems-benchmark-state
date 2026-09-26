---
{
  "branch": "feature/ar-1308-full-exhaustive-qemu-capacity",
  "checkpoint_commit": "df0e402f442468e43e06b7c1acb3c3667277fb75",
  "claim_expires": "2026-09-26T20:51:06+00:00",
  "depends_on": [
    "AR-1304"
  ],
  "id": "AR-1308",
  "next_action": "Clean runner ready: 64 GiB disk, x86_64 QEMU 8.2.2, 8 vCPU, 32 GiB RAM, no network/mounts. Bind exact AR-1307 bundle, pinned JDK/TLC, lock, image and seed; preflight before boot.",
  "observed_branch": "feature/ar-1308-full-exhaustive-qemu-capacity",
  "observed_dirty": 0,
  "observed_head": "659030fffd7e5aa2c0eaaa4dc384d2c619dc57ca",
  "owner": "coordinator-ar1308-preflight",
  "plan": "../plans/AR-1308.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Provide governed disposable capacity for exact full-exhaustive TLC liveness qualification.",
  "task_revision": 540,
  "title": "Full-exhaustive QEMU capacity qualification",
  "updated_at": "2026-09-26T18:53:32+00:00",
  "worktree_key": "agent-systems-benchmark-asb-ar-1308-full-exhaustive-qemu-capacity"
}
---

# AR-1308

AR-1307's exact-head full-exhaustive qualification reached approximately 45.77M generated and
37.99M distinct states, then failed because Java ran out of memory during liveness checking under
the existing 3G memory and 3G swap contract. This follow-on owns only the disposable capacity and
evidence needed to rerun that exact qualification truthfully; it must not weaken AR-1307's limits,
model, admission, or attestation gates.

The dependency on AR-1304 provides the reviewed required-tier QEMU runner and user-bus foundation.
The run must consume the exact signed AR-1307 head and pinned TLC/JDK/model inputs, without changing
source code or treating a capacity failure as a model result.

Local `unsigned-development` fixtures are limited to labelled diagnostic
preflight/capacity checks. They cannot qualify the full-exhaustive liveness
run or provide formal, publication, or release evidence. The run must reject
missing, unsigned, stale, or mismatched signed AR-1307 inputs and never
replace them with synthetic authority or a weaker resource contract.
The preflight defaults to the signed qualification profile. An explicit
`unsigned-development` invocation may validate only a diagnostic fixture and
must report `qualification_authorized: false`.


- 2026-09-18T13:45:32+00:00: AR-1304 is done; promote capacity follow-on to open for independent
  worker assignment. Preserve AR-1307 3G/3G contract and exact-head dependency.

- 2026-09-18T13:47:05+00:00: Claimed by codex-ar1308-qemu-capacity-20260918.

- 2026-09-18T13:47:23+00:00: Recorded command exit 128; command argv SHA-256
  3c23ab8c7aef5e69413a67148e540252a0be1c5f0afbf399d42a0b9fde7ef802.

- 2026-09-18T13:47:37+00:00: Recorded command exit 0; command argv SHA-256
  ae02b81cc87b547b19688a831039dc959be03909d2e8e8486319fe841ede01c3.

- 2026-09-18T13:51:59+00:00: Recorded command exit 0; command argv SHA-256
  9216f649f27dd4b7d9d0a6f363edd54f10a42e125b3802be7b1ef90da1e133d7.

- 2026-09-18T13:52:21+00:00: Recorded command exit 0; command argv SHA-256
  a1e22af43f312aca7eb94e3247acdcda3397b77489c6b756c25032889be42756.

- 2026-09-18T13:52:43+00:00: Recorded command exit 0; command argv SHA-256
  6788e083bb57e4638deb59f3ad667c37d7da4278328cc0b97dda64087b54d291.

- 2026-09-18T13:53:24+00:00: Recorded command exit 0; command argv SHA-256
  d47cc6663d902762ead98e64bc95b11888e9bae0a80a1b41e89586e488c7468f.

- 2026-09-18T13:54:16+00:00: Recorded command exit 0; command argv SHA-256
  087e8b4d4560b54bf6f050af48dae960159bde94f309fa84da4ac438c41e1ce4.

- 2026-09-18T13:54:27+00:00: Recorded command exit 0; command argv SHA-256
  09485738bdc509f7235ee90ba6fbe4f9976f846437a37a7fb65dd4bcddc472f8.

- 2026-09-18T13:55:49+00:00: Recorded command exit 0; command argv SHA-256
  1bcaa710b254d2cacd043de64e28c05c95e268f597892a361c5543d0cdf8ea61.

- 2026-09-18T13:56:01+00:00: Recorded command exit 0; command argv SHA-256
  4f9691df5cd21483d2cf25abb01c8bd13a3c26316d4c04ee70a777814164bd5b.

- 2026-09-18T13:56:16+00:00: Recorded command exit 0; command argv SHA-256
  44e5b46c4ba6f255e7da6353be6e542bf96670815399b816d90ab91de37a8011.

- 2026-09-18T13:56:33+00:00: Recorded command exit 1; command argv SHA-256
  672bc8b0e4b5dc6f601d619f56873dbf2ab9087c955c7d8adcba7b10d3cff76c.

- 2026-09-18T13:58:02+00:00: Recorded command exit 0; command argv SHA-256
  ee4145add4dfd9ecc477b588ee49d479dacaffee60ee2e0d08c4d4f60d994a04.

- 2026-09-18T13:58:48+00:00: Recorded command exit 0; command argv SHA-256
  3b341e11434d275c8731a357d340024fa55ade02c998b8e97c276190b39070a0.

- 2026-09-18T13:59:31+00:00: Recorded command exit 0; command argv SHA-256
  e85b09e8044353156f6d17fc343209531cd2b9ccea337f93689018e564631954.

- 2026-09-18T13:59:41+00:00: Recorded command exit 0; command argv SHA-256
  1040bf72dac6afd78bc6e6b8c39bff9885671f66d6b6996d82c81879b0ecaa8e.

- 2026-09-18T13:59:50+00:00: Recorded command exit 0; command argv SHA-256
  e58b3ac9a7f1d254c72c3070d26ed4d78b494ede3743ec7cc0fba31f1fd2b483.

- 2026-09-18T14:00:02+00:00: Recorded command exit 0; command argv SHA-256
  35f6e4bb709c55773c41df46b693e4d1341242518469522a99120c6c0258d776.

- 2026-09-18T14:00:16+00:00: Recorded command exit 0; command argv SHA-256
  746f25205abb8ea61c110b306bc9134d8c263b798b13b4c1763b02f588aa324d.

- 2026-09-18T14:00:55+00:00: Added signed AR-1308 QEMU receipt/preflight at e11adae64; focused and
  140-test state suites pass, vendor and Ruff/source-header checks pass, and live host preflight is
  ready. No formal qualification claimed.

- 2026-09-18T14:01:05+00:00: Recorded command exit 0; command argv SHA-256
  757c4b4bf4f927ca983e9d79b069750eaad8c94ab28e20ac329bc70932e9134d.

- 2026-09-18T14:02:07+00:00: Recorded command exit 0; command argv SHA-256
  861b1a7441c782e47d917e52b2399111c1e845370a0b30f3d9a2d4467bba1881.

- 2026-09-18T14:02:25+00:00: Recorded command exit 0; command argv SHA-256
  f17779708a925f0dcc26fc9cdcd368fe043b47f787a9a60fa8d602ed07b1cc6e.

- 2026-09-18T14:02:47+00:00: Recorded command exit 0; command argv SHA-256
  58fb4bbe8d27e49cbdd159472795563d646c135e9815848b5b90981edd0efd72.

- 2026-09-18T14:02:59+00:00: Recorded command exit 0; command argv SHA-256
  3f941d8a4e010ddd8e805267769620b170dcc131894f43b17e29b72e8b66ebd9.

- 2026-09-18T14:03:11+00:00: Recorded command exit 0; command argv SHA-256
  68d78a4b6b4389402f69de69aa1765e605732b82e7028704640097581e6267e8.

- 2026-09-18T14:03:49+00:00: Recorded command exit 0; command argv SHA-256
  1022577fddafec7384c8490079fadaf7a572406ee2b2afdfbc85da3d2457989d.

- 2026-09-18T14:04:00+00:00: Recorded command exit 0; command argv SHA-256
  00f13f785156b998a70cdf5c4b6aa801aeb0e90b8ee3be998e3453e8029796d5.

- 2026-09-18T14:04:11+00:00: Recorded command exit 0; command argv SHA-256
  40d21775cfff79bc9378e2d8d91ed0ecdba7fb4e44ce45e8e6f056bc4292ffcd.

- 2026-09-18T14:04:28+00:00: Recorded command exit 0; command argv SHA-256
  58e638f7403db6113096c740c95394f200f721043edb362d88522b684fcc93f7.

- 2026-09-18T14:04:39+00:00: Recorded command exit 0; command argv SHA-256
  764e14590382d5a51bba582b52dbca5780b9b4baca00d902a0cf3997e5642dbb.

- 2026-09-18T14:04:48+00:00: Recorded command exit 0; command argv SHA-256
  a7a908dcc05a743e2ab78e6b26247165f001552403604ced00c4c2f1bb18a0da.

- 2026-09-18T14:05:21+00:00: Recorded command exit 0; command argv SHA-256
  a173a4dc9beb580c82e5d1c18bb8bfc803e9d95617a77e3400bffde056a50f5d.

- 2026-09-18T14:05:34+00:00: Recorded command exit 1; command argv SHA-256
  29883c44d1418bf16191d9afec9f953beb7c21640b8d38f6806b824a43a573b5.

- 2026-09-18T14:05:44+00:00: Recorded command exit 0; command argv SHA-256
  280e1a80ac7e4b5e97bce4c1042cfda98b51e2bdee90430faab59aab44d82496.

- 2026-09-18T14:05:53+00:00: Recorded command exit 2; command argv SHA-256
  754d834e75ed805e27598dad82edbfadc6c5de8beeb0c6f02c8757d345c5c2d2.

- 2026-09-18T14:06:03+00:00: Recorded command exit 0; command argv SHA-256
  2115dbd68e737bfcdba8bc7fde15a45802a68aa0f6dd8d6121aec0a632441d06.

- 2026-09-18T14:06:13+00:00: Recorded command exit 0; command argv SHA-256
  754d834e75ed805e27598dad82edbfadc6c5de8beeb0c6f02c8757d345c5c2d2.

- 2026-09-18T14:06:23+00:00: Recorded command exit 0; command argv SHA-256
  80a7367b94e73b1c4cbf0c3400e8a9f5daebce6deb7448e69350762cf6ab8143.

- 2026-09-18T14:06:32+00:00: Recorded command exit 0; command argv SHA-256
  80a7367b94e73b1c4cbf0c3400e8a9f5daebce6deb7448e69350762cf6ab8143.

- 2026-09-18T14:06:57+00:00: Recorded command exit 1; command argv SHA-256
  826a645e617d99747db07f68d2b789c48fc853daeb08a890a2b2efaf2cb9da2a.

- 2026-09-18T14:07:18+00:00: Recorded command exit 0; command argv SHA-256
  a7febce4d42446ce9be74009d38f732b9a2c02a37b21caded7291f92939bc79c.

- 2026-09-18T14:09:11+00:00: Recorded command exit 0; command argv SHA-256
  047ece499027d2611735c5369e9bb8432b4f76460fe2f3073f6f88a99d284500.

- 2026-09-18T14:09:54+00:00: Recorded command exit 1; command argv SHA-256
  457f36e163e18a3bc3d9fb144a82e1e04e6f20334b0a5fdb54c7fbd7f1d034af.

- 2026-09-18T14:10:14+00:00: Recorded command exit 0; command argv SHA-256
  263c028becda07aba2ffe9770e6db8b12c21e421536130f7ae63f831c0fee941.

- 2026-09-18T14:10:26+00:00: Recorded command exit 0; command argv SHA-256
  83a9ad3771a8430279bcae0c70912d621fe6195d948a336face870ff289c4040.

- 2026-09-18T14:10:35+00:00: Recorded command exit 0; command argv SHA-256
  044035386a04b92b899e1b73fd14d9ab7417cd7b463bb966b061552b8dbf8cb7.

- 2026-09-18T14:10:49+00:00: Recorded command exit 0; command argv SHA-256
  66912eb9cd69c62d7de653dd2da6befd11ee69b387b0293034c2bd07396ccec2.

- 2026-09-18T14:11:01+00:00: Recorded command exit 0; command argv SHA-256
  4c5bceca20b54e8dc9592f86a8c7bc028eb6e29b683507f64646248c93b5de33.

- 2026-09-18T14:11:13+00:00: Recorded command exit 0; command argv SHA-256
  b0ef1ebcf96cbd6870afc99e5b09010f4637f2de1483b06ba3eb30c8a0328ef2.

- 2026-09-18T14:11:23+00:00: Recorded command exit 0; command argv SHA-256
  3e33ae5026b56b2952c6edfe09614dd3f43d0ee53938682dd4fcb0417c8388b1.

- 2026-09-18T14:11:34+00:00: Recorded command exit 0; command argv SHA-256
  934f79b23cfb32922ac60efb6fecced9c3c3507ec05ea0f1c7971b44ffa68791.

- 2026-09-18T14:11:49+00:00: Recorded command exit 0; command argv SHA-256
  7f0a3b06bec566e94db84e9cf150fb0ec1334dcd44a5796840be2e04f3f0dcfb.

- 2026-09-18T14:12:00+00:00: Recorded command exit 0; command argv SHA-256
  a1e22af43f312aca7eb94e3247acdcda3397b77489c6b756c25032889be42756.

- 2026-09-18T14:12:12+00:00: Recorded command exit 0; command argv SHA-256
  83a9ad3771a8430279bcae0c70912d621fe6195d948a336face870ff289c4040.

- 2026-09-18T14:12:23+00:00: Recorded command exit 0; command argv SHA-256
  66912eb9cd69c62d7de653dd2da6befd11ee69b387b0293034c2bd07396ccec2.

- 2026-09-18T14:12:33+00:00: Recorded command exit 0; command argv SHA-256
  4c5bceca20b54e8dc9592f86a8c7bc028eb6e29b683507f64646248c93b5de33.

- 2026-09-18T14:12:45+00:00: Recorded command exit 0; command argv SHA-256
  b0ef1ebcf96cbd6870afc99e5b09010f4637f2de1483b06ba3eb30c8a0328ef2.

- 2026-09-18T14:12:57+00:00: Recorded command exit 0; command argv SHA-256
  3e33ae5026b56b2952c6edfe09614dd3f43d0ee53938682dd4fcb0417c8388b1.

- 2026-09-18T14:13:06+00:00: Recorded command exit 0; command argv SHA-256
  934f79b23cfb32922ac60efb6fecced9c3c3507ec05ea0f1c7971b44ffa68791.

- 2026-09-18T14:27:03+00:00: Recorded independent-review blockers before further PR work. No
  full-exhaustive QEMU run is authorized until the exact signed AR-1307 head, bounded
  preflight/cleanup, exact-head review, and green required checks are satisfied.

- 2026-09-18T14:27:10+00:00: Recorded command exit 0; command argv SHA-256
  99beec250f1c9b45024601b855699804266fead0951f1d71e4fd7cca246e55fe.

- 2026-09-18T14:27:26+00:00: Recorded command exit 0; command argv SHA-256
  93d4e4a0691bf2b552d1d0a1df93b5b438d350ecc16a8c5457aca28387560535.

- 2026-09-18T14:27:40+00:00: Recorded command exit 0; command argv SHA-256
  2a6e7f4c0dab971d1616332a6b5e3951e98e4535b2dd902935a981f391136765.

- 2026-09-18T14:27:53+00:00: Recorded command exit 0; command argv SHA-256
  5e1449585aae35b4f522cdf010684483028a5fb66bbae82834b10dce0aa385f9.

- 2026-09-18T14:28:13+00:00: Recorded command exit 0; command argv SHA-256
  28cd5e9b62d2bc37abd137652a4e2d4dc441885a9bc8df4deda18994dbe4c694.

- 2026-09-18T14:28:37+00:00: Recorded command exit 0; command argv SHA-256
  1a1e0287ff2227fd62e81f9446dfba7e4a69704f1d910f17a5c68e3223788195.

- 2026-09-18T14:31:38+00:00: Recorded command exit 0; command argv SHA-256
  6c1925df7c16458f8e2c3ecb08105eee54ff5f5f6f9ad5873242fe8ac78508fa.

- 2026-09-18T14:31:56+00:00: Recorded command exit 0; command argv SHA-256
  28cd5e9b62d2bc37abd137652a4e2d4dc441885a9bc8df4deda18994dbe4c694.

- 2026-09-18T14:32:11+00:00: Recorded command exit 0; command argv SHA-256
  1a1e0287ff2227fd62e81f9446dfba7e4a69704f1d910f17a5c68e3223788195.

- 2026-09-18T14:33:57+00:00: Review fixes are pushed in PR #26. Full-quality CI first run failed
  only schema observation: scanner left observed_head empty because configured product checkout does
  not enumerate this state-repository worktree. Coverage now passes at 95%; re-run after observation
  repair.

- 2026-09-18T14:34:14+00:00: Recorded command exit 0; command argv SHA-256
  5e1449585aae35b4f522cdf010684483028a5fb66bbae82834b10dce0aa385f9.

- 2026-09-18T14:34:30+00:00: Recorded command exit 0; command argv SHA-256
  28cd5e9b62d2bc37abd137652a4e2d4dc441885a9bc8df4deda18994dbe4c694.

- 2026-09-18T14:57:36+00:00: Recorded command exit 0; command argv SHA-256
  ac8f7be2bd946d9c122d93779c769dc70a2c3a67375d35e638c0860c7707b9a3.

- 2026-09-18T14:57:58+00:00: Recorded command exit 0; command argv SHA-256
  ac8f7be2bd946d9c122d93779c769dc70a2c3a67375d35e638c0860c7707b9a3.

- 2026-09-18T14:58:22+00:00: Recorded command exit 0; command argv SHA-256
  bcc510a0f4286474b2374a6c98096a4109be5b4c94626e42e330f4f59985bee0.

- 2026-09-18T14:58:43+00:00: Recorded command exit 0; command argv SHA-256
  9a875aa9f3adede6d422bba6cfa2fc589166a6aa2bd1a13c5f37082dc8c87104.

- 2026-09-18T14:59:06+00:00: Recorded command exit 0; command argv SHA-256
  28cd5e9b62d2bc37abd137652a4e2d4dc441885a9bc8df4deda18994dbe4c694.

- 2026-09-18T15:04:46+00:00: Heartbeat by codex-ar1308-qemu-capacity-20260918.

- 2026-09-18T15:06:14+00:00: Recorded command exit 0; command argv SHA-256
  60885ad3f90e78c0528a2c93b3672e8901e197475cea65a1c135b7ad0572ddd0.

- 2026-09-18T15:06:31+00:00: Recorded command exit 2; command argv SHA-256
  0c07a66d430f3e56c0b122264953d37c571d3e84cceb6f838f4f1f49f717c3de.

- 2026-09-18T15:08:23+00:00: Recorded command exit 0; command argv SHA-256
  d076911137d44d9b388fef43cc3034158307bc88c87a1f01a6874151379932b3.

- 2026-09-18T15:08:42+00:00: Recorded command exit 0; command argv SHA-256
  2e92cf3d6c1d9f1d251e293a3f030c33e652ad30fb70f9f6828552b9d6baa82a.

- 2026-09-18T15:09:01+00:00: Recorded command exit 0; command argv SHA-256
  28cd5e9b62d2bc37abd137652a4e2d4dc441885a9bc8df4deda18994dbe4c694.

- 2026-09-18T15:09:19+00:00: Recorded command exit 0; command argv SHA-256
  1a1e0287ff2227fd62e81f9446dfba7e4a69704f1d910f17a5c68e3223788195.

- 2026-09-18T15:09:37+00:00: Recorded command exit 0; command argv SHA-256
  3b135d58667e42661cba4d48445e2245849d7dde1eb024308dcf77fd3822a39e.

- 2026-09-18T15:10:53+00:00: Recorded command exit 0; command argv SHA-256
  ee60708a1ac24f574f5bda89d29d1ee5853aba8630cb1a1b9f2ef806ef7096a8.

- 2026-09-18T15:11:11+00:00: Recorded command exit 0; command argv SHA-256
  28cd5e9b62d2bc37abd137652a4e2d4dc441885a9bc8df4deda18994dbe4c694.

- 2026-09-18T15:11:30+00:00: Recorded command exit 0; command argv SHA-256
  1a1e0287ff2227fd62e81f9446dfba7e4a69704f1d910f17a5c68e3223788195.

- 2026-09-18T15:11:49+00:00: Recorded command exit 0; command argv SHA-256
  3b135d58667e42661cba4d48445e2245849d7dde1eb024308dcf77fd3822a39e.

- 2026-09-18T15:13:05+00:00: Recorded command exit 0; command argv SHA-256
  e3cf67a71b77e9c9d121113b7a9c1eb82ff33571e11b4708309de761e2876d4f.

- 2026-09-18T15:13:22+00:00: Recorded command exit 0; command argv SHA-256
  28cd5e9b62d2bc37abd137652a4e2d4dc441885a9bc8df4deda18994dbe4c694.

- 2026-09-18T15:13:39+00:00: Recorded command exit 0; command argv SHA-256
  1a1e0287ff2227fd62e81f9446dfba7e4a69704f1d910f17a5c68e3223788195.

- 2026-09-18T15:13:58+00:00: Recorded command exit 0; command argv SHA-256
  3b135d58667e42661cba4d48445e2245849d7dde1eb024308dcf77fd3822a39e.

- 2026-09-18T15:15:33+00:00: Recorded command exit 0; command argv SHA-256
  6e80e944ef486a2e2b012a901bad44d883effa494f42dd970f880b0594e0bfbe.

- 2026-09-18T15:15:52+00:00: Recorded command exit 0; command argv SHA-256
  28cd5e9b62d2bc37abd137652a4e2d4dc441885a9bc8df4deda18994dbe4c694.

- 2026-09-18T15:16:10+00:00: Recorded command exit 0; command argv SHA-256
  1a1e0287ff2227fd62e81f9446dfba7e4a69704f1d910f17a5c68e3223788195.

- 2026-09-18T15:16:28+00:00: Recorded command exit 0; command argv SHA-256
  3b135d58667e42661cba4d48445e2245849d7dde1eb024308dcf77fd3822a39e.

- 2026-09-18T15:17:38+00:00: Recorded command exit 0; command argv SHA-256
  286ddab2049d3a9d8d304bb548c7a78eb0945c9c25ec80671f1dab78301bc39d.

- 2026-09-18T15:17:57+00:00: Recorded command exit 0; command argv SHA-256
  28cd5e9b62d2bc37abd137652a4e2d4dc441885a9bc8df4deda18994dbe4c694.

- 2026-09-18T15:18:15+00:00: Recorded command exit 0; command argv SHA-256
  1a1e0287ff2227fd62e81f9446dfba7e4a69704f1d910f17a5c68e3223788195.

- 2026-09-18T15:18:33+00:00: Recorded command exit 0; command argv SHA-256
  3b135d58667e42661cba4d48445e2245849d7dde1eb024308dcf77fd3822a39e.

- 2026-09-18T15:19:11+00:00: Recorded command exit 0; command argv SHA-256
  ce917a0fd76faa1a0c803829ad15f109b5a402a4ec77f8fbc0f374525290a68f.

- 2026-09-18T15:19:29+00:00: Recorded command exit 0; command argv SHA-256
  773eae9606dc53ae4e867a74b29c0038b8ed756ad998f471e67b2b978fb38ffd.

- 2026-09-18T15:20:02+00:00: Recorded command exit 0; command argv SHA-256
  adab0ea506929a16d37bc9ef3994d464b24b65fd59d1cef5f951b9e60f8e4b57.

- 2026-09-18T15:20:14+00:00: Recorded command exit 0; command argv SHA-256
  c736518740607a371a16f24f3df6f4019f77b25f31316eafb737383c71e85d95.

- 2026-09-18T15:20:36+00:00: Recorded command exit 0; command argv SHA-256
  28cd5e9b62d2bc37abd137652a4e2d4dc441885a9bc8df4deda18994dbe4c694.

- 2026-09-18T15:20:54+00:00: Recorded command exit 0; command argv SHA-256
  1a1e0287ff2227fd62e81f9446dfba7e4a69704f1d910f17a5c68e3223788195.

- 2026-09-18T15:21:12+00:00: Recorded command exit 0; command argv SHA-256
  3b135d58667e42661cba4d48445e2245849d7dde1eb024308dcf77fd3822a39e.

- 2026-09-18T15:24:46+00:00: Heartbeat by codex-ar1308-qemu-capacity-20260918.

- 2026-09-18T15:28:26+00:00: Recorded command exit 0; command argv SHA-256
  fd0a59dd857b45bd9056dc44ebc9a33926b59520bf30fd6d9a22e684a4d8a538.

- 2026-09-18T15:28:38+00:00: Recorded command exit 0; command argv SHA-256
  3d8a26932150a9e469cd80e8e503b6fbd1fed660ef20e9c8bdf01b7764e6cbf2.

- 2026-09-18T15:28:55+00:00: Recorded command exit 0; command argv SHA-256
  28cd5e9b62d2bc37abd137652a4e2d4dc441885a9bc8df4deda18994dbe4c694.

- 2026-09-18T15:29:13+00:00: Recorded command exit 0; command argv SHA-256
  1a1e0287ff2227fd62e81f9446dfba7e4a69704f1d910f17a5c68e3223788195.

- 2026-09-18T15:29:31+00:00: Recorded command exit 0; command argv SHA-256
  3b135d58667e42661cba4d48445e2245849d7dde1eb024308dcf77fd3822a39e.

- 2026-09-18T15:30:48+00:00: Recorded command exit 0; command argv SHA-256
  5e1449585aae35b4f522cdf010684483028a5fb66bbae82834b10dce0aa385f9.

- 2026-09-18T15:31:06+00:00: Recorded command exit 0; command argv SHA-256
  28cd5e9b62d2bc37abd137652a4e2d4dc441885a9bc8df4deda18994dbe4c694.

- 2026-09-18T15:33:32+00:00: Recorded command exit 0; command argv SHA-256
  5421199e2a1ec0602fdf560b89e8a00aae5c6f4b157735e007b5f5aa029ceb1a.

- 2026-09-18T15:33:44+00:00: Recorded command exit 0; command argv SHA-256
  605ef143deb6518bd40e9fc6139f52274ce92d19fd6025c0c4b0c6825d84a357.

- 2026-09-18T15:34:02+00:00: Recorded command exit 0; command argv SHA-256
  28cd5e9b62d2bc37abd137652a4e2d4dc441885a9bc8df4deda18994dbe4c694.

- 2026-09-18T15:34:56+00:00: Recorded command exit 0; command argv SHA-256
  092aa90f1582fb05763dca35e6d496ac298ea6456bc8880eea8072741d305466.

- 2026-09-18T15:36:04+00:00: Recorded command exit 0; command argv SHA-256
  5421199e2a1ec0602fdf560b89e8a00aae5c6f4b157735e007b5f5aa029ceb1a.

- 2026-09-18T15:36:16+00:00: Recorded command exit 0; command argv SHA-256
  2a2df927171fe1c6d0c4d8261756b433ec4466d96b2d8761cff7f0ece2a2185c.

- 2026-09-18T15:37:11+00:00: Recorded command exit 0; command argv SHA-256
  ddb9168b418cab12618af8af83662ec10fd4f9273daaf3fca447954f8ad73ab4.

- 2026-09-18T15:37:28+00:00: Recorded command exit 0; command argv SHA-256
  0ed9acf954162e40651c9aa2aefbe7d0b07b0fd4794d7584178017119e46a4f2.

- 2026-09-18T15:37:51+00:00: Checkpoint recorded through handoffctl for signed implementation head
  ed70f0b6d95e577d1fb8cc4ca32bba95d513bb6b. Formal runner, tier fixtures, approved runtime paths,
  vendor digest, and coverage fixes are in the PR; no QEMU run yet.

- 2026-09-18T15:38:04+00:00: Recorded command exit 0; command argv SHA-256
  28cd5e9b62d2bc37abd137652a4e2d4dc441885a9bc8df4deda18994dbe4c694.

- 2026-09-18T15:38:22+00:00: Recorded command exit 1; command argv SHA-256
  9028e58ade258483acdc4fc82cbbef44a699c55ed6f250d7dddc97f9fa3ecaff.

- 2026-09-18T15:39:00+00:00: Recorded command exit 0; command argv SHA-256
  c9898597d1e070bf456d6a13c2659bb670043422ee8871044c6072711f2e9b0d.

- 2026-09-18T15:39:12+00:00: Recorded command exit 0; command argv SHA-256
  1a9f834d77deccbfc5ebd74a8f72075451aee56ef09cc16985173d07b94ada61.

- 2026-09-18T15:39:31+00:00: Recorded command exit 0; command argv SHA-256
  28cd5e9b62d2bc37abd137652a4e2d4dc441885a9bc8df4deda18994dbe4c694.

- 2026-09-18T15:39:50+00:00: Recorded command exit 0; command argv SHA-256
  1a1e0287ff2227fd62e81f9446dfba7e4a69704f1d910f17a5c68e3223788195.

- 2026-09-18T15:40:09+00:00: Recorded command exit 0; command argv SHA-256
  3b135d58667e42661cba4d48445e2245849d7dde1eb024308dcf77fd3822a39e.

- 2026-09-18T15:40:27+00:00: Recorded command exit 0; command argv SHA-256
  e8d3993742362702bad68590b9f57de929f860c5f1eb68cea271a79de6f574f0.

- 2026-09-18T15:40:45+00:00: Recorded command exit 0; command argv SHA-256
  7b349b027c31e0885c01a21b5b21626d042f5f941d05c0f9afd300083eca1cb4.

- 2026-09-18T15:44:51+00:00: Recorded command exit 0; command argv SHA-256
  a59baf676093f97d476b7c0f3565fa8a1bc2af27aa8b66bb156844cb46d2eefe.

- 2026-09-18T15:45:05+00:00: Recorded command exit 0; command argv SHA-256
  6ce6b65ec411e7ba86b85d7d6f6d7d9066ea2d21317a578e01f02663eef9bdd9.

- 2026-09-18T15:45:24+00:00: Recorded command exit 0; command argv SHA-256
  28cd5e9b62d2bc37abd137652a4e2d4dc441885a9bc8df4deda18994dbe4c694.

- 2026-09-18T15:45:47+00:00: Checkpoint advanced through handoffctl to signed exact PR head
  df0e402f442468e43e06b7c1acb3c3667277fb75 after coverage and checkpoint-path tests. Required gates
  are being rerun; QEMU remains paused.

- 2026-09-18T15:45:54+00:00: Recorded command exit 1; command argv SHA-256
  55b7ac64074e6ba48d9aa0109b081f466a6a7dc81a329e4a898df3da00717791.

- 2026-09-18T15:46:26+00:00: Recorded command exit 0; command argv SHA-256
  c9898597d1e070bf456d6a13c2659bb670043422ee8871044c6072711f2e9b0d.

- 2026-09-18T15:46:38+00:00: Recorded command exit 0; command argv SHA-256
  1a9f834d77deccbfc5ebd74a8f72075451aee56ef09cc16985173d07b94ada61.

- 2026-09-18T15:46:58+00:00: Recorded command exit 0; command argv SHA-256
  28cd5e9b62d2bc37abd137652a4e2d4dc441885a9bc8df4deda18994dbe4c694.

- 2026-09-18T15:47:17+00:00: Recorded command exit 0; command argv SHA-256
  1a1e0287ff2227fd62e81f9446dfba7e4a69704f1d910f17a5c68e3223788195.

- 2026-09-18T15:47:32+00:00: Recorded command exit 0; command argv SHA-256
  3b135d58667e42661cba4d48445e2245849d7dde1eb024308dcf77fd3822a39e.

- 2026-09-18T15:47:46+00:00: Recorded command exit 0; command argv SHA-256
  e8d3993742362702bad68590b9f57de929f860c5f1eb68cea271a79de6f574f0.

- 2026-09-18T15:47:59+00:00: Recorded command exit 0; command argv SHA-256
  7b349b027c31e0885c01a21b5b21626d042f5f941d05c0f9afd300083eca1cb4.

- 2026-09-18T15:49:12+00:00: Exact-head a30b2de72e94977b9c75e7b63d801dcf8cf4690d has handoffctl
  formal, strict coordination, AWQ shadow, and source-header workflows green: runs 35364562857,
  35364541277, 35364585118, 35364607523. Local focused tests passed (41 TLC, 78 coordinator, 8
  vendor); full CI ran 194 tests at 95% coverage. Host preflight remains correctly blocked by low
  host swap/disk; no QEMU run started.

- 2026-09-18T15:49:54+00:00: Recorded command exit 0; command argv SHA-256
  2a6e7f4c0dab971d1616332a6b5e3951e98e4535b2dd902935a981f391136765.

- 2026-09-18T15:50:14+00:00: Recorded command exit 1; command argv SHA-256
  5e1449585aae35b4f522cdf010684483028a5fb66bbae82834b10dce0aa385f9.

- 2026-09-18T15:50:35+00:00: Heartbeat by codex-ar1308-qemu-capacity-20260918.

- 2026-09-18T15:51:03+00:00: Recorded command exit 0; command argv SHA-256
  60885ad3f90e78c0528a2c93b3672e8901e197475cea65a1c135b7ad0572ddd0.

- 2026-09-18T15:51:15+00:00: Recorded command exit 1; command argv SHA-256
  9c9feb8c2186cb4883c12c8a4986852bd77d585d1176a7c08719588fbed1dc31.

- 2026-09-18T15:51:32+00:00: Recorded command exit 1; command argv SHA-256
  9c9feb8c2186cb4883c12c8a4986852bd77d585d1176a7c08719588fbed1dc31.

- 2026-09-18T15:52:06+00:00: Recorded command exit 0; command argv SHA-256
  adab0ea506929a16d37bc9ef3994d464b24b65fd59d1cef5f951b9e60f8e4b57.

- 2026-09-18T15:52:18+00:00: Recorded command exit 1; command argv SHA-256
  9c9feb8c2186cb4883c12c8a4986852bd77d585d1176a7c08719588fbed1dc31.

- 2026-09-18T15:52:40+00:00: Recorded command exit 1; command argv SHA-256
  c2ec791a650cd6e7e95c8b15da5438cc060521d6c6f8c25a5481699f17b08ec0.

- 2026-09-18T15:52:58+00:00: Recorded command exit 1; command argv SHA-256
  c2ec791a650cd6e7e95c8b15da5438cc060521d6c6f8c25a5481699f17b08ec0.

- 2026-09-18T15:53:21+00:00: Recorded command exit 0; command argv SHA-256
  c2ec791a650cd6e7e95c8b15da5438cc060521d6c6f8c25a5481699f17b08ec0.

- 2026-09-18T15:53:48+00:00: Heartbeat by codex-ar1308-qemu-capacity-20260918.

- 2026-09-18T15:54:00+00:00: Recorded command exit 0; command argv SHA-256
  28cd5e9b62d2bc37abd137652a4e2d4dc441885a9bc8df4deda18994dbe4c694.

- 2026-09-18T15:54:39+00:00: Recorded command exit 0; command argv SHA-256
  1a1e0287ff2227fd62e81f9446dfba7e4a69704f1d910f17a5c68e3223788195.

- 2026-09-18T15:54:53+00:00: Recorded command exit 0; command argv SHA-256
  3b135d58667e42661cba4d48445e2245849d7dde1eb024308dcf77fd3822a39e.

- 2026-09-18T15:55:06+00:00: Recorded command exit 0; command argv SHA-256
  e8d3993742362702bad68590b9f57de929f860c5f1eb68cea271a79de6f574f0.

- 2026-09-18T15:55:20+00:00: Recorded command exit 0; command argv SHA-256
  7b349b027c31e0885c01a21b5b21626d042f5f941d05c0f9afd300083eca1cb4.

- 2026-09-18T15:56:49+00:00: Recorded command exit 0; command argv SHA-256
  1ea5be485f58dc3809faf59c62631986ea6f90f6361f8f3ef3beb01a72f51054.

- 2026-09-18T15:59:11+00:00: PR #26 merged at e9de9677ae6d071fa053ab4fc41d82f3e3381d81. Post-merge
  main contains the reviewed AR-1308 runner at exact merge commit; transition is now post-merge
  verification and governed preflight.

- 2026-09-18T15:59:27+00:00: Recorded command exit 1; command argv SHA-256
  76f107d648f95578172531bd0a75f4da58d0f616811f0c8f2303b6c1e8fc5689.

- 2026-09-18T15:59:58+00:00: Recorded command exit 0; command argv SHA-256
  7c7f61ed6cbc16d87f5098c2383a08ce5a8bbb3ddf709e4f0269d701eba4dbfb.

- 2026-09-18T16:00:29+00:00: Recorded command exit 1; command argv SHA-256
  5900aa5d4830ceb2f0a073d55a7f59a92e7047175a109f6dce3be3ec571640c9.

- 2026-09-18T16:00:56+00:00: Post-merge preflight ran against merged runner. It failed closed
  truthfully: host SwapFree measured about 232 KiB versus required 1 GiB; /srv/data had about 38 GiB
  free and 28 GiB available memory. Canonical /srv/data/projects/.asb-tlc admission lock is
  owner-private to gha-asb-state and inaccessible to this worker, so no full run was attempted. A
  temporary accessible lock was used only to expose the host-swap blocker; no gate was weakened.

- 2026-09-18T16:01:05+00:00: Blocked after merged PR #26: governed post-merge preflight failed
  closed on host SwapFree approximately 232 KiB, below required 1 GiB. Provision an approved
  disposable runner with sufficient host swap and accessible owner-private admission lock, then
  resume and rerun preflight before any QEMU attempt.

- 2026-09-18T16:01:39+00:00: Coordinator is provisioning a disposable second-disk runner: temporary
  host swap capacity and an owner-accessible admission lock. Resume only to perform measured
  preflight and preserve fail-closed gates.

- 2026-09-18T16:01:42+00:00: Claimed by codex-ar1308-runner-provision-20260918.

- 2026-09-18T16:01:58+00:00: Recorded command exit 0; command argv SHA-256
  d01ec9815109888cbe3c2cb2925927fcd44864ade58c52b9bbfc1618bedf8735.

- 2026-09-18T16:02:09+00:00: Recorded command exit 1; command argv SHA-256
  46b983242a416aeee2369732f2d119633221cd8142dbd3cadd3086601a2fec10.

- 2026-09-18T16:02:49+00:00: Recorded command exit 0; command argv SHA-256
  e9b89888ce83755db374d5507968d2fabf5b54b4187140b37966a6897c27f44e.

- 2026-09-18T16:03:01+00:00: Recorded command exit 0; command argv SHA-256
  4870871166cbcc9d79402152537888b491533edc4b893e2c1cf0fb9ab80e5ea4.

- 2026-09-18T16:03:12+00:00: Recorded command exit 0; command argv SHA-256
  40c3a3c1afe97815fb80fd1a25c39b55bb386de8a4e6473a33952d17f7b4b6a0.

- 2026-09-18T16:03:24+00:00: Recorded command exit 0; command argv SHA-256
  c7651711ca61ea1ed87bfcfb6d91a3b66f82e2a445d83cda6e924cc7c2fcd5ab.

- 2026-09-18T16:04:42+00:00: Recorded command exit 1; command argv SHA-256
  130a754978e9398da845ba226488e07e64645db5d2ad043d74186899789f776d.

- 2026-09-18T16:05:12+00:00: Recorded command exit 1; command argv SHA-256
  b4161edb2991abeaaad99e88ff1839ca36af04760b325e0afd56257c8b2a2251.

- 2026-09-18T16:05:51+00:00: Recorded command exit 0; command argv SHA-256
  ed5d2ff9d272d35d14040aaeaff820206a1b9ca483537ba860f62e45d5755402.

- 2026-09-18T16:06:03+00:00: Recorded command exit 0; command argv SHA-256
  243291b83e62c0fec662fca202d7ceb9a77361e6fe71a30ed085c8d7db6c7a1d.

- 2026-09-18T16:06:15+00:00: Recorded command exit 1; command argv SHA-256
  b4161edb2991abeaaad99e88ff1839ca36af04760b325e0afd56257c8b2a2251.

- 2026-09-18T16:07:01+00:00: Recorded command exit 0; command argv SHA-256
  a6e88d2258e7120409f58ec8f57b1db76a8d72976df19b7dff424e6848bac7b2.

- 2026-09-18T16:07:13+00:00: Recorded command exit 0; command argv SHA-256
  5a5ffcdae0d02fa9ffd4a1edfcc322d91ccab3b7d4512bdc479f25197eb370d9.

- 2026-09-18T16:07:25+00:00: Recorded command exit 0; command argv SHA-256
  1eac9c14da9f259f53087be14ba4cad1d75c4fc6e55855f12ccfeb91c146fd22.

- 2026-09-18T16:07:37+00:00: Recorded command exit 0; command argv SHA-256
  d837dd9a9980dee514713c367651f613c956cb1167f5615056fdae150565d35e.

- 2026-09-18T16:07:48+00:00: Recorded command exit 0; command argv SHA-256
  72b3964db0c9bbe0779355445f1cf62e7d016abf5c7e06131a2cfc5e04107a5f.

- 2026-09-18T16:08:00+00:00: Recorded command exit 0; command argv SHA-256
  7c45e865bf863165814ed7c18fd2a85fdb1afe0e263f4afe8650b08981c23147.

- 2026-09-18T16:08:38+00:00: Recorded command exit 0; command argv SHA-256
  63f9e515002eb716166603adc9d3bb614dac69380a5f0ed86bfa0b34ede66e2e.

- 2026-09-18T16:09:11+00:00: Recorded command exit 0; command argv SHA-256
  4130f91db3dc6e24340951f981069258e6f998b292d82971a1efb0fe6617a839.

- 2026-09-18T16:10:23+00:00: Recorded command exit 0; command argv SHA-256
  68dc95f7b8dc867e70e69a76bcce320d90989d41a8416da37b10de47dd6ccd3e.

- 2026-09-18T16:10:35+00:00: Recorded command exit 0; command argv SHA-256
  07a1e8952f907aaf8f54a3a69c97b49ee38a37a192a1c92ffedf9eb36e3bdbe6.

- 2026-09-18T16:10:47+00:00: Recorded command exit 0; command argv SHA-256
  3237a25a51ba3139d4e2af7786f4036dcdeea32826020019ff471df3ef731b3a.

- 2026-09-18T16:11:21+00:00: Recorded command exit 0; command argv SHA-256
  44e5a0b326b4936328a34f2d3aaf06a3d4865e1e83b8645ec4edb2be62c4096e.

- 2026-09-18T16:11:33+00:00: Recorded command exit 1; command argv SHA-256
  e6caf7cd02baebd75c3321a0e1d1d71a5c16bf9bf248664d977124bca406cde3.

- 2026-09-18T16:12:11+00:00: Recorded command exit 0; command argv SHA-256
  12d87177b2bfa25a288c45aa9f0dd3a7ebe9353bca2452610d94b8c437ebe7b4.

- 2026-09-18T16:12:38+00:00: Recorded command exit 0; command argv SHA-256
  c131e3428eb8a1483422c6bb33fbc5b599cf6ee3a5baa111ce60bdda3553a664.

- 2026-09-18T16:12:49+00:00: Recorded command exit 0; command argv SHA-256
  83da5d5fa805dfbcb459a92b50ea5ccfd881777ce43c0b0ec504152351f19230.

- 2026-09-18T16:13:01+00:00: Recorded command exit 0; command argv SHA-256
  e6caf7cd02baebd75c3321a0e1d1d71a5c16bf9bf248664d977124bca406cde3.

- 2026-09-18T16:13:51+00:00: Recorded command exit 0; command argv SHA-256
  dd44ed7fa2b9fd1ca84668f502e1b07da58790c494f216b247ec1f49387bf097.

- 2026-09-18T16:14:03+00:00: Recorded command exit 0; command argv SHA-256
  36876b1cf5a1c0bbb2998752f541755ee96cd8f61472426424c5eb80175333bf.

- 2026-09-18T16:14:14+00:00: Recorded command exit 0; command argv SHA-256
  4a6a4b1bdab42c8f4c689aa9452c0cc7273633b62bc3a23af3daa2764ecc5b02.

- 2026-09-18T16:14:30+00:00: Recorded command exit 0; command argv SHA-256
  9353c0189e3da2de83d5044aeda16339f335da57b91fee07151b3d327cb064a1.

- 2026-09-18T16:16:52+00:00: Heartbeat by codex-ar1308-runner-provision-20260918.

- 2026-09-18T16:18:41+00:00: Recorded command exit 0; command argv SHA-256
  1c642a62c701bbb6bb760c1e8556d31b185adb1d579f9ba946867f8882fa8c26.

- 2026-09-18T16:18:53+00:00: Recorded command exit 0; command argv SHA-256
  75b283bbb7e2bba199b0b0b2b93c456f633b630058d25e75832e80b723c5003c.

- 2026-09-18T16:19:04+00:00: Recorded command exit 1; command argv SHA-256
  0d16bce14ba333e2521c370f6c066e753b02cc02f959fcad07f7037955c68c1e.

- 2026-09-18T16:19:16+00:00: Recorded command exit 0; command argv SHA-256
  4b1d6415265449645cb195ac5c7dfd8a8feec54e693b4b04bd3f284051ea4cdd.

- 2026-09-18T16:19:28+00:00: Heartbeat by codex-ar1308-runner-provision-20260918.

- 2026-09-18T16:19:52+00:00: Post-merge serial boot failed closed before evidence: the seed contract
  expects /mnt/asb-data/etc/java-17-openjdk/security files, while the prepared data fixture contains
  etc-java-17-openjdk, so JDK security symlinks resolve to absent paths and the guest powers off.
  This is a runner bootstrap fixture mismatch, not a qualification result. The AR-1293 canonical
  repair exists on signed commits d57b495b9/92238e735/9b9491d08 (copy pinned security files into a
  private fixed JDK and remove dangling links), but is not part of merged AR-1308. Rebuild or
  provision the exact reviewed fixture contract, preserve pinned digests, and rerun fail-closed
  checks.

- 2026-09-18T16:20:16+00:00: Resuming only to correct the durable next action after the newly
  diagnosed bootstrap fixture mismatch; no qualification run authorized.

- 2026-09-18T16:20:24+00:00: Claimed by codex-ar1308-runner-provision-20260918.

- 2026-09-18T16:20:33+00:00: Durable next action corrected after serial diagnosis. The merged
  AR-1308 seed invokes the mounted JDK, whose security links require
  /mnt/asb-data/etc/java-17-openjdk; the prepared fixture instead exposes etc-java-17-openjdk. The
  guest therefore powers off before attestation. AR-1293 signed commits d57b495b9, 92238e735, and
  9b9491d08 document the canonical private fixed-JDK/security-file repair, but are not merged into
  AR-1308. No qualification claim.

- 2026-09-18T16:20:43+00:00: Blocked on disposable runner bootstrap fixture mismatch. Serial boot
  reached the mounted data but failed before any attestation because the seed/JDK security links
  require /mnt/asb-data/etc/java-17-openjdk while the prepared fixture has etc-java-17-openjdk. The
  merged AR-1308 contract has no canonical fix; AR-1293 signed repairs d57b495b9/92238e735/9b9491d08
  are the reference. Rebuild the reviewed fixture or apply an approved equivalent, verify
  fsck/hash/serial bootstrap, then preflight; do not claim qualification.

- 2026-09-18T16:21:53+00:00: Coordinator resumed briefly to terminate the bounded disposable VM
  process and preserve the classified fixture mismatch evidence.

- 2026-09-18T16:21:56+00:00: Claimed by codex-coordinator-ar1308-runner-20260918.

- 2026-09-18T16:22:01+00:00: Recorded command exit 0; command argv SHA-256
  7e45f5e1e40fed516ec51062e5979d82637c99ff6fed6bb2f3cc00774fbb964b.

- 2026-09-18T16:22:12+00:00: Governed preflight passed after host swap, kvm access, admission-lock
  ownership and signer setup. A bounded disposable QEMU boot using the pinned image and offline seed
  failed closed before TLC: seed requested
  /mnt/asb-data/etc/java-17-openjdk/{java.security,java.policy,nss.cfg}, but the prepared data
  fixture exposed only etc-java-17-openjdk; serial recorded cp ENOENT and no attestation/evidence. A
  fresh disposable data copy added the canonical symlink, but a network-none boot did not reach
  cloud-init final stage before bounded cleanup, so no qualification is claimed. Repair/rebuild the
  reviewed fixture/seed chain, verify fsck/hash and serial bootstrap, then rerun preflight and one
  bounded exact-head attempt.

- 2026-09-18T16:25:59+00:00: Resume fixture repair after reviewing the durable mismatch. Repair only
  the disposable data/seed chain for pinned JDK security files; retain exact model, 3G/3G limits,
  offline/no-host-mount and bounded-QEMU gates.

- 2026-09-18T16:26:05+00:00: Claimed by codex-ar1308-fixture-repair-20260918.

- 2026-09-18T16:27:54+00:00: Recorded command exit 0; command argv SHA-256
  345b7f045a692dbcc079b4545803eedce545827bb52f2e19e959b757381e7f59.

- 2026-09-18T16:29:09+00:00: Recorded command exit 0; command argv SHA-256
  32e712471e499450a053e957b29f02727a1fbfee61f9851c66d20fa7a481e613.

- 2026-09-18T16:29:26+00:00: Recorded command exit 0; command argv SHA-256
  7cc8d9754e56cd4e2bc904207aaad3efda387dee3628ac4a3f6ef0751f3b222b.

- 2026-09-18T16:29:43+00:00: Recorded command exit 0; command argv SHA-256
  80fb99a55d4d6234e0c59ccc7738f88aa9d96eee44d9692884f4915101b344a9.

- 2026-09-18T16:30:36+00:00: Recorded command exit 1; command argv SHA-256
  40a5a9d356c271721c0a9f9e6994db644d9f1b0e42560b6dab1e69b44802d8fa.

- 2026-09-18T16:31:07+00:00: Recorded command exit 0; command argv SHA-256
  d163fb1eb0303d311a48c6cbee76b0977f9c6997946211229908b0d36e2bebc0.

- 2026-09-18T16:31:28+00:00: Recorded command exit 1; command argv SHA-256
  40a5a9d356c271721c0a9f9e6994db644d9f1b0e42560b6dab1e69b44802d8fa.

- 2026-09-18T16:32:16+00:00: Recorded command exit 1; command argv SHA-256
  e9719feb3ec82e8a665934ee24e9399e720e589bbff0956649cc756d61f5bf89.

- 2026-09-18T16:32:34+00:00: Recorded command exit 0; command argv SHA-256
  9845efacc375950c95c26285190b069f48f64da3fb09627e3accb4126c33f1c5.

- 2026-09-18T16:32:59+00:00: Recorded command exit 1; command argv SHA-256
  b830070d0036981191ae3881471f70e6e2ab2604ce8642cf2295b9f3d59fdbca.

- 2026-09-18T16:33:45+00:00: Recorded command exit 0; command argv SHA-256
  eb8b1864862699c51eb0e393d2098c574bc79927310cac168666796719850789.

- 2026-09-18T16:34:24+00:00: Recorded command exit 0; command argv SHA-256
  62845ad9d48c107baf3810e18aaafd474c481e393794bca18c45e07178c837a4.

- 2026-09-18T16:34:41+00:00: Recorded command exit 0; command argv SHA-256
  fc2acfed937ecc1a46e59e058b994f61e5bad3d66df87c2a42aecabf9fd2a033.

- 2026-09-18T16:35:01+00:00: Recorded command exit 1; command argv SHA-256
  40a5a9d356c271721c0a9f9e6994db644d9f1b0e42560b6dab1e69b44802d8fa.

- 2026-09-18T16:35:21+00:00: Recorded command exit 0; command argv SHA-256
  cbc674bfd545fe3b1585d80046b3c5da7d650523e3bef39ceee386cf489bc8b8.

- 2026-09-18T16:35:47+00:00: Recorded command exit 0; command argv SHA-256
  40a5a9d356c271721c0a9f9e6994db644d9f1b0e42560b6dab1e69b44802d8fa.

- 2026-09-18T16:36:39+00:00: Recorded command exit 0; command argv SHA-256
  32e712471e499450a053e957b29f02727a1fbfee61f9851c66d20fa7a481e613.

- 2026-09-18T16:37:17+00:00: Recorded command exit 1; command argv SHA-256
  67313d2f737641cd0d49935a01a4fd21173ba46236ad73a84424e41421952c38.

- 2026-09-18T16:38:34+00:00: Recorded command exit 0; command argv SHA-256
  7dd6aaa6fe50ba6857758628d5285c534a8db4fb6b57cae20929c8012670554c.

- 2026-09-18T16:38:58+00:00: Recorded command exit 1; command argv SHA-256
  fb63f8e5ae9ded6d55269338e62a4badba8db84e4a1e2d6fa7f5e20e78f1d814.

- 2026-09-18T16:39:46+00:00: Recorded command exit 0; command argv SHA-256
  55f09b47229ba010cd4e6bdfe57315f040d2eebc4aabc061728001c5f8c5d646.

- 2026-09-18T16:40:13+00:00: Recorded command exit 0; command argv SHA-256
  fb63f8e5ae9ded6d55269338e62a4badba8db84e4a1e2d6fa7f5e20e78f1d814.

- 2026-09-18T16:42:32+00:00: Recorded command exit 0; command argv SHA-256
  2ac78657ead59decc28cda6e747dc8d64261410da2ea8ee7a10509125e1e235a.

- 2026-09-18T16:43:04+00:00: Recorded command exit 0; command argv SHA-256
  f63987ea87cef7a070ec39d25319506773867feceb7bf1597dbd529b4f994bde.

- 2026-09-18T16:43:24+00:00: Recorded command exit 0; command argv SHA-256
  96701d5b0d830da6e9e51f3297e004e7bdf95e5ad511b41347552ad431bb016f.

- 2026-09-18T16:47:00+00:00: Preflight passed after fsck-clean data repair and expected JDK security
  paths. One bounded networkless QEMU boot terminated after cloud-final with five runuser failures:
  user asb does not exist; no TLC or attestation was emitted. Capacity qualification remains
  unproven.

- 2026-09-18T16:47:09+00:00: Released blocked after exact bounded QEMU evidence: fsck-clean repaired
  data and governed preflight passed, but fresh networkless guest emitted five runuser failures
  because user asb is absent, then powered off without TLC or attestation. Rebuild reviewed guest
  user/user-manager fixture before retry.

- 2026-09-18T16:50:13+00:00: Starting fresh bounded repair: reuse reviewed AR-1305 image-native
  user/user-manager root image read-only as disposable overlay; preserve exact limits and network
  isolation.

- 2026-09-18T16:50:16+00:00: Claimed by codex-ar1308-fixture-repair-20260918.

- 2026-09-18T16:50:30+00:00: Recorded command exit 1; command argv SHA-256
  7ea028c174ee40790446b8a86a380e05beef3c108ebc29fa33c2a950f93af0c3.

- 2026-09-18T16:50:52+00:00: Recorded command exit 0; command argv SHA-256
  abc4ea05931e6e1b0cade9cf90c439c941c0845591e933b53e8afc87e98867f5.

- 2026-09-18T16:51:03+00:00: Recorded command exit 0; command argv SHA-256
  1198b70b549341c317b6c3be4380d8a841065401ce3f4a91d21d600e3d60f9ba.

- 2026-09-18T16:52:02+00:00: Recorded command exit 0; command argv SHA-256
  2ac37e4198742f8943aa7c93b94e26df5909db15bd5b8de8254ad09590e1d2a7.

- 2026-09-18T16:52:15+00:00: Recorded command exit 0; command argv SHA-256
  50a586f5c81fe95da436fca6de6d5703483a8ef3655e32aea8145958966aa6e8.

- 2026-09-18T16:52:39+00:00: Recorded command exit 1; command argv SHA-256
  fc859cabbfd08adc0d787973c739f9fae0db4e8c80217c192118021fbe6bc06d.

- 2026-09-18T16:53:03+00:00: Recorded command exit 0; command argv SHA-256
  64fb8ab7c0d58b1adfefcf0a49a2cd8c0d91d1a6989b66352b54cb7047c119e3.

- 2026-09-18T16:53:16+00:00: Recorded command exit 1; command argv SHA-256
  fc859cabbfd08adc0d787973c739f9fae0db4e8c80217c192118021fbe6bc06d.

- 2026-09-18T16:54:15+00:00: Recorded command exit 0; command argv SHA-256
  862f0fbaca20f5dbef944ba32e0e61696872dd93b0783c2e4c9e4b154039e68a.

- 2026-09-18T16:54:27+00:00: Recorded command exit 1; command argv SHA-256
  fc859cabbfd08adc0d787973c739f9fae0db4e8c80217c192118021fbe6bc06d.

- 2026-09-18T16:55:02+00:00: Recorded command exit 1; command argv SHA-256
  fc859cabbfd08adc0d787973c739f9fae0db4e8c80217c192118021fbe6bc06d.

- 2026-09-18T16:55:32+00:00: Recorded command exit 0; command argv SHA-256
  2da8a5ceb7d3f5a60c9c3f31b9f945a8f04b4b19e047e87da631e5233e3987be.

- 2026-09-18T16:55:58+00:00: Recorded command exit 0; command argv SHA-256
  32e712471e499450a053e957b29f02727a1fbfee61f9851c66d20fa7a481e613.

- 2026-09-18T16:56:10+00:00: Recorded command exit 0; command argv SHA-256
  9260087a09bf53c1d86bb816078be3a7e7aef8ff1b5a75260842df6e303b6bcf.

- 2026-09-18T16:58:12+00:00: Reused reviewed AR-1305 root fixture by creating a disposable overlay
  from the pinned Ubuntu image and adding uid 1000 asb plus systemd linger. Governed preflight
  passed with absolute receipt paths. The bounded QEMU boot then stalled at
  systemd-networkd-wait-online for at least 1m44s and emitted no cloud-init, TLC, or attestation;
  process was gone afterward. This is a guest bootstrap blocker, not qualification.

- 2026-09-18T16:58:14+00:00: Released blocked: disposable asb-user overlay preflight passed, but
  QEMU networkless boot stalled indefinitely at systemd-networkd-wait-online before cloud-init/TLC.
  Next action is to mask that wait-online unit in the reviewed disposable overlay and retry once.

- 2026-09-18T16:59:47+00:00: Resuming bounded guest bootstrap repair: mask networkd wait-online in
  disposable overlay, then rerun preflight and exactly one networkless QEMU attempt.

- 2026-09-18T16:59:50+00:00: Claimed by codex-ar1308-fixture-repair-20260918.

- 2026-09-18T17:00:01+00:00: Recorded command exit 0; command argv SHA-256
  a376e2909747d4690f63c633d91c9de9d4abd3ebdec69d91a31b8889b99856e3.

- 2026-09-18T17:00:28+00:00: Recorded command exit 0; command argv SHA-256
  2f85692882d1a3aefd7e383c0e3a89dbea780223066dfc19442d8657a7db547e.

- 2026-09-18T17:00:41+00:00: Recorded command exit 0; command argv SHA-256
  38cea66496036951d335c9e9573e5bccfb3e8f1cbeb070ca818bc5ddfe33ed95.

- 2026-09-18T17:00:53+00:00: Recorded command exit 0; command argv SHA-256
  b102c62c48f28a09bd9768da3a06f829453c71bbda4036ca7e1be1e49b23d9c3.

- 2026-09-18T17:01:08+00:00: Recorded command exit 0; command argv SHA-256
  64fb8ab7c0d58b1adfefcf0a49a2cd8c0d91d1a6989b66352b54cb7047c119e3.

- 2026-09-18T17:01:21+00:00: Recorded command exit 1; command argv SHA-256
  2da8a5ceb7d3f5a60c9c3f31b9f945a8f04b4b19e047e87da631e5233e3987be.

- 2026-09-18T17:02:18+00:00: Recorded command exit 0; command argv SHA-256
  907e72c1973bb43473491bfa56e66c051db7ec2823de47c9f8162a711f8c7505.

- 2026-09-18T17:02:30+00:00: Recorded command exit 0; command argv SHA-256
  308788221dcc7b9f94e1717ecc0f23e1a57e634b63d7b953d7c162bbdcc74719.

- 2026-09-18T17:02:43+00:00: Recorded command exit 0; command argv SHA-256
  6e3690656343d82c1ce6d92c71c289ec4f60672e26c94d795b472d8d80cf4abf.

- 2026-09-18T17:02:54+00:00: Recorded command exit 0; command argv SHA-256
  edfdc89f585e02cef0185092254a79bf064418012cca73d64db4a9b2bc35634c.

- 2026-09-18T17:03:30+00:00: Recorded command exit 0; command argv SHA-256
  2da8a5ceb7d3f5a60c9c3f31b9f945a8f04b4b19e047e87da631e5233e3987be.

- 2026-09-18T17:03:57+00:00: Recorded command exit 0; command argv SHA-256
  32e712471e499450a053e957b29f02727a1fbfee61f9851c66d20fa7a481e613.

- 2026-09-18T17:04:09+00:00: Recorded command exit 0; command argv SHA-256
  51279695736ea819088f09be3324a2aa5ddcfda23e8c734cce64d62c35738b9a.

- 2026-09-18T17:06:07+00:00: Fresh overlay now contains uid 1000 asb, linger, and masked
  systemd-networkd-wait-online; host swap was restored and governed preflight passed. Bounded QEMU
  boot reached user-runtime-dir@1000 and user@1000 successfully, but cloud-init final completed in
  10.6s without executing the seed commands (no mount, TLC, or attestation) and guest remained at
  login; no qualification evidence.

- 2026-09-18T17:06:09+00:00: Released blocked: guest user manager and wait-online prerequisites
  passed, but stale cloud-init state prevented NoCloud seed execution; no TLC or attestation.
  Rebuild fresh overlay clearing cloud-init instance/seed state, then retry once.

- 2026-09-18T17:06:46+00:00: Fresh repair cycle: build a new overlay from pinned image with reviewed
  asb user/linger, masked wait-online, and cleared cloud-init state; then preflight and one bounded
  networkless QEMU attempt.

- 2026-09-18T17:06:49+00:00: Claimed by codex-ar1308-fixture-repair-20260918.

- 2026-09-18T17:07:03+00:00: Recorded command exit 0; command argv SHA-256
  c3954d561c6f988d2a748b5b52dab62b59cacdec1177b85e2890b2eb011008de.

- 2026-09-18T17:07:17+00:00: Recorded command exit 0; command argv SHA-256
  e57f41a9f8d0b80dbfd4ecf639c144a33921b200d49d679e86811a9d9436b24b.

- 2026-09-18T17:07:39+00:00: Recorded command exit 0; command argv SHA-256
  64fb8ab7c0d58b1adfefcf0a49a2cd8c0d91d1a6989b66352b54cb7047c119e3.

- 2026-09-18T17:07:51+00:00: Recorded command exit 1; command argv SHA-256
  55bfcc9abdf7abce14c6f5a96931bc4fd72414094b112c6ca4af431e9b577aac.

- 2026-09-18T17:08:22+00:00: Recorded command exit 0; command argv SHA-256
  3466f849aeebe9881019679561739a3e2b6fe852fc563b3e6e9328e33998a3e4.

- 2026-09-18T17:08:34+00:00: Recorded command exit 0; command argv SHA-256
  2d2f1b9bd0f7b6b0134292cbcae46322e81fe3343905678768e983f67bc0a71c.

- 2026-09-18T17:08:45+00:00: Recorded command exit 0; command argv SHA-256
  8872c219b63f189518e0f3de9b310ca20855dabc52b1d64b259130d21f499844.

- 2026-09-18T17:08:57+00:00: Recorded command exit 0; command argv SHA-256
  2a417015c73f58cbfd30321027ad2abc64f54eb3dfb3debeb45a21d6b591aa0d.

- 2026-09-18T17:09:19+00:00: Recorded command exit 0; command argv SHA-256
  55bfcc9abdf7abce14c6f5a96931bc4fd72414094b112c6ca4af431e9b577aac.

- 2026-09-18T17:09:39+00:00: Recorded command exit 0; command argv SHA-256
  32e712471e499450a053e957b29f02727a1fbfee61f9851c66d20fa7a481e613.

- 2026-09-18T17:09:51+00:00: Recorded command exit 1; command argv SHA-256
  fedd2e98179aa11280b6c77941d19fbd1992e85e708ad73497df7197af34dabf.

- 2026-09-18T17:11:24+00:00: Recorded command exit 0; command argv SHA-256
  65aaa1a9ac826d3e39359717c55004442458c71df774f7f5ff212af4dae69eb5.

- 2026-09-18T17:12:54+00:00: Recorded command exit 0; command argv SHA-256
  64fb8ab7c0d58b1adfefcf0a49a2cd8c0d91d1a6989b66352b54cb7047c119e3.

- 2026-09-18T17:13:26+00:00: Recorded command exit 0; command argv SHA-256
  32e712471e499450a053e957b29f02727a1fbfee61f9851c66d20fa7a481e613.

- 2026-09-18T17:13:38+00:00: Recorded command exit 1; command argv SHA-256
  330d02845dccb9b30ddd98644ee680b6244c1844cbcbf20208cd6fb71b87e382.

- 2026-09-18T17:14:02+00:00: Recorded command exit 1; command argv SHA-256
  330d02845dccb9b30ddd98644ee680b6244c1844cbcbf20208cd6fb71b87e382.

- 2026-09-18T17:14:28+00:00: Recorded command exit 0; command argv SHA-256
  d07d39a56570e8497e0234009d145a4616921172299bb61dcb123cc087547cc4.

- 2026-09-18T17:14:47+00:00: Recorded command exit 0; command argv SHA-256
  330d02845dccb9b30ddd98644ee680b6244c1844cbcbf20208cd6fb71b87e382.

- 2026-09-18T17:14:58+00:00: Recorded command exit 0; command argv SHA-256
  d07d39a56570e8497e0234009d145a4616921172299bb61dcb123cc087547cc4.

- 2026-09-18T17:15:21+00:00: Recorded command exit 0; command argv SHA-256
  64fb8ab7c0d58b1adfefcf0a49a2cd8c0d91d1a6989b66352b54cb7047c119e3.

- 2026-09-18T17:15:33+00:00: Recorded command exit 1; command argv SHA-256
  55bfcc9abdf7abce14c6f5a96931bc4fd72414094b112c6ca4af431e9b577aac.

- 2026-09-18T17:16:34+00:00: Concrete diagnosis: prior fresh boot executed NoCloud and transient
  RC=0, but verify.sh failed closed because the data filesystem UUID differed from the reviewed seed
  UUID; this prevented /mnt/asb-data and caused TLC_JAR_PATH rejection. The data UUID is now
  corrected and fsck-clean. Latest governed preflight was blocked before QEMU because host SwapFree
  was below 1 GiB: all 13 GiB active swap was consumed. Stop retries until swap is freed safely.

- 2026-09-18T17:16:36+00:00: Released blocked with measured causes: corrected data UUID after prior
  NoCloud mount failure; current preflight blocker is SwapFree below 1 GiB with 13 GiB swap fully
  used. Free swap without violating disk/resource gates before the next single QEMU attempt.

- 2026-09-18T17:19:44+00:00: Resource repair: swap is fully consumed by unrelated processes;
  preserve them, reclaim free swap by cycling the existing swap device with ample RAM, then rerun
  preflight.

- 2026-09-18T17:19:47+00:00: Claimed by codex-ar1308-fixture-repair-20260918.

- 2026-09-18T17:21:14+00:00: Recorded command exit 0; command argv SHA-256
  2d425d1d3898917919a80455bbf33d95846bff98dc10a9c21d4c5f1babd44bc0.

- 2026-09-18T17:21:25+00:00: Recorded command exit 0; command argv SHA-256
  475580fb76432d198e074a25154e0a6c982abdc130fdddc592a4b1c8022eaf44.

- 2026-09-18T17:22:03+00:00: Recorded command exit 0; command argv SHA-256
  55bfcc9abdf7abce14c6f5a96931bc4fd72414094b112c6ca4af431e9b577aac.

- 2026-09-18T17:22:26+00:00: Recorded command exit 0; command argv SHA-256
  32e712471e499450a053e957b29f02727a1fbfee61f9851c66d20fa7a481e613.

- 2026-09-18T17:22:37+00:00: Recorded command exit 0; command argv SHA-256
  73e2f18ec536dc17af713b694670c8235851bded09d3c5f6cce14d695d2fe1d8.

- 2026-09-18T17:23:52+00:00: Recorded command exit 0; command argv SHA-256
  157d8d7af7b73819932256559865c3d56a3d8fb22eedf8e97be2bcf7cf146e8f.

- 2026-09-18T17:24:10+00:00: Recorded command exit 0; command argv SHA-256
  1cbbecb30c30f92512d1e638d910d6ed262ee5e631c5d05fa81778838dbea4a2.

- 2026-09-18T17:24:22+00:00: Recorded command exit 0; command argv SHA-256
  b1404bf48f794bd8e67e21460d2453e2070da64ad36572be4d3b77e09fa3566e.

- 2026-09-18T17:25:01+00:00: Recorded command exit 4; command argv SHA-256
  89fd29a56353f956acc2c441216d683b5ababfafe67e1159bd5ff95291eb07d8.

- 2026-09-18T17:25:24+00:00: Recorded command exit 0; command argv SHA-256
  fd45842c30b5fef6afb30c4005b9f484e0ba30f7441ba0568b4a2d27e6bdff59.

- 2026-09-18T17:25:36+00:00: Recorded command exit 0; command argv SHA-256
  1e825cbbf50aa00f4a216c4c25b17d4b0f213414777e4024f579341ab00ef79a.

- 2026-09-18T17:25:48+00:00: Recorded command exit 0; command argv SHA-256
  24893ea7873a6f0168d6269f3ba74d0a42d1720923a3b81b0f5cbb2d6519498d.

- 2026-09-18T17:26:00+00:00: Recorded command exit 0; command argv SHA-256
  41b6d73fa421ada967bc9bb02e0e20b3d3e32d5081c8c9cdfdc28590e2b88ba4.

- 2026-09-18T17:26:40+00:00: Recorded command exit 0; command argv SHA-256
  f574a9e68e0ae5a0b9603c9431aadcccaf3cf60e19783673e643b700a93b5907.

- 2026-09-18T17:26:52+00:00: Recorded command exit 0; command argv SHA-256
  38cea66496036951d335c9e9573e5bccfb3e8f1cbeb070ca818bc5ddfe33ed95.

- 2026-09-18T17:27:04+00:00: Recorded command exit 0; command argv SHA-256
  96344a1a2a662f97349709e46cf5f667a088cc983b4a17cb21e02b5c0cfb7910.

- 2026-09-18T17:27:30+00:00: Recorded command exit 0; command argv SHA-256
  82c168c3f2ce6ed8fe4001612c76fe8da47fd3febfd0696adadf99c5bd421c14.

- 2026-09-18T17:27:51+00:00: Recorded command exit 0; command argv SHA-256
  64fb8ab7c0d58b1adfefcf0a49a2cd8c0d91d1a6989b66352b54cb7047c119e3.

- 2026-09-18T17:28:03+00:00: Recorded command exit 0; command argv SHA-256
  55bfcc9abdf7abce14c6f5a96931bc4fd72414094b112c6ca4af431e9b577aac.

- 2026-09-18T17:28:23+00:00: Recorded command exit 0; command argv SHA-256
  32e712471e499450a053e957b29f02727a1fbfee61f9851c66d20fa7a481e613.

- 2026-09-18T17:28:35+00:00: Recorded command exit 0; command argv SHA-256
  848e8860838a0813185466182b9d0ce634e237107bc9cc8d1a46390c8065986b.

- 2026-09-18T17:30:19+00:00: Recorded command exit 0; command argv SHA-256
  590676fcc7ab2aeb7667b3b1bacca738693bc446b3fd94ff9bc8b8c35dff2828.

- 2026-09-18T17:30:30+00:00: Recorded command exit 0; command argv SHA-256
  dab2d8a2a8186ec9ba024e092d58eeafe145e67f1277e2136dcb74344dfd06cd.

- 2026-09-18T17:30:44+00:00: Recorded command exit 0; command argv SHA-256
  1445643dd3c354e2a171194b462fde44bbc8650057416a18b4bbbee14e1f780b.

- 2026-09-18T17:30:59+00:00: Recorded command exit 0; command argv SHA-256
  64fb8ab7c0d58b1adfefcf0a49a2cd8c0d91d1a6989b66352b54cb7047c119e3.

- 2026-09-18T17:31:11+00:00: Recorded command exit 0; command argv SHA-256
  87092d088b82d18739478b88ec6ee22456257bc78852c506dbc3bddbccacaa6f.

- 2026-09-18T17:31:37+00:00: Recorded command exit 0; command argv SHA-256
  32e712471e499450a053e957b29f02727a1fbfee61f9851c66d20fa7a481e613.

- 2026-09-18T17:31:49+00:00: Recorded command exit 0; command argv SHA-256
  f46c9e32e9c010ee1c943c14f10ea52378fb618fe5f4bb31fea332cd279d47bf.

- 2026-09-18T17:32:53+00:00: Recorded command exit 0; command argv SHA-256
  9e149541fdc9b23e83ad3db22f1e69b88188d1ddf9ff5cf0035c67f356003035.

- 2026-09-18T17:33:05+00:00: Recorded command exit 0; command argv SHA-256
  dbe4373f89245c391738f4c07981f3f4d8b56c0705599010bb68a7bf5c074fc8.

- 2026-09-18T17:33:17+00:00: Recorded command exit 0; command argv SHA-256
  59f71b1be2f0f63d88d270d84df56a643e9d496031bb5048c496b2aef12a6ec1.

- 2026-09-18T17:33:28+00:00: Recorded command exit 0; command argv SHA-256
  41b6d73fa421ada967bc9bb02e0e20b3d3e32d5081c8c9cdfdc28590e2b88ba4.

- 2026-09-18T17:33:40+00:00: Recorded command exit 0; command argv SHA-256
  82c168c3f2ce6ed8fe4001612c76fe8da47fd3febfd0696adadf99c5bd421c14.

- 2026-09-18T17:33:52+00:00: Recorded command exit 0; command argv SHA-256
  03b11d051169b0ff6ed74241277dac21475bb5a981092d658b38293939c6b1d4.

- 2026-09-18T17:34:04+00:00: Recorded command exit 0; command argv SHA-256
  38cea66496036951d335c9e9573e5bccfb3e8f1cbeb070ca818bc5ddfe33ed95.

- 2026-09-18T17:34:15+00:00: Recorded command exit 0; command argv SHA-256
  0883ec5d58bc41d36187f50d580bf4b36dfd9fdc66eaf4d0ce46b0b316db949e.

- 2026-09-18T17:34:51+00:00: Recorded command exit 0; command argv SHA-256
  3d9a15424956cfbca318c7c02a1ab55efaad1023396ce673258dbf961dd6d67d.

- 2026-09-18T17:35:04+00:00: Recorded command exit 0; command argv SHA-256
  1df2d308a119863bdd11afe92cd66b826e0796d9833b74da05912fdaf54fe72e.

- 2026-09-18T17:35:25+00:00: Recorded command exit 0; command argv SHA-256
  64fb8ab7c0d58b1adfefcf0a49a2cd8c0d91d1a6989b66352b54cb7047c119e3.

- 2026-09-18T17:35:37+00:00: Recorded command exit 0; command argv SHA-256
  9cba9102188ca10db40bf2065515d886121fe82637c6e85e8b50a7f6de944360.

- 2026-09-18T17:35:59+00:00: Durable diagnosis update: corrected2 reached transient RC=0 but failed
  closed because the seed omitted TLC_JAR_PATH/TLC_JAR_SHA256; a fresh corrected seed now exports
  both exact values, receipt hash is refreshed, and overlay3 is newly built with
  asb/linger/wait-online mask. Governed preflight passed; QEMU is next.

- 2026-09-18T17:36:10+00:00: Recorded command exit 0; command argv SHA-256
  32e712471e499450a053e957b29f02727a1fbfee61f9851c66d20fa7a481e613.

- 2026-09-18T17:36:22+00:00: Recorded command exit 0; command argv SHA-256
  3d91f0697d3e7455c773f5b860bfa149c6511152e4c2e488b25f7e76e13a2f39.

- 2026-09-18T17:38:23+00:00: Recorded command exit 1; command argv SHA-256
  a67410a6889c60853f71a7e714d6f7fb279a734307b1b978e39c3d96d89c1fec.

- 2026-09-18T17:38:48+00:00: Recorded command exit 0; command argv SHA-256
  f0e57191b2c5b8b533559933c359a861856ade8e79ad38365bbcda991f2331c0.

- 2026-09-18T17:39:11+00:00: The prior corrected final reached transient RC=0 but failed before TLC
  because /srv/data/projects/.asb-tlc and worker paths were absent inside the guest; serial showed
  FileNotFoundError and missing attestation. Seed was updated to create data-backed guest .asb-tlc,
  admission.lock, worker queue, and bind it at /srv/data/projects/.asb-tlc. Earlier combined command
  had a quoting assertion failure; the direct replacement now succeeded and was recorded.

- 2026-09-18T17:39:21+00:00: Recorded command exit 0; command argv SHA-256
  e01bd8b8af55c39c7fb2a0d0c0b2ada678b055bda1120d4c0bd4524fa6d57924.

- 2026-09-18T17:39:33+00:00: Recorded command exit 0; command argv SHA-256
  68012b8bece9b3a46e886a5fc5e095397b06cb38c1e500c02b882902047632bb.

- 2026-09-18T17:39:44+00:00: Recorded command exit 0; command argv SHA-256
  4f6ed094e72b396b222e4f7bdd67498d33a5dc8cb6fd48fb9c3a095d56e13827.

- 2026-09-18T17:40:25+00:00: Recorded command exit 0; command argv SHA-256
  b6221e457593d5fc9abf2a6d19828c9b6d234e830a1502afb93bdd53ca49ac4b.

- 2026-09-18T17:40:36+00:00: Recorded command exit 0; command argv SHA-256
  38cea66496036951d335c9e9573e5bccfb3e8f1cbeb070ca818bc5ddfe33ed95.

- 2026-09-18T17:40:47+00:00: Recorded command exit 0; command argv SHA-256
  1e6e7eede18cb44fb86d19b1e1fbd875e839cd511c16c759002bd34cde3fcbcf.

- 2026-09-18T17:41:02+00:00: Recorded command exit 0; command argv SHA-256
  4a9579798999fd467ca3a62e246cf826d448b52092b8e9afca94ebb8757c481d.

- 2026-09-18T17:41:15+00:00: Recorded command exit 0; command argv SHA-256
  a310387167572effc360d07990189a6d97be918e181208bfe5cdc90fcc6e3179.

- 2026-09-18T17:41:36+00:00: Recorded command exit 0; command argv SHA-256
  64fb8ab7c0d58b1adfefcf0a49a2cd8c0d91d1a6989b66352b54cb7047c119e3.

- 2026-09-18T17:41:49+00:00: Recorded command exit 0; command argv SHA-256
  efe730b21571ac155af2bed941662a3240ea0e64c46aa07195b916f38ea2a199.

- 2026-09-18T17:42:09+00:00: Recorded command exit 0; command argv SHA-256
  32e712471e499450a053e957b29f02727a1fbfee61f9851c66d20fa7a481e613.

- 2026-09-18T17:42:21+00:00: Recorded command exit 0; command argv SHA-256
  70ef960905df3abf1a244f532a61aa3ce92d5d95b72b91ad18e3cc5a21adc570.

- 2026-09-18T17:44:01+00:00: Recorded command exit 0; command argv SHA-256
  0eaefe363797e87e4ae8b92118e134722be4287372fe2339a0e94c2c12db61d5.

- 2026-09-18T17:44:13+00:00: Recorded command exit 0; command argv SHA-256
  548616da45f4704e3c7647badeee994219aad97aef74ecb93ede3683c130a1a7.

- 2026-09-18T17:44:25+00:00: Recorded command exit 0; command argv SHA-256
  821b91e383e9ff256cbd9a4ad0b86b43488e25611dd1ea7bccdb6e06b0191b1e.

- 2026-09-18T17:44:36+00:00: Recorded command exit 0; command argv SHA-256
  4f6ed094e72b396b222e4f7bdd67498d33a5dc8cb6fd48fb9c3a095d56e13827.

- 2026-09-18T17:45:05+00:00: Recorded command exit 0; command argv SHA-256
  58681ece3523eb742f60c1a0a3a25aa6db2632b5d3986534962056235473e8d4.

- 2026-09-18T17:45:16+00:00: Recorded command exit 0; command argv SHA-256
  38cea66496036951d335c9e9573e5bccfb3e8f1cbeb070ca818bc5ddfe33ed95.

- 2026-09-18T17:45:28+00:00: Recorded command exit 0; command argv SHA-256
  a32a93857b618086cdc70081bead82e420af69a984d05630a0f3614bf67feab2.

- 2026-09-18T17:45:44+00:00: Recorded command exit 0; command argv SHA-256
  075a8b014ad80608ec906bfdad6804604f97f5bf8d7b483163c4572f46412907.

- 2026-09-18T17:45:57+00:00: Recorded command exit 0; command argv SHA-256
  f52a5f4b986479fa536e7f26df7ff321e54e249944a7364cd3447c0d80bd6813.

- 2026-09-18T17:46:17+00:00: Recorded command exit 0; command argv SHA-256
  64fb8ab7c0d58b1adfefcf0a49a2cd8c0d91d1a6989b66352b54cb7047c119e3.

- 2026-09-18T17:46:29+00:00: Recorded command exit 0; command argv SHA-256
  9cb678f8fd6b2a30e31c352c2e0b1e5778425212a26233050b84fb44cc4b02a2.

- 2026-09-18T17:46:50+00:00: Seed now includes guest-internal data-backed .asb-tlc bind mapping and
  guest-local safe.directory for the mounted state repository. Fresh overlay5 built; corrected seed
  receipt committed; governed preflight passed. QEMU is next.

- 2026-09-18T17:47:02+00:00: Recorded command exit 0; command argv SHA-256
  32e712471e499450a053e957b29f02727a1fbfee61f9851c66d20fa7a481e613.

- 2026-09-18T17:47:14+00:00: Recorded command exit 0; command argv SHA-256
  a4db7fbcb9e26718e925983549d4e264eb7bb28b65d803cc9750b748f4a19d2f.

- 2026-09-18T17:48:53+00:00: Recorded command exit 0; command argv SHA-256
  288cf2163af3448a3633148853d9a5b30f57304be00b5cf8b657e821c9dcb7c5.

- 2026-09-18T17:49:05+00:00: Recorded command exit 0; command argv SHA-256
  2f8ee1120a13b643a129451d9b15281deaa9301ee4274590d5c9d556273e07c2.

- 2026-09-18T17:49:17+00:00: Recorded command exit 0; command argv SHA-256
  e9c1c44de6100f750a228ce332045df1a32c046c7d5f69b0a6247ac388c1b5d3.

- 2026-09-18T17:49:28+00:00: Recorded command exit 0; command argv SHA-256
  4f6ed094e72b396b222e4f7bdd67498d33a5dc8cb6fd48fb9c3a095d56e13827.

- 2026-09-18T17:49:58+00:00: Recorded command exit 0; command argv SHA-256
  721be5c39b7ce046fe127367337abbfc1584ccb1159edb93de0edbf6df87166a.

- 2026-09-18T17:50:10+00:00: Recorded command exit 0; command argv SHA-256
  6509e0143f2c4f4ce843a158305bf178f01c24d908f2ae8ba8ed733e5a0045cb.

- 2026-09-18T17:50:22+00:00: Recorded command exit 0; command argv SHA-256
  785e2c82f3d400e820f108b0bdf67b98f3cb3af3e1b741120ea1c52dbcab2aa1.

- 2026-09-18T17:50:34+00:00: Recorded command exit 0; command argv SHA-256
  4f6ed094e72b396b222e4f7bdd67498d33a5dc8cb6fd48fb9c3a095d56e13827.

- 2026-09-18T17:50:56+00:00: Recorded command exit 0; command argv SHA-256
  89dc7071ad6250d783b7caae22b403b35d6880123dedd7c037675a2b0c5296c1.

- 2026-09-18T17:51:07+00:00: Recorded command exit 0; command argv SHA-256
  38cea66496036951d335c9e9573e5bccfb3e8f1cbeb070ca818bc5ddfe33ed95.

- 2026-09-18T17:51:19+00:00: Recorded command exit 0; command argv SHA-256
  0297126317023e34e0348358da8dcc5be6c8bef1412f1fe4dd560ec61c4bbd1f.

- 2026-09-18T17:51:34+00:00: Recorded command exit 0; command argv SHA-256
  38f27c49d91f24e5bb624507a27b1c11bf69e2f93b15bedd02ea3a5e53cf326d.

- 2026-09-18T17:51:48+00:00: Recorded command exit 0; command argv SHA-256
  deff4c3b44a3192aebd5c202f434df9e698bfbcec5ec973e42a1fe498ddf84a3.

- 2026-09-18T17:52:08+00:00: Recorded command exit 0; command argv SHA-256
  64fb8ab7c0d58b1adfefcf0a49a2cd8c0d91d1a6989b66352b54cb7047c119e3.

- 2026-09-18T17:52:20+00:00: Recorded command exit 0; command argv SHA-256
  b3468c7a6ed2c2dc5b45503411fb4dbd795b6fa518c43b6376ecbfe049708d20.

- 2026-09-18T17:52:42+00:00: Previous bind-final reached transient RC=0 but Git provenance failed.
  The seed correction now adds safe.directory entries for state/formal/git and chowns disposable
  mounted state/git to asb; malformed literal newline was corrected and new seed hash recorded.
  Fresh overlay6 built and governed preflight passed.

- 2026-09-18T17:52:53+00:00: Recorded command exit 0; command argv SHA-256
  32e712471e499450a053e957b29f02727a1fbfee61f9851c66d20fa7a481e613.

- 2026-09-18T17:53:04+00:00: Recorded command exit 0; command argv SHA-256
  35b7a5232dc1ef6e9e110dba17bce23d77710b97ccd2a3d0faa38152dea7416a.

- 2026-09-18T17:54:05+00:00: Recorded command exit 0; command argv SHA-256
  64fb8ab7c0d58b1adfefcf0a49a2cd8c0d91d1a6989b66352b54cb7047c119e3.

- 2026-09-18T17:54:36+00:00: Recorded command exit 0; command argv SHA-256
  9a3e7c89a40450da1f3521f595a85660ac11c6b3efc57b53b2f5bda47369b176.

- 2026-09-18T17:54:47+00:00: Recorded command exit 0; command argv SHA-256
  9031d0a8a30d9e8235241cc09fdff9d256387f99f2427ac9303bd6e660b2ad85.

- 2026-09-18T17:54:58+00:00: Recorded command exit 0; command argv SHA-256
  654402be4ddb9bfcc2c087f082ce505fdf490baced4bb8bc74543455c7c7d7ea.

- 2026-09-18T17:55:10+00:00: Recorded command exit 0; command argv SHA-256
  4f6ed094e72b396b222e4f7bdd67498d33a5dc8cb6fd48fb9c3a095d56e13827.

- 2026-09-18T17:55:33+00:00: Recorded command exit 0; command argv SHA-256
  32e712471e499450a053e957b29f02727a1fbfee61f9851c66d20fa7a481e613.

- 2026-09-18T17:55:45+00:00: Recorded command exit 0; command argv SHA-256
  675e7b88d2a0c04c6334dda0febb29f5c9498c39f58d611403d5c90f5bf15d8a.

- 2026-09-18T17:55:56+00:00: Recorded command exit 0; command argv SHA-256
  38cea66496036951d335c9e9573e5bccfb3e8f1cbeb070ca818bc5ddfe33ed95.

- 2026-09-18T17:56:08+00:00: Recorded command exit 0; command argv SHA-256
  3487168b08b55270aa6c62f3d5567ccf6a18ed4e6c46c83416965449a8b39663.

- 2026-09-18T17:56:20+00:00: Recorded command exit 0; command argv SHA-256
  8516ded688f7297ec31c2b4c868f2059171ebb588f501ceccf2fe5fe4774c8fa.

- 2026-09-18T17:56:39+00:00: Recorded command exit 0; command argv SHA-256
  4c84c54f0493e2eebd583679386ecca673064a9b8fba767d0723643697f1b7d8.

- 2026-09-18T17:57:02+00:00: Recorded command exit 0; command argv SHA-256
  64fb8ab7c0d58b1adfefcf0a49a2cd8c0d91d1a6989b66352b54cb7047c119e3.

- 2026-09-18T17:57:14+00:00: Recorded command exit 0; command argv SHA-256
  c6327c2bcaf4e504f01d66708e1b5737741f1a6ac0e336ec443a46c3388c3757.

- 2026-09-18T17:57:35+00:00: Definitive prior blocker: data fixture contains state/.git, not
  top-level git; GIT_DIR=/mnt/asb-data/git caused provenance failure. Seed now uses
  GIT_DIR=/mnt/asb-data/state/.git, retains state work tree, and adds exact safe-directory/ownership
  setup. Fresh overlay7 built; governed preflight passed.

- 2026-09-18T17:57:50+00:00: Recorded command exit 0; command argv SHA-256
  32e712471e499450a053e957b29f02727a1fbfee61f9851c66d20fa7a481e613.

- 2026-09-18T17:58:09+00:00: Recorded command exit 0; command argv SHA-256
  44eaa7f2f713530affb2895d05db262af865747da652bc44c0ca50a2f33bbe86.

- 2026-09-18T18:04:50+00:00: Heartbeat by codex-ar1308-fixture-repair-20260918.

- 2026-09-18T18:11:09+00:00: Heartbeat by codex-ar1308-fixture-repair-20260918.

- 2026-09-18T18:12:41+00:00: Heartbeat by codex-ar1308-fixture-repair-20260918.

- 2026-09-18T18:15:31+00:00: Heartbeat by codex-ar1308-fixture-repair-20260918.

- 2026-09-18T18:16:16+00:00: Heartbeat by codex-ar1308-fixture-repair-20260918.

- 2026-09-18T18:18:06+00:00: Heartbeat by codex-ar1308-fixture-repair-20260918.

- 2026-09-18T18:22:49+00:00: Heartbeat by codex-ar1308-fixture-repair-20260918.

- 2026-09-18T18:24:17+00:00: Heartbeat by codex-ar1308-fixture-repair-20260918.

- 2026-09-18T18:28:44+00:00: Heartbeat by codex-ar1308-fixture-repair-20260918.

- 2026-09-18T18:30:46+00:00: Heartbeat by codex-ar1308-fixture-repair-20260918.

- 2026-09-18T18:33:17+00:00: Heartbeat by codex-ar1308-fixture-repair-20260918.

- 2026-09-18T18:35:42+00:00: Heartbeat by codex-ar1308-fixture-repair-20260918.

- 2026-09-18T18:53:22+00:00: Heartbeat by codex-ar1308-fixture-repair-20260918.

- 2026-09-18T18:54:55+00:00: Heartbeat by codex-ar1308-fixture-repair-20260918.

- 2026-09-18T19:08:55+00:00: Recorded command exit 0; command argv SHA-256
  4735a967a0efbd68c5a2b78147594936318ac9bdfa9d3a74e2db9125c4e43804.

- 2026-09-18T19:09:46+00:00: Final bounded networkless QEMU terminated after 4200 seconds. TLC
  transient admission passed, then liveness checking failed closed with Java out of memory:
  46,920,678 generated states, 38,735,235 distinct states, and 10,722,623 states left on the queue;
  exit=1 and no success attestation was emitted. The validator consequently found no attestation
  file. This is a truthful capacity failure, not a model success; AR-1307 is not qualified.

- 2026-09-18T19:09:49+00:00: Released blocked after terminal capacity failure: the final networkless
  QEMU run reached liveness checking, Java exhausted memory, exited 1, and emitted no attestation.
  Further work requires a separately reviewed capacity contract or model reduction; do not qualify
  AR-1307 from this run.

- 2026-09-18T20:43:02+00:00: Re-opening bounded capacity repair after prior Java OOM: AR-1304 is
  done, no active AR-1308 worker/process exists, and a fresh disposable runner may be attempted
  without changing the AR-1307 3G/3G/2-worker/2-core process contract. Claim only to audit existing
  fixture provenance and provision a larger guest capacity; preserve any terminal failure.

- 2026-09-18T20:43:05+00:00: Claimed by asb-ar1308-capacity-repair-20260918.

- 2026-09-18T20:44:35+00:00: Heartbeat by asb-ar1308-capacity-repair-20260918.

- 2026-09-18T20:45:19+00:00: Recorded command exit 0; command argv SHA-256
  1be7d5e73eb01f7e1083a3cfe31d4aa1f7ce8afc64bfd90fa3c6f8b00ba9f34a.

- 2026-09-18T20:46:07+00:00: Recorded command exit 0; command argv SHA-256
  4ee6deb1cb919432c64a4f7a8e4f61c148017cd8c8bd53edaf7252b35f7f8724.

- 2026-09-18T20:46:26+00:00: Recorded command exit 0; command argv SHA-256
  c7651711ca61ea1ed87bfcfb6d91a3b66f82e2a445d83cda6e924cc7c2fcd5ab.

- 2026-09-18T20:46:41+00:00: Recorded command exit 0; command argv SHA-256
  edfdc89f585e02cef0185092254a79bf064418012cca73d64db4a9b2bc35634c.

- 2026-09-18T20:47:11+00:00: Recorded command exit 1; command argv SHA-256
  f4dd6145c4e57d78e685c3e0a6d248aee969a3049db1176342cfc7af89ad9686.

- 2026-09-18T20:47:37+00:00: Bounded audit result: no AR-1308 QEMU is active and AR-1304 is done.
  Existing receipt is x86_64, network none, no host mounts, QEMU 8.2.2, 8 vCPU, 16 GiB guest swap,
  64 GiB disk, and unchanged 3G memory/3G swap/2-worker/2-core/8G-address-space/7200s process
  contract, but it pins older AR-1307 head ab485f767 rather than current signed task head 969eef058.
  Live preflight was run through handoffctl and failed closed: approved root has only about 4.9 GiB
  free versus 16 GiB minimum; admission lock, pinned JDK, and TLC JAR are absent at the supplied
  runtime root. No formal QEMU/TLC attempt was started. Host swap was restored after bounded
  capacity inspection; no unrelated process was stopped and no cache/artifact was deleted. Required
  next action is provision approved second-disk headroom and exact current input bundle; do not
  weaken validator or process limits.

- 2026-09-18T20:47:46+00:00: Released blocked after bounded live preflight. No formal run was
  attempted. Current receipt preserves the 3G/3G/2-worker/2-core/8G/7200s process contract, network
  none, no host mounts, x86_64 QEMU 8.2.2, 8 vCPU, and 16 GiB guest swap, but it is bound to stale
  AR-1307 head ab485f767. Preflight failed closed on only 4.9 GiB approved-root free space versus 16
  GiB required, and missing admission lock, pinned JDK, and TLC JAR at the supplied runtime root.
  AR-1307 current signed head is 969eef058. Host swap was restored; no caches or artifacts were
  deleted, and no unrelated process was stopped. Reopen only after an approved second-disk
  capacity/input bundle is available and the exact current receipt passes all gates.

- 2026-09-18T21:15:25+00:00: Coordinator authorized runner-provisioning attempt: inspect approved
  second-disk capacity and prepare only the exact isolated QEMU contract; fail closed if
  disk/headroom or pinned inputs are unavailable.

- 2026-09-18T21:15:28+00:00: Claimed by codex-ar1308-runner-provision-20260918.

- 2026-09-18T21:15:56+00:00: Recorded command exit 1; command argv SHA-256
  7201d0db32254111fcd4abb58f3a33ad14e1be0eae79deb36cace649c67172d0.

- 2026-09-18T21:16:17+00:00: Runner provisioning attempt complete. No VM was booted. Exact validator
  run via handoffctl at 2026-09-18T21:15Z failed closed: approved second-disk root has only ~4.9 GiB
  free (<16 GiB minimum); source is not signed AR-1307 969eef058;
  receipt/model/seed/JDK/TLC/admission-lock inputs are not all present and bound. Preserved existing
  evidence and unchanged 3G/3G/2-worker/2-core/8G/7200s process contract. Next action: provision
  approved second-disk headroom and exact current input bundle, then rerun validator before any QEMU
  boot.

- 2026-09-18T22:12:21+00:00: Fresh bounded preflight audit: verify current second-disk capacity and
  exact AR-1307 signed input bundle before any runner provisioning; fail closed if any contract gate
  is absent.

- 2026-09-18T22:12:24+00:00: Claimed by ar1310_followup_routing.

- 2026-09-18T22:12:50+00:00: Recorded command exit 0; command argv SHA-256
  fcf82da0d8662eb74778e1a3ff8d4a1cab9924248b6c9803e7989df28bd064e3.

- 2026-09-18T22:13:05+00:00: Recorded command exit 0; command argv SHA-256
  de365e9064be09323bd473a1f9cdfc3e01c2d88c5cf8a5a4db60e931f08ec14c.

- 2026-09-18T22:13:20+00:00: Recorded command exit 0; command argv SHA-256
  c2d4e99e505197c27ccd1d9520ddc5466bba414d260a658bb3cf820835ecfc6f.

- 2026-09-18T22:13:34+00:00: Heartbeat by ar1310_followup_routing.

- 2026-09-18T22:13:57+00:00: Heartbeat by ar1310_followup_routing.

- 2026-09-18T22:14:26+00:00: Recorded command exit 1; command argv SHA-256
  24322d15e205508aa27e564988dd8aa4a0dd303e8504abbd7def1cade0c87e05.

- 2026-09-18T22:14:55+00:00: Recorded command exit 0; command argv SHA-256
  190318643b5aa43246de70b4cb595f3734e92e07352c2b937ce0565abe6c8f60.

- 2026-09-18T22:17:06+00:00: Interrupted provisioning worker after bounded preflight; capacity is
  now above disk floor but exact AR-1307 969eef058 input bundle and pinned runtime inputs are still
  not proven present. Preserve unchanged 3G/3G/2-worker/2-core/8G/7200s contract; next run must
  provision only after exact bundle and all preflight gates pass.

- 2026-09-18T22:18:11+00:00: Coordinator-authorized runner-only preparation: provision a clean
  disposable base/overlay and receipt under /srv/data/projects. Do not boot or qualify until exact
  signed AR-1307 input bundle and all preflight inputs are present.

- 2026-09-18T22:18:14+00:00: Claimed by coordinator-ar1308-runner.

- 2026-09-18T22:18:28+00:00: Recorded command exit 0; command argv SHA-256
  60721d549a5e0c55db17bf773ce56487f01205fd76e867ca73d0b3080fe3946c.

- 2026-09-18T22:18:41+00:00: Recorded command exit 0; command argv SHA-256
  16d12de5b482ba60784e720725bc1698c7d017f30cfb6d48f4aec37ce3a6c1df.

- 2026-09-18T22:18:53+00:00: Recorded command exit 0; command argv SHA-256
  8b42956c1bcd1b0e4ffb940e7069ebb4821b2ad3f9b0da62b3f16fc3b41b742c.

- 2026-09-18T22:20:02+00:00: Recorded command exit 0; command argv SHA-256
  45068ac056e80cd18eec684ecd4283fec35652d280b4a55ccf0d20645e6ac23b.

- 2026-09-18T22:20:15+00:00: Heartbeat by coordinator-ar1308-runner.

- 2026-09-18T22:20:29+00:00: Recorded command exit 0; command argv SHA-256
  865e3b8d6530ed42aa06cc0b372949bf0148aee9b63ac534dff6f1d35de0dec4.

- 2026-09-18T22:21:13+00:00: Prepared clean disposable runner at
  /srv/data/projects/asb-state-tlc-vm-ar1308-clean-v1 via handoffctl: x86_64 QEMU 8.2.2, q35
  KVM-or-TCG, 8 vCPU, 32768 MiB guest RAM, 16384 MiB guest swap contract, no NIC, no host mounts,
  sparse 16 GiB data image, disposable qcow2 root overlay. Receipt and argv are recorded with status
  prepared-not-qualified. No VM was booted and no qualification claimed because exact signed AR-1307
  969eef058 object/input bundle, pinned JDK/TLC, admission lock, and exact seed remain unavailable;
  preserve unchanged 3G/3G/2-worker/2-core/8G/7200s process contract. Next action: bind exact
  inputs, regenerate seed, run full preflight, then boot only after every gate passes.

- 2026-09-18T22:41:19+00:00: Repair runner contract: reviewed capacity evidence requires a >=64 GiB
  virtual disk; enlarge the prepared sparse data image only, preserve no-network/no-mounts and the
  3G/3G process contract, and do not boot.

- 2026-09-18T22:41:22+00:00: Claimed by coordinator-ar1308-runner.

- 2026-09-18T22:41:29+00:00: Recorded command exit 0; command argv SHA-256
  6f172b22f9ed55918fc516c48a1549e602623700745a6bbaae1d00c3c7d298d5.

- 2026-09-18T22:41:41+00:00: Recorded command exit 0; command argv SHA-256
  cd43819517698c99736916283b7a0e90aeb4e49bb8cfc8569e553efd4798f342.

- 2026-09-18T22:42:03+00:00: Recorded command exit 1; command argv SHA-256
  3b22a7b24c200811a7cdc6b19b84f08172933b2c9eb7715c489f3fc7b3fdd205.

- 2026-09-18T22:42:30+00:00: Recorded command exit 0; command argv SHA-256
  68e27c941b8dd556a41dfa5ca3c66a70eda8b07a2ddd9859d7c03d2f1bbeea72.

- 2026-09-18T22:43:23+00:00: Recorded command exit -9; command argv SHA-256
  a5540bef81253d58bb5e3099f15dbbc670c14839b271db9b5c02a5ca761b60da.

- 2026-09-18T22:44:48+00:00: Recorded command exit 0; command argv SHA-256
  2e2fd0bfbd13db2a5a5349e4990c643c96fff24946c3dbd73fa0eed951d4dce6.

- 2026-09-18T22:45:01+00:00: Recorded command exit 0; command argv SHA-256
  d1040736945ddb9eb8a1299ce8704ac70b34e8463570a040e91bce13cccbb5d2.

- 2026-09-18T22:45:34+00:00: Repaired runner disk property to reviewed >=64 GiB virtual capacity;
  receipt remains prepared-not-qualified.

- 2026-09-18T22:45:36+00:00: Runner now has 64 GiB sparse data disk, QEMU 8.2.2 x86_64, 8 vCPU, 32
  GiB RAM, 16 GiB swap contract, no network/mounts. Exact AR-1307 inputs and pinned runtime
  artifacts remain unavailable; no VM boot or TLC qualification.

- 2026-09-18T22:50:44+00:00: Coordinator repair: validate and normalize the prepared clean-v1 runner
  receipt/command metadata; no qualification or VM boot.

- 2026-09-18T22:51:06+00:00: Claimed by coordinator-ar1308-runner-repair.

- 2026-09-18T22:51:14+00:00: Recorded command exit 0; command argv SHA-256
  0726db46f1475cd18e62a743f8645a6457a8bcbcafa0c55775a300ed3cff3af6.

- 2026-09-18T22:51:43+00:00: Recorded command exit 0; command argv SHA-256
  43facd3d31c8262bd7f8f923a4ffb7275faf13156c45e0245691b112bafefa38.

- 2026-09-18T22:52:06+00:00: Repaired qemu-command.json through handoffctl run: removed the literal
  backslash-n trailer and confirmed strict JSON parsing. Receipt and argv agree on 64 GiB data
  capacity, 32 GiB guest memory, 8 vCPU, and network none. No VM boot or qualification claim.

- 2026-09-18T22:52:15+00:00: Runner preparation complete and durable: strict JSON command metadata
  and receipt validated; 64 GiB sparse disk, x86_64 QEMU 8.2.2, q35, 8 vCPU, 32 GiB RAM, 16 GiB swap
  contract, no network/mounts. AR remains blocked because the exact signed AR-1307 969eef058 runtime
  bundle, pinned JDK/TLC/model/seed/admission lock are not all available; no VM boot or
  qualification claimed.

- 2026-09-18T22:52:40+00:00: Shorten next action to satisfy schema length; preserve runner and
  blocker evidence.

- 2026-09-18T22:52:43+00:00: Claimed by coordinator-ar1308-runner-repair.

- 2026-09-18T22:52:46+00:00: Schema repair: shortened next_action. Runner remains
  prepared-not-qualified; no VM boot.

- 2026-09-18T22:52:48+00:00: Runner metadata is valid and capacity contract is recorded. Exact
  AR-1307 runtime bundle and pinned inputs remain unavailable; no qualification claimed.

- 2026-09-26T18:50:40+00:00: Reopen for bounded preflight audit of the prepared offline QEMU runner
  and exact AR-1307 input bundle; do not claim formal qualification without all signed inputs.

- 2026-09-26T18:50:43+00:00: Claimed by coordinator-ar1308-preflight.

- 2026-09-26T18:51:06+00:00: Heartbeat by coordinator-ar1308-preflight.

- 2026-09-26T18:51:09+00:00: Recorded command exit 0; command argv SHA-256
  56fc20b745597869b6079538c2ce4f8c8e81575664f4e107ac98e15a5ef7bb3d.

- 2026-09-26T18:51:23+00:00: Recorded command exit 0; command argv SHA-256
  c5226efbf2d9122478fb3425829f24ae96077c2557647e62a2c4cd0f9f5f7773.

- 2026-09-26T18:51:38+00:00: Recorded command exit 0; command argv SHA-256
  404edb8781b55ef84c4a9a0a1511e35f552f46c9a385029a6b36967b9ae4e414.

- 2026-09-26T18:51:52+00:00: Recorded command exit 0; command argv SHA-256
  6ae81408bf7bfc67e12b86f3045d4f29239d1ccfe7ed5fd48b593f1ceda9502b.

- 2026-09-26T18:52:07+00:00: Recorded command exit 0; command argv SHA-256
  d46ee55cc4d03459728d000ce76f4e2bc45c668b0bdae657885fb6e62f872e74.

- 2026-09-26T18:52:22+00:00: Recorded command exit 1; command argv SHA-256
  85d99fde26e92e8de5d8828563fcf79bf4f6bfad37519b4277b75ac4db1376ae.

- 2026-09-26T18:52:36+00:00: Recorded command exit 0; command argv SHA-256
  e0af271940e91b3451f34d43f9e14f4c19b8ee8234fe31ec6ea2defbb0cc558c.

- 2026-09-26T18:52:51+00:00: Recorded command exit 1; command argv SHA-256
  467d8f54b6dceacedcd1a1f6aeb295f5cbc26d84918b3e2689533a77543fcdc6.

- 2026-09-26T18:53:15+00:00: Recorded command exit 0; command argv SHA-256
  e0af271940e91b3451f34d43f9e14f4c19b8ee8234fe31ec6ea2defbb0cc558c.

- 2026-09-26T18:53:32+00:00: Recorded command exit 0; command argv SHA-256
  076e41b5fec43bd74e9c7735fa540cf14e0e80ea0f26da138719a68a0c29e29b.
