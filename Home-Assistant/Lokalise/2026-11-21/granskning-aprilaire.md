# Home Assistant Core – Aprilaire

Datum: 2026-11-21  
Källa: Core `2fdaa177`, `homeassistant/components/aprilaire/strings.json`, Lokalise API med direkt återläsning.

Status: samtliga 46 aktuella bladsträngar och referensmål är radgranskade. Två korrigeringar är sparade och återlästa.

| Nyckel | Sparad text | Motivering |
|---|---|---|
| `entity::sensor::indoor_humidity_controlling_sensor::name` | `Sensor för styrning av luftfuktighet inomhus` | Anpassar termen till motsvarande sensorer och svenska tekniska formuleringar. |
| `entity::select::air_cleaning_mode::state::constant_clean` | `Konstant luftrening` | *Air cleaning* är luftrening, inte allmän rengöring. |

Värd/port, termostat, luftfuktare, avfuktare, statusnamn och delade tillståndsreferenser är korrekta. Direkt API-återläsning bekräftade båda ändringarna. TMX-ledgern är uppdaterad och validerad (1 705 poster).
