# Home Assistant Core – Lokalise-granskning, sida 609

Datum: 2026-11-20  
Omfattning: Lokalise API, 20 Core-strängar (`flux_led`, `foscam`).

## Sparade ändringar

| Nyckel | Sparad svensk text | Motivering |
|---|---|---|
| `component::flux_led::services::set_music_mode::fields::effect::description` | `Effekt (1–16 på adresserbara modeller, 0–3 på RGB-med-MIC-modeller).` | Korrekt intervalltecken och tydlig modellbeteckning. |
| `component::flux_led::services::set_music_mode::fields::light_screen::description` | `Ljusskärmsläge för tvådimensionella pixlar (endast adresserbara modeller).` | Naturlig svensk sammansättning. |
| `component::flux_led::services::set_zones::description` | `Ställer in LED-stripzoner för adresserbara v3-styrenheter (0xA3).` | Tydlig sammansättning. |
| `component::flux_led::services::set_zones::fields::colors::description` | `Lista över färger för varje zon (RGB). Längden på varje zon är antalet pixlar per segment dividerat med antalet färger. (Högst 2 048 färger.)` | Svensk sifferformatering och naturligt begränsningsuttryck. |

## Verifiering

Alla fyra ändringar skickades med Lokalise API och återlästes. Referenserna på sidan är giltiga; övriga strängar behöver ingen ändring.

Status: sparat och återläst i Lokalise.
