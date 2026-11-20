# Home Assistant Core — granskning sida 471 (AccuWeather, NextDNS och Person)

Datum: 2026-11-20  
Status: sparat i Lokalise 2026-11-20

NextDNS-källtexten kontrollerades mot `homeassistant/components/nextdns/strings.json` på Home Assistant Cores `dev`-gren.

| Fullständig nyckel | Befintlig svenska | Föreslagen svenska | Motivering |
|---|---|---|---|
| `component::nextdns::entity::switch::block_playstation_network::name` | `Blockera Playstation Network (PSN)` | `Blockera PlayStation Network` | Varumärket skrivs `PlayStation` med stort S. Förkortningen finns inte i källtexten och tillför ingen nödvändig information i enhetsnamnet. |

Övriga 19 nycklar på sidan granskades utan dokumenterat ändringsförslag. Sju AccuWeather-nycklar och tre Person-attribut är direkta referenser. Övriga NextDNS-namn använder korrekta varumärken och konsekvent imperativ form.