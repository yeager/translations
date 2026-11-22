# Home Assistant Core – granskningsstatus

Status den 22 november 2026, beräknad från den aktuella Core-exporten och det
validerade Home Assistant-minnet.

| Mått | Antal |
| --- | ---: |
| Poster i Core-exporten | 75 106 |
| Poster i validerad Core-TMX | 3 369 |
| Konservativt återstående omfång | 71 737 |

Det återstående antalet är konservativt: utöver TMX-posterna finns
livegranskade strängar utan ny TMX-post, exempelvis hela komponenter där inga
ändringar behövdes. En TMX-post betyder att texten har en spårbar, verifierad
källa; den är inte en generell markering att en hel komponent eller Core som
helhet är klar.

Senast liveverifierade undergrupper: Template-maskinidentifierare,
Bayesian-resultatvärden och komponenterna Launch Library, Nissan Leaf, RPi
Power, Sensirion BLE, ThermoPro, ThermoBeacon, Input Button, Mold Indicator,
Harman Luxury, Linear Garage Door, SwitchBee, NextBus, Streamlabs Water,
RTSPtoWebRTC, NMBS, Home+ Control, RuuviTag BLE, SensorPro, Modem Caller ID,
Sanix, SenseME, Sunricher DALI Center, Channels och Rympro. Sparade ändringar
har lästs tillbaka via Lokalise API och de senaste TMX-posterna har
validerats i `swedish-tm`. Senast rättades Modern Forms två sensor-etiketter
till den konsekventa termen `insomningstid`.

Ingen verktygsrelease publicerades efter dagens tidigare release, enligt
arbetsregeln om högst en release per dag.
