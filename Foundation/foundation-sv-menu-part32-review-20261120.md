# Foundation – menu.json, granskningsomgång 32

Datum: 2026-11-20  
Metod: Crowdin API; förslaget kontrollerades med `l10n-lint` och `hunspell-sv`.

| Nyckel | Engelsk källsträng | Tidigare svenska | Sparad svenska | Lint/stavning |
|---|---|---|---|---|
| MENU_SAVEGAME_COMPATIBILITY_POPUP → DEMO_POPUP_DESC_3 | If you buy the Early Access version … | Källans styckeindelning och signaturrad saknades. | Förbättrad text med tre bevarade textstycken och signatur. | l10n-lint: inga fel. Hunspell: inga fel. |

Källans två tomradavgränsningar och avslutande signaturprefix `- ` bevarades. Ändringen skickades direkt till Crowdin via API (HTTP 201). Gettext gav endast den generella UTF-8-portabilitetsvarningen för den temporära PO-filen.