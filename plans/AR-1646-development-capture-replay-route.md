# AR-1646 — Development capture and replay route

Add a bounded development-only control operation that captures provider
responses during selected workloads, seals a cassette, issues replay authority
inside the runtime boundary, and runs offline replay without provider egress.
Production authority and security gates remain unchanged; missing development
authentication/signatures/key management are warnings only.
