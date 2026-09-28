# AR-1497: AR-1495 protected-main topology repair

## Evidence and dependencies

AR-1495 supplies the reviewed development-only bundle profile tree and merged
protected-main commit `03d2d0700696bad9549455510f37b24a1588b10e`. Its post-merge
Repository Quality run `36428739174` failed only because the protected-main
topic synchronization merge was not at the tip. AR-1493 supplies the signed
customer-release boundary. AR-1496 is unrelated and must not be modified.

## Acceptance

- Refresh protected `origin/main` and create the smallest topology-only topic
  preserving the exact AR-1495 tree; do not edit product files or weaken policy.
- Preserve signed SSH commits and matching DCO trailers, with a normal
  two-parent protected merge and no squash, rewrite, or force of protected main.
- Independently verify the AR-1495 tree, parent topology, exact reviewed diff,
  and unchanged signature policy before publication.
- Publish through reviewed PR exact-head CI; merge only when every required
  check is green. Run and record all eight exact-main post-merge workflows.
- Keep AR-1490 blocked until an authorized external signed customer package and
  signing authority exist. Development/unverified output is never release
  evidence.

## Non-goals

No changes to unsigned-development behavior, no asb-tui changes, no provider or
network access, no credentials, and no gate or policy weakening.
