# Home Assistant Core – Lokalise-granskning, sida 606

Datum: 2026-11-20  
Omfattning: Lokalise API, 20 Core-strängar (`evohome`, `ezviz`, `facebox`).

## Sparade ändringar

| Nyckel | Sparad svensk text | Motivering |
|---|---|---|
| `component::evohome::services::set_zone_override::name` | `Ställ in zonens åsidosättning` | Följer terminologin för samma åtgärdsfamilj. |
| `component::ezviz::services::set_alarm_detection_sensibility::fields::level::description` | `Känslighetsnivå. 1–6 för typ 0 (vanlig kamera) eller 1–100 för typ 3 (kamera med PIR-sensor).` | Svenskt ordval och korrekt intervalltecken. |
| `component::ezviz::services::set_alarm_detection_sensibility::fields::type_value::description` | `Detekteringstyp. 0 för vanlig kamera eller 3 för kamera med PIR-sensor.` | Naturligare sammansättning. |
| `component::facebox::services::teach_face::fields::entity_id::description` | `Facebox-entitet som ska tränas.` | Entiteten tränas, inte "lärs". |

## Verifiering

Alla fyra ändringar skickades med Lokalise API och återlästes. Övriga strängar på sidan behöver ingen ändring.

Status: sparat och återläst i Lokalise.
