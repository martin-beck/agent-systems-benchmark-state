# AR-1809 plan: end-to-end CLI UX contract qualification

Use AR-1805's generated inventory as the test matrix, not a manually selected
smoke set. Exercise clean project setup, discovery, selection, expected errors,
and normal operation through TTY and redirected writers. Compare human output
to reviewed semantic assertions rather than brittle complete transcripts. Run
the normal exact-head and post-merge qualification process and create narrow
successors for any new route-specific gap.
