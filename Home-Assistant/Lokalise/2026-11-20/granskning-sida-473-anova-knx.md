# Home Assistant Core — granskning sida 473 (Hass.io, Anova och KNX)

Datum: 2026-11-20  
Status: sparat i Lokalise 2026-11-20

Anova-källtexten kontrollerades mot `homeassistant/components/anova/strings.json` på Home Assistant Cores `dev`-gren.

| Fullständig nyckel | Befintlig svenska | Föreslagen svenska | Motivering |
|---|---|---|---|
| `component::anova::entity::sensor::cook_time_remaining::name` | `Tillagningstid återstår` | `Återstående tillagningstid` | Sensorbenämningen ska vara en nominalfras, inte en ofullständig sats. |
| `component::anova::entity::sensor::triac_temperature::name` | `Triac temperatur` | `Triac-temperatur` | Bindestreck gör den tekniska sammansättningen tydlig på svenska. |

Övriga 18 nycklar på sidan granskades utan dokumenterat ändringsförslag. Fem Anova-nycklar och en KNX-nyckel är direkta referenser; övriga sensor- och anslutningsnamn är sakligt korrekta.