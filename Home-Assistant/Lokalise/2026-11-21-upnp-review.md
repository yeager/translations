# Home Assistant Core – UPnP/IGD

Datum: 2026-11-21

Samtliga 28 UPnP/IGD-strängar har kontrollerats mot aktuell källa och tidigare granskningsrapport. Två sensornamn rättades, sparades och återlästes via Lokalise API.

| Nyckel | Tidigare svenska | Sparad svenska | Motivering |
| --- | --- | --- | --- |
| `component::upnp::entity::sensor::data_received::name` | `Data mottaget` | `Mottagen data` | Korrekt kongruens och naturlig svensk etikett. |
| `component::upnp::entity::sensor::data_sent::name` | `Data skickat` | `Skickade data` | Korrekt kongruens och naturlig svensk etikett. |

Övriga strängar, inklusive tidigare dokumenterade undantag, är korrekta. Variablerna `{location}`, `{device_url}` och `{usn}` är oförändrade.
