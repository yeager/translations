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
| Console Shelf PS5 | [#3](https://github.com/Iswebro/console-shelf-ps5/pull/3) | Rebasa den svenska native-UI-lokaliseringen på aktuell stabil huvudgren; återställ sparad språkpreferens, inkluderar katalogen i host- och PS5-källistorna samt lägger visuella svenska renderingskontroller. Rättar även macOS-grenen i den befintliga POSIX-filidentitetskontrollen, så att den använder `st_mtimespec`/`st_ctimespec`. | `npm run test:native`, `npm run test:native-renderer`, `npm test`, `git diff --check` och Gitleaks. | Pushad som `7fd8927`; väntar på ny granskning. PS5-byggning når verktygskedjespärren och kräver x86_64-Linux/WSL, så den kan inte verifieras på macOS. |
| ComfyUI Frontend | [#17064](https://github.com/Comfy-Org/ComfyUI_frontend/pull/17064) | Rebasa svenska kataloger mot aktuell `main`, komplettera 92 nya eller ändrade UI-strängar, rätta två bevarade token och lägg test för `sv`/`sv-SE` i språkupplösningen. | `pnpm locale:check` utan tokenfel, `pnpm exec vitest run src/i18n.test.ts` (50 tester), formateringskontroll, `git diff --check` och Gitleaks för ändrade filer. | Pushad som `c4b2d73f`; CLA- och båda Socket-kontrollerna passerade. Äldre oöversatta svenska strängar rapporteras separat och är inte påstått kompletta här; väntar på ny granskning. |

## Kräver extern input eller avsiktlig uppföljning

| Projekt | PR | Bedömning | Nästa steg |
| --- | --- | --- | --- |
| Laya | [#729](https://github.com/NandhaKishorM/laya/pull/729) | Den konkreta CI-failuren var att Java-fixturegeneratorn felaktigt tog med privata Python-tabeller som publika presets. Generatorn ignorerar nu namn med inledande `_`; korrigeringen `3364ac50` har passerat hela CI-körningen [41856150511](https://github.com/NandhaKishorM/laya/actions/runs/41856150511), inklusive alla Java-, språkparitets-, bygg- och säkerhetsbanor. Maintainern kräver dessutom mätning av svenska frågeuppsättningar mot engelska på MASSIVE `sv-SE` med den flerspråkiga kontrollpunktsmodellen. PR:n är utkast tills denna evidens finns. | Kör den överenskomna jämförelsen och bifoga radresultat innan ändringar skickas för ny granskning. |
| Xemu | [#2837](https://github.com/xemu-project/xemu/pull/2837) | Tidigare robotanmärkningar om katalogbygge och Windows-paketering är redan åtgärdade i aktuell head (`1ab255f230`); inga nya kontroller eller maintainerkrav finns. | Vänta på maintainergranskning; undvik nya orelaterade rebases. |
| Kodi TV | [#1314](https://github.com/xbmc/kodi-tv/pull/1314) | Maintainer har bett att arbetet stoppas. | Ingen kodändring utan nytt upstream-besked. |
| LibreSpeed | [#860](https://github.com/librespeed/speedtest/pull/860) | Maintainer har integrerat idén i sitt eget förslag. | Ingen parallell ändring; följ deras uppströmsarbete. |
| OpenClaw iOS | [#160981](https://github.com/openclaw/openclaw/pull/160981) | Kod- och i18n-kontroller passerar, men ClawSweeper kräver faktisk, nybyggd iOS-evidens som visar `Färdigheter`, samt Xcode-status för sju återstående nya enheter. Den existerande bilden är uttryckligen tagen före korrigeringen. | Bygg iOS-appen med svenska vald, fånga den berörda vyn och den aktuella lokaliseringsstatusen, bifoga sanerad evidens och begär sedan omgranskning. |

## Kontrollerade utan ny kodändring

| Projekt | PR | Evidens | Bedömning |
| --- | --- | --- | --- |
| TigerVNC | [#2167](https://github.com/TigerVNC/tigervnc/pull/2167) | Aktuell kod använder nu `EnumParameter`, väljer endast den angivna kodningen och återanvänder befintliga CPU-räknare. `encperf` byggde och körde ett genererat RFB-spår med ZRLE. | De synliga granskningskommentarerna gäller äldre commit-id:n och är redan implementerade i aktuell head; PR:n väntar på omgranskning. |
| FreeRDP | [#13388](https://github.com/FreeRDP/FreeRDP/pull/13388) | Floatbar är nu en egen komponent enligt kommentarerna och de ändrade SDL3-källorna kompilerar. | En komplett lokal länkning med en avskalad kanal-konfiguration saknade `client_rail_server_start_cmd`; det är en konsekvens av den avskalade lokala konfigurationen, inte en ändring i floatbar-diffen. Riktig RDP-sessionsverifiering och maintainergranskning återstår. |
| Firestaff | [#252](https://github.com/yeager/firestaff/pull/252) | De sex CodeRabbit-fynden kontrollerades mot aktuell head `5d8850d`: dokumentationen skiljer nu `Not Run` från `Passed`, standardkatalogen för retaildata används, replay- och displayplan jämförs före ägarredovisning, skuggberäkning lämnar befintlig ägare orörd och mode-5:s MSB/adressfall täcks. Det berörda CMake-målet bygger lokalt. | Samtliga synliga fynd gäller äldre commit-id:n eller är implementerade i aktuell head; ingen ny spekulativ ändring behövs. CTest markerar realdatatestet som `Skipped` utan de autentiska capture- och spelfilerna, alltså inte som passerad parity-verifiering. |
| KytyPS5 | [#1496](https://github.com/KytyPS5/KytyPS5/pull/1496) | Aktuell head `8d30a0d` har en grön CodeRabbit-kontroll utan åtgärdskrav. | Väntar på projektets maintainer; `UNSTABLE` saknar konkret fel- eller granskningsunderlag. |
| FreeSWITCH | [#3242](https://github.com/signalwire/freeswitch/pull/3242), [#3243](https://github.com/signalwire/freeswitch/pull/3243) | Båda PR:erna har rena statuskontroller och inga externa kommentarer eller recensioner att åtgärda. | `REVIEW_REQUIRED` och `BEHIND` i sig motiverar inte en riskfylld rutinrebase; invänta konkret maintainerkrav. |
| Vorta, Langflow, Shutter | [Vorta #2550](https://github.com/borgbase/vorta/pull/2550), [Langflow #14864](https://github.com/langflow-ai/langflow/pull/14864), [Shutter #840](https://github.com/shutter-project/shutter/pull/840) | PR-status visar granskningsbehov men inga nya externa granskningskommentarer eller inline-krav. | Ingen spekulativ kodändring gjordes. |

## Notering

Statusen ovan gäller vid auditdatumet. `Waiting for review`, en neutral botkommentar
och en ren lokal diff är inte samma sak som att en ändring är godkänd eller mergad.

## Uppföljning 4 november 2026, 16:46 CET

Samtliga 126 öppna PR:er lästes om via GitHub API med aktuell head, kommentarer,
recensioner och statuskontroller. 110 saknar både aktivt granskningskrav och
misslyckad/pågående kontroll. De 16 signalerade PR:erna granskades manuellt.

* Console Shelf PS5 #3 har fortfarande den äldre begäran om ändringar markerad,
  men den aktuella headen `7fd8927` innehåller de efterfrågade källiste- och
  macOS-rättningarna. Host- och renderartesterna är redan verifierade; PS5-länkning
  kräver fortsatt en x86_64-Linux/WSL-byggmiljö.
* ComfyUI Frontend #17064, TigerVNC #2167 och FreeRDP #13388 har endast äldre
  granskningshändelser; de synliga kraven kontrollerades mot respektive nuvarande
  head och har ingen ny konkret diff att tillämpa. De inväntar en maintainer.
* Laya #729 visar fortfarande äldre, fastnade kontrollstatusar i PR-vyn medan den
  efterföljande fullständiga körningen 41856150511 är grön. Det återstående kravet
  är den av maintainern begärda, märkta svenska stöduppgiftsutvärderingen – inte en
  CI- eller koddefekt.
* OpenClaw #160981 saknar den uttryckligen begärda nya iOS-körningens skärmevidens;
  de röda/avbrutna kontrollerna hör till den gamla evidensworkflowen. Utan en
  tillgänglig iOS-miljö går det inte att ersätta den med påhittad verifiering.
* Stirling PDF #7833:s kvarvarande robotkommentarer skulle kräva ändringar av
  källspråket eller projektets särskilda lokaliseringsflöde. Ingen svensk
  katalogändring görs runt den dokumenterade upstream-policyn.
* LibreSpeed #860 har en misslyckad äldre e2e-körning, men maintainern har uttryckligen
  integrerat förslaget i sitt eget spår. Den parallella PR:n lämnas orörd.

Inga nya säkra kodändringar återstod efter den kompletta uppföljningen. Externa
miljöer, maintainergranskningar och uttryckliga projektpolicyer redovisas därför som
uppföljning i stället för att döljas med rutinrebases eller spekulativa patchar.
