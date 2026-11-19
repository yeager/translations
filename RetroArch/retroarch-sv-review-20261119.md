# RetroArch – svensk granskningsbatch 2026-11-19

Sex förslag baserade på aktuella källsträngar och svenska översättningar i RetroArchs Crowdin-projekt. Förslagen har inte skrivits till Crowdin.

| Sträng-ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 1929190 | Saving | Sparningar | Sparande |
| 1929794 | Device Index | Enhetindex | Enhetsindex |
| 1930116 | Hide the overlay while inside the menu, and show it again when exiting the menu. | Dölj överlägg  i meny och visa igen när meny stängs. | Dölj överlägget i menyn och visa det igen när menyn stängs. |
| 1929482 | Sync to Exact Content Framerate (G-Sync, FreeSync) | Synkronisera exakt till innehållets bildhastighet (G-Sync, FreeSync) | Synkronisera till innehållets exakta bildfrekvens (G-Sync, FreeSync) |
| 1929970 | Write save state files in an archived format. Dramatically reduces file size at the expense of increased saving/loading times. | Lagrar dina sparade tillståndsfiler i ett arkiverat format. Minskar dramatiskt filstorleken på bekostnad av längre spar- och inläsningstider. | Spara tillståndsfiler i ett komprimerat arkivformat. Filstorleken minskar kraftigt, men det tar längre tid att spara och läsa in dem. |
| 1929922 | Load Override Files Automatically | Läs automatiskt in åsidosättningsfiler | Läs in åsidosättningsfiler automatiskt |

## Granskningsnoteringar

- **Saving:** Strängen är en inställningsrubrik. *Sparande* beskriver området/aktiviteten; *Sparningar* låter som flera sparade filer eller speltillstånd. Crowdin-TM innehåller bara den nuvarande formuleringen.
- **Device Index:** *Enhetsindex* är korrekt sammansatt med foge-s. Crowdin rapporterar att förslaget redan finns som en annan översättning och rekommenderar att den befintliga översättningen röstas upp eller godkänns. Det är en QA-dubblett, inte en stavningsanmärkning.
- **Overlay:** Förslaget rättar dubbelt blanksteg, lägger till bestämd form och gör meningsbyggnaden idiomatisk. Crowdin-TM återger den nuvarande felaktiga texten.
- **Bildfrekvens:** Förslaget följer Crowdin-TM:s närliggande översättningar med *innehållets exakta bildfrekvens*. Behåll produktnamnen G-Sync och FreeSync oförändrade.
- **Tillståndsfiler:** Förslaget ersätter den bokstavliga formuleringen *arkiverat format* med *komprimerat arkivformat* och delar upp den långa följdmeningen. *Tillståndsfil* stämmer med etablerad svensk emulatorterminologi.
- **Override-filer:** *Läs in åsidosättningsfiler automatiskt* följer den naturliga ordställningen i RetroArchs närliggande sträng för att läsa in ommappningsfiler.

## Verktygskontroller

- Crowdin API läste aktuella källor, översättningar och språk-QA-status. Crowdin QA-validering av förslagen gav inga anmärkningar för *Sparande* eller overlay-texten; den flaggade dubbletten *Enhetsindex* samt stavningskontrollerna markerade *G-Sync*, *tillståndsfiler* och *åsidosättningsfiler*.
- Crowdin-projektets TM söktes via API:ets concordance-funktion. Den faktiska projektminnet heter **RetroArch's TM**. Någon separat CLI/MCP med namnet `swedish-tm` var inte tillgänglig; projektets TM användes i stället.
- `l10n-lint --language sv`: inga problem i PO-underlaget med de fyra förslagen.
- `hunspell -d sv_SE -a`: de svenska orden godkändes. Hunspell markerade produktnamnen G-Sync och FreeSync samt sammansättningen *åsidosättningsfiler*. Produktnamnen ska bevaras; *åsidosättningsfiler* är en korrekt svensk sammansättning som ordlistan inte känner igen.
- Platshållare och markup förekommer inte i dessa fyra strängar.

## Omfattning och källor

Detta är en sexsträngars granskningsbatch, inte en fullständig genomgång av RetroArchs svenska katalog. Projektets API visade 10 120 fraser i 37 svenska filer, varav 9 990 var översatta vid granskningen. QA-felstatus användes som urvalssignal, men varje förslag bedömdes mot sin källsträng och sitt sammanhang.

- [RetroArch på Crowdin](https://crowdin.com/project/retroarch)
- [Crowdin API v2 – översättningar och TM-concordance](https://support.crowdin.com/developer/api/v2/)
