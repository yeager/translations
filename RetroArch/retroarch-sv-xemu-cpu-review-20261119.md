# RetroArch Xemu – DSP-, CPU- och FPU-inställningar, svensk granskningsbatch 2026-11-19

Åtta oöversatta svenska Xemu-strängar i `xemu-libretro.json` har granskats via Crowdin API. Förslagen är inte sparade eller skickade till Crowdin.

| Sträng-ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 6238655 | DSP JIT | — | DSP-JIT |
| 6238657 | Runs APU DSP Emulation's programs as compiled code instead of interpreting them: faster, as standalone's DSP JIT. Only does something with APU DSP Emulation on. Takes effect right away. | — | Kör programmen för APU-DSP-emulering som kompilerad kod i stället för att tolka dem: snabbare, som den fristående versionens DSP-JIT. Har bara effekt när APU-DSP-emulering är aktiverad. Träder i kraft omedelbart. |
| 6238659 | Profiler (F10) | — | Profilerare (F10) |
| 6238663 | CPU Boost (Restart) | — | CPU-boost (omstart) |
| 6238665 | Faster paths for the guest CPU and the audio processor: native SSE and a wider jump cache. Turn it off if a game misbehaves. Taken when the content starts. | — | Snabbare kodvägar för gästprocessorn och ljudprocessorn: inbyggd SSE och en större hoppcache. Stäng av om ett spel inte fungerar som det ska. Inställningen läses in när innehållet startar. |
| 6238667 | Hardware FPU Emulation (Restart) | — | Maskinvaru-FPU-emulering (omstart) |
| 6238669 | Use host FPU for x87 emulation. Faster but may have minor inaccuracies. Taken when the content starts. | — | Använd värdens FPU för x87-emulering. Snabbare men kan ge små felaktigheter. Inställningen läses in när innehållet startar. |
| 6238671 | Skip Idle TLB Modes | — | Hoppa över inaktiva TLB-lägen |

## Kontroller

- Projektets Crowdin-TM kontrollerades via concordance i API:t. Något separat verktyg med namnet `swedish-tm` finns inte installerat; projektets TM användes som tillgänglig motsvarighet.
- `l10n-lint --language sv` passerade utan anmärkningar.
- `hunspell -d sv_SE` markerar DSP-JIT, APU-DSP-emulering, F10, SSE, hoppcache, FPU, x87-emulering och TLB-lägen. Det är förkortningar, produkt-/tekniktermer eller korrekta sammansättningar.
- Crowdins QA markerar DSP-JIT, APU-DSP-emulering, F10, kodvägar, hoppcache, Maskinvaru-FPU-emulering och TLB-lägen av samma skäl. Inga platshållare eller formateringsmarkörer finns i batchen.
