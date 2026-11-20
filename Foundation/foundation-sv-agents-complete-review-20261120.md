# Foundation – agents.json: komplett svensk radgranskning

Datum: 2026-11-20

Komponenten `agents.json` (Crowdin-fil-ID 5) innehåller 119 aktuella källsträngar. Samtliga rader i API-intervallen 0–119 har radgranskats. En efterföljande avläsning från offset 120 returnerade inga ytterligare strängar.

För varje sparat förslag kördes `l10n-lint` och `hunspell-sv`; inga sakfel återstod. Gettext rapporterade enbart den generella portabilitetsvarningen för UTF-8-teckenuppsättning i temporära PO-filer.

Ändringar och eventuella dubblettförslag är arkiverade per granskningsomgång i `foundation-sv-agents-part2-review-20261120.md` till `foundation-sv-agents-part7-review-20261120.md`. Alla godkända ändringar skickades direkt till Crowdin via API.