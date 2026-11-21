# Home Assistant Core – YouLess

Datum: 2026-11-21

Alla 24 YouLess-strängar har granskats mot aktuell källa. Tre sensorbenämningar är korrigerade, sparade och API-återlästa.

| Nyckel | Tidigare svenska | Sparad svenska |
| --- | --- | --- |
| `entity::sensor::active_current_phase_a::name` | `Ström fas {phase}` | `Strömfas {phase}` |
| `entity::sensor::active_power_phase_w::name` | `Effekt fas {phase}` | `Effektfas {phase}` |
| `entity::sensor::active_voltage_phase_v::name` | `Spänning fas {phase}` | `Spänningsfas {phase}` |

Svenska sammansättningar har rättats utan att ändra platshållaren `{phase}`. Övriga mätar- och tarifftexter är korrekta.
