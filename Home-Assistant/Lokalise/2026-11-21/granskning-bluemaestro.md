# Home Assistant Core – Bluemaestro

Datum: 2026-11-21  
Källa: Core `2fdaa177`, `homeassistant/components/bluemaestro/strings.json` och Lokalise API med direkt återläsning.

Status: samtliga nio aktuella bladsträngar, inklusive upplösta referenser, är radgranskade. Ingen ändring behövs i Lokalise.

| Nyckel | Sparad text | Bedömning |
|---|---|---|
| `config::abort::already_configured` | `Enheten är redan konfigurerad` | Korrekt. |
| `config::abort::already_in_progress` | `Detta konfigureras redan. Slutför den befintliga konfigurationen innan du börjar igen.` | Korrekt och konsekvent med gemensam HA-text. |
| `config::abort::no_devices_found` | `Inga enheter hittades i nätverket` | Korrekt. |
| `config::abort::not_supported` | `Enheten stöds inte` | Korrekt. |
| `config::flow_title` | `{name}` | Platshållaren är oförändrad. |
| `config::step::bluetooth_confirm::description` | `Vill du konfigurera {name}?` | Korrekt; platshållaren är bevarad. |
| `config::step::user::data::address` | `Enhet` | Korrekt fältnamn. |
| `config::step::user::description` | `Välj en enhet att konfigurera` | Korrekt. |
| `entity::sensor::dew_point::name` | `Daggpunkt` | Korrekt fackterm. |

Källfilen innehåller referenser till Bluetooth- och common-nycklar. De aktiva, upplösta Lokalise-värdena ovan är direkt återlästa och har bedömts i respektive UI-kontext.
