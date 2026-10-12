# AR-1807 plan: complete contextual CLI help contract

Build help tests from AR-1805 rather than a manually curated command list.
Ensure parser-generated usage remains correct, then add reviewed prose for
meaning, examples, selection/discovery, and next steps. Treat help as a pure,
offline query: it must neither initialize a project nor contact a provider.
