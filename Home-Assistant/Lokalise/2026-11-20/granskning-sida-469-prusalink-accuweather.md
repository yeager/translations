# Home Assistant Core — granskning sida 469 (PrusaLink och AccuWeather)

Datum: 2026-11-20  
Status: dokumenterade förslag; **inte sparade i Lokalise**

PrusaLink-källtexten kontrollerades mot `homeassistant/components/prusalink/strings.json` på Home Assistant Cores `dev`-gren.

| Fullständig nyckel | Befintlig svenska | Föreslagen svenska | Motivering |
|---|---|---|---|
| `component::prusalink::entity::sensor::heatbed_target_temperature::name` | `Värmebädd måltemperatur` | `Måltemperatur för värmebädden` | Korrekt svensk ordföljd och bestämd form gör sensorns betydelse tydlig. |
| `component::prusalink::entity::sensor::nozzle_target_temperature::name` | `Munstycke måltemperatur` | `Måltemperatur för munstycket` | Korrekt svensk ordföljd och bestämd form gör sensorns betydelse tydlig. |

Övriga 18 nycklar på sidan granskades utan dokumenterat ändringsförslag. Sex AccuWeather-poster är referenser. Luftkvalitets- och pollennivåernas befintliga svenska adjektiv behålls för konsekvens mellan tillstånd.
