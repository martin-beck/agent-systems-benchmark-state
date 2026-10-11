# AR-1798 plan: pinned source-checkout acquisition

1. Read the complete AR-1776, AR-1778, and AR-1779 contracts and reproduce the
   current source-only resolution failure.
2. Define the checkout provider API and typed failure taxonomy; accept only the
   catalog repository and exact immutable revision.
3. Implement bounded credential-free checkout staging with controlled argv/env,
   no hooks, exact identity/HEAD verification, cancellation, and cleanup.
4. Connect AR-1779 to the provider and pass the verified checkout to the
   existing AR-1778 source builder; never relabel an artifact as a source build.
5. Add offline fixture coverage for success, wrong revision, wrong repository,
   moving reference, unavailable source, timeout, cancellation, size/path
   limits, and cleanup; run focused and full applicable gates.
6. Obtain independent review, publish a signed-DCO PR, wait for exact-head CI,
   merge through the protected signed workflow, and record exact-main evidence.
