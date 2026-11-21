# Home Assistant Core – Cert Expiry

Datum: 2026-11-21

Källa: Home Assistant Core `2fdaa177`,
`homeassistant/components/cert_expiry/strings.json`, tidigare Cert Expiry-logg
och direkt återläsning från Lokalise API.

Alla 20 aktuella `component::cert_expiry::*`-nycklar har radgranskats. En säker
korrigering sparades och återlästes:

| Nyckel | Sparad svenska | Motivering |
| --- | --- | --- |
| `component::cert_expiry::config::error::connection_reset` | Anslutningen återställdes vid anslutning till värden. | Korrigerar saknat verb i feltexten. |

Språkparet har lagts till i kanoniska HA-TMX:n och validerats.
