# Home Assistant – Date: käll-/projektavvikelse

Datum: 2026-11-21  
Komponent: `date`  
Aktuella källrader: 6

## Resultat

Lokalise API returnerade HTTP 200 men inga poster för de sex exakta lokala källnycklarna:

- `component::date::entity_component::_::name`
- `component::date::services::set_value::description`
- `component::date::services::set_value::fields::date::description`
- `component::date::services::set_value::fields::date::name`
- `component::date::services::set_value::name`
- `component::date::title`

Det saknas därmed en aktuell svensk måltext för säker radgranskning och uppdatering.

## Uppföljning

- Kontrollera synkroniseringen/versionerna mellan källträdet och Lokalise-projektet.
- Inga ändringar skickades och inga språkverktyg kördes utan API-måltexter.
