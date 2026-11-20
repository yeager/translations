# Foundation – menu.json, granskningsomgång 34

Datum: 2026-11-20  
Metod: Crowdin API; förslagen kontrollerades med `l10n-lint` och `hunspell-sv`.

| Nyckel | Engelsk källsträng | Tidigare svenska | Sparad svenska | Lint/stavning |
|---|---|---|---|---|
| MENU_GENERAL_SETTINGS → QUICK_SAVE_IN_CLOUD | Quicksave To Cloud | Spara till molnet | Snabbspara till molnet | l10n-lint: inga fel. Hunspell: inga fel. |
| MENU_GENERAL_SETTINGS → AUTOSAVE_MAXIMUM_COUNT_PER_PLAYTHROUGH | Autosave Limit Per Playthrough | Gräns för automatiska sparningar per spelomgång | Gräns för automatiska sparningar per genomspelning | l10n-lint: inga fel. Hunspell: inga fel. |
| MENU_GENERAL_SETTINGS → QUICKSAVE_MAXIMUM_COUNT_PER_PLAYTHROUGH | Quicksave Limit Per Playthrough | Gräns för snabbsparningar per spelomgång | Gräns för snabbsparningar per genomspelning | l10n-lint: inga fel. Hunspell: inga fel. |

Snabbsparningens innebörd och termen ”genomspelning” är nu konsekventa. Alla ändringar skickades direkt till Crowdin via API (HTTP 201). Gettext gav endast den generella UTF-8-portabilitetsvarningen för den temporära PO-filen.