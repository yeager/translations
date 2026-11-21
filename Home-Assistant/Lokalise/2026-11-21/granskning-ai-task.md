# Home Assistant Core – AI Task

Datum: 2026-11-21  
Källa: Core `2fdaa177`, `homeassistant/components/ai_task/strings.json`, aktuell Lokalise-export.

Status: pågående radgranskning. Två tydliga korrigeringar är sparade och återlästa.

| Nyckel | Svenska efter granskning | Motivering |
| --- | --- | --- |
| `component::ai_task::services::generate_image::description` | Använder AI för att generera en bild. | Källan avser en bild i singular; tidigare måltext använde felaktigt plural. Lokalise-ID `701747105`. |
| `component::ai_task::services::generate_data::fields::structure::description` | Om den är inställd matar AI-uppgiften ut fält med den här strukturen. Strukturen är en ordbok … | Rättar oöversatta `dictionary` och oidiomatisk ordföljd. De schemafältsnamn som ska vara bokstavliga bevaras. Lokalise-ID `675492529`. |

Aktuella undantag, tjänster och respektive entitets-ID-fält fortsätter granskas radvis. Äldre `generate_text`-poster hålls åtskilda eftersom de saknas i aktuell källfil.
