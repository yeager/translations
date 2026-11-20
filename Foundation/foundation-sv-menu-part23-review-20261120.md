# Foundation – menu.json, granskningsomgång 23

Datum: 2026-11-20  
Metod: Crowdin API; förslaget kontrollerades med `l10n-lint` och `hunspell-sv`.

| Nyckel | Engelsk källsträng | Tidigare svenska | Sparad svenska | Lint/stavning |
|---|---|---|---|---|
| MENU_GRAPHICS_SETTINGS → DISPLAY_MONITOR | Display Monitor | Visningsskärm | Bildskärm | l10n-lint: inga fel. Hunspell: inga fel. |

Den vanliga svenska inställningstermen ”Bildskärm” används nu. Ändringen skickades direkt till Crowdin via API (HTTP 201). Gettext gav endast den generella UTF-8-portabilitetsvarningen för den temporära PO-filen.