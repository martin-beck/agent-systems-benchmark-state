# Development review identity policy

This state repository distinguishes development integration from verified
release publication. Development changes still require exact-head checks,
privacy review, accepted SSH signatures, matching DCO trailers, and a separate
independent technical review-worker record bound to the candidate head/tree.

The independent requirement is about the worker and evidence boundary, not the
GitHub login identity. Once that worker review is approved, a same-account
GitHub approval by the topic author is sufficient for a development pull
request; no additional authorized maintainer, collaborator, or second-account
approval is required. The GitHub approval may not replace the independent
review-worker record or any exact-head, signature, DCO, privacy, or
post-merge-assurance check.

Verified release and provenance requirements remain unchanged and fail closed.
Development approval is never release evidence.
