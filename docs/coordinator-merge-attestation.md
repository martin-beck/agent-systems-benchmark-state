# Coordinator v0.1.4 merge attestation

This additive record binds the installed coordinator v0.1.4 content to the immutable evidence
below. The signed commit that adds this record attests the exact objects; it does **not** add a
Martin Beck SSH signature or a Signed-off-by trailer to the already-published merge commit.

| Evidence | Exact identity |
| --- | --- |
| Pull request | `https://github.com/martin-beck/agent-systems-benchmark-state/pull/10` |
| Pull-request head | `e4fecc1e65e640d436e4d01b8418fb7dc73c7c4e` |
| Pull-request head tree | `600b2d960e16cb5b144ec0db8b1e833f7fe797a0` |
| Published merge | `e52ce3aaa59ffc4cc6f97657b6ea2c7dfceb2ac1` |
| Merge parents, in order | `b90f28ccaa300c9ccca0167cee97925b211d2844 e4fecc1e65e640d436e4d01b8418fb7dc73c7c4e` |
| Merge tree | `37ba9d70bdb25b61a66ae0c58c5b6e370cddfcce` |
| Upstream signed tag object | `bd786b124a0e9ec926247e4c1de17ef4bbb84c0d` |
| Upstream signed release commit | `9733b341f25b145d6dfad8414933cb6348701769` |
| Installed vendor manifest SHA-256 | `60d7c3c634c14f6df34874ace6044e9058a3621f78d51491407f9ed5aa0c871a` |

The pull-request head has a locally verifiable Martin Beck SSH signature and matching DCO
trailer. The published merge has the correct parents and content, but its GitHub-generated GPG
signature is not locally attributable to Martin Beck and its message has no Signed-off-by trailer.
This record preserves that limitation rather than rewriting public history or claiming retroactive
compliance.

Fresh pull-request checkouts are not required to contain the GitHub-created merge object because
it is outside the pull-request head's ancestry. Automated checks therefore validate this exact,
closed representation and the installed manifest. The signed attestation binds the recorded
identities, but it is not an independent cryptographic proof of an unavailable historical object;
reviewers must compare the merge facts with the durable GitHub PR and main-ref evidence.
