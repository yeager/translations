# Home Assistant Core – fortsatta direkta uppmaningar

Datum: 2026-11-23. Samtliga poster sparades i Lokalise via API, lästes tillbaka
med samma översättnings-ID och fördes in i det kanoniska TMX-minnet.

| Nyckel | Tidigare svensk text | Sparad svensk text | Motivering |
|---|---|---|---|
| `component::asuswrt::config::error::pwd_or_ssh` | Vänligen ange lösenord eller SSH-nyckelfil | Ange lösenord eller SSH-nyckelfil. | Direkt felåtgärd och konsekvent slutpunkt. |
| `component::overkiz::config::error::no_such_token` | Det går inte att skapa en token för den här gatewayen. Vänligen bekräfta om kontot är länkat till denna gateway. | Det går inte att skapa en token för den här gatewayen. Bekräfta att kontot är länkat till den här gatewayen. | Naturligare konstruktionsval och konsekvent demonstrativ. |
| `component::aosmith::config::step::reauth_confirm::description` | Vänligen uppdatera ditt lösenord för `{email}` | Uppdatera ditt lösenord för `{email}`. | Direkt instruktion; platshållaren bevarad. |
| `component::webmin::config::step::user::description` | Vänligen ange anslutningsinformationen för din instans. | Ange anslutningsuppgifterna för din instans. | Mer idiomatiskt fältspråk. |
| `component::peco::config::error::http_error` | Det uppstod ett fel i kommunikationen med PECO. Det mest troliga är att du har angett ett ogiltigt telefonnummer. Vänligen kontrollera telefonnumret eller försök igen senare. | Det uppstod ett kommunikationsfel med PECO. Du har troligen angett ett ogiltigt telefonnummer. Kontrollera telefonnumret eller försök igen senare. | Kortare, tydligare felmeddelande och direkt åtgärd. |
| `component::cloud::issues::deprecated_tts_platform_config::description` | … Vänligen justera din `configuration.yaml` och starta om Home Assistant för att åtgärda detta problem. | … Justera din `configuration.yaml` och starta om Home Assistant för att åtgärda problemet. | Direkt instruktion och mindre tung avslutning. |
| `component::system_bridge::config::abort::unsupported_version` | Din version av System Bridge stöds inte. Vänligen uppgradera till den senaste versionen. | Din version av System Bridge stöds inte. Uppgradera till den senaste versionen. | Direkt instruktion. |

TM-manifest: `2026-11-23-asuswrt-overkiz-aosmith-webmin-live-verified.json` och
`2026-11-23-peco-cloud-systembridge-live-verified.json` i `yeager/swedish-tm`.
