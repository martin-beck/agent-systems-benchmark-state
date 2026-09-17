---
{
  "branch": "feature/ar-1287-delegated-sandbox-runner",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1287",
  "next_action": "Release AR-1287 done after final reconciliation: protected merge 7ea3e001 exact-main workflows 35202285902/85873/85881/85905/85917/85930/85955 all green; KVM guest passed 51 normal plus qualified backend test. Promote AR-1301 afterward.",
  "observed_branch": "feature/ar-1287-delegated-sandbox-runner",
  "observed_dirty": 0,
  "observed_head": "dba5f9bb6973cbb256695161e83f7a0eee860fb9",
  "owner": "",
  "plan": "../plans/AR-1287.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "done",
  "summary": "Provide a delegated runner for real strict-replay child lifecycle qualification.",
  "task_revision": 18,
  "title": "Delegated sandbox runner capability",
  "updated_at": "2026-09-17T09:03:58+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1287-delegated-sandbox-runner"
}
---

## AR-1287

Set up the approved container/VM execution boundary required by AR-1286. Do not claim product
lifecycle completion until the actual child and fault fixtures run in the qualified boundary.

- 2026-09-17T02:33:02+00:00: Runner setup is independent remediation for AR-1286 namespace
  capability blocker.

- 2026-09-17T02:33:14+00:00: Claimed by asb_ar1287_namespace_runner.

- 2026-09-17T02:34:29+00:00: Initial capability checkpoint: Docker 29.7.2 overlay2 cgroupv2 is
  available through the project-local socket. Pinned invocation candidate
  awq-runner-v1:python3.13.15 image ID
  sha256:e9edc4a58d865bb8de5e1ec29df920d37721204e31b6d31a969d37ac16c028ae, Architecture amd64, no
  RepoDigests. Bounded --network none --read-only --cap-drop ALL --pids-limit 32 --memory 128m
  --cpus 1 run succeeded; outbound socket failed with OSError, write failed read-only, and Docker
  reported no mounts. This is capability evidence only, not approved provenance. binfmt qemu-aarch64
  is enabled; no pinned arm64 image is locally available. No product/asb-tui mutation.

- 2026-09-17T02:36:35+00:00: 2026-09-17T02:36:00+00:00: Qualification follow-up: docker image
  inspect awq-runner-v1:python3.13.15 reports Id
  sha256:e9edc4a58d865bb8de5e1ec29df920d37721204e31b6d31a969d37ac16c028ae, RepoTags only,
  RepoDigests=[], Config.Labels=null, no User/Entrypoint/Cmd metadata, Architecture amd64, six local
  rootfs layers, and no source/revision/signature/license provenance. Bounded Docker daemon remains
  29.7.2 overlay2 cgroupv2 with AppArmor/seccomp/cgroupns security options. In-container probe as
  uid 0 found bwrap=None, systemd-run=None, /run/systemd/system=false; therefore this image cannot
  host the required AR-1286 bwrap/systemd-scope contract. Local command inventory found no podman,
  systemd-nspawn, firecracker, qemu-system-x86_64, or virt-install; user systemd reports degraded.
  Network-none/read-only/no-mount probe remains only generic Docker evidence, not qualified runner
  evidence. No product/asb-tui mutation.

- 2026-09-17T02:36:49+00:00: 2026-09-17T02:37:00+00:00: Released ownerless blocked after read-only
  qualification. Exact evidence: local Docker 29.7.2 candidate awq-runner-v1:python3.13.15 Id
  sha256:e9edc4a58d865bb8de5e1ec29df920d37721204e31b6d31a969d37ac16c028ae is amd64 only,
  RepoDigests=[] and Config.Labels=null with no source/revision/signature/license provenance;
  in-container probe has bwrap=None, systemd-run=None, /run/systemd/system=false. Docker
  network-none/read-only/no-mount and outbound denial are generic capability only. No approved
  immutable multi-arch image or VM/systemd-nspawn/firecracker/qemu-system runtime is available
  locally; AR-1286 positive lifecycle remains blocked and must not be claimed. Next action:
  coordinator provision an approved signed/pinned delegated runner or successor AR; preserve AR-1286
  fail-closed.

- 2026-09-17T07:51:33+00:00: Created disposable KVM Ubuntu 24.04 VM under
  /srv/data/projects/asb-replay-vm with checksum-verified cloud image; installed pinned QEMU 8.2.2.
  Guest-only AppArmor userns setting enabled. As user asb, unshare -Ur, bwrap --unshare-net, user
  systemd-run scope, and denied-egress probes pass; qualified AR-1286 runtime test passes. Continue
  full lifecycle qualification and record bounded evidence.

- 2026-09-17T07:51:39+00:00: Claimed by root.

- 2026-09-17T07:52:31+00:00: Provisioned /srv/data/projects/asb-replay-vm: checksum-verified Ubuntu
  24.04 cloud image, qcow2 overlay, cloud-init, QEMU/KVM 8.2.2. Guest systemd manager is running;
  guest-only AppArmor userns restriction was set to 0. As unprivileged user asb, unshare -Ur, bwrap
  --unshare-net, user systemd-run TasksMax=16/MemoryMax=64M, and denied-egress probes pass. The
  AR-1286 qualified runtime backend test passes as asb. Full copied test binary run found one VM
  path-sensitive malformed-spec assertion failure; retain as follow-up, do not claim full suite.

- 2026-09-17T07:55:07+00:00: VM fixture path was corrected by creating the immutable expected
  workspace prefix inside the guest, without mounting host source. Re-ran as unprivileged asb: all
  51 normal asb-runtime tests pass (1 qualified test intentionally ignored in normal suite), and
  explicit ignored qualified_runtime_backend_executes_and_reaps_child passes. Capability and
  denied-egress probes remain green.

- 2026-09-17T08:28:20+00:00: Heartbeat by root.

- 2026-09-17T08:30:27+00:00: PR #216 merged protected; runner/KVM evidence is complete, but
  exact-main policy failed on protected-main merge-tree mismatch. Preserve AR-1301 dependency
  ordering.

- 2026-09-17T08:37:23+00:00: Heartbeat by root.

- 2026-09-17T08:57:30+00:00: AR-1226 repair PR #218 merged protected as 7ea3e001; prior 8737bbed
  policy failure is superseded. Await exact-main assurance before release.

- 2026-09-17T09:03:55+00:00: Final exact-main evidence is terminal green for all required workflows,
  including policy, Rust, formal, fault, hosted portability, headers, repository quality, and
  emulated AArch64. Runner PR #216 merged as 8737bbed; repair PR #218 merged as 7ea3e001. KVM
  evidence remains under /srv/data/projects/asb-replay-vm.

- 2026-09-17T09:03:58+00:00: AR-1287 complete: signed/DCO runner PR #216 merged, KVM capability and
  runtime evidence passed, and repaired exact-main merge 7ea3e001 passed all required hosted gates.
  Ownerless done; AR-1301 dependency is now satisfied.
