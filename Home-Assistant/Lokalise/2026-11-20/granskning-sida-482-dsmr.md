# Home Assistant Core — granskning sida 482 (Luftfuktare och DSMR)

Datum: 2026-11-20  
Status: dokumenterade förslag; **inte sparade i Lokalise**

DSMR-källtexten kontrollerades mot `homeassistant/components/dsmr/strings.json` på Home Assistant Cores `dev`-gren. Ingen av de berörda nycklarna finns i tidigare DSMR-rapporter i `yeager/translations`.

| Fullständig nyckel | Befintlig svenska | Föreslagen svenska | Motivering |
|---|---|---|---|
| `component::dsmr::entity::sensor::current_electricity_delivery::name` | `Energiproduktion` | `Effektproduktion` | Källans ”Power production” avser momentan effekt, inte ackumulerad energi. |
| `component::dsmr::entity::sensor::instantaneous_active_power_l1_negative::name` | `Kraftproduktion fas L1` | `Effektproduktion fas L1` | Elektrisk ”power” är effekt; ”kraft” har fel fysisk betydelse här. |
| `component::dsmr::entity::sensor::instantaneous_active_power_l1_positive::name` | `Strömförbrukning fas L1` | `Effektförbrukning fas L1` | Källans ”power consumption” är effektförbrukning, inte elektrisk ström. |
| `component::dsmr::entity::sensor::instantaneous_active_power_l2_negative::name` | `Kraftproduktion fas L2` | `Effektproduktion fas L2` | Elektrisk ”power” är effekt; ”kraft” har fel fysisk betydelse här. |
| `component::dsmr::entity::sensor::instantaneous_active_power_l2_positive::name` | `Strömförbrukning fas L2` | `Effektförbrukning fas L2` | Källans ”power consumption” är effektförbrukning, inte elektrisk ström. |
| `component::dsmr::entity::sensor::instantaneous_active_power_l3_negative::name` | `Kraftproduktion fas L3` | `Effektproduktion fas L3` | Elektrisk ”power” är effekt; ”kraft” har fel fysisk betydelse här. |
| `component::dsmr::entity::sensor::instantaneous_active_power_l3_positive::name` | `Strömförbrukning fas L3` | `Effektförbrukning fas L3` | Källans ”power consumption” är effektförbrukning, inte elektrisk ström. |
| `component::dsmr::entity::sensor::instantaneous_current_l1::name` | `Ström fas L1` | `Ström i fas L1` | Prepositionen behövs för en naturlig svensk fasangivelse. |

Övriga 12 nycklar på sidan granskades utan dokumenterat ändringsförslag. `Sömnläge`, tariffnamn, energi- och gasförbrukning är sakligt och terminologiskt korrekta.
