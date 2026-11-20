# Home Assistant Core — granskning sida 468 (Roborock, Wyoming och Waze Travel Time)

Datum: 2026-11-20  
Status: dokumenterade förslag; **inte sparade i Lokalise**

Roborock-källtexten kontrollerades mot `homeassistant/components/roborock/strings.json` på Home Assistant Cores `dev`-gren.

| Fullständig nyckel | Befintlig svenska | Föreslagen svenska | Motivering |
|---|---|---|---|
| `component::roborock::config::step::code::data::code` | `Verifierings kod` | `Verifieringskod` | Svensk sammansättning skrivs ihop. |
| `component::roborock::config::step::code::description` | `Ange verifieringskoden som skickas till din e-post` | `Ange verifieringskoden som skickades till din e-postadress` | Koden har redan levererats när användaren ska ange den; förslaget använder korrekt tempus och den fullständiga termen ”e-postadress”. |

Övriga 18 nycklar på sidan granskades utan dokumenterat ändringsförslag. Fem nycklar är direkta referenser. Alternativen `Imperiskt` och `Metriskt` behålls: de är korta och passar som val under enhetsväljaren.