# AR-1682 formal hierarchy model repair

The clean current main PR-publication model fails `HierarchyCoherent` because
the one-process configuration declares only `t1` while the model's fixed
hierarchy includes child `t2`. Restore the fixture's declared task domain to
`t1` and `t2`; do not remove or weaken invariants. Run the formal verifier and
record exact attestation/check evidence.
