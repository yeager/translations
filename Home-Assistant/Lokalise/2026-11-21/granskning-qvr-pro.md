# Home Assistant Core – QVR Pro

Datum: 2026-11-21  
Källa: aktuell Core `2fdaa177`, `homeassistant/components/qvr_pro/strings.json`  
Status: samtliga åtta aktuella källsträngar är radgranskade mot Lokalise utan ändringsförslag.

## Verifierade poster

- Tjänsten `start_record` använder korrekta svenska verb och beskrivningar: `Starta inspelning`, `Startar QVR Pro-inspelning på angiven kanal.` och GUID-beskrivningen för start.
- Motsvarande `stop_record`-poster är konsekventa: `Stoppa inspelning`, `Stoppar QVR Pro-inspelning på angiven kanal.` och GUID-beskrivningen för stopp.
- `GUID` är korrekt oförändrat, och stopptjänstens fältnamn följer exakt referensen till starttjänstens fältnamn.
- Produktnamnet `QVR Pro` bevaras exakt i svensk text.

Lokalise-sökningen visade exakt åtta poster, samma antal som den aktuella källfilen. Inga ändringar krävs och inga nya TMX-poster skapas förrän nästa verifierade TMX-synkning.
