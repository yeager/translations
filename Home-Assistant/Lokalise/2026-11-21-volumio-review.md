# Home Assistant Core – Volumio

Datum: 2026-11-21

Alla nio Volumio-strängar är granskade mot tidigare sparat arbete och aktuell källa. Två förbättringar är sparade och API-återlästa.

| Nyckel | Sparad svenska | Motivering |
| --- | --- | --- |
| `config::step::discovery_confirm::description` | `Vill du lägga till Volumio ({name}) i Home Assistant?` | Rätt preposition i integrationskontext. Kodmarkeringen kring `{name}` är bevarad i Lokalise. |
| `config::step::discovery_confirm::title` | `Volumio har upptäckts` | Fullständig och naturlig svensk dialogrubrik. |

Den tidigare sparade anslutningsfelstexten är fortfarande korrekt. Produktnamnet `Volumio`, platshållaren `{name}` och `Home Assistant` är bevarade.
