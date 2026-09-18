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

Run the non-mutating preflight from this checkout. Set the paths to the
reviewed, disposable runner inputs supplied by the execution environment;
the validator intentionally requires every input explicitly and has no host
skip option:

```sh
RUNTIME_ROOT=/approved/ar1308-runtime
IMAGE="$RUNTIME_ROOT/ubuntu-24.04.img"
OVERLAY="$RUNTIME_ROOT/ar1308-root.qcow2"
SOURCE="$RUNTIME_ROOT/ar1307-source"
MODEL="$SOURCE/formal/tier-evidence.json"
SEED="$RUNTIME_ROOT/ar1308-user-data.yaml"
JDK="$RUNTIME_ROOT/jvm"
TLC_JAR="$RUNTIME_ROOT/tla2tools.jar"
ADMISSION_LOCK="$RUNTIME_ROOT/admission.lock"

uv run --frozen --offline python tools/validate_ar1308_capacity.py \
  --receipt runner/asb-state-tlc-vm-ar1308/runner-receipt.json \
  --runtime-root "$RUNTIME_ROOT" \
  --image "$IMAGE" \
  --overlay "$OVERLAY" \
  --source "$SOURCE" \
  --model "$MODEL" \
  --seed "$SEED" \
  --jdk "$JDK" \
  --tlc-jar "$TLC_JAR" \
  --admission-lock "$ADMISSION_LOCK"
```

No full-exhaustive result is implied by a passing preflight.  A terminal
attestation is valid only when the canonical AR-1307 runner, admission lock,
cleanup and exact-head evidence also pass.
