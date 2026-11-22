# Home Assistant Core – granskningsstatus

Status den 22 november 2026, beräknad från den aktuella Core-exporten och det
validerade Home Assistant-minnet.

| Mått | Antal |
| --- | ---: |
| Poster i Core-exporten | 75 106 |
| Poster i validerad Core-TMX | 3 318 |
| Konservativt återstående omfång | 71 788 |

Det återstående antalet är konservativt: utöver TMX-posterna finns
livegranskade strängar utan ny TMX-post, exempelvis hela komponenter där inga
ändringar behövdes. En TMX-post betyder att texten har en spårbar, verifierad
källa; den är inte en generell markering att en hel komponent eller Core som
helhet är klar.

Senast liveverifierade undergrupper: Template-maskinidentifierare,
Bayesian-resultatvärden och komponenterna Launch Library, Nissan Leaf, RPi
Power, Sensirion BLE, ThermoPro, ThermoBeacon, Input Button, Mold Indicator,
Harman Luxury, Linear Garage Door, SwitchBee och NextBus. Sammanlagt 114
strängar i dessa komponentgrupper har kontrollerats rad för rad i den aktuella
Lokalise-versionen; sparade ändringar har lästs tillbaka via API.

Ingen verktygsrelease publicerades efter dagens tidigare release, enligt
arbetsregeln om högst en release per dag.
