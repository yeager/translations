# Foundation — svensk granskningsrapport: buildings.release.json

Datum: 2026-11-20  
Komponent: `buildings.release.json`  
Omfattning: samtliga 365 aktuella källsträngar (Crowdin API, fil-ID 64)

Radgranskningen genomfördes i 25 API-hämtade block (offset 0–374). Granskade ändringar arkiveras separat i delrapporterna `foundation-sv-buildings-release-part1-review-20261120.md` till `foundation-sv-buildings-release-part24-review-20261120.md`.

Varje nytt förslag har kontrollerats med `l10n-lint --language sv` och `hunspell-sv`, och därefter skickats direkt till Crowdin med explicita sträng-ID:n. Platshållare, markup och källans avsedda formatering har bevarats. När Crowdin svarade att en identisk översättning redan fanns skapades ingen dubblett.

Den sista kontrollen vid offset 375 returnerade noll strängar, vilket verifierar att komponenten är fullständigt genomgången.