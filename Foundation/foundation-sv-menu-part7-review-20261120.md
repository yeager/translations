# Foundation – menu.json, granskningsomgång 7

Datum: 2026-11-20  
Metod: Crowdin API; förslagen kontrollerades med `l10n-lint` och `hunspell-sv`.

| Nyckel | Engelsk källsträng | Tidigare svenska | Sparad svenska | Lint/stavning |
|---|---|---|---|---|
| MAIN_MENU → INCOMPATIBLE_WITH_PREVIEW_MSG | This preview save game cannot be loaded in a non-preview version of Foundation. | Denna förhandsgranskade sparfil kan inte laddas i en icke förhandsgranskad version av Foundation. | Den här sparfilen från förhandsversionen kan inte läsas in i en version av Foundation som inte är en förhandsversion. | l10n-lint: inga fel. Hunspell: inga fel. |
| MAIN_MENU → INCOMPATIBLE_PREVIEW_SAVE_GAME_MSG | This preview save game is incompatible with this version of Foundation. | Denna förhandsgranskade sparfil är inkompatibel med denna version av Foundation. | Den här sparfilen från förhandsversionen är inkompatibel med denna version av Foundation. | l10n-lint: inga fel. Hunspell: inga fel. |

Översättningarna gör klart att det är en sparfil skapad i en förhandsversion. Båda ändringarna skickades direkt till Crowdin via API (HTTP 201). Gettext gav endast den generella UTF-8-portabilitetsvarningen för den temporära PO-filen.