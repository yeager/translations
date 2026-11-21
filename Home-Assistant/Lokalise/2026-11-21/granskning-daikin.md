# Home Assistant Core – Daikin

Datum: 2026-11-21

Alla 45 aktuella strängar jämfördes med Core `2fdaa177` och direkt återlästes från Lokalise. Konfiguration, zonfel, API-termer, effektstyrning och platshållarna `{zone_id}`, `{max_zone}` och `{error}` kontrollerades.

| Nyckel | Befintlig text | Sparad text | Motivering |
| --- | --- | --- | --- |
| `component::daikin::entity::sensor::cool_energy_consumption::name` | `Kyla energiförbrukning (senaste timmen)` | `Energiförbrukning för kyla (senaste timmen)` | Korrekt svensk nominalfras och parallell form med värmeetiketten. |

Ändringen PUT-sparades och direkt återlästes. Det verifierade Core-TMX-minnet validerades efter uppdateringen till 2 026 poster.
