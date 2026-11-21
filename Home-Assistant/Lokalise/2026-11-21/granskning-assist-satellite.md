# Home Assistant Core – Assist Satellite

Datum: 2026-11-21  
Källa: Core `2fdaa177`, `homeassistant/components/assist_satellite/strings.json`, tidigare rapporter och Lokalise API med direkt återläsning.

Status: pågående radgranskning av 103 aktuella Lokalise-poster. Sju korrigeringar är sparade och återlästa.

| Nyckelgrupp | Sparad text | Motivering |
|---|---|---|
| `entity_component::_::name`, `title` | `Assist-satellit` | Korrekt svensk sammansättning. |
| `*::preannounce_media_id::name` | `Media-ID för förannonsering` | Korrekt svensk fältetikett i samtliga tre tjänster. |
| `common::trigger_for_name`, `common::condition_for_name` | `I minst` | Korrigerar den felaktiga frasen *I åtminstone*. |

Nuvarande villkor, utlösare, tjänster, undantag och referensmål är under fortsatt radgranskning. TMX-ledgern är uppdaterad och validerad (1 736 poster).
