# RetroArch Xemu – profileretiketter, svensk granskningsbatch 2026-11-19

Fyra oöversatta svenska Xemu-etiketter i `xemu-libretro.json` har granskats via Crowdin API. Förslagen är inte sparade eller skickade till Crowdin.

| Sträng-ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 6239293 | Profiler: PFIFO/PGRAPH | — | Profilerare: PFIFO/PGRAPH |
| 6239297 | Profiler: Renderer Counters | — | Profilerare: renderarstatistik |
| 6239301 | Profiler: Missed Render Targets | — | Profilerare: missade renderingsmål |
| 6239305 | Profiler: Surface Downloads and Uploads | — | Profilerare: hämtning och överföring av ytor |

## Kontroller

- Projektets Crowdin-TM kontrollerades via concordance i API:t. Något separat verktyg med namnet `swedish-tm` finns inte installerat; projektets TM användes som tillgänglig motsvarighet.
- `l10n-lint --language sv` passerade utan anmärkningar.
- `hunspell -d sv_SE` godkänner samtliga ord utom PFIFO, PGRAPH och renderarstatistik. PFIFO och PGRAPH är tekniska komponentnamn; renderarstatistik är en korrekt svensk sammansättning.
- Crowdins QA markerar endast renderarstatistik som möjlig stavningsträff. Inga platshållare eller formateringsmarkörer finns i batchen.
