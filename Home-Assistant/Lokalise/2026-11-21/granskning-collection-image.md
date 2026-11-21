# Home Assistant Core – Collection Image

Datum: 2026-11-21

Källa: Home Assistant Core `2fdaa177`, `homeassistant/components/collection_image/strings.json`, tidigare förslag och direkt återläsning via Lokalise API.

Alla 33 aktuella strängar har kontrollerats. Fem servicebeskrivningar korrigerades och lästes tillbaka från Lokalise. Felplatshållarna `{error}`, `{path}`, `{entity}`, `{id}` och `{mime_type}` är oförändrade.

| Fullständig nyckel | Sparad svenska |
| --- | --- |
| `component::collection_image::services::shuffle::description` | Uppdaterar bildentiteten till en slumpmässig bild från det konfigurerade mediet. |
| `component::collection_image::services::select_first::description` | Uppdaterar bildentiteten till den första bilden i det konfigurerade mediet. |
| `component::collection_image::services::select_last::description` | Uppdaterar bildentiteten till den sista bilden i det konfigurerade mediet. |
| `component::collection_image::services::select_next::description` | Uppdaterar bildentiteten till nästa bild i det konfigurerade mediet. |
| `component::collection_image::services::select_previous::description` | Uppdaterar bildentiteten till föregående bild i det konfigurerade mediet. |

Ändringen gör beskrivningarna konsekventa med övriga servicebeskrivningar genom sakligt presens och termen `bildentitet`. De fem språkparen är inlagda i TMX-minnet; valideraren godkände 1 973 poster.
