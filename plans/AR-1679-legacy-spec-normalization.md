# AR-1679 — ASB legacy task-spec normalization

Normalize only the remaining ASB task-spec records rejected by the strict
validator. Preserve every acceptance predicate, evidence requirement, and
development-only warning boundary while adding the current schema vocabulary.
Classify malformed legacy records separately from records missing only fields,
validate from a fresh checkout, regenerate projections through handoffctl, and
require signed DCO metadata-only review.
