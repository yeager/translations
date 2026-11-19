# Foundation – general.json, full radgranskning

Granskningen omfattar samtliga 1 848 aktuella källsträngar i `general.json`, hämtade via Crowdin API 2026-11-19. Förslag med ändrad eller saknad svensk text har arkiverats per granskningsblock i `foundation-sv-general-part1-review-20261119.md` till `foundation-sv-general-part19-review-20261119.md`.

Varje förslag kontrollerades med:

- `l10n-lint --language sv`
- `hunspell -d sv_SE`

Platshållare, bildtoken och formatering har bevarats. Förslagen från del 3–19 är lokala och har inte skickats till Crowdin; delar som uttryckligen godkändes för publicering tidigare kan förekomma som Crowdin-förslag.