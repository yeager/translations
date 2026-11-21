# Home Assistant Core – Aurora

Datum: 2026-11-21  
Källa: Core `2fdaa177`, `homeassistant/components/aurora/strings.json`, tidigare granskningsunderlag och Lokalise API med direkt återläsning.

Status: samtliga 6 aktuella bladsträngar och referensmål i Core-källan är radgranskade. En korrigering är sparad och återläst.

| Fullständig nyckel | Befintlig text | Sparad text | Motivering |
|---|---|---|---|
| `component::aurora::entity::binary_sensor::visibility_alert::name` | `Synlighetslarm` | `Synlighetsvarning` | Återger *alert* med den svenska varningstermen i stället för ett tekniskt larm. |

`NOAA norrskenssensor`, `Synlighet`, `Tröskelvärde (%)` samt gemensamma anslutnings- och platsreferenser är korrekta. Fem äldre Lokalise-poster för tidigare konfigurationsfält finns inte längre i källfilen och omfattas inte av den aktuella granskningen. TMX-ledgern har uppdaterats med den återlästa posten.
