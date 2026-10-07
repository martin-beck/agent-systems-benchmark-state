# AR-1722 — PR #487 protected-main requalification and merge-settings recovery

Diagnose and repair the publication-integrity incident from PR #487. The
protected-main merge was accepted, but Repository Quality rejected the result
because the merge tree differed from the reviewed topic tree. Preserve the
immutable evidence and reproduce the mismatch with the exact base/topic/merge
identities before changing merge settings.

Acceptance requires:

1. independent review of the exact mismatch and comparison of reviewed topic,
   protected base, merge commit, and resulting trees;
2. recovery of protected merge settings or a repository-side merge procedure
   that guarantees reviewed-tree equivalence, with no policy exception;
3. a fresh signed/DCO PR or requalification run whose exact merge tree passes
   Repository Quality, Rust, portability, policy, formal, and fault checks;
4. the portable five-case matrix receipt for AR-1718, including network denial,
   approved backend identity, cleanup, and typed unavailable outcomes;
5. explicit unblocking evidence for AR-1718 and AR-1596 only after all gates
   pass.

AR-1722 is coordination and release-integrity work; it must not rewrite PR
#487 history, weaken protected-main policy, or use host-network fallback.
Development authentication, signatures, and key management remain warning-only
and are unrelated to this fail-closed publication gate.
