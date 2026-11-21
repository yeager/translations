# Home Assistant Core – RFLink

Datum: 2026-11-21  
Källa: aktuell Core `2fdaa177`, `homeassistant/components/rflink/strings.json`  
Status: samtliga sex aktuella källsträngar är radgranskade mot Lokalise utan ändringsförslag.

Den aktuella Core-källan innehåller sex bladsträngar:

- `services::send_command::name` — `Send command`
- `services::send_command::description` — `Sends device command through RFLink.`
- `services::send_command::fields::command::name` — `Command`
- `services::send_command::fields::command::description` — `The command to be sent.`
- `services::send_command::fields::device_id::name` — `Device ID`
- `services::send_command::fields::device_id::description` — `RFLink device ID.`

Lokalise lästes efter återställd anslutning. Befintliga svenska måltexter är:

- `Skicka kommando`
- `Skickar enhetskommando via RFLink.`
- `Kommando`
- `Kommandot som ska skickas.`
- `Enhets-ID`
- `RFLink-enhets-ID.`

Samtliga följer källans innebörd, terminologi och skiljetecken. Inga
platshållare eller referenser förekommer i de sex aktuella strängarna. Den sista
strängen är redan spårbar i det kanoniska TMX-minnet som
`lokalise:2807711617`; övriga redan korrekta, oförändrade UI-värden läggs inte
till utan säkra översättnings-ID:n.

Lokalise visar dessutom två äldre YAML-migreringsnycklar
(`issues::yaml_migration::title` och `issues::yaml_migration::description`). De
saknas i den aktuella Core-källan och är därför historiska. Produktnamnet
`Home Assistant` förekommer inte i de sex aktuella RFLink-källsträngarna.
