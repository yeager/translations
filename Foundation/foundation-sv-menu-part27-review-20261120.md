# Foundation – menu.json, granskningsomgång 27

Datum: 2026-11-20  
Metod: Crowdin API; förslagen kontrollerades med `l10n-lint` och `hunspell-sv`.

| Nyckel | Engelsk källsträng | Tidigare svenska | Sparad svenska | Lint/stavning |
|---|---|---|---|---|
| MENU_MAP_SELECTOR → MAPGEN_MAPCODE_DEPRECATED_TITLE | Deprecated Map Code | Utdaterad kartkod | Utfasad kartkod | l10n-lint: inga fel. Hunspell: inga fel. |
| MENU_MAP_SELECTOR → MAPGEN_MAPCODE_DEPRECATED_TEXT | This Map Code is outdated and cannot be processed. | Denna kartkod är utdaterad och kan inte behandlas. | Den här kartkoden är föråldrad och kan inte bearbetas. | l10n-lint: inga fel. Hunspell: inga fel. |
| MENU_MAP_SELECTOR → MAPGEN_MAPCODE_MORE_RECENT_TITLE | Outdated Map Code | Utdaterad kartkod | Inaktuell kartkod | l10n-lint: inga fel. Hunspell: inga fel. |
| MENU_MODS_BROWSER → DATE_UPDATED | Date updated | Uppdaterat datum | Uppdaterad den | l10n-lint: inga fel. Hunspell: inga fel. |

”Utfasad” och ”inaktuell” skiljer nu de två källbegreppen åt. Samtliga ändringar skickades direkt till Crowdin via API (HTTP 201). Gettext gav endast den generella UTF-8-portabilitetsvarningen för den temporära PO-filen.