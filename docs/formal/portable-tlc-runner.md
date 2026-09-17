# Portable TLC resource bounds

The state runner keeps virtual address-space admission separate from the
attested physical and swap envelope. `memory_max=3G` and `swap_max=3G` remain
the publication contract; portable execution applies `RLIMIT_AS=8G` so the
JVM's native mappings cannot be mistaken for 3 GiB of physical memory.

The 8 GiB address-space limit is bounded and is recorded as
`resource_bounds.address_space_max` in every success attestation. It is not a
replacement for the physical/swap limits, and lowering or removing either
bound is invalid. A requested address-space limit at or below the JVM heap is
rejected before admission.
