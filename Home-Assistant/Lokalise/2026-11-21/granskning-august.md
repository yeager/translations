# Home Assistant Core – August

Datum: 2026-11-21  
Källa: Core `2fdaa177`, `homeassistant/components/august/strings.json`, tidigare granskningsunderlag och Lokalise API med direkt återläsning.

Status: samtliga 18 aktuella bladsträngar och referensmål i Core-källan är radgranskade. Två korrigeringar är sparade och återlästa.

| Fullständig nyckel | Befintlig text | Sparad text | Motivering |
|---|---|---|---|
| `component::august::entity::binary_sensor::image_capture::name` | `Ta bild` | `Bildtagning` | Källan är en sensorbenämning, inte en uppmaning. |
| `component::august::entity::button::wake::name` | `Vakna` | `Väck` | Knappen väcker enheten; den svenska imperativformen är *Väck*. |

OAuth2-referenserna, kontokontrollerna och Yale-migreringsinformationen är korrekta. Länken och platshållaren `{migrate_url}` är bevarade. De 27 äldre Lokalise-poster som tillhör borttagna inloggningsflöden ingår inte i den aktuella Core-källans omfattning.

TMX-ledgern har uppdaterats med båda återlästa Lokalise-posterna.
