# Home Assistant Core — granskning sida 467 (Workday och Wyoming)

Datum: 2026-11-20  
Status: sparat i Lokalise 2026-11-20

Workday-källtexten kontrollerades mot `homeassistant/components/workday/strings.json` och Wyoming-källtexten mot `homeassistant/components/wyoming/strings.json` på Home Assistant Cores `dev`-gren.

| Fullständig nyckel | Befintlig svenska | Föreslagen svenska | Motivering |
|---|---|---|---|
| `component::wyoming::config::abort::no_services` | `Inga tjänster hittades vid slutpunkten` | `Inga tjänster hittades på slutpunkten` | ”På slutpunkten” är den naturliga svenska prepositionen för ett nätverksändpunkt i denna feltext. |

Övriga 19 nycklar på sidan granskades utan dokumenterat ändringsförslag. Femton Workday-nycklar är direkta referenser och ändras inte lokalt. `component::workday::selector::province::options::none` behålls som `Ingen landsdel`, eftersom källans överordnade val på samma sida är översatt med `Landsdel` och en ändring skulle kräva en samordnad terminologigranskning.