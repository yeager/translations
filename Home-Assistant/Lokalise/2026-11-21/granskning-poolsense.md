# Home Assistant Core – PoolSense

Datum: 2026-11-21

## Delgranskning

| Nyckel | Källa | Svenska | Bedömning |
| --- | --- | --- | --- |
| `component::poolsense::exceptions::invalid_auth::message` | Invalid authentication | Ogiltig autentisering | Verifierad i Lokalise (ID `951170040`). |
| `component::poolsense::entity::binary_sensor::chlorine_status::name` | Chlorine status | Klorstatus | Verifierad i Lokalise (ID `354342470`). |
| `component::poolsense::entity::binary_sensor::ph_status::name` | pH status | pH-status | Verifierad i Lokalise (ID `354342471`). |
| `component::poolsense::entity::sensor::chlorine::name` | Chlorine | Klor | Verifierad i Lokalise (ID `354342472`). |
| `component::poolsense::entity::sensor::chlorine_high::name` | Chlorine high | Hög klorhalt | Verifierad i Lokalise (ID `354342473`). |
| `component::poolsense::entity::sensor::chlorine_low::name` | Chlorine low | Låg klorhalt | Verifierad i Lokalise (ID `354342474`). |
| `component::poolsense::entity::sensor::last_seen::name` | Last seen | Senast sedd | Verifierad i Lokalise (ID `354342475`). |

## Sparade och API-verifierade förslag

| Nyckel | Befintlig svenska | Föreslagen svenska | Motivering |
| --- | --- | --- | --- |
| `component::poolsense::entity::sensor::ph_high::name` | Hög pH | Högt pH-värde | Korrekt svenskt måttuttryck och begriplig entitetsrubrik. |
| `component::poolsense::entity::sensor::ph_low::name` | Låg pH | Lågt pH-värde | Korrekt svenskt måttuttryck och begriplig entitetsrubrik. |

De två förslagen är sparade och återlästa via Lokalise API 2026-11-21 med
översättnings-ID `2846175336` respektive `2846175396` och ingår i verifierad
HA-TMX.

