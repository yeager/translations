# Foundation – menu.json, granskningsomgång 6

Datum: 2026-11-20  
Metod: Crowdin API; förslagen kontrollerades med `l10n-lint` och `hunspell-sv`.

| Nyckel | Engelsk källsträng | Tidigare svenska | Sparad svenska | Lint/stavning |
|---|---|---|---|---|
| MENU_MOD_PRIORITY → CANNOT_LOAD_MOD_BEFORE_DEPENDENCY | Cannot load a mod before its dependency | Kan inte ladda en mod innan dess beroenden | Kan inte ladda en mod före dess beroenden | l10n-lint: inga fel. Hunspell: inga fel. |
| MENU_MOD_PRIORITY → MOD_DEPENDENCIES_LOADED_AFTER_THE_MOD | Dependencies loaded after the mod | Beroenden laddade efter mod | Beroenden laddas efter modden | l10n-lint: inga fel. Hunspell: inga fel. |

Båda ändringarna skickades direkt till Crowdin via API (HTTP 201). Gettext gav endast den generella UTF-8-portabilitetsvarningen för den temporära PO-filen.