# Home Assistant Core — granskning sida 483 (DSMR, ONVIF, YaleXSBLE och Roborock)

Datum: 2026-11-20  
Status: sparat i Lokalise 2026-11-20

DSMR-källtexten kontrollerades mot `homeassistant/components/dsmr/strings.json` på Home Assistant Cores `dev`-gren. Förslagen följer den redan korrekta formuleringen `Spänningsökning i fas L1–L3` på samma sida.

| Fullständig nyckel | Befintlig svenska | Föreslagen svenska | Motivering |
|---|---|---|---|
| `component::dsmr::entity::sensor::instantaneous_current_l2::name` | `Ström fas L2` | `Ström i fas L2` | Naturlig svensk fasangivelse och konsekvens med föregående DSMR-sida. |
| `component::dsmr::entity::sensor::instantaneous_current_l3::name` | `Ström fas L3` | `Ström i fas L3` | Naturlig svensk fasangivelse och konsekvens med föregående DSMR-sida. |
| `component::dsmr::entity::sensor::instantaneous_voltage_l1::name` | `Spänning fas L1` | `Spänning i fas L1` | Naturlig svensk fasangivelse. |
| `component::dsmr::entity::sensor::instantaneous_voltage_l2::name` | `Spänning fas L2` | `Spänning i fas L2` | Naturlig svensk fasangivelse. |
| `component::dsmr::entity::sensor::instantaneous_voltage_l3::name` | `Spänning fas L3` | `Spänning i fas L3` | Naturlig svensk fasangivelse. |
| `component::dsmr::entity::sensor::voltage_sag_l1_count::name` | `Spänningsfall fas L1` | `Spänningsfall i fas L1` | Naturlig svensk fasangivelse och konsekvens med spänningsökning. |
| `component::dsmr::entity::sensor::voltage_sag_l2_count::name` | `Spänningsfall fas L2` | `Spänningsfall i fas L2` | Naturlig svensk fasangivelse och konsekvens med spänningsökning. |
| `component::dsmr::entity::sensor::voltage_sag_l3_count::name` | `Spänningsfall fas L3` | `Spänningsfall i fas L3` | Naturlig svensk fasangivelse och konsekvens med spänningsökning. |

## Uppföljning

YaleXSBLE:s `always_connected` har värdet `Alltid ansluten`, men beskrivningen talar om låset och ett läge. Kontrollera den faktiska inställningsvyn innan eventuell ändring till exempelvis `Alltid anslutet` eller en omformulering med ”läget”.

Övriga 12 nycklar på sidan granskades utan dokumenterat ändringsförslag. ONVIF-webhooks, UpCloud-referensen, Roborocks `Snabb` och DSMR:s avbrotts- och maxvärdesbenämningar bevaras.