# Home Assistant Core – Lokalise-granskning, sida 611

Datum: 2026-11-20  
Omfattning: Lokalise API, 20 Core-strängar (`fully_kiosk`, `lcn`).

## Sparade ändringar

| Nyckel | Sparad svensk text | Motivering |
|---|---|---|
| `component::fully_kiosk::services::set_config::name` | `Ställ in konfiguration` | Konsekvent åtgärdsform. |
| `component::lcn::services::dyn_text::fields::text::description` | `Text att skicka (upp till 60 tecken, kodade i UTF-8).` | Rätt preposition för teckenkodning. |

## Verifiering

Båda ändringar skickades med Lokalise API och återlästes. Referensen för LCN-adress är giltig; övriga strängar behöver ingen ändring.

Status: sparat och återläst i Lokalise.
