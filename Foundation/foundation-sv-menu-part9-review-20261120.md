# Foundation – menu.json, granskningsomgång 9

Datum: 2026-11-20  
Metod: Crowdin API; förslaget kontrollerades med `l10n-lint` och `hunspell-sv`.

| Nyckel | Engelsk källsträng | Tidigare svenska | Sparad svenska | Lint/stavning |
|---|---|---|---|---|
| MENU_CONTROL_REMAPPER_SETTINGS → REMAPPER_PRESS_KEY | PRESS KEY | TRYCK TANGENT | TRYCK PÅ EN TANGENT | l10n-lint: inga fel. Hunspell: inga fel. |

Versaliseringen behölls och uppmaningen är nu grammatisk på svenska. Ändringen skickades direkt till Crowdin via API (HTTP 201). Gettext gav endast den generella UTF-8-portabilitetsvarningen för den temporära PO-filen.