# Home Assistant Core — granskning sida 476 (Roborock, Prosegur, Elmax och ONVIF)

Datum: 2026-11-20  
Status: dokumenterat förslag; **inte sparat i Lokalise**

Elmax-källtexten kontrollerades mot `homeassistant/components/elmax/strings.json` på Home Assistant Cores `dev`-gren.

| Fullständig nyckel | Befintlig svenska | Föreslagen svenska | Motivering |
|---|---|---|---|
| `component::elmax::config::step::reauth_confirm::data::panel_pin` | `Panel PIN-kod` | `Panelens PIN-kod` | Svenskan behöver genitiv för att ange vilken panel PIN-koden hör till. |

## Uppföljning

`component::roborock::entity::select::mop_mode::state::deep` (`Djup`) och `deep_plus` (`Djup+`) är språkligt ofullständiga som lägesnamn, men källtexten avgör inte om de är fasta produktnamn. Kontrollera Roborocks faktiska gränssnitt innan exempelvis `Djupgående` föreslås.

Övriga 19 nycklar på sidan granskades utan dokumenterat ändringsförslag. Två Roborock- och fyra autentiseringsnycklar är direkta referenser.
