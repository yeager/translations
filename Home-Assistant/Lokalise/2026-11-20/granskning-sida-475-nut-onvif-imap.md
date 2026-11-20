# Home Assistant Core — granskning sida 475 (NUT, ONVIF, IMAP och Powerwall)

Datum: 2026-11-20  
Status: dokumenterade förslag; **inte sparade i Lokalise**

ONVIF- och IMAP-källtexterna kontrollerades mot respektive `strings.json` på Home Assistant Cores `dev`-gren.

| Fullständig nyckel | Befintlig svenska | Föreslagen svenska | Motivering |
|---|---|---|---|
| `component::onvif::config::error::onvif_error` | `Problem med att konfigurera ONVIF-enheten: {error}. Kolla loggarna för mer information.` | `Problem med att konfigurera ONVIF-enheten: {error}. Kontrollera loggarna för mer information.` | `Kontrollera` har saklig och konsekvent ton i en feltext; platshållaren bevaras. |
| `component::imap::config::error::ssl_error` | `Ett SSL-fel uppstod. Ändra SSL-chifferlista och försök igen` | `Ett SSL-fel uppstod. Ändra SSL-chifferlista och försök igen.` | Avslutande punkt saknas i den svenska feltexten. |

Övriga 18 nycklar på sidan granskades utan dokumenterat ändringsförslag. NUT-åtgärderna använder konsekventa imperativ och tekniska termer; SSL-chifferalternativen och Powerwall-referensen är korrekta.
