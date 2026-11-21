# Home Assistant Core – UptimeRobot, uppföljning

Datum: 2026-11-21

En äldre granskningsrapport innehöll ett osparat förslag för reconfiguration-flödet. Aktuella Lokalise-strängar kontrollerades och följande korrigeringar sparades samt API-återlästes.

| Nyckel | Tidigare svenska | Sparad svenska |
| --- | --- | --- |
| `component::uptimerobot::config::step::reconfigure::data::api_key` | `API nyckel` | `API-nyckel` |
| `component::uptimerobot::config::step::reconfigure::data_description::api_key` | `Den "huvudsakliga" API nyckeln för ditt UptimeRobot konto` | `Den "huvudsakliga" API-nyckeln för ditt UptimeRobot-konto` |
| `component::uptimerobot::exceptions::api_key_wrong_type::message` | `... använd "huvud" API-nyckeln` | `... använd "huvud-API-nyckeln"` |

Formerna följer samma terminologi som övriga UptimeRobot-strängar. Inga platshållare berörs.
