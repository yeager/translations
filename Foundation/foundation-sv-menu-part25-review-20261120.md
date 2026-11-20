# Foundation – menu.json, granskningsomgång 25

Datum: 2026-11-20  
Metod: Crowdin API; förslaget kontrollerades med `l10n-lint` och `hunspell-sv`.

| Nyckel | Engelsk källsträng | Tidigare svenska | Sparad svenska | Lint/stavning |
|---|---|---|---|---|
| MENU_MAP_SELECTOR → MAPGEN_SLIDER_ISLAND_DESC | Controls the overall surface taken by islands in main water masses. | Styr den totala ytan som täcks av öar i huvudsakliga vattenmassor. | Styr den totala ytan som täcks av öar i större vattenmassor. | l10n-lint: inga fel. Hunspell: inga fel. |

”Större vattenmassor” återger betydelsen naturligt på svenska. Ändringen skickades direkt till Crowdin via API (HTTP 201). Gettext gav endast den generella UTF-8-portabilitetsvarningen för den temporära PO-filen.