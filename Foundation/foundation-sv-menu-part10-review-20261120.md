# Foundation – menu.json, granskningsomgång 10

Datum: 2026-11-20  
Metod: Crowdin API; förslaget kontrollerades med `l10n-lint` och `hunspell-sv`.

| Nyckel | Engelsk källsträng | Tidigare svenska | Sparad svenska | Lint/stavning |
|---|---|---|---|---|
| MENU_CONTROL_REMAPPER_CONTROL__GROUP_NAMES → CONTROL_GROUP_CONSTRUCTION | Construction | Konstruktion | Byggande | l10n-lint: inga fel. Hunspell: inga fel. |

”Byggande” avser kontrollgruppens spelhandling och undviker den tekniska betydelsen hos ”konstruktion”. Ändringen skickades direkt till Crowdin via API (HTTP 201). Gettext gav endast den generella UTF-8-portabilitetsvarningen för den temporära PO-filen.