# Home Assistant Core: kompletterande kontroll av Matter

Kontrollerat i Lokalise den 19 november 2026. Inga ändringar gjorda i Lokalise. De tre mellanliggande nycklarna och de gemensamma referensmålen kontrollerades därefter i Lokalise. Nästa nyckel i den tidigare dokumenterade ordningen är ID 653073959; jämför alltid med aktuell ordning.

| Fullständig nyckel | Engelska i Lokalise | Svenska i Lokalise | Bedömning |
|---|---|---|---|
| `component::matter::entity::sensor::esa_state::state::fault` | [%key:common::state::fault%] | [%key:common::state::fault%] | Behåll referensen. Målet har källtexten ”Fault” och svenska ”Fel”. |
| `component::matter::entity::sensor::esa_state::name` | Appliance energy state | Apparatens energistatus | Behåll. |
| `component::matter::entity::select::door_lock_sound_volume::state::silent` | Silent | Tyst | Behåll. |
| `component::matter::entity::select::door_lock_sound_volume::state::medium` | [%key:common::state::medium%] | [%key:common::state::medium%] | Behåll referensen; målet är ”Medium” → ”Medel”. |
| `component::matter::entity::select::door_lock_sound_volume::state::low` | [%key:common::state::low%] | [%key:common::state::low%] | Behåll referensen; målet är ”Low” → ”Låg”. |
| `component::matter::entity::select::door_lock_sound_volume::state::high` | [%key:common::state::high%] | [%key:common::state::high%] | Behåll referensen; målet är ”High” → ”Hög”. |
| `component::matter::entity::select::door_lock_sound_volume::name` | Sound volume | Ljudvolym | Behåll. |
| `component::matter::entity::sensor::window_covering_target_position::name` | Target opening position | Målöppningsposition | Föreslå: Målposition för öppning. Tydligare sammansättning. |
| `component::matter::entity::sensor::min_pin_code_length::name` | Min PIN code length | Minsta längd på PIN-kod | Behåll. |
| `component::matter::entity::sensor::max_pin_code_length::name` | Max PIN code length | Maximal längd på PIN-kod | Föreslå: Största längd på PIN-kod. Ger ett konsekvent par med ”minsta”. |
