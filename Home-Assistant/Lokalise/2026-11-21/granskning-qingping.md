# Home Assistant Core – Qingping

Datum: 2026-11-21  
Källa: aktuell Core `2fdaa177`, `homeassistant/components/qingping/strings.json`  
Status: samtliga åtta aktuella källsträngar är radgranskade mot Lokalise utan ändringsförslag.

## Verifierade poster

- Referenserna för redan konfigurerad enhet, inga enheter hittades, Bluetooth-bekräftelse, Bluetooth-användarbeskrivning och det gemensamma fältet för enhet följer källan exakt.
- Flödestiteln bevarar platshållaren `{name}`.
- `Device not supported` är korrekt översatt till `Enheten stöds inte`.
- `Select the Qingping device you want to set up` är korrekt återgivet som `Välj den Qingping-enhet som du vill konfigurera`.

Lokalise-sökningen visade nio poster. `component::qingping::config::abort::already_in_progress` (Lokalise-ID `205230863`) finns där men saknas i den aktuella Core-källan och är därför en historisk post. Den ändras inte. Inga värden från den här kontrollen förs in i TMX förrän en avgränsad, verifierad TMX-synkning genomförs.
