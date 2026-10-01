# AR-1577 interactive development supervision

Separate bounded broker handshake/acquisition and cleanup deadlines from the
interactive TUI lifetime. After successful negotiation, let the user session
run until the child exits; on failure or explicit timeout, terminate the entire
private process group, join workers, close inherited descriptors, and remove
temporary endpoints deterministically. Add descendant and long-session tests.

