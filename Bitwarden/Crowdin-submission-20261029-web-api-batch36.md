# Bitwarden Web — Crowdin API-häfte 36 och slutkontroll

Häftet innehåller de fem sista saknade svenska måltexterna i Web-komponenten:
historikomfattning samt HTTP-autentiseringens standardmatchningsflöde.

- Underlag: `Bitwarden-Web-api-http-auth-batch36-20261029.json`.
- Översättnings-id: `1980883`–`1980891`.
- Två förslag har QA-status `passed`; tre kvarstår som förslag med Crowdins
  QA-status `failed`.

## Aktuell komponentstatus

Efter API-uppladdningen rapporterar Crowdin för fil `58`:

| Mått | Resultat |
| --- | ---: |
| Strängar totalt | 5 173 |
| Översatta | 5 173 |
| Översättningsgrad | 100 % |
| Godkända | 1 323 (18 %) |
| QA passerade | 3 186 |
| QA med varning | 1 987 |

Häftet har passerat JSON-validering, `svlang skrivregler` och `hunspell-sv`.
Alla fem måltexter lästes tillbaka exakt från API:t. Denna kontroll styrker
att Web-komponenten saknar oöversatta strängar, inte att alla Crowdins
historiska QA-varningar är åtgärdade eller att förslagen är godkända.
