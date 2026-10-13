# AR-1842 plan: name-first selection and internal identity resolution

1. Inventory the logical names already exposed by ASB and asb-tui for agents,
   providers, models, tools, workloads, benchmarks, and report dimensions. Map
   every current path, digest, version, endpoint, and executable field to the
   catalog/config resolver that owns it.
2. Freeze a shared resolver contract. A user selects a stable name; the resolver
   returns a canonical internal identity containing the physical executable or
   endpoint, supported model/provider metadata, version and integrity evidence,
   and a diagnostic-safe display record. Reject duplicate or stale names before
   plan creation and provide a name-based remediation choice.
3. Replace direct path/hash/version selection in setup, plan creation,
   validation, run, sweep, report, compare, and recording flows with logical
   name selections. Keep physical data in machine-readable config/catalog state
   and internal evidence, but never require users to type, copy, or remember it.
4. Wire the same resolver and name catalog into embedded ASB TUI and standalone
   asb-tui. Ensure both surfaces render the same names, selection summaries,
   warnings, and recovery actions; remove duplicated ad-hoc name/path binding.
5. Add negative coverage for omitted names, ambiguous names, renamed entries,
   stale catalog entries, wrong executable behind a name, and provider/model
   incompatibility. Verify structural safety failures remain blocking and that
   development-channel warning-only policy is not broadened.
6. Qualify a clean fresh-user CLI and TUI journey using deterministic fakes,
   plus an opt-in redacted live smoke where available. Verify human output is
   name-first and JSON contains only the documented machine envelope.
7. Obtain independent review, exact-head CI, protected signed merge, and
   post-merge evidence before closing the AR.
