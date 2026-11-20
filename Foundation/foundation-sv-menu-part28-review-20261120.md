# Foundation – menu.json, granskningsomgång 28

Datum: 2026-11-20  
Metod: Crowdin API; förslagen kontrollerades med `l10n-lint` och `hunspell-sv`.

| Nyckel | Engelsk källsträng | Tidigare svenska | Sparad svenska | Lint/stavning |
|---|---|---|---|---|
| MAIN_MENU → DELETE_PLAYTHROUGH_WARNING | Warning: Playthrough Deletion | Varning: Borttagning av genomspelning | Varning: borttagning av genomspelning | l10n-lint: inga fel. Hunspell: inga fel. |
| MAIN_MENU → ALL_SAVES_ARE_CLOUD | All Saved Games in this Playthrough are Cloud Saves | Alla sparade spel i denna genomgång är molnsparningar | Alla sparade spel i den här genomspelningen är molnsparningar | l10n-lint: inga fel. Hunspell: inga fel. |

”Genomspelning” är nu konsekvent inom detta gränssnitt. Båda ändringarna skickades direkt till Crowdin via API (HTTP 201). Gettext gav endast den generella UTF-8-portabilitetsvarningen för den temporära PO-filen.