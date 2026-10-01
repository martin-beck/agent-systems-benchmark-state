# AR-1596 — cassette and offline lifecycle integration

Integrate recording, cassette sealing, replay selection, and offline
benchmark execution with the ASB control lifecycle. Recording must be
selectable for one or all agents/workloads; replay must prove no provider
egress and deterministic missing/expired-cassette failures.

Dependencies: AR-1590 and AR-1595. Downstream: paired TUI AR-1595.

Required evidence: lifecycle state transitions, bounded cancellation and
cleanup, cassette manifest/digest fixtures, offline replay tests, human and
JSON CLI projections, signed/DCO PR, independent review, and hosted checks.
