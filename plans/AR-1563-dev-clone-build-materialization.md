# AR-1563 implementation plan

Own source acquisition/build/staging only. Use fixed trusted `git`/`cargo`
tools, exact remote-head capture, private temporary directories, bounded output,
and atomic promotion. Add success, stale-head, build-failure, timeout, quota,
cleanup, and prior-install-preservation tests.
