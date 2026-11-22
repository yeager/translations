# Kolon före URL- och värdplatshållare

Sju Core-strängar rättades via Lokalise API den 22 november 2026 och lästes
tillbaka efter sparning. Ett kolon som följt med från den engelska källan
togs bort efter svensk löpande text före URL- eller värdplatshållaren.

| Nyckel | Ändring |
| --- | --- |
| `component::sonarr::config::step::reauth_confirm::description` | `på: {url}` → `på {url}` |
| `component::roomba::config::step::link_manual::description` | `på: {auth_help_url}` → `på {auth_help_url}` |
| `component::awair::config::step::cloud::description` | `på: {url}` → `på {url}` |
| `component::google_sheets::config::create_entry::default` | `på: {url}` → `på {url}` |
| `component::lametric::services::message::fields::icon::description` | `på: {icons_url}` → `på {icons_url}` |
| `component::fritz::config::step::reconfigure::description` | `för: {host}` → `för {host}` |
| `component::tesla_fleet::config::step::domain_registration::description` | `på:\n\n{public_key_url}` → `på\n\n{public_key_url}` |

Alla platshållare, radbrytningar och Tesla Fleet-kodblocket är bevarade.
