# Foundation – menu.json, granskningsomgång 40

Datum: 2026-11-20  
Metod: Crowdin API; förslagen kontrollerades med `l10n-lint` och `hunspell-sv`.

| Nyckel | Engelsk källsträng | Tidigare svenska | Sparad svenska | Lint/stavning |
|---|---|---|---|---|
| MENU_MODS → MENU_MODS_DESC | Some mods might have dependencies. … | Vissa modifikationer kan ha beroenden. Se till att ladda dina modifikationer i rätt ordning (dra och släpp för att ändra ordning på dem, föräldern först). | Vissa modifikationer kan ha beroenden. Se till att läsa in dem i rätt ordning (dra och släpp för att ändra ordning; den överordnade modden först). | l10n-lint: inga fel. Hunspell: inga fel. |
| MENU_LOADING_SCREEN → DEFAULT_PLAYTHROUGH_NAME | No playthrough saves | Inga genomspelningssparingar | Inga sparfiler för genomspelningen | l10n-lint: inga fel. Hunspell: inga fel. |

Båda ändringarna skickades direkt till Crowdin via API (HTTP 201). Gettext gav endast den generella UTF-8-portabilitetsvarningen för den temporära PO-filen.