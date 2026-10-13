# AR-1860 plan: dependency-safe formal work-root repair adoption

Adopt and qualify the existing signed v0.7.0 repair at product HEAD
`1f3c7f65ca61e1e77fe4d357e37940ad8eddbe12`. This narrowly scoped successor
exists because AR-1858's terminal 95% run exposed the formal work-root seam,
while AR-1859 is correctly held behind unfinished AR-1858. It has no
unfinished dependency and must preserve both historical task records.

The repair must retain rc64 rejection before TLC/Java execution, add no gate
weakening, and complete focused/full/formal, independent review, exact-head CI,
merge, post-merge assurance, and durable state reconciliation.
