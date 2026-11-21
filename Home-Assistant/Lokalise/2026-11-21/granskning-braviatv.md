# Home Assistant Core – Bravia TV

Datum: 2026-11-21

Källa: Home Assistant Core `2fdaa177`,
`homeassistant/components/braviatv/strings.json`, tidigare Bravia-rapporter och
direkt återläsning från Lokalise API.

## Resultat

Samtliga 41 aktuella Bravia TV-nycklar radgranskades. Den svenska texten hämtades
direkt från Lokalise med respektive översättnings-ID, efter jämförelse med aktuell
källtext och äldre dokumenterade ändringar. Inga nya ändringar behövdes.

De tidigare korrigeringarna för tv-form, PSK/SSL-anvisningar, omkonfiguration och
Sony Bravia-instruktioner finns kvar. Platshållarna i undantagsmeddelandena
(`{device}`, `{error}`, `{media_type}`, `{query}`, `{command}` och
`{media_content_*}`) är oförändrade. Citerade engelska menynamn i PSK-flödet
bevaras eftersom de betecknar TV:ns faktiska inställningsetiketter.

| Omfattning | Lokalise-resultat | Sparade ändringar |
| --- | ---: | ---: |
| `component::braviatv::*` | 41/41 direkt återlästa | 0 |

Ingen TMX-uppdatering eller release krävdes, eftersom inga nya verifierade
språkpar tillkom.
