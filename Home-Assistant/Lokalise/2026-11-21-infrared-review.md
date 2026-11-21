# Home Assistant – Infrared: svensk radgranskning

Datum: 2026-11-21  
Projekt: Home Assistant Core i Lokalise  
Komponent: `infrared`

## Underlag och verifiering

Alla fem aktuella strängar i `homeassistant/components/infrared/strings.json` jämfördes med Lokalise API. `l10n-lint` godkände svensk katalog mot engelsk referens. Hunspell och svlang markerade `entity_id`; det är den bevarade tekniska platshållaren. Svlangens V2-signal beror på flera korta etiketter i samma analysfil och är inte en språklig avvikelse.

## Radvis resultat

| Fullständig nyckel | Engelska | Svenska | Resultat |
| --- | --- | --- | --- |
| `component::infrared::entity_component::emitter::name` | Infrared emitter | Infraröd sändare | Behåll. |
| `component::infrared::entity_component::receiver::name` | Infrared receiver | Infraröd mottagare | Behåll. |
| `component::infrared::exceptions::component_not_loaded::message` | Infrared component not loaded | Den infraröda komponenten har inte laddats | Behåll. |
| `component::infrared::exceptions::entity_not_found::message` | Infrared entity `{entity_id}` not found | Den infraröda entiteten `{entity_id}` hittades inte | Behåll. Platshållaren bevarad. |
| `component::infrared::exceptions::receiver_not_found::message` | Infrared receiver entity `{entity_id}` not found | Den infraröda mottagarentiteten `{entity_id}` hittades inte | Behåll. Platshållaren bevarad. |

Inga ändringar behövde sparas i Lokalise.