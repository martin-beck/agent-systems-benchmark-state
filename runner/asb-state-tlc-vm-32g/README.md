# ASB state TLC clean 32 GiB VM runner

This disposable qualification runner is provisioned under
`/srv/data/projects/asb-state-tlc-vm-32g` for AR-1302.

Properties:

- Ubuntu 24.04 cloud image with the recorded SHA-256 in `runner-receipt.json`.
- QEMU/KVM x86_64 with 8 vCPUs and 32 GiB guest RAM; the QEMU `-m 32768`
  setting is the effective memory ceiling required by the AR.
- Disposable qcow2 overlay, 16 GiB guest swap, no host swap dependency.
- No QEMU network device and no host filesystem mounts.
- State checkout and evidence disks are explicit readonly/virtio inputs under
  `/srv/data/projects`; no credentials or private host paths are exposed.
- The runner is an execution environment only. The signed task candidate,
  handoffctl evidence, and exact terminal gate result remain authoritative.
