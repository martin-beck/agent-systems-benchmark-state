# AR-1657 — Agent/provider/model compatibility matrix

Qualify the complete selection matrix for `opencode` and `opendesk` across
every provider and model exposed by the connected catalog. Prove shared
defaults, per-agent overrides, reconfiguration, unavailable tuple reasons,
and persistence across restart while feeding benchmark, capture/replay, and
comparison routes.

Dependencies: AR-1641, AR-1645, AR-1647, AR-1651, AR-1656. Downstream:
AR-1655.

Development-only generated credentials and signatures are acceptable fixtures;
missing authentication or key management must never block matrix coverage or
offline replay.

Required evidence: a deterministic matrix runner, positive/negative tuple
fixtures, restart and default-propagation checks, online/offline parity,
human/JSON reports, exact-head hosted CI, independent review, and a receipt.
