# Nivåetiketten Medium

Datum: 2026-11-23. Fem aktuella Lokalise-nycklar lästes direkt via API. Sammanhanget visar att `Medium` är en nivå mellan låg och hög, inte den kulinariska tillagningsgraden; den svenska UI-termen är därför `Medel`.

| Fullständig nyckel | Befintlig svenska | Sparad svenska | Motivering |
| --- | --- | --- | --- |
| `component::climacell::platform::sensor::state::climacell__pollen_index::medium` | `Medium` | `Medel` | Pollenindexnivå. |
| `component::tomorrowio::platform::sensor::state::tomorrowio__pollen_index::medium` | `Medium` | `Medel` | Pollenindexnivå. |
| `component::xiaomi_miio::platform::select::state::xiaomi_miio__ptc_level::medium` | `Medium` | `Medel` | Valbar effektnivå för PTC. |
| `component::nam::platform::sensor::state::nam__caqi_level::medium` | `Medium` | `Medel` | Luftkvalitetsindexnivå. |
| `component::litterrobot::entity::select::globe_brightness::state::medium` | `Medium` | `Medel` | Inställningsnivå för klotets ljusstyrka. |

Varje ändring sparades och lästes tillbaka via Lokalise API. De verifierade live-posterna finns i den kanoniska Home Assistant-TMX:en.
