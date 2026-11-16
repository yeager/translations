# Home Assistant – live-status för frontend och Companion

Datum: 2026-11-16  
Tjänst: Lokalise API  
Språk: `sv`

## Verifierad status

| Komponent | Projekt-id | Förlopp | Ord kvar |
| --- | --- | ---: | ---: |
| Frontend | `3420425759f6d6d241f598.13594006` | 100 % | 0 |
| Companion för Android | `145814835dd655bc5ab0d0.36753359` | 100 % | 0 |
| Companion för iOS | `834452985a05254348aee2.46389241` | 100 % | 0 |

Statusen kommer direkt från respektive projekts `statistics.languages`-post
för `sv`. Ingen översättning behövde ändras eller skickas in i denna kontroll.

## Core-behörighet

Två oberoende, sparade Lokalise-tokenen listar Home Assistant – Core
(`130246255a974bd3b5e8a1.51616605`) men projektresursen returnerar HTTP 403
för båda. Det är därför ett projektbehörighetsproblem, inte en fråga om vilket
av de tillgängliga kontona som används. Det bevisar inte något nytt om
Core-översättningarnas täckning och ingen skrivning gjordes där. Den här
statuskontrollen gäller därför bara de tre komponenter som kunde läsas
autentiserat.
