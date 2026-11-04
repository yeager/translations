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
| ComfyUI Frontend | [#17064](https://github.com/Comfy-Org/ComfyUI_frontend/pull/17064) | Rebasa svenska kataloger mot aktuell `main`, komplettera 92 nya eller ändrade UI-strängar, rätta två bevarade token och lägg test för `sv`/`sv-SE` i språkupplösningen. | `pnpm locale:check` utan tokenfel, `pnpm exec vitest run src/i18n.test.ts` (50 tester), formateringskontroll, `git diff --check` och Gitleaks för ändrade filer. | Pushad som `c4b2d73f`; GitHub-kontroller startade, väntar på ny granskning. Kontrollens rapporterar äldre oöversatta svenska strängar separat; de är inte påstått kompletta här. |

## Kräver extern input eller avsiktlig uppföljning

| Projekt | PR | Bedömning | Nästa steg |
| --- | --- | --- | --- |
| Laya | [#729](https://github.com/NandhaKishorM/laya/pull/729) | En konkret CI-kontroll misslyckas. Maintainern har dessutom krävt mätning av svenska frågeuppsättningar mot engelska på MASSIVE `sv-SE` med det flerspråkiga kontrollpunktsmodellen. PR:n är utkast och blockerad tills denna evidens finns. | Kör den överenskomna jämförelsen och bifoga radresultat innan ändringar skickas för ny granskning. |
| Xemu | [#2837](https://github.com/xemu-project/xemu/pull/2837) | Tidigare robotanmärkningar om katalogbygge och Windows-paketering är redan åtgärdade i aktuell head (`1ab255f230`); inga nya kontroller eller maintainerkrav finns. | Vänta på maintainergranskning; undvik nya orelaterade rebases. |
| Kodi TV | [#1314](https://github.com/xbmc/kodi-tv/pull/1314) | Maintainer har bett att arbetet stoppas. | Ingen kodändring utan nytt upstream-besked. |
| LibreSpeed | [#860](https://github.com/librespeed/speedtest/pull/860) | Maintainer har integrerat idén i sitt eget förslag. | Ingen parallell ändring; följ deras uppströmsarbete. |

## Kontrollerade utan ny kodändring

| Projekt | PR | Evidens | Bedömning |
| --- | --- | --- | --- |
| TigerVNC | [#2167](https://github.com/TigerVNC/tigervnc/pull/2167) | Aktuell kod använder nu `EnumParameter`, väljer endast den angivna kodningen och återanvänder befintliga CPU-räknare. `encperf` byggde och körde ett genererat RFB-spår med ZRLE. | De synliga granskningskommentarerna gäller äldre commit-id:n och är redan implementerade i aktuell head; PR:n väntar på omgranskning. |
| FreeRDP | [#13388](https://github.com/FreeRDP/FreeRDP/pull/13388) | Floatbar är nu en egen komponent enligt kommentarerna och de ändrade SDL3-källorna kompilerar. | En komplett lokal länkning med en avskalad kanal-konfiguration saknade `client_rail_server_start_cmd`; det är en konsekvens av den avskalade lokala konfigurationen, inte en ändring i floatbar-diffen. Riktig RDP-sessionsverifiering och maintainergranskning återstår. |
| Vorta, Langflow, Shutter | [Vorta #2550](https://github.com/borgbase/vorta/pull/2550), [Langflow #14864](https://github.com/langflow-ai/langflow/pull/14864), [Shutter #840](https://github.com/shutter-project/shutter/pull/840) | PR-status visar granskningsbehov men inga nya externa granskningskommentarer eller inline-krav. | Ingen spekulativ kodändring gjordes. |

## Notering

Statusen ovan gäller vid auditdatumet. `Waiting for review`, en neutral botkommentar
och en ren lokal diff är inte samma sak som att en ändring är godkänd eller mergad.
