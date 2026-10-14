# Wireshark-uppdatering 2026-10-14

Patchen bygger på den aktuella svenska TS-katalogen från Wiresharks `master`.

Den ersätter fyra svenska tankstreck med kolon. Ingen av de berörda källsträngarna använder tankstreck, medan tecknet `→` i två källsträngar lämnas kvar.

Kontroller:

- TS-filen är välformad XML enligt `xmllint`.
- `l10n-lint` hittar inga svenska tankstreck utan motsvarighet i källan.
- Gitleaks hittar inga hemligheter.
