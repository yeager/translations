# Rättelse: Kiosker Blackout

Datum: 2026-11-23. En komponentgranskning efter den första etikettkorrigeringen visade att Kiosker använder *blackout* för sin appstyrda mörkläggningsskärm, inte för avbrott i elförsörjningen. Den tidigare formuleringen `Strömavbrott` skulle därför ha ändrat funktionens betydelse och har ersatts direkt.

| Fullständig nyckel | Felaktig mellanversion | Sparad svenska | Motivering |
| --- | --- | --- | --- |
| `component::kiosker::entity::binary_sensor::blackout_state::name` | `Strömavbrott` | `Mörkläggningsläge` | Sensorstatusen gäller om appens blackout-/mörkläggningsläge visas. |

Homee-nyckeln `component::homee::entity::binary_sensor::blackout_alarm::name` avser däremot ett verkligt strömavbrott och behåller `Strömavbrott`.

Rättelsen sparades via Lokalise API, lästes tillbaka och ersatte den tidigare live-posten i den kanoniska Home Assistant-TMX:en.
