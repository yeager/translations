# RetroArch – status för aktuella oöversatta svenska strängar, 2026-11-19

Crowdin API-inventeringen för projekt 380544 bekräftar följande aktuella restmängd. Samtliga nedanstående saknade strängar har granskats som **utkast**, validerats enligt respektive batchrapport och arkiverats i detta repository. Inget förslag har sparats eller skickats till Crowdin.

| Fil | Saknade strängar enligt API | Arkiverat underlag |
| --- | ---: | --- |
| `msg_hash_us.json` | 81 | Säkerhets-/kärnsignaturer, XMB-/firmwaretexter, handkontroll/OpenXR, spelskärmar, VBlank, stereo/headset och systemmeddelanden i batchrapporterna från 2026-11-19 |
| `xemu-libretro.json` | 25 | Xemu-system/DSP, CPU/FPU, profilerare, TLB, Vulkan och shaderkompilering |
| `beetle-psx-libretro.json` | 15 | GPU-tråd/etiketter, VRAM-kopia och parallell programvarurendering |
| `rpcs3-libretro.json` | 8 | Spakars dödzon/antidödzon och avtryckartrösklar |
| `pcee2-libretro.json` | 1 | GunCon 2-hårkors |
| **Summa** | **130** | **130 granskade, ej inskrivna utkast** |

## Kontrollomfattning

- Källsträngar och svenska översättningsstatus hämtades via Crowdin API.
- Projektets tillgängliga Crowdin-TM kontrollerades via concordance. Ett separat lokalt verktyg med namnet `swedish-tm` finns inte installerat; TM-kontrollen dokumenteras därför som projekt-TM i varje batch.
- Varje arkiverad batch har körts med `l10n-lint --language sv` och `hunspell -d sv_SE` samt genom Crowdins QA-validerings-API.
- Kvarvarande QA-/stavningsträffar i rapporterna är verifierade egennamn, filvägar, förkortningar eller korrekta svenska tekniska sammansättningar.
- Denna rapport omfattar inte Crowdins befintliga QA-fel i redan översatta strängar. De behöver fortsatt separat, radvis granskning.

## Upstreamstatus

Förslagen är lokala granskningsunderlag i `yeager/translations`, inte uppdateringar av Crowdin. En uttrycklig instruktion krävs före eventuell inskrivning eller inlämning till projektet.
