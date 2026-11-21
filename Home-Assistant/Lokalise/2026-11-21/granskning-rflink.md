# Home Assistant Core – RFLink

Datum: 2026-11-21  
Källa: aktuell Core `2fdaa177`, `homeassistant/components/rflink/strings.json`  
Status: källinventering klar; Lokalise-resultaten har inte kunnat läsas i denna kontrollpunkt.

Den aktuella Core-källan innehåller sex bladsträngar:

- `services::send_command::name` — `Send command`
- `services::send_command::description` — `Sends device command through RFLink.`
- `services::send_command::fields::command::name` — `Command`
- `services::send_command::fields::command::description` — `The command to be sent.`
- `services::send_command::fields::device_id::name` — `Device ID`
- `services::send_command::fields::device_id::description` — `RFLink device ID.`

Lokalise-ytan kunde inte anslutas för den läsande kontrollen efter att sessionen
återställdes. Därför har inga svenska måltexter, Lokalise-ID:n, ändringsförslag
eller TMX-enheter registrerats och komponenten är inte markerad som radgranskad.
När åtkomsten fungerar ska samtliga sex måltexter jämföras med källan och
produktnamnet `Home Assistant` alltid behållas exakt om det förekommer i en
berörd sträng.
