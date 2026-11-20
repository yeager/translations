# Foundation – menu.json, granskningsomgång 13

Datum: 2026-11-20  
Metod: Crowdin API; förslagen kontrollerades med `l10n-lint` och `hunspell-sv`.

| Nyckel | Engelsk källsträng | Tidigare svenska | Förslag | Resultat | Lint/stavning |
|---|---|---|---|---|---|
| MAIN_MENU → X_POPULATION | {1} pop. | {1} Pop. | {1} inv. | Sparad i Crowdin (HTTP 201). | l10n-lint: inga fel. Hunspell: inga fel. |
| MENU_MODS_BROWSER → ALL_STATUS | All status | All status | Alla statusar | Sparad i Crowdin (HTTP 201). | l10n-lint: inga fel. Hunspell: inga fel. |
| MAIN_MENU → YOUTUBE | YouTube | Youtube | YouTube | Identisk översättning fanns redan i Crowdin; API:t rapporterade dubblett. | l10n-lint: inga fel. Hunspell: inga fel. |

Platshållaren `{1}` bevarades. Gettext gav endast den generella UTF-8-portabilitetsvarningen för den temporära PO-filen.