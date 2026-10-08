# AR-1736 — backend model catalog and execution parity

Create a canonical registry-driven model capability contract across every ASB
backend. The implementation must derive completeness checks from the backend
registry rather than a hand-maintained subset, so adding a backend without its
model semantics, selection path, and execution coverage fails CI.

For every model-bearing backend:

- enumerate a bounded normalized model catalog with backend identity,
  generation, digest, availability, capabilities, and typed unavailability;
- expose human and stable JSON selection through the supported setup/easy CLI
  surfaces, reject unknown, stale, unavailable, and cross-backend selections
  before provider contact or state mutation, and persist no secrets;
- carry the exact selected backend/profile/model/catalog generation and digest
  through plan creation, a complete normal benchmark run, every point in a
  bounded sweep, results, reports, and comparison provenance;
- preserve explicit execution mode and never fall back between live, cli2key,
  local/mock, or strict replay paths;
- provide deterministic positive and hostile fixtures. Real provider or OAuth
  checks are optional development evidence and cannot be a completion blocker.

For a backend that is intentionally model-less, register a typed `not_applicable`
model capability with a reason and test its full run/sweep path. CI must compare
the canonical backend registry with the model-capability matrix and fail for a
missing or duplicated backend, an untested supported cell, or a backend that
advertises run/sweep without the matching model-selection semantics.

Qualification must include every backend supported at the exact implementation
head, including the OpenRouter and cli2key paths introduced by their dependency
ARs, and any deterministic local/mock or replay backend ASB continues to
advertise. Evidence must distinguish deterministic development qualification
from optional live-provider reachability and make no production-readiness claim.
