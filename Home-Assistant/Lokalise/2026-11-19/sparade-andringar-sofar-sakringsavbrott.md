# Rättade Sofar-säkringsfel

Kontrollerade och återlästa via Lokalise API i Home Assistant Core 2026-11-19. Fjorton feltexter hade förskjutna sträng- eller säkringsnummer. Båda texterna för sträng 8 var redan korrekta och behölls. Tabellen visar faktiska värden före ändringen och efter återläsning.

| Nyckel | Engelska | Tidigare svenska | Sparad svenska |
| --- | --- | --- | --- |
| `component::sofar::entity::event::fault::state_attributes::event_type::state::string_fuse_open_circuit_1_1` | String 1 fuse 1 open circuit | Avbrott i säkring 2 för sträng 1 | Avbrott i säkring 1 för sträng 1 |
| `component::sofar::entity::event::fault::state_attributes::event_type::state::string_fuse_open_circuit_1_2` | String 1 fuse 2 open circuit | Avbrott i säkring 1 för sträng 2 | Avbrott i säkring 2 för sträng 1 |
| `component::sofar::entity::event::fault::state_attributes::event_type::state::string_fuse_open_circuit_2_1` | String 2 fuse 1 open circuit | Avbrott i säkring 2 för sträng 2 | Avbrott i säkring 1 för sträng 2 |
| `component::sofar::entity::event::fault::state_attributes::event_type::state::string_fuse_open_circuit_2_2` | String 2 fuse 2 open circuit | Avbrott i säkring 1 för sträng 3 | Avbrott i säkring 2 för sträng 2 |
| `component::sofar::entity::event::fault::state_attributes::event_type::state::string_fuse_open_circuit_3_1` | String 3 fuse 1 open circuit | Avbrott i säkring 2 för sträng 3 | Avbrott i säkring 1 för sträng 3 |
| `component::sofar::entity::event::fault::state_attributes::event_type::state::string_fuse_open_circuit_3_2` | String 3 fuse 2 open circuit | Avbrott i säkring 1 för sträng 4 | Avbrott i säkring 2 för sträng 3 |
| `component::sofar::entity::event::fault::state_attributes::event_type::state::string_fuse_open_circuit_4_1` | String 4 fuse 1 open circuit | Avbrott i säkring 2 för sträng 4 | Avbrott i säkring 1 för sträng 4 |
| `component::sofar::entity::event::fault::state_attributes::event_type::state::string_fuse_open_circuit_4_2` | String 4 fuse 2 open circuit | Avbrott i säkring 1 för sträng 5 | Avbrott i säkring 2 för sträng 4 |
| `component::sofar::entity::event::fault::state_attributes::event_type::state::string_fuse_open_circuit_5_1` | String 5 fuse 1 open circuit | Avbrott i säkring 2 för sträng 5 | Avbrott i säkring 1 för sträng 5 |
| `component::sofar::entity::event::fault::state_attributes::event_type::state::string_fuse_open_circuit_5_2` | String 5 fuse 2 open circuit | Avbrott i säkring 1 för sträng 6 | Avbrott i säkring 2 för sträng 5 |
| `component::sofar::entity::event::fault::state_attributes::event_type::state::string_fuse_open_circuit_6_1` | String 6 fuse 1 open circuit | Avbrott i säkring 2 för sträng 6 | Avbrott i säkring 1 för sträng 6 |
| `component::sofar::entity::event::fault::state_attributes::event_type::state::string_fuse_open_circuit_6_2` | String 6 fuse 2 open circuit | Avbrott i säkring 1 för sträng 7 | Avbrott i säkring 2 för sträng 6 |
| `component::sofar::entity::event::fault::state_attributes::event_type::state::string_fuse_open_circuit_7_1` | String 7 fuse 1 open circuit | Avbrott i säkring 2 för sträng 7 | Avbrott i säkring 1 för sträng 7 |
| `component::sofar::entity::event::fault::state_attributes::event_type::state::string_fuse_open_circuit_7_2` | String 7 fuse 2 open circuit | Avbrott i säkring 1 för sträng 8 | Avbrott i säkring 2 för sträng 7 |
