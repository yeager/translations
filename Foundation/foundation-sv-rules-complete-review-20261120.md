# Foundation – rules.json: komplett svensk radgranskning

Datum: 2026-11-20

Komponenten `rules.json` (Crowdin-fil-ID 10) innehåller 155 aktuella källsträngar. Samtliga rader i API-intervallen 0–154 har radgranskats. En efterföljande avläsning från offset 160 returnerade inga ytterligare strängar.

För varje sparat förslag kördes `l10n-lint` och `hunspell-sv`; inga sakfel återstod. Gettext rapporterade endast den generella portabilitetsvarningen för UTF-8-teckenuppsättning i temporära PO-filer.

Ändringar och eventuella dubblettförslag är arkiverade per granskningsomgång i `foundation-sv-rules-part1-review-20261120.md` till `foundation-sv-rules-part13-review-20261120.md`. Alla godkända ändringar skickades direkt till Crowdin via API.