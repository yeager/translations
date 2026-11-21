# Home Assistant Core – PoolDose

Datum: 2026-11-21

## Delgranskning

| Nyckel | Källa | Befintlig svenska | Svenska efter granskning | Bedömning |
| --- | --- | --- | --- | --- |
| `component::pooldose::config::step::dhcp_confirm::description` | A PoolDose device was found on your network at {ip} with MAC address {mac}.\n\nDo you want to add {name} to Home Assistant? | En PoolDose enhet hittades i ditt nätverk på {ip} med MAC-dressen {mac}.\n\nVill du lägga till {name} i Home Assistant? | En PoolDose-enhet hittades i ditt nätverk på {ip} med MAC-adressen {mac}.\n\nVill du lägga till {name} i Home Assistant? | Sparad och återläst i Lokalise (ID `714669662`). Rättar sammansättningarna `PoolDose-enhet` och `MAC-adressen`; `{ip}`, `{mac}` och `{name}` samt styckeindelning bevaras. |
| `component::pooldose::config::error::no_device_info` | Unable to retrieve device information. Device may not be properly initialized or may be an unsupported model. | Det går inte att hämta enhetsinformation. Enheten är kanske inte korrekt initialiserad eller så är det en modell som inte stöds. | Verifierad i Lokalise (ID `701475653`). |
| `component::pooldose::config::step::user::description` | Login handling not supported by API. Device password must be deactivated, i.e., set to default value (0000). | Inloggningshantering stöds inte av API:et. Enhetens lösenord måste inaktiveras, dvs. återställas till standardvärdet (0000). | Verifierad i Lokalise (ID `701475659`). |
| `component::pooldose::exceptions::write_rejected::message` | The device rejected the value for {entity}: {value} | Enheten avvisade värdet för {entity}: {value} | Verifierad i Lokalise (ID `779987563`); båda platshållarna är bevarade. |
| `component::pooldose::exceptions::connect_timeout::message` | Timeout connecting to PoolDose device | Timeout vid anslutning till PoolDose-enhet | Tidsgränsen överskreds vid anslutning till PoolDose-enheten. | Sparad och återläst i Lokalise (ID `857959052`). Rättar oöversatt teknisk term samt sammansättning och bestämd form. |
| `component::pooldose::exceptions::connect_failed::message` | Failed to connect to PoolDose device | Det gick inte att ansluta till PoolDose-enheten | Verifierad i Lokalise (ID `857959051`). |

## Sparade och återlästa fortsättningskorrigeringar

Följande etiketter har rättats i Lokalise och återlästs via API:t: `ORP överdosering larmtid` och `pH överdosering larmtid` till `Larmtid för ORP-överdosering` respektive `Larmtid för pH-överdosering` (båda förekomsterna); `ORP-kalibrering offset`, `ORP-kalibrering lutning`, `ORP-kalibrering typ` och `ORP-dosering typ` till korrekta sammansättningar; samt `Flödesfördröjning timer` och de tre särskrivna stopptidsetiketterna till `Flödesfördröjningstimer` respektive `Stopptid för …-dosering`. Berörda nyckel-ID:n: `701475661`, `701475662`, `701475664`–`701475666`, `701475670`, `752126899`, `752126900` och `822808369`, `822808371`–`822808373`.

Överdoseringstermerna har dessutom enhetliggjorts och återlästs: alla sex larmgränser använder nu `… gräns för larm vid …-överdosering`, och de tre alternativa larmen har korrekta sammansättningar. Berörda nyckel-ID:n: `766455722`–`766455727` och `822808361`–`822808363`.

