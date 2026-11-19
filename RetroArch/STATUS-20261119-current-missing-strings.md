# RetroArch – status för aktuella oöversatta svenska strängar, 2026-11-19

Crowdin API-inventeringen för projekt 380544 bekräftade följande aktuella restmängd. Samtliga nedanstående saknade strängar granskades som **utkast**, validerades enligt respektive batchrapport och arkiverades i detta repository. Efter användarens uttryckliga godkännande sparades förslagen i Crowdin den 2026-11-19.

| Fil | Saknade strängar enligt API | Arkiverat underlag |
| --- | ---: | --- |
| `msg_hash_us.json` | 81 | Säkerhets-/kärnsignaturer, XMB-/firmwaretexter, handkontroll/OpenXR, spelskärmar, VBlank, stereo/headset och systemmeddelanden i batchrapporterna från 2026-11-19 |
| `xemu-libretro.json` | 25 | Xemu-system/DSP, CPU/FPU, profilerare, TLB, Vulkan och shaderkompilering |
| `beetle-psx-libretro.json` | 15 | GPU-tråd/etiketter, VRAM-kopia och parallell programvarurendering |
| `rpcs3-libretro.json` | 8 | Spakars dödzon/antidödzon och avtryckartrösklar |
| `pcee2-libretro.json` | 1 | GunCon 2-hårkors |
| **Summa** | **130** | **130 granskade och sparade i Crowdin** |

## Kontrollomfattning

- Källsträngar och svenska översättningsstatus hämtades via Crowdin API.
- Projektets tillgängliga Crowdin-TM kontrollerades via concordance. Ett separat lokalt verktyg med namnet `swedish-tm` finns inte installerat; TM-kontrollen dokumenteras därför som projekt-TM i varje batch.
- Varje arkiverad batch har körts med `l10n-lint --language sv` och `hunspell -d sv_SE` samt genom Crowdins QA-validerings-API.
- Kvarvarande QA-/stavningsträffar i rapporterna är verifierade egennamn, filvägar, förkortningar eller korrekta svenska tekniska sammansättningar.
- Denna rapport omfattar inte Crowdins befintliga QA-fel i redan översatta strängar. De behöver fortsatt separat, radvis granskning.

## Upstreamstatus

Efter uttryckligt användargodkännande sparades de 130 saknade strängarna och de arkiverade förbättringsförslagen i Crowdin. API-återläsning bekräftar nu 100 % svenska översättningar i `msg_hash_us.json`, `xemu-libretro.json`, `beetle-psx-libretro.json`, `rpcs3-libretro.json` och `pcee2-libretro.json`. Inga översättningar godkändes och inga projektinställningar ändrades.
