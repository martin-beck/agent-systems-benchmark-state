# ASB state TLC clean VM runner

This disposable runner is created under `/srv/data/projects/asb-state-tlc-vm`.

Properties:

- Ubuntu 24.04 cloud image with recorded SHA-256 `612b2c0cc1bc413a6cb8c38fd611794caf0f2b436c50013d8b3794db12ad7354`.
- QEMU/KVM 8.2.2, x86_64, 4 vCPUs, 16 GiB RAM.
- 16 GiB guest swap, no host swap dependency.
- No QEMU network device, no host filesystem mounts, disposable qcow2 overlay.
- State checkout and caches are copied into the guest explicitly; results are copied out as bounded evidence.
- The VM is not a qualification authority by itself; the state task and exact runner receipt remain authoritative.
