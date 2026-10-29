# Bitwarden Web — Crowdin API-häfte 30

- Projekt: Bitwarden - Web (`308189`), svenska (`sv-SE`).
- Underlag: `Bitwarden-Web-api-pam-batch30-20261029.json`.
- Metod: Crowdins API v2; autentiseringsuppgifter har inte lagrats i detta arkiv.

## Resultat

Tolv svenska PAM-förslag har skickats in och lästs tillbaka med Crowdins API.
De skapades som översättningarna `1980757`–`1980779`.

| QA-status | Antal | Strängar |
| --- | ---: | --- |
| `passed` | 7 | Återkallad åtkomst, indraget godkännande, fel vid återkallande, tidsfönster, *Alla*, *Skapade av mig* och tom historik. |
| `failed` | 5 | Filtertext, inläsningstexter, samlingsomfång och historikbeskrivning. De finns sparade som förslag, men lämnas åt Crowdin-granskning eftersom projektets QA markerar dem. |

## Lokal kvalitetssäkring

- JSON-strukturen validerades med `jq empty`.
- `svlang skrivregler` rapporterade inga skrivregelfel.
- Hunspell med `hunspell-sv` rapporterade inga okända ord efter att två
  onödigt sammansatta formuleringar skrivits om till naturligare svenska.
- Arkivet kontrollerades först; ingen av häftets nycklar fanns i tidigare
  Bitwarden-underlag.

Förslagen är inte automatiskt godkända och får sin slutliga status genom
Bitwardens Crowdin-granskning.
