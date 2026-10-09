# AR-1758 repair plan

1. Preserve the exact failed merge identity, tree, parents, and provenance failure.
2. Inspect and use the supported `tools/integration/merge_pr.py` repair/publication path; never force-push or rewrite protected main.
3. Create the smallest reviewed signed+DCO repair PR, run focused merge-integrity tests and every required hosted check.
4. Independently review the exact repair head, merge through the protected path, wait for exact-main CI, and record the repaired provenance.
5. Only then attach the AR-1731 hosted acceptance receipt and release it done.
