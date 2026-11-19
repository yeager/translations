# RetroArch Beetle PSX – GPU-tråd och skalningsetiketter, svensk granskningsbatch 2026-11-19

Tretton oöversatta svenska etiketter i `beetle-psx-libretro.json` har granskats via Crowdin API. Förslagen är inte sparade eller skickade till Crowdin.

| Sträng-ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 6239315 | GPU Thread | — | GPU-tråd |
| 6239325 | 1 Lane | — | 1 tråd |
| 6239327 | 2 Lanes | — | 2 trådar |
| 6239329 | 3 Lanes | — | 3 trådar |
| 6239331 | 4 Lanes | — | 4 trådar |
| 6239333 | 6 Lanes | — | 6 trådar |
| 6239335 | 8 Lanes | — | 8 trådar |
| 6239337 | 4 stops (Blender default) | — | 4 stopp (Blenders standardvärde) |
| 6239339 | 6 stops (saturates at 64) | — | 6 stopp (mättas vid 64) |
| 6239341 | 8 stops (saturates at 256) | — | 8 stopp (mättas vid 256) |
| 6239343 | 1 Second Delay | — | 1 sekunds fördröjning |
| 6239345 | 2 Second Delay | — | 2 sekunders fördröjning |
| 6239347 | 3 Second Delay | — | 3 sekunders fördröjning |

## Kontroller

- Projektets Crowdin-TM kontrollerades via concordance i API:t. Något separat verktyg med namnet `swedish-tm` finns inte installerat; projektets TM användes som tillgänglig motsvarighet.
- `l10n-lint --language sv` passerade utan anmärkningar.
- `hunspell -d sv_SE` och Crowdins QA markerar enbart Blenders, ett korrekt egennamn i genitiv.
- Inga platshållare eller formateringsmarkörer finns i batchen.
