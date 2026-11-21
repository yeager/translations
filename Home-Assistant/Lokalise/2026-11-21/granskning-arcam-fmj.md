# Home Assistant Core – Arcam FMJ

Datum: 2026-11-21  
Källa: Core `2fdaa177`, `homeassistant/components/arcam_fmj/strings.json`, tidigare rapporter och Lokalise API med direkt återläsning.

Status: pågående radgranskning av 108 aktuella Lokalise-poster. Fyra korrigeringar är sparade och återlästa.

| Nyckel | Sparad text | Motivering |
|---|---|---|
| `config::step::confirm::description` | `Vill du lägga till Arcam FMJ på `{host}` i Home Assistant?` | Rätt svensk preposition; kodmarkeringen och produktnamnet är bevarade. |
| `entity::sensor::incoming_audio_config::state::undetected` | `Inte upptäckt` | Idiomatisk status i stället för den otympliga formen *oupptäckt*. |
| `entity::sensor::incoming_audio_format::state::undetected` | `Inte upptäckt` | Samma status ska ha samma svenska formulering. |
| `config::error::connection_refused` | `Värden avvisade anslutningen` | Korrekt svensk satsstruktur. |

Ljudformaten Dolby, DTS, Auro, PCM, LFE och kanalnotationerna har lämnats tekniskt oförändrade. Resterande sensor- och undantagssträngar fortsätter granskas rad för rad. TMX-ledgern är uppdaterad och validerad (1 729 poster).
