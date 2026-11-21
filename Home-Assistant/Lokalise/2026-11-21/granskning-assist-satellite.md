# Home Assistant Core – Assist Satellite

Datum: 2026-11-21  
Källa: Core `2fdaa177`, `homeassistant/components/assist_satellite/strings.json`, tidigare rapporter och Lokalise API med direkt återläsning.

Status: samtliga 84 aktuella bladsträngar och referensmål i Core-källan är radgranskade. Tjugofem korrigeringar är sparade och återlästa.

| Nyckelgrupp | Sparad text | Motivering |
|---|---|---|
| `entity_component::_::name`, `title` | `Assist-satellit` | Korrekt svensk sammansättning. |
| `*::preannounce_media_id::name` | `Media-ID för förannonsering` | Korrekt svensk fältetikett i samtliga tre tjänster. |
| `common::trigger_for_name`, `common::condition_for_name` | `I minst` | Korrigerar den felaktiga frasen *I åtminstone*. |
| `services::ask_question` | `Låter en Assist-satellit ställa en fråga och ta emot användarens svar.`; `Ställ en fråga på satelliten` | Tydligare svensk tjänstetext. |
| `services::ask_question::fields::*` | `Den Assist-satellitentitet som frågan ska ställas på.`; `Frågans media-ID som ska användas i stället för text-till-tal.` | Rätt preposition, sammansättning och skrivregel för *i stället*. |
| `common::trigger_behavior_description` | `Det beteende hos de valda Assist-satelliterna som ska utlösa villkoret.` | Ersätter det oidiomatiska verbet *trigga*. |
| `services::*::preannounce*`, `start_media_id` | `… i stället för …`; `… eller mediet.` | Korrigerar skrivregeln *i stället* och bestämd form. |
| `conditions::is_*::name` | `Satelliten är inaktiv`; `Satelliten lyssnar`; `Satelliten bearbetar`; `Satelliten svarar` | Fullständiga svenska villkorsnamn. |
| `exceptions::tts_engine_not_found` | `Text-till-tal-motorn {engine} hittades inte.` | Korrekt teknisk sammansättning och platshållare. |
| `services::announce::name`, `services::start_conversation::name` | `Spela upp på satelliten`; `Starta en konversation på satelliten` | Fullständiga svenska tjänstetitlar. |
| `common::condition_behavior_name` | `Villkoret uppfylls om` | Tydlig och korrekt villkorsetiktett. |

Villkor, utlösare, tjänster, undantag och referensmål är nu kontrollerade. De 19 äldre Lokalise-poster som inte längre finns i den aktuella Core-källan ingår inte i komponentens färdiga omfattning. TMX-ledgern är uppdaterad och validerad (1 754 poster).
