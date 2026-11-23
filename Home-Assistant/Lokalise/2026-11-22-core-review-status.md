# Home Assistant Core – granskningsstatus

Status den 22 november 2026, beräknad från den aktuella Core-exporten och det
validerade Home Assistant-minnet.

| Mått | Antal |
| --- | ---: |
| Poster i Core-exporten | 75 106 |
| Poster i validerad Core-TMX | 3 483 |
| Konservativt återstående omfång | 71 623 |

Det återstående antalet är konservativt: utöver TMX-posterna finns
livegranskade strängar utan ny TMX-post, exempelvis hela komponenter där inga
ändringar behövdes. En TMX-post betyder att texten har en spårbar, verifierad
källa; den är inte en generell markering att en hel komponent eller Core som
helhet är klar.

Senast liveverifierade undergrupper: Media Source, Mailbox, UpCloud, Coronavirus, Duke Energy,
Möhlenhoff Alpha2, Sky Remote, Tilt BLE, TriggerCMD,
Template-maskinidentifierare,
Bayesian-resultatvärden och komponenterna Launch Library, Nissan Leaf, RPi
Power, Sensirion BLE, ThermoPro, ThermoBeacon, Input Button, Mold Indicator,
Harman Luxury, Linear Garage Door, SwitchBee, NextBus, Streamlabs Water,
RTSPtoWebRTC, NMBS, Home+ Control, RuuviTag BLE, SensorPro, Modem Caller ID,
Sanix, SenseME, Sunricher DALI Center, Channels och Rympro. Sparade ändringar
har lästs tillbaka via Lokalise API och de senaste TMX-posterna har
validerats i `swedish-tm`. Senast rättades Modern Forms två sensor-etiketter
till den konsekventa termen `insomningstid`. Green Planet Energys
elprisrad förfinades senast till den naturliga sammansättningen
`elprisintegration`.

Keymitt BLE har nu granskats rad för rad (22 liveåterlästa strängar). Samtliga
var korrekta; de är tillagda i det validerade TMX-minnet med spårbar
Lokalise-manifestfil.

IAMMETER har nu granskats rad för rad (21 liveåterlästa strängar). Tre etiketter
har rättats från den felaktiga uppdelningen `Import Energi A–C` till
`Importerad energi A–C`; den validerade TMX-posten är sparad med en spårbar
Lokalise-manifestfil.

Dune HD har nu granskats rad för rad (sju liveåterlästa strängar). Samtliga
var korrekta och har lagts till i det validerade TMX-minnet med en spårbar
Lokalise-manifestfil.

Ingen verktygsrelease publicerades efter dagens tidigare release, enligt
arbetsregeln om högst en release per dag.
