# Foundation svenska — help.json slutförd

Datum: 2026-11-20  
Projekt: Crowdin Foundation (306855), språk `sv-SE`  
Komponent: `help.json` (fil-ID 16)

Hela komponenten radgranskades via Crowdin API, i tjugosträngarsintervall. Slutkontroll med `GET /strings?fileId=16&limit=20&offset=400` returnerade 0 strängar.

Sparade förbättringar omfattar konsekvent Foundation-terminologi (bland annat byggmästare, kämpar, kunglig hovman, delbyggnad och lagerhållning), idiomatisk svenska och UI-texter. Varje ändringspost finns med källa, tidigare text, förslag och resultat i granskningsdelarna 1–13.

Alla nya förslag validerades med:
- `l10n-lint --language sv`
- `hunspell -d sv_SE`

Kontrollerna rapporterade inga lint- eller stavningsfel. Crowdin-svar HTTP 201 bekräftade sparning av nya översättningar; redan befintliga identiska förslag har dokumenterats som dubbletter i respektive granskningsdel. Markdown, platshållare och övrig formatering bevarades.
