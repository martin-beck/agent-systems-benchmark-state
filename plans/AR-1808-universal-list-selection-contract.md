# AR-1808 plan: universal list and selection contract

Introduce one typed discovery descriptor shared by every command. `--list`
without a value reports domains applicable to that route; `--list <domain>`
reports stable choices and the exact flag used to select one or more entries.
Use existing catalogs as sources of truth, never a duplicated hand-maintained
registry. Test human/JSON parity, ordering, unavailable states, and that every
advertised selection can be parsed by the owning command.
