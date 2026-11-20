# Home Assistant Core – Lokalise-granskning, sida 605

Datum: 2026-11-20  
Omfattning: Lokalise API, 20 Core-strängar (`epson`, `evohome`).

## Sparade ändringar

| Nyckel | Befintlig svensk text | Sparad svensk text | Motivering |
|---|---|---|---|
| `component::evohome::services::clear_zone_override::description` | `Ställer in en zon så att den följer sitt schema.` | `Ställer in en zon så att den följer sitt schema (utfasad).` | Bevarar källans deprecationsmarkering. |
| `component::evohome::services::clear_zone_override::name` | `Rensa åsidosättande för zon` | `Ta bort zonens åsidosättning` | Naturligare och korrekt svensk form. |
| `component::evohome::services::set_system_mode::fields::mode::description` | `Läge att ställa in systemet på.` | `Läge som systemet ska ställas in på.` | Korrekt satsstruktur. |

## Verifiering

Alla tre ändringar skickades med Lokalise API och återlästes. Lokalise-referenserna är giltiga; övriga 15 strängar behöver ingen ändring.

Status: sparat och återläst i Lokalise.
