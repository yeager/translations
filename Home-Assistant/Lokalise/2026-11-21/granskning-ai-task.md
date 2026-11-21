# Home Assistant Core – AI Task

Datum: 2026-11-21  
Källa: Core `2fdaa177`, `homeassistant/components/ai_task/strings.json`, aktuell Lokalise-export.

Status: samtliga aktuella bladnycklar i Core `2fdaa177` är radgranskade. Sju korrigeringar är sparade och återlästa.

| Nyckel | Svenska efter granskning | Motivering |
| --- | --- | --- |
| `component::ai_task::services::generate_image::description` | Använder AI för att generera en bild. | Källan avser en bild i singular; tidigare måltext använde felaktigt plural. Lokalise-ID `701747105`. |
| `component::ai_task::services::generate_data::fields::structure::description` | Om den är inställd matar AI-uppgiften ut fält med den här strukturen. Strukturen är en ordbok … | Rättar oöversatta `dictionary` och oidiomatisk ordföljd. De schemafältsnamn som ska vara bokstavliga bevaras. Lokalise-ID `675492529`. |
| `component::ai_task::exceptions::{attachments_not_supported,entity_not_found,evaluate_not_supported,generate_data_not_supported,generate_image_not_supported}` | AI-uppgiftsentiteten `{entity_id}` … | Gör benämningen konsekvent med komponenttiteln `AI-uppgift`; samtliga `{entity_id}` är bevarade. Lokalise-ID `954271059`, `954271060`, `954271062`–`954271064`. |

Tjänsterna för rensning, utvärdering, data- och bildgenerering samt aktuella undantag är granskade. Äldre `generate_text`-poster hålls åtskilda eftersom de saknas i aktuell källfil.
