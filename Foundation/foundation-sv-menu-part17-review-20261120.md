# Foundation – menu.json, granskningsomgång 17

Datum: 2026-11-20  
Metod: Crowdin API; förslagen kontrollerades med `l10n-lint` och `hunspell-sv`.

| Nyckel | Engelsk källsträng | Tidigare svenska | Sparad svenska | Lint/stavning |
|---|---|---|---|---|
| MENU_MOD_PRIORITY → MOD_MISSING_DEPENDENCIES | Missing Dependencies | Saknar beroenden | Saknade beroenden | l10n-lint: inga fel. Hunspell: inga fel. |
| MENU_MOD_PRIORITY → MISSING_DEPENDENCIES | Missing dependencies | Saknar beroenden | Saknade beroenden | l10n-lint: inga fel. Hunspell: inga fel. |

Båda rubrikerna använder nu korrekt svensk nominalform. Ändringarna skickades direkt till Crowdin via API (HTTP 201). Gettext gav endast den generella UTF-8-portabilitetsvarningen för den temporära PO-filen.