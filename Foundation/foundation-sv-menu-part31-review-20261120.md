# Foundation – menu.json, granskningsomgång 31

Datum: 2026-11-20  
Metod: Crowdin API; förslaget kontrollerades med `l10n-lint` och `hunspell-sv`.

| Nyckel | Engelsk källsträng | Tidigare svenska | Sparad svenska | Lint/stavning |
|---|---|---|---|---|
| MENU_SAVEGAME_COMPATIBILITY_POPUP → PRIVATE_PLAYTEST_REMINDER_NDA | Hello, playtesters! … | Stycket saknade källans radbrytningar och hade onaturlig formulering. | Förbättrad NDA-text med bevarade stycken och naturlig svenska. | l10n-lint: inga fel. Hunspell: inga fel. |

Källans tre tomradavgränsade stycken bevarades exakt. Ändringen skickades direkt till Crowdin via API (HTTP 201). Gettext gav endast den generella UTF-8-portabilitetsvarningen för den temporära PO-filen.