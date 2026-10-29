# Bitwarden Web — Crowdin API-häfte 31

- Projekt: Bitwarden - Web (`308189`), svenska (`sv-SE`).
- Underlag: `Bitwarden-Web-api-pam-batch31-20261029.json`.

Elva förslag för åtkomstbegäran och HTTP-autentisering skickades via Crowdins
API och verifierades sedan genom att läsas tillbaka från samma projekt och
språk.

| QA-status | Antal | Notering |
| --- | ---: | --- |
| `passed` | 3 | Åtkomstregel, privilegierad åtkomst och ingen åtkomstregel. |
| `failed` | 8 | Crowdins QA markerar återstående texter som förslag för manuell granskning. API-svaret bekräftar måltexterna och platshållaren `$ITEM$` oförändrad, men exponerar inte detaljorsaken för varje markerad rad. |

Lokal kvalitetssäkring passerade före uppladdning: giltig JSON, inga
skrivregelfel från `svlang` och inga okända ord i `hunspell-sv`. Arkivet och
Crowdins aktuella svenska måltexter kontrollerades före POST; inga av dessa
elva nycklar hade en aktuell svensk översättning.

Förslagen är inte automatiskt godkända.
