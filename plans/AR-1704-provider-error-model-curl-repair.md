# AR-1704 typed provider failures, model admission, and trusted curl discovery

## Scope

Audit and repair the ASB provider boundary for the current live-development
path. The work covers:

1. non-2xx HTTP responses, malformed responses, timeouts, connection failures,
   and curl/process failures propagating as stable typed outcomes through
   backend, CLI, human output, and `--json` output;
2. provider/model/auth compatibility admission across the connected catalog,
   including unavailable and stale discovery generations, with no arbitrary
   model accepted merely because it is named;
3. bounded trusted curl discovery that does not require `/usr/bin/curl`, does
   not execute ambient PATH content, and reports a typed unavailable-tool
   diagnostic when no approved tool exists.

Use deterministic local fixtures and denied-network tests. A real provider key
is optional supplementary evidence only and never a completion gate.

## Deliverables

- focused source/tests or a qualification-only receipt when current behavior
  already satisfies a predicate;
- exact human-default and explicit `--json` output evidence;
- negative matrix for 401/403/429/5xx, malformed body, timeout, connection
  failure, incompatible model, stale discovery, and missing trusted curl;
- signed privacy-safe receipt binding exact ASB head and hosted checks.

Do not close AR-1657 or this AR from older receipts. Preserve the explicit
development warning-only authentication/signature/key boundary.
