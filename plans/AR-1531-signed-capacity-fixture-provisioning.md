# AR-1531 plan: signed-capacity-8g fixture provisioning

1. Refresh the state-runner worktree to protected main and verify the merged
   `signed-capacity-8g` validator profile.
2. Provision only disposable files under `/srv/data/projects`: pinned image,
   64 GiB overlay, 8 GiB guest memory, 8 GiB guest swap, eight vCPUs,
   network disabled and no host mounts.
3. Measure host memory, swap, disk and inode headroom. If the host cannot meet
   the gate, stop and record the blocker; do not reclaim unrelated swaps or
   delete other project data.
4. Bind exact signed source/model/JDK/TLC/seed inputs when available and emit
   only sanitized receipt evidence. A development seed is never accepted by
   the formal profile.
5. Run focused/full state gates and independent review, then hand the fixture
   to AR-1522. No TLC qualification run is authorized by this provisioning AR.
