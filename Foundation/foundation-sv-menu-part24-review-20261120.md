# Foundation – menu.json, granskningsomgång 24

Datum: 2026-11-20  
Metod: Crowdin API; förslaget kontrollerades med `l10n-lint` och `hunspell-sv`.

| Nyckel | Engelsk källsträng | Tidigare svenska | Sparad svenska | Lint/stavning |
|---|---|---|---|---|
| MENU_MAP_SELECTOR → MAPGEN_SLIDER_BEACH_DESC | Controls the overall surface taken by sand around bodies of water. | Styr den totala ytan som täcks av sand kring vattendrag. | Styr den totala ytan som täcks av sand kring vattensamlingar. | l10n-lint: inga fel. Hunspell: inga fel. |

”Vattensamlingar” omfattar både sjöar, hav och andra vattenområden, till skillnad från ”vattendrag”. Ändringen skickades direkt till Crowdin via API (HTTP 201). Gettext gav endast den generella UTF-8-portabilitetsvarningen för den temporära PO-filen.