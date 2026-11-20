# Foundation – menu.json, granskningsomgång 3

Datum: 2026-11-20  
Metod: Crowdin API; förslaget kontrollerades med `l10n-lint` och `hunspell-sv`.

| Nyckel | Engelsk källsträng | Tidigare svenska | Sparad svenska | Lint/stavning |
|---|---|---|---|---|
| MENU_GENERAL_SETTINGS → EDGE_MOVE | Edge Scrolling | Kantrullning | Skärmkantsrullning | l10n-lint: inga fel. Hunspell: inga fel. |

Den nya termen anger tydligt kamerarullning när markören förs till skärmens kant. Ändringen skickades direkt till Crowdin via API (HTTP 201). Gettext gav endast den generella UTF-8-portabilitetsvarningen för den temporära PO-filen.