# Philips TV och IPP: saknade Core-översättningar

> **Aktuell status:** Fyra förslag nedan sparades och återlästes i Lokalise 2026-11-19 efter användarens instruktion. Tidigare formuleringar om osparade förslag avser läget före sparningen.

Lokalise kontrollerades den 19 november 2026. Svenska måltexter för de fyra nycklarna nedan var tomma; förslagen är lokala och har inte sparats i Lokalise.

| Fullständig nyckel | Engelsk källtext | Befintlig svenska | Lokalt förslag |
|---|---|---|---|
| `component::philips_js::config::step::reconfigure::data::host` | `[%key:common::config_flow::data::host%]` | Tom | `[%key:common::config_flow::data::host%]` |
| `component::philips_js::config::step::reconfigure::data::api_version` | `[%key:component::philips_js::config::step::user::data::api_version%]` | Tom | `[%key:component::philips_js::config::step::user::data::api_version%]` |
| `component::philips_js::config::abort::unique_id_mismatch` | The host you entered belongs to a different Philips TV. | Tom | Värden du angav tillhör en annan Philips-tv. |
| `component::ipp::exceptions::cannot_connect::message` | Could not connect to the printer | Tom | Det gick inte att ansluta till skrivaren |

Referensmålen har kontrollerats i Lokalise: `common::config_flow::data::host` är ”Host” / ”Värd” och `component::philips_js::config::step::user::data::api_version` är ”API Version” / ”API-version”. Föreslagna referenser återger källans mål exakt; textförslagen har inga platshållare eller pluralformer. Kontrollera aktuella värden igen före eventuell användning.
