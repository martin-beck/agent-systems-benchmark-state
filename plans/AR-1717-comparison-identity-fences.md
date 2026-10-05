# AR-1717 — Comparison identity fences

Before comparison joins online and offline result members, require exact
provider identity, model/settings digest, endpoint identity, catalog/run
generation, and agent/workload identity equality. Reject asymmetric or
multi-candidate comparisons with stable typed unavailable reasons; never
silently compare results from a different provider endpoint or settings.
Preserve human-default and `--json` output and keep all diagnostics secret-free.

Acceptance:

1. Matching provider/settings/endpoint/generation identities compare normally.
2. Each provider, model/settings, endpoint, generation, agent, and workload
   mismatch fails closed with deterministic typed unavailable diagnostics.
3. Symmetric, asymmetric, and multi-candidate cases have focused coverage and
   no network/provider fallback.
4. Focused/full tests, privacy, independent review, and hosted gates pass at
   the exact current ASB head.
