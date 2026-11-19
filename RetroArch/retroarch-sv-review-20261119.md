# RetroArch – svensk granskningsbatch 2026-11-19

Fyra förslag baserade på aktuella källsträngar och svenska översättningar i RetroArchs Crowdin-projekt. Förslagen har inte skrivits till Crowdin.

| Sträng-ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 1929190 | Saving | Sparningar | Sparande |
| 1929794 | Device Index | Enhetindex | Enhetsindex |
| 1930116 | Hide the overlay while inside the menu, and show it again when exiting the menu. | Dölj överlägg  i meny och visa igen när meny stängs. | Dölj överlägget i menyn och visa det igen när menyn stängs. |
| 1929482 | Sync to Exact Content Framerate (G-Sync, FreeSync) | Synkronisera exakt till innehållets bildhastighet (G-Sync, FreeSync) | Synkronisera till innehållets exakta bildfrekvens (G-Sync, FreeSync) |

## Granskningsnoteringar

- **Saving:** Strängen är en inställningsrubrik. *Sparande* beskriver området/aktiviteten; *Sparningar* låter som flera sparade filer eller speltillstånd. Crowdin-TM innehåller bara den nuvarande formuleringen.
- **Device Index:** *Enhetsindex* är korrekt sammansatt med foge-s. Crowdin rapporterar att förslaget redan finns som en annan översättning och rekommenderar att den befintliga översättningen röstas upp eller godkänns. Det är en QA-dubblett, inte en stavningsanmärkning.
- **Overlay:** Förslaget rättar dubbelt blanksteg, lägger till bestämd form och gör meningsbyggnaden idiomatisk. Crowdin-TM återger den nuvarande felaktiga texten.
- **Bildfrekvens:** Förslaget följer Crowdin-TM:s närliggande översättningar med *innehållets exakta bildfrekvens*. Behåll produktnamnen G-Sync och FreeSync oförändrade.

## Verktygskontroller

- Crowdin API läste aktuella källor, översättningar och språk-QA-status. Crowdin QA-validering av förslagen gav inga anmärkningar för *Sparande* eller overlay-texten; den flaggade dubbletten *Enhetsindex* och stavningskontrollen markerade *G-Sync*.
- Crowdin-projektets TM söktes via API:ets concordance-funktion. Den faktiska projektminnet heter **RetroArch's TM**. Någon separat CLI/MCP med namnet `swedish-tm` var inte tillgänglig; projektets TM användes i stället.
- `l10n-lint --language sv`: inga problem i PO-underlaget med de fyra förslagen.
- `hunspell -d sv_SE -a`: de svenska orden godkändes. Hunspell markerade G-Sync och FreeSync, som är produktnamn och ska bevaras.
- Platshållare och markup förekommer inte i dessa fyra strängar.

## Omfattning och källor

Detta är en fyrasträngars granskningsbatch, inte en fullständig genomgång av RetroArchs svenska katalog. Projektets senaste API-statistik vid granskningen visade 37 svenska filer. QA-felstatus användes som urvalssignal, men varje förslag bedömdes mot sin källsträng och sitt sammanhang.

- [RetroArch på Crowdin](https://crowdin.com/project/retroarch)
- [Crowdin API v2 – översättningar och TM-concordance](https://support.crowdin.com/developer/api/v2/)
