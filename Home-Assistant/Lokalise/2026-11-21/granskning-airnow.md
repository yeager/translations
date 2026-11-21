# Home Assistant Core – AirNow

Datum: 2026-11-21  
Källa: Core `2fdaa177`, `homeassistant/components/airnow/strings.json`, aktuell Lokalise-export.

Status: samtliga 27 aktuella bladnycklar är radgranskade. Tre korrigeringar är sparade och återlästa.

| Nyckelgrupp | Svenska efter granskning | Motivering |
| --- | --- | --- |
| `options::step::init::data::radius` | Stationsradie (engelska mil) | Ersätter oöversatta `miles`. Lokalise-ID `369009473`. |
| Beskrivningar för radie i config och options | Radien i engelska mil runt din plats … | Enhetlig svensk enhetsangivelse i båda förekomsterna. Lokalise-ID `846905534`, `850742318`. |

API-nyckel, koordinater, station, ozon, plats- och återautentiseringstexter är i övrigt korrekta. `{name}` och `{api_key_url}` är bevarade.
