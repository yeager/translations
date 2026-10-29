# Bitwarden Web — Crowdin API-häfte 29

- Projekt: Bitwarden - Web (`308189`), svenska (`sv-SE`).
- Metod: Crowdins API v2, med autentisering enbart i den körande processen.
- Underlag: `Bitwarden-Web-api-pam-batch29-20261029.json`.

## Inskickat och verifierat

Tretton nya PAM-relaterade förslag skickades med `POST /projects/308189/translations`.
API:t bekräftade därefter varje sträng med `GET /projects/308189/languages/sv-SE/translations`:

| Antal | Utfall |
| ---: | --- |
| 13 | Förslagen skapades med id 1980729–1980753 (udda löpnummer). |
| 11 | Crowdins QA-status är `passed`. |
| 2 | Crowdins QA-status är `failed` för *Access rule updated* och *Access rule deleted*. Den svenska terminologin är konsekvent (*åtkomstregel*), men Crowdins detaljdiagnostik returnerades inte av tillgängligt API-anrop. De lämnas som förslag för granskning, inte godkända översättningar. |

Dessutom ersattes en tidigare tom suggeston för `pamAuditNoMatchesMessage` med
`Inga händelser matchar de aktuella filtren.` (översättnings-id `1980727`),
vilken API:t bekräftar med QA-status `passed`.

De sex närliggande editorförslagen för grupp-, gransknings- och kolumntexter
verifierades också via API. Fem passerar QA. `groupEdited` är sparad som
`Grupp redigerad`, men Crowdins terminologikontroll flaggar den mekaniskt
eftersom den kräver exakt uppslagsformen *redigera*; ingen ogrammatisk
imperativform har tvingats fram.

## Lokal granskning

- `jq empty` bekräftade giltig JSON.
- `svlang skrivregler` rapporterade inga skrivregelfel.
- Hunspell med projektets `sv_SE`-ordlista rapporterade inga okända ord.
- `swedish-tm` kontrollerades för etablerade former som
  *inloggningsuppgifter*, *åtkomstregel* och *granskningslogg*.
- `l10n-lint` är avsett för lokalkataloger och avvisar detta API-manifest med
  metadatafält som `stringId`; Crowdins QA-svar är den relevanta
  maskinella kontrollen för just detta häfte.

Förslagen är inte automatiskt godkända. Crowdins reviewerflöde avgör deras
slutliga status.
