# AR-1678 — Development install host preflight and typed recovery

Add a disposable preflight for the default `dev` materializer that checks the
bounded toolchain, PTY, filesystem, and linker prerequisites before spawning a
build. Return stable human/JSON diagnostics with remediation and distinguish a
host limitation from a product failure. Verify retry, cleanup, and rollback
after a failed preflight, and record exact ASB/TUI heads in the receipt.

The preflight must not require provider authentication, production signatures,
or key-management chains in development mode; those remain explicit warnings.
