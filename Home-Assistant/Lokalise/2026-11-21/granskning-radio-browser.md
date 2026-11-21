# Home Assistant Core – Radio Browser

Datum: 2026-11-21  
Källa: aktuell Core `2fdaa177`, `homeassistant/components/radio_browser/strings.json`  
Status: sju aktuella strängar granskade; två ändringsförslag väntar på sparning i Lokalise.

Fem undantagsmeddelanden är språkligt korrekta. Två korrigeringar har
identifierats:

| Nyckel | Befintlig svensk text | Föreslagen svensk text | Motivering |
| --- | --- | --- | --- |
| `config::error::cannot_connect` | `Anslutningen misslyckades` | `[%key:common::config_flow::error::cannot_connect%]` | Källan är en obligatorisk Lokalise-referens, inte en fristående engelsk text. Den nuvarande måltexten ger QA-fel och bryter arv från common. |
| `config::step::user::description` | `Vill du lägga till Radio Browser till Home Assistant?` | `Vill du lägga till Radio Browser i Home Assistant?` | Idiomatisk svensk preposition för att lägga till en integration i produkten. Produktnamnet bevaras exakt som `Home Assistant`. |

Förslagen är inte sparade och därför inte tillagda i TMX-minnet.
