---
{
  "branch": "feature/ar-1308-full-exhaustive-qemu-capacity",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-18T15:47:05+00:00",
  "depends_on": [
    "AR-1304"
  ],
  "id": "AR-1308",
  "next_action": "PR #26 is blocked by independent review: require closed validator schema and actual image/overlay/QEMU/version/hypervisor/disk/inode/swap checks, exact TLC/source identity, sanitized receipt digests, complete negative tests and applicable full-quality CI. Rebase and re-review before any full QEMU attempt.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "codex-ar1308-qemu-capacity-20260918",
  "plan": "../plans/AR-1308.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Provide governed disposable capacity for exact full-exhaustive TLC liveness qualification.",
  "task_revision": 65,
  "title": "Full-exhaustive QEMU capacity qualification",
  "updated_at": "2026-09-18T14:27:10+00:00",
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
