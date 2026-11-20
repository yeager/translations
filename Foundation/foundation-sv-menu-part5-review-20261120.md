# Foundation – menu.json, granskningsomgång 5

Datum: 2026-11-20  
Metod: Crowdin API; förslagen kontrollerades med `l10n-lint` och `hunspell-sv`.

| Nyckel | Engelsk källsträng | Tidigare svenska | Förslag | Resultat | Lint/stavning |
|---|---|---|---|---|---|
| MAIN_MENU → LOAD_GAME_DELETE_WARNING | Warning: save game deletion | Varning: sparfil raderas | Varning: radering av sparfil | Sparad i Crowdin (HTTP 201). | l10n-lint: inga fel. Hunspell: inga fel. |
| MENU_GRAPHICS_SETTINGS → WINDOWED | Windowed | Fönster | Fönsterläge | Sparad i Crowdin (HTTP 201). | l10n-lint: inga fel. Hunspell: inga fel. |
| MAIN_MENU → EDIT_MODS | Edit Mods | Redigera Mods | Redigera moddar | Identisk översättning fanns redan i Crowdin; API:t rapporterade dubblett. | l10n-lint: inga fel. Hunspell: inga fel. |

Gettext gav endast den generella UTF-8-portabilitetsvarningen för den temporära PO-filen.