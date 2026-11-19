# RetroArch Xemu – renderarstatistik, svensk granskningsbatch 2026-11-19

En oöversatt svensk Xemu-beskrivning i `xemu-libretro.json` har granskats via Crowdin API. Förslaget är inte sparat eller skickat till Crowdin.

| Sträng-ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 6239299 | The profile file ends with the renderer's counters per second over the run: draws, pipeline and shader binds, texture uploads, surface downloads, syncs with the host GPU and why. | — | Profilfilen avslutas med renderarens räknare per sekund för körningen: ritanrop, pipeline- och shaderbindningar, texturuppladdningar, ytnedladdningar, synkroniseringar med värdens GPU och deras orsaker. |

## Kontroller

- Projektets Crowdin-TM kontrollerades via concordance i API:t. Något separat verktyg med namnet `swedish-tm` finns inte installerat; projektets TM användes som tillgänglig motsvarighet.
- `l10n-lint --language sv` passerade utan anmärkningar.
- `hunspell -d sv_SE` och Crowdins QA markerar profilfilen, renderarens, ritanrop, shaderbindningar och ytnedladdningar. De är korrekta svenska sammansättningar eller tekniska termer.
- Inga platshållare eller formateringsmarkörer finns i posten.
