# Foundation – menu.json, granskningsomgång 26

Datum: 2026-11-20  
Metod: Crowdin API; förslaget kontrollerades med `l10n-lint` och `hunspell-sv`.

| Nyckel | Engelsk källsträng | Tidigare svenska | Sparad svenska | Lint/stavning |
|---|---|---|---|---|
| MENU_MAP_SELECTOR → MAPGEN_TOGGLE_TERRITORIES_TOOLTIP | Toggle territories preview | Växla territorieöversikt | Växla förhandsvisning av territorier | l10n-lint: inga fel. Hunspell: inga fel. |

Den nya formuleringen bevarar att reglaget växlar just en förhandsvisning. Ändringen skickades direkt till Crowdin via API (HTTP 201). Gettext gav endast den generella UTF-8-portabilitetsvarningen för den temporära PO-filen.