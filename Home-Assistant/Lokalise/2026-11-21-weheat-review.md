# Home Assistant Core – Weheat

Datum: 2026-11-21

Alla 134 Weheat-strängar har granskats mot aktuell källa och tidigare granskningsunderlag. Fyra fel är rättade, sparade och API-återlästa.

| Nyckel | Sparad svenska | Motivering |
| --- | --- | --- |
| `entity::sensor::energy_output_cooling::name` | `Avgiven energi för kylning` | Källan avser energiutbyte, inte elförbrukning. |
| `entity::sensor::energy_output_defrost::name` | `Avgiven energi för avfrostning` | Källan avser energiutbyte, inte elförbrukning. |
| `entity::sensor::energy_output_dhw::name` | `Avgiven energi för varmvatten` | Källan avser energiutbyte, inte elförbrukning. |
| `entity::sensor::energy_output_heating::name` | `Avgiven energi för uppvärmning` | Källan avser energiutbyte, inte elförbrukning. |

Övriga konfigurations-, värmepumps- och kylstatussträngar är korrekta. Tidigare motiverade bedömningar i backupen har beaktats för att undvika dubbelarbete.
