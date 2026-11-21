# Home Assistant – Plant: käll-/projektavvikelse

Datum: 2026-11-21  
Komponent: `plant`  
Aktuella källrader: 4

## Resultat

Den lokala aktuella källfilen innehåller följande nycklar:

- `component::plant::entity_component::_::name`
- `component::plant::entity_component::_::state::ok`
- `component::plant::entity_component::_::state::problem`
- `component::plant::title`

En Lokalise API-förfrågan med samtliga exakta nycklar och både engelska och svenska språkfilter returnerade HTTP 200 men inga nyckelposter. Därför finns ingen auktoritativ aktuell svensk måltext att radgranska eller säkert uppdatera.

## Uppföljning

- Kräver kontroll av synkroniseringen mellan Home Assistant-källträdet och Lokalise-projektet.
- Inga ändringar skickades till Lokalise.
- Ingen lint- eller Hunspell-körning gjordes, eftersom målvärden saknas.
