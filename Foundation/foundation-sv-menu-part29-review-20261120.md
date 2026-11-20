# Foundation – menu.json, granskningsomgång 29

Datum: 2026-11-20  
Metod: Crowdin API; förslagen kontrollerades med `l10n-lint` och `hunspell-sv`.

| Nyckel | Engelsk källsträng | Tidigare svenska | Förslag | Resultat | Lint/stavning |
|---|---|---|---|---|---|
| MAIN_MENU → VILLAGE_DETAILS_VILLAGE_NAME_TITLE | Your village name | Namnet för din by | Din bys namn | Sparad i Crowdin (HTTP 201). | l10n-lint: inga fel. Hunspell: inga fel. |
| MAIN_MENU → RANDOMIZE_VILLAGE_NAME | Randomize Name | Slumpmässigt namn | Slumpa namn | Identisk översättning fanns redan i Crowdin; API:t rapporterade dubblett. | l10n-lint: inga fel. Hunspell: inga fel. |
| MAIN_MENU → RANDOMIZE_PLAYER_NAME_TITLE | Randomize Name and Title | Slumpmässigt namn och titel | Slumpa namn och titel | Identisk översättning fanns redan i Crowdin; API:t rapporterade dubblett. | l10n-lint: inga fel. Hunspell: inga fel. |

Gettext gav endast den generella UTF-8-portabilitetsvarningen för den temporära PO-filen.