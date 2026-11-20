# Foundation – menu.json, granskningsomgång 2

Datum: 2026-11-20  
Metod: Crowdin API; förslagen kontrollerades med `l10n-lint` och `hunspell-sv`.

| Nyckel | Engelsk källsträng | Tidigare svenska | Förslag | Resultat | Lint/stavning |
|---|---|---|---|---|---|
| MENU_GRAPHICS_SETTINGS → QUALITY_MEDIUM | Medium | Medium | Medel | Identisk översättning fanns redan i Crowdin; API:t rapporterade dubblett. | l10n-lint: inga fel. Hunspell: inga fel. |
| MAIN_MENU → LOAD_GAME_ERROR_MSG | Impossible to read the file '{1}'. | Omöjligt att läsa filen '{1}'. | Det går inte att läsa filen '{1}'. | Sparad i Crowdin (HTTP 201). | l10n-lint: inga fel. Hunspell: inga fel. |
| MAIN_MENU → INCOMPATIBLE_SAVE_GAME | Incompatible Save Game | Inkompatibelt sparat spel | Inkompatibel sparfil | Identisk översättning fanns redan i Crowdin; API:t rapporterade dubblett. | l10n-lint: inga fel. Hunspell: inga fel. |

Platshållaren `{1}` bevarades. Gettext gav endast den generella UTF-8-portabilitetsvarningen för den temporära PO-filen.