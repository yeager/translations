# PCSX2: release- och katalogkontroll 2026-10-27

PCSX2:s senaste officiella release är `v2.9.146`, publicerad 2026-10-25.
Den uppfyller 48-månadersregeln.

Den aktuella svenska Qt-katalogen på `master` kontrollerades med SHA-256
`db1b69c560caa1df71fe9d6aa15d0a538d42f449cd31ffb9a1c5751c46c6866a`.
De två posterna i `pcsx2-achievements-review-20261026.ts` finns kvar och
skiljer sig från Git-katalogens måltext. Filen är lokal och inte inskickad
uppströms.

De tio posterna i `pcsx2-new-menu-strings-20261026.ts` saknas i den aktuella
Git-katalogen. De är Crowdin-specifika strängar och kan därför inte markeras
som föråldrade på grundval av Git-jämförelsen; deras status ska följas i
Crowdin.
