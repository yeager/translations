# Foundation – menu.json, granskningsomgång 33

Datum: 2026-11-20  
Metod: Crowdin API; förslaget kontrollerades med `l10n-lint` och `hunspell-sv`.

| Nyckel | Engelsk källsträng | Tidigare svenska | Sparad svenska | Lint/stavning |
|---|---|---|---|---|
| MENU_MAP_SELECTOR → PROCEDURAL_MAPS_TOOLTIP_CONTENT | Thanks to randomly generated procedural maps … | Källans fyrstycksindelning saknades. | Befintlig svenska med fyra bevarade textstycken. | l10n-lint: inga fel. Hunspell: inga fel. |

Källans tre tomradavgränsningar bevarades. Ändringen skickades direkt till Crowdin via API (HTTP 201). Gettext gav endast den generella UTF-8-portabilitetsvarningen för den temporära PO-filen.