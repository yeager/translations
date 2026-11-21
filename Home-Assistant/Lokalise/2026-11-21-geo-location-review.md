# Home Assistant – Geolocation: svensk radgranskning

Datum: 2026-11-21  
Projekt: Home Assistant Core i Lokalise  
Komponent: `geo_location`

## Underlag och verifiering

Samtliga fem strängar i `homeassistant/components/geo_location/strings.json` kontrollerades mot aktuell Lokalise-data. `l10n-lint` godkände katalogen med engelskan som referens. Hunspell gav inga relevanta stavningsträffar. Svlang markerade “geolokalisering” som ovanligt; det är den etablerade svenska facktermen och är korrekt i detta sammanhang.

## Radvis resultat

| Fullständig nyckel | Engelska | Svenska | Resultat |
| --- | --- | --- | --- |
| `component::geo_location::entity_component::_::name` | Geolocation | Geolokalisering | Behåll. |
| `component::geo_location::entity_component::_::state_attributes::latitude::name` | Latitude | Latitud | Behåll. |
| `component::geo_location::entity_component::_::state_attributes::longitude::name` | Longitude | Longitud | Behåll. |
| `component::geo_location::entity_component::_::state_attributes::source::name` | Source | Källa | Behåll. |
| `component::geo_location::title` | Geolocation | Geolokalisering | Behåll. Konsekvent med entitetens namn. |

Inga ändringar behövde sparas i Lokalise.