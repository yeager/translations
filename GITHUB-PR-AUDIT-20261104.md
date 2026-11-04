# GitHub PR-audit – 4 november 2026

## Omfattning

En aktuell GitHub-kontroll av `yeager` hittade 126 öppna pull requests. Varje
post kontrollerades mot aktuell head, granskningsstatus, kommentarer och
statuskontroller. En PR som bara ligger efter huvudgrenen har inte rebats
slentrianmässigt: det görs först när det finns ett konkret granskningskrav eller
när en reproducerbar konflikt måste lösas.

## Åtgärdade

| Projekt | PR | Åtgärd | Verifiering | Status |
| --- | --- | --- | --- | --- |
| Console Shelf PS5 | [#3](https://github.com/Iswebro/console-shelf-ps5/pull/3) | Rebasa den svenska native-UI-lokaliseringen på aktuell stabil huvudgren; återställ sparad språkpreferens, inkluderar katalogen i host- och PS5-källistorna samt lägger visuella svenska renderingskontroller. | `npm run test:native-renderer`, `git diff --check`, Gitleaks. | Pushad som `f1bad9f`; väntar på ny granskning. PS5-byggning kräver x86_64-Linux/WSL och kördes därför inte på macOS. |

## Kräver extern input eller avsiktlig uppföljning

| Projekt | PR | Bedömning | Nästa steg |
| --- | --- | --- | --- |
| Laya | [#729](https://github.com/NandhaKishorM/laya/pull/729) | En konkret CI-kontroll misslyckas. Maintainern har dessutom krävt mätning av svenska frågeuppsättningar mot engelska på MASSIVE `sv-SE` med det flerspråkiga kontrollpunktsmodellen. PR:n är utkast och blockerad tills denna evidens finns. | Kör den överenskomna jämförelsen och bifoga radresultat innan ändringar skickas för ny granskning. |
| Xemu | [#2837](https://github.com/xemu-project/xemu/pull/2837) | Tidigare robotanmärkningar om katalogbygge och Windows-paketering är redan åtgärdade i aktuell head (`1ab255f230`); inga nya kontroller eller maintainerkrav finns. | Vänta på maintainergranskning; undvik nya orelaterade rebases. |
| Kodi TV | [#1314](https://github.com/xbmc/kodi-tv/pull/1314) | Maintainer har bett att arbetet stoppas. | Ingen kodändring utan nytt upstream-besked. |
| LibreSpeed | [#860](https://github.com/librespeed/speedtest/pull/860) | Maintainer har integrerat idén i sitt eget förslag. | Ingen parallell ändring; följ deras uppströmsarbete. |

## Notering

Statusen ovan gäller vid auditdatumet. `Waiting for review`, en neutral botkommentar
och en ren lokal diff är inte samma sak som att en ändring är godkänd eller mergad.
