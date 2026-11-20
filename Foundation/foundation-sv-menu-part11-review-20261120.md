# Foundation – menu.json, granskningsomgång 11

Datum: 2026-11-20  
Metod: Crowdin API; förslaget kontrollerades med `l10n-lint` och `hunspell-sv`.

| Nyckel | Engelsk källsträng | Tidigare svenska | Sparad svenska | Lint/stavning |
|---|---|---|---|---|
| MENU_CONTROL_REMAPPER_CONTROL_NAMES → CONTROL_CLOSE_WINDOW | Close Focused Window | Stäng fokuserat fönster | Stäng aktivt fönster | l10n-lint: inga fel. Hunspell: inga fel. |

”Aktivt fönster” är den naturliga svenska UI-termen för ett fokuserat fönster. Ändringen skickades direkt till Crowdin via API (HTTP 201). Gettext gav endast den generella UTF-8-portabilitetsvarningen för den temporära PO-filen.