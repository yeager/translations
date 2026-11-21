# Home Assistant Core – Discovergy

Datum: 2026-11-21

Alla 25 aktuella strängar jämfördes med Core `2fdaa177` och direkt återlästes från Lokalise. Konfiguration, fasvärden, mätarundantag och `{meter_id}` kontrollerades.

| Nyckel | Befintlig text | Sparad text | Motivering |
| --- | --- | --- | --- |
| `entity::sensor::phase_1_power::name` | `Ström fas 1` | `Effekt i fas 1` | `power` är effekt, inte elektrisk ström. |
| `entity::sensor::phase_1_voltage::name` | `Spänning fas 1` | `Spänning i fas 1` | Korrekt svensk etikett. |
| `entity::sensor::phase_2_power::name` | `Ström fas 2` | `Effekt i fas 2` | `power` är effekt, inte elektrisk ström. |
| `entity::sensor::phase_2_voltage::name` | `Spänning fas 2` | `Spänning i fas 2` | Korrekt svensk etikett. |
| `entity::sensor::phase_3_power::name` | `Ström fas 3` | `Effekt i fas 3` | `power` är effekt, inte elektrisk ström. |
| `entity::sensor::phase_3_voltage::name` | `Spänning fas 3` | `Spänning i fas 3` | Korrekt svensk etikett. |

Ändringarna PUT-sparades och direkt återlästes. Det verifierade Core-TMX-minnet validerades efter uppdateringen till 2 074 poster.
