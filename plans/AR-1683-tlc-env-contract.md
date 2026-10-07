# AR-1683 TLC environment contract

The hosted formal workflow must provide the approved `TLC_MEMORY_MAX=3G` and
`TLC_SWAP_MAX=3G` values already defined by the `pr-publication` resource
profile. Add regression assertions for the workflow contract; do not increase
limits, bypass cgroup admission, or weaken attestation.
