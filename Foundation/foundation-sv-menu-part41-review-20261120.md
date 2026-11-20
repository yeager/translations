# Foundation – menu.json, granskningsomgång 41

Datum: 2026-11-20  
Metod: Crowdin API; samtliga förslag kontrollerades med `l10n-lint` och `hunspell-sv`.

| Nyckel | Engelsk källsträng | Tidigare svenska | Förslag | Resultat |
|---|---|---|---|---|
| LANGUAGE_MOD_TRANSLATION | Mod | *(tom)* | Mod | Dubblett i Crowdin. |
| INSTALLED | Installed | *(tom)* | Installerad | Dubblett i Crowdin. |
| SHOW_AUTOSAVE | Show Autosaves | *(tom)* | Visa automatiska sparningar | Dubblett i Crowdin. |
| CONTROL_SELECT_ALL_PARTS | Select All Parts | *(tom)* | Markera alla delar | Sparad (HTTP 201). |
| WARNING_QOL1_TITLE | Pre-Update 1 save file detected | *(tom)* | Sparfil från före uppdatering 1 hittades | Dubblett i Crowdin. |
| WARNING_QOL1_DESC | Be advised that Update 1… | *(tom)* | Observera att uppdatering 1 medför flera ändringar i patrullsystemet… | Sparad (HTTP 201). |
| WARNING_QOL1_END | Enjoy! | *(tom)* | Ha så roligt! | Sparad (HTTP 201). |
| WARNING_QOL1_ITEM_1 | **Split large Watchposts:** … | *(tom)* | **Dela upp stora vaktposter:** … | Sparad (HTTP 201). |
| WARNING_QOL1_ITEM_3 | **Repaint Patrol Areas:** … | *(tom)* | **Måla om patrullområden:** … | Sparad (HTTP 201). |
| WARNING_QOL1_ITEM_2 | **Spread Patrollers across multiple buildings:** … | *(tom)* | **Sprid ut patrullerare över flera byggnader:** … | Sparad (HTTP 201). |

Fetstilmarkeringen `**…:**` och den inledande osynliga markören i berörda källsträngar bevarades. l10n-lint och Hunspell gav inga fel; Gettext gav endast den generella UTF-8-portabilitetsvarningen för den temporära PO-filen.