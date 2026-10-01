# AR-1600 — bounded development build-artifact staging

Repair the ASB development materializer so a normal fresh-user TUI release
build does not place an unbounded Cargo target tree inside the source/workspace
quota.  Use a private sibling target/cache with explicit bounded accounting and
cleanup, preserve the 2 GiB source/workspace limit, and copy only the validated
executable and identity metadata into the atomic publication root.  Oversized
source, target, output, timeout, and cleanup cases must remain typed failures.

Dependencies: AR-1599, AR-1597.  Downstream: asb-tui AR-1599 and final fresh-user
qualification AR-1598.

Required evidence: real paired ASB/TUI install run with explicit trusted Cargo,
source/workspace and target quota tests, interruption/rollback/cleanup tests,
offline and missing-auth warning behavior, signed/DCO PR, independent review,
hosted checks, and exact post-merge qualification.  No development path may
block on missing authentication, signatures, or key management; production
boundaries remain fail-closed.
