# AR-1630 development availability coverage

## Scope

Provide behavior-relevant coverage for the AR-1628 unavailable-agent bootstrap
filter so the protected coverage gate remains green without hiding the branch.

## Acceptance

- Exercise a development catalog containing unavailable agents and assert that
  choices remain visible while unsupported lifecycle polls are skipped.
- Keep the full library coverage threshold at or above the repository gate.
- Run hosted quality/AWQ checks on a signed DCO commit.
- Missing authentication, signatures, and key management remain warning-only.

## Out of scope

Changing production authentication policy or weakening coverage thresholds.
