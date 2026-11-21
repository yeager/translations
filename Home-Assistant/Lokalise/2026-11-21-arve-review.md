# Home Assistant – Arve: käll-/projektavvikelse

Datum: 2026-11-21  
Komponent: `arve`  
Aktuella källrader: 6

## Resultat

Följande lokala källnycklar finns men returnerades inte av Lokalise API när de efterfrågades exakt med engelska och svenska språkfilter:

- `component::arve::config::abort::already_configured`
- `component::arve::config::error::cannot_connect`
- `component::arve::config::step::user::data::access_token`
- `component::arve::config::step::user::data::client_secret`
- `component::arve::config::step::user::description`
- `component::arve::entity::sensor::tvoc::name`

API-svaret var HTTP 200 med tom nyckellista. Ingen aktuell svensk måltext kunde därför granskas eller uppdateras säkert.

## Uppföljning

- Kontrollera synkroniseringen mellan aktuellt Home Assistant-källträd och Lokalise-projektet.
- Inga ändringar eller lintkörningar genomfördes utan måltexter.
