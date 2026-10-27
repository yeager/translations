# Core: LDAP-autentisering 2026-10-27

Den lokala Core-katalogen på 5 528 poster hade ett faktiskt kontrollfel:
LDAP-hjälptexten för autentiseringsläge innehöll ett extra kursiveringstaggpar
och otydlig svenska. Deltafilen återställer samma HTML-struktur som källtexten
och förtydligar LDAP-termerna på svenska.

Filen omfattar en post, är arkiverad och är inte uppladdad till Cacti
Translate.

En radvis jämförelse 2026-10-27 mot den aktuella Core-katalogen på `develop`
(SHA-256 `10139e9de84ea1a1abc52dc7c1e2aafca9a55389cf00cb82f1baa7dab520b86d`)
visar att källsträngen fortfarande finns kvar och att måltexten fortfarande
skiljer sig från rättelsen. `msgfmt`, `l10n-lint` (0 fel och 0 varningar),
`svlang`, Hunspell-granskning och Gitleaks passerar. Hunspell träffar endast
Cacti-, LDAP- och HTML-termer.
