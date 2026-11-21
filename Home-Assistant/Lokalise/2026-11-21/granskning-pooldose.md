# Home Assistant Core – PoolDose

Datum: 2026-11-21

## Delgranskning

| Nyckel | Källa | Befintlig svenska | Svenska efter granskning | Bedömning |
| --- | --- | --- | --- | --- |
| `component::pooldose::config::step::dhcp_confirm::description` | A PoolDose device was found on your network at {ip} with MAC address {mac}.\n\nDo you want to add {name} to Home Assistant? | En PoolDose enhet hittades i ditt nätverk på {ip} med MAC-dressen {mac}.\n\nVill du lägga till {name} i Home Assistant? | En PoolDose-enhet hittades i ditt nätverk på {ip} med MAC-adressen {mac}.\n\nVill du lägga till {name} i Home Assistant? | Sparad och återläst i Lokalise (ID `714669662`). Rättar sammansättningarna `PoolDose-enhet` och `MAC-adressen`; `{ip}`, `{mac}` och `{name}` samt styckeindelning bevaras. |
| `component::pooldose::config::error::no_device_info` | Unable to retrieve device information. Device may not be properly initialized or may be an unsupported model. | Det går inte att hämta enhetsinformation. Enheten är kanske inte korrekt initialiserad eller så är det en modell som inte stöds. | Verifierad i Lokalise (ID `701475653`). |
| `component::pooldose::config::step::user::description` | Login handling not supported by API. Device password must be deactivated, i.e., set to default value (0000). | Inloggningshantering stöds inte av API:et. Enhetens lösenord måste inaktiveras, dvs. återställas till standardvärdet (0000). | Verifierad i Lokalise (ID `701475659`). |

