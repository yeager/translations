# Foundation – menu.json, granskningsomgång 18

Datum: 2026-11-20  
Metod: Crowdin API; förslagen kontrollerades med `l10n-lint` och `hunspell-sv`.

| Nyckel | Engelsk källsträng | Tidigare svenska | Sparad svenska | Lint/stavning |
|---|---|---|---|---|
| MENU_GENERAL_SETTINGS → USER_INTERFACE_SCALE_WARNING | User Interface Scale is above the recommended scale ({1}) for the current resolution. | Användargränssnittsskala överskrider den rekommenderade skalan ({1}) för den aktuella upplösningen. | Användargränssnittets skala överskrider den rekommenderade skalan ({1}) för den aktuella upplösningen. | l10n-lint: inga fel. Hunspell: inga fel. |
| MENU_MODS_BROWSER → COMMENT_ON_MOD_PAGE | Open mod webpage | Öppna modifikationswebbsida | Öppna moddens webbsida | l10n-lint: inga fel. Hunspell: inga fel. |

Platshållaren `{1}` bevarades. Båda ändringarna skickades direkt till Crowdin via API (HTTP 201). Gettext gav endast den generella UTF-8-portabilitetsvarningen för den temporära PO-filen.