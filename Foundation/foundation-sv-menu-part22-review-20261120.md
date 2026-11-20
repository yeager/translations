# Foundation – menu.json, granskningsomgång 22

Datum: 2026-11-20  
Metod: Crowdin API; förslaget kontrollerades med `l10n-lint` och `hunspell-sv`.

| Nyckel | Engelsk källsträng | Tidigare svenska | Sparad svenska | Lint/stavning |
|---|---|---|---|---|
| MENU_MAP_SELECTOR → COMMUNITY_MAPS | Community Maps | Communityns kartor | Gemenskapskartor | l10n-lint: inga fel. Hunspell: inga fel. |

Ändringen följer den befintliga termen ”Gemenskapskarta” och undviker den engelska hybridböjningen. Den skickades direkt till Crowdin via API (HTTP 201). Gettext gav endast den generella UTF-8-portabilitetsvarningen för den temporära PO-filen.