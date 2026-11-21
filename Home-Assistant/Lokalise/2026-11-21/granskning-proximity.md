# Home Assistant Core – Proximity

Datum: 2026-11-21  
Status: samtliga aktuella bladnycklar är radgranskade mot Core `2fdaa177` och Lokalise.

| Nyckel | Källa | Svenska | Bedömning |
| --- | --- | --- | --- |
| `component::proximity::title` | Proximity | Närhet | Verifierad i Lokalise (ID `42081257`). |
| `component::proximity::config::abort::success` | Changes saved | Ändringar sparade | Verifierad i Lokalise (ID `437680439`). |
| `component::proximity::config::step::user::data::ignored_zones` | Zones to ignore | Zoner som ska ignoreras | Verifierad i Lokalise (ID `437680441`). |
| `component::proximity::config::step::user::data::tolerance` | Tolerance distance | Toleransavstånd | Verifierad i Lokalise (ID `437680442`). |
| `component::proximity::config::step::user::data::tracked_entities` | Devices or persons to track | Enheter eller personer att spåra | Verifierad i Lokalise (ID `437680443`). |
| `component::proximity::config::step::user::data::zone` | Zone to track distance to | Zon att mäta avstånd till | Verifierad i Lokalise (ID `437680444`). |
| `component::proximity::issues::tracked_entity_removed::title` | Tracked entity has been removed | Den spårade entiteten har tagits bort | Verifierad i Lokalise (ID `437680447`). |
| `component::proximity::issues::tracked_entity_removed::fix_flow::step::confirm::description` | The entity `{entity_id}` has been removed from Home Assistant, but is used in proximity {name}. Please remove `{entity_id}` from the list of tracked entities. Related proximity sensor entities were set to unavailable and can be removed. | Entiteten `{entity_id}` har tagits bort från Home Assistant, men används i närheten av {name}. Ta bort `{entity_id}` från listan över spårade entiteter. Relaterade entiteter för närhetssensorer har satts till otillgängliga och kan tas bort. | Sparad och återläst i Lokalise (nyckel-ID `437680445`, översättnings-ID `3488060358`). Produktnamnet, båda platshållarna och backtick-markeringen är bevarade. |
| `component::proximity::entity::sensor::dir_of_travel::{name,state::arrived,state::away_from,state::stationary,state::towards}` | `{tracked_entity} direction of travel`; Arrived; Away from; Stationary; Towards | `{tracked_entity} färdriktning`; Anlände; Bort från; Stilla; På väg mot | Verifierade i Lokalise (ID `434249154`–`434249158`); platshållaren är intakt. |
| `component::proximity::entity::sensor::{dist_to_zone::name,nearest::name,nearest_dir_of_travel::name,nearest_dist_to_zone::name}` | `{tracked_entity} distance`; Nearest device; Nearest direction of travel; Nearest distance | `{tracked_entity} avstånd`; Närmaste enhet; Närmaste färdriktning; Närmaste avstånd | Verifierade i Lokalise (ID `439012799`, `434249159`, `439012800`, `439012805`). |

## Referenser

- `config::abort::already_configured`, `config::flow_title`, samtliga `options::step::init::data` och `nearest_dir_of_travel`-tillstånd är korrekta referenser.
- `issues::tracked_entity_removed::fix_flow::step::confirm::title` refererar korrekt till ärendets titel.
