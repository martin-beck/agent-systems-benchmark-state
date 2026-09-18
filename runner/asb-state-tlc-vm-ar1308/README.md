# ASB AR-1308 disposable exhaustive-capacity runner

This receipt describes the disposable x86_64 QEMU capacity reserved for the
single AR-1307 full-exhaustive attempt.  It is an execution fixture, not a
qualification result.  The model process contract remains exactly 3 GiB
`MemoryMax`, 3 GiB `MemorySwapMax`, two TLC workers, two CPUs, an 8 GiB
address-space limit, and a 7200-second deadline.

The guest has additional capacity only for the kernel, JDK, TLC, filesystem,
and bounded evidence overhead.  Increasing guest capacity must never be used
to increase the process limits.  The guest is disposable, x86_64, offline,
has no host filesystem mounts, and uses an immutable Ubuntu 24.04 image and
preloaded JDK/TLC artifacts.  The host-capacity validator must pass immediately
before boot and the receipt must be bound to the exact signed AR-1307 commit.

Run the non-mutating preflight from this checkout:

```sh
uv run --frozen --offline python tools/validate_ar1308_capacity.py \
  --receipt runner/asb-state-tlc-vm-ar1308/runner-receipt.json
```

No full-exhaustive result is implied by a passing preflight.  A terminal
attestation is valid only when the canonical AR-1307 runner, admission lock,
cleanup and exact-head evidence also pass.
