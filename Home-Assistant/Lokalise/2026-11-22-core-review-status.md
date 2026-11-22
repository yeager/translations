# Home Assistant Core – granskningsstatus

Status den 22 november 2026, beräknad från den aktuella Core-exporten och det
validerade Home Assistant-minnet.

| Mått | Antal |
| --- | ---: |
| Poster i Core-exporten | 75 106 |
| Poster i validerad Core-TMX | 3 233 |
| Konservativt återstående omfång | 71 873 |

Det återstående antalet är konservativt: utöver TMX-posterna finns
livegranskade strängar utan ny TMX-post, exempelvis hela komponenter där inga
ändringar behövdes. En TMX-post betyder att texten har en spårbar, verifierad
källa; den är inte en generell markering att en hel komponent eller Core som
helhet är klar.

Senast liveverifierade Template-undergrupp: 71
tillgänglighetsbeskrivningar med de maskinella värdena `available` och
`unavailable`. De kontrollerades direkt via Lokalise och var korrekta efter
sparade korrigeringar. Ingen verktygsrelease publicerades efter dagens tidigare
release, enligt arbetsregeln om högst en release per dag.
