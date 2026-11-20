# Foundation – menu.json, granskningsomgång 20

Datum: 2026-11-20  
Metod: Crowdin API; förslaget kontrollerades med `l10n-lint` och `hunspell-sv`.

| Nyckel | Engelsk källsträng | Tidigare svenska | Sparad svenska | Lint/stavning |
|---|---|---|---|---|
| MENU_MODS_BROWSER → DATE_ADDED | Date added | Datum tillagt | Tillagd den | l10n-lint: inga fel. Hunspell: inga fel. |

Ändringen använder den idiomatiska svenska etiketten för när en mod lades till. Den skickades direkt till Crowdin via API (HTTP 201). Gettext gav endast den generella UTF-8-portabilitetsvarningen för den temporära PO-filen.