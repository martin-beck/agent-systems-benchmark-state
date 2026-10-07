# AR-1684 selector safety

Extend the authority defensive matrix to cover symlink and non-regular
selector entries. Existing helper behavior must reject hostile entries with
`AuthorityError`; no test or gate is weakened.
