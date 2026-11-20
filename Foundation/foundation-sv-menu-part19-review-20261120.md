# Foundation – menu.json, granskningsomgång 19

Datum: 2026-11-20  
Metod: Crowdin API; förslagen kontrollerades med `l10n-lint` och `hunspell-sv`.

| Nyckel | Engelsk källsträng | Tidigare svenska | Sparad svenska | Lint/stavning |
|---|---|---|---|---|
| MENU_MAP_SELECTOR → MOUNTAIN_MAP_DESC | The Mountain map offers a small coastal stretch of land with rough elevated terrain at your back that will challenge your establishment. | Bergskartan erbjuder en liten kuststräcka med tufft stigande terräng bakom sig som kommer att utmana din etablering. | Bergskartan erbjuder en liten kuststräcka med oländig, höglänt terräng i ryggen som kommer att utmana din bosättning. | l10n-lint: inga fel. Hunspell: inga fel. |
| MENU_MAP_SELECTOR → MAP_RESOURCES_MISSING | Missing resources | Saknar resurser | Saknade resurser | l10n-lint: inga fel. Hunspell: inga fel. |

Båda ändringarna skickades direkt till Crowdin via API (HTTP 201). Gettext gav endast den generella UTF-8-portabilitetsvarningen för den temporära PO-filen.