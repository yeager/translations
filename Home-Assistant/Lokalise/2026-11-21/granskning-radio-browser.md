# Home Assistant Core – Radio Browser

Datum: 2026-11-21  
Källa: aktuell Core `2fdaa177`, `homeassistant/components/radio_browser/strings.json`  
Status: sju aktuella strängar granskade; två ändringar är sparade och återlästa.

Fem undantagsmeddelanden är språkligt korrekta. Två korrigeringar har
identifierats:

| Nyckel | Befintlig svensk text | Föreslagen svensk text | Motivering |
| --- | --- | --- | --- |
| `config::error::cannot_connect` | `Anslutningen misslyckades` | `Det gick inte att ansluta` | Aktuell Lokalise återläst 2026-11-21; den semantiskt korrekta gemensamma måltexten används som direkt måltext. |
| `config::step::user::description` | `Vill du lägga till Radio Browser till Home Assistant?` | `Vill du lägga till Radio Browser i Home Assistant?` | Sparad och återläst i Lokalise 2026-11-21. Idiomatisk svensk preposition för att lägga till en integration i produkten. Produktnamnet bevaras exakt som `Home Assistant`. |

Ingen ytterligare korrigering behövs. Båda måltexterna är API-verifierade med
Lokalise-ID `9917708619` respektive `1139463530` och ingår i det kanoniska
TMX-minnet.
