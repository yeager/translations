# Home Assistant Core – Arcam FMJ

Datum: 2026-11-21  
Källa: Core `2fdaa177`, `homeassistant/components/arcam_fmj/strings.json`, tidigare rapporter och Lokalise API med direkt återläsning.

Status: samtliga 106 aktuella bladsträngar och referensmål är radgranskade. Fyra korrigeringar är sparade och återlästa.

| Nyckel | Sparad text | Motivering |
|---|---|---|
| `config::step::confirm::description` | `Vill du lägga till Arcam FMJ på `{host}` i Home Assistant?` | Rätt svensk preposition; kodmarkeringen och produktnamnet är bevarade. |
| `entity::sensor::incoming_audio_config::state::undetected` | `Inte upptäckt` | Idiomatisk status i stället för den otympliga formen *oupptäckt*. |
| `entity::sensor::incoming_audio_format::state::undetected` | `Inte upptäckt` | Samma status ska ha samma svenska formulering. |
| `config::error::connection_refused` | `Värden avvisade anslutningen` | Korrekt svensk satsstruktur. |

Ljudformaten Dolby, DTS, Auro, PCM, LFE och kanalnotationerna har lämnats tekniskt oförändrade. Återstående sensor- och undantagstext är korrekt; två äldre Lokalise-poster förekommer inte längre i den aktuella Core-källan. TMX-ledgern är uppdaterad och validerad (1 729 poster).
