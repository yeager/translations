# Home Assistant Core – WeatherFlow

Datum: 2026-11-21

Alla 33 WeatherFlow-strängar har granskats mot aktuell källa och tidigare granskningsunderlag. Sex fel är rättade, sparade och API-återlästa.

| Nyckel | Sparad svenska | Motivering |
| --- | --- | --- |
| `entity::sensor::lightning_average_distance::name` | `Genomsnittligt avstånd till blixtar` | Rätt preposition för avståndet till det observerade fenomenet. |
| `entity::sensor::wet_bulb_temperature::name` | `Våtkulbstemperatur` | Etablerad meteorologisk fackterm. |
| `entity::event::precip_start_event::name` | `Nederbördsstart` | Kort, korrekt händelseetikett. |
| `entity::sensor::lightning_strike_last_distance::name` | `Avstånd till senaste blixtnedslag` | Tidigare ofullständig ordställning har rättats. |
| `entity::sensor::lightning_strike_last_energy::name` | `Energi vid senaste blixtnedslag` | Tidigare ofullständig ordställning har rättats. |
| `entity::sensor::lightning_strike_last_epoch::name` | `Senaste blixtnedslag` | Tydlig och naturlig svensk etikett. |

Övriga konfigurations-, sensor- och tillståndssträngar är korrekta.
