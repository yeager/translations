# RetroArch Xemu – PFIFO/PGRAPH-profilerare, svensk granskningsbatch 2026-11-19

En oöversatt svensk Xemu-beskrivning i `xemu-libretro.json` har granskats via Crowdin API. Förslaget är inte sparat eller skickat till Crowdin.

| Sträng-ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 6239295 | Windows: with the profiler on, the GPU thread (the pushbuffer and the renderer) is sampled beside the CPU emulation, and the profile file gets its section after the CPU's: where it spends its time and what it waits for. Read when the profiler comes on. | — | Windows: när profileraren är aktiverad samplas GPU-tråden (pushbufferten och renderaren) parallellt med CPU-emuleringen, och profilfilen får sitt avsnitt efter avsnittet om processorn: var den tillbringar tid och vad den väntar på. Läses in när profileraren aktiveras. |

## Kontroller

- Projektets Crowdin-TM kontrollerades via concordance i API:t. Något separat verktyg med namnet `swedish-tm` finns inte installerat; projektets TM användes som tillgänglig motsvarighet.
- `l10n-lint --language sv` passerade utan anmärkningar.
- `hunspell -d sv_SE` och Crowdins QA markerar pushbufferten, renderaren och profilfilen som möjliga stavningsträffar. Det är korrekta tekniska sammansättningar.
- Första formuleringen fick Crowdins falska skiljeteckensträff för `CPU:ns`; den är ersatt med ”avsnittet om processorn”. Slutlig QA innehåller bara stavningsträffarna ovan.
- Inga platshållare eller formateringsmarkörer finns i posten.
