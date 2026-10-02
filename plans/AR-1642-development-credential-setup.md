# AR-1642 — Development credential setup

Add a simple provider authentication step that accepts an API key through the
wizard/CLI, stores only the supported development configuration reference, and
reports missing credentials as typed warning-only state. Never print keys,
persist them in evidence, or make development setup fail closed on absent
production secret infrastructure.
