# Home Assistant Core – Aranet, återgranskning

Datum: 2026-11-23

Den äldre rapporten jämfördes mot den aktuella livekatalogen. Samtliga tretton
strängar lästes tillbaka via Lokalise; en direktivtext behövde uppdateras.

| Nyckel | Tidigare svenska | Sparad svenska | Bedömning |
| --- | --- | --- | --- |
| `component::aranet::config::abort::already_configured` | Enheten är redan konfigurerad | Enheten är redan konfigurerad | Korrekt. |
| `component::aranet::config::abort::no_devices_found` | Inga okonfigurerade Aranet-enheter hittades. | Inga okonfigurerade Aranet-enheter hittades. | Korrekt. |
| `component::aranet::config::abort::outdated_version` | Enheten använder en utdaterad firmware. Vänligen uppdatera den till minst v1.2.0 och försök igen | Enheten använder en utdaterad firmware. Uppdatera den till minst v1.2.0 och försök igen. | Imperativ stil och avslutande punkt. |
| `component::aranet::config::error::unknown` | Oväntat fel | Oväntat fel | Korrekt. |
| `component::aranet::config::flow_title` | `{name}` | `{name}` | Platshållaren bevarad. |
| `component::aranet::config::step::bluetooth_confirm::description` | Vill du konfigurera `{name}`? | Vill du konfigurera `{name}`? | Platshållaren bevarad. |
| `component::aranet::config::step::user::data::address` | Enhet | Enhet | Korrekt. |
| `component::aranet::config::step::user::description` | Välj en enhet att konfigurera | Välj en enhet att konfigurera | Korrekt. |
| `component::aranet::config::abort::integrations_disabled` | Integrationer är inte aktiverade för den här enheten. Aktivera smarta hem-integrationer med appen och försök igen. | Oförändrad | Korrekt. |
| `component::aranet::entity::sensor::threshold::state::error` | Fel | Fel | Korrekt. |
| `component::aranet::entity::sensor::threshold::state::green` | Grön | Grön | Korrekt. |
| `component::aranet::entity::sensor::threshold::state::red` | Röd | Röd | Korrekt. |
| `component::aranet::entity::sensor::threshold::state::yellow` | Gul | Gul | Korrekt. |

Inga pluralformer eller referenser förekommer. `firmware` är etablerat i
Core-katalogen i just denna kontext och behålls; `v1.2.0` är ett produktformat.
Den uppdaterade texten lästes tillbaka från Lokalise och samtliga tretton
poster har lagts i det validerade TMX-minnet.
