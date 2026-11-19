# RetroArch Xemu – system-, språk- och DSP-inställningar, svensk granskningsbatch 2026-11-19

Sex oöversatta svenska Xemu-strängar i xemu-libretro.json har granskats via Crowdin API. Förslagen är inte sparade eller skickade till Crowdin.

| Sträng-ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 6238641 | The machine itself: memory, network, boot and language. Taken when the content starts (Trim HDD on Close when it closes). | — | Själva maskinen: minne, nätverk, start och språk. Inställningarna läses in när innehållet startar (Trim HDD on Close när det stängs). |
| 6238645 | The profiler and switches for finding what slows a game down or breaks it: the CPU and GPU fast paths and the renderer's details. Best left as they are otherwise. | — | Profileraren och reglagen för att hitta vad som gör ett spel långsamt eller får det att sluta fungera: processorns och grafikprocessorns snabba kodvägar samt renderarens detaljer. I övrigt bör de lämnas som de är. |
| 6238647 | The language the console's settings give games, in place of the dashboard's setting. Auto is RetroArch's language when the Xbox has it, English otherwise. | — | Språket som konsolens inställningar anger för spel i stället för instrumentpanelens inställning. Med alternativet Automatiskt används RetroArchs språk när Xbox har det, annars engelska. |
| 6238649 | The display shape the console's video settings report to games, in place of the dashboard's setting. At 16:9, games that support widescreen run in widescreen; at 4:3 they run in 4:3. Set it to the shape of your display. Letterbox is the dashboard's 4:3 with widescreen games letterboxed. | — | Det bildformat som konsolens videoinställningar rapporterar till spel, i stället för instrumentpanelens inställning. Vid 16:9 körs spel med stöd för bredbild i bredbild; vid 4:3 körs de i 4:3. Ställ in det på din bildskärms bildformat. Letterbox är instrumentpanelens 4:3 med bredbildsspel i letterbox-format. |
| 6238651 | APU DSP Emulation | — | Emulering av APU-DSP |
| 6238653 | Emulates the APU's DSP, which plays the games' effects, reverb and much of their music: without it the sound is flat. Takes effect right away. | — | Emulerar ljudprocessorns digitala signalprocessor, som återger spelens effekter, efterklang och mycket av musiken: utan den låter ljudet platt. Träder i kraft omedelbart. |

## Kontroller

- Tidigare Xemu-underlag i arkivet användes för terminologi kring instrumentpanelen, APU-DSP och automatiskt språkval.
- l10n-lint med svenska regler passerade utan anmärkningar.
- Crowdins återstående QA-träffar gäller HDD on Close, kodvägar, renderaren, bredbild, Letterbox och APU-DSP. De är produktnamn, gränssnittsetiketter eller korrekta sammansättningar.
