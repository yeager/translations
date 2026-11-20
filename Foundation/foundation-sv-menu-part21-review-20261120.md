# Foundation – menu.json, granskningsomgång 21

Datum: 2026-11-20  
Metod: Crowdin API; förslaget kontrollerades med `l10n-lint` och `hunspell-sv`.

| Nyckel | Engelsk källsträng | Tidigare svenska | Sparad svenska | Lint/stavning |
|---|---|---|---|---|
| MAIN_MENU → INCOMPATIBLE_SAVE_GAME_VERSION_BRANCH_MSG | This save game has been saved from a branch ({1}) that is not compatible with the current game version ({2}). | Denna sparfil har sparats från en gren ({1}) som inte är kompatibel med den aktuella spelversionen ({2}). | Den här sparfilen skapades i en utvecklingsgren ({1}) som inte är kompatibel med den aktuella spelversionen ({2}). | l10n-lint: inga fel. Hunspell: inga fel. |

Båda platshållarna bevarades och ”utvecklingsgren” klargör den tekniska betydelsen. Ändringen skickades direkt till Crowdin via API (HTTP 201). Gettext gav endast den generella UTF-8-portabilitetsvarningen för den temporära PO-filen.