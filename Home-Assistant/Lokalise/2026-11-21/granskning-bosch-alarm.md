# Home Assistant Core – Bosch Alarm

Datum: 2026-11-21  
Källa: Core `2fdaa177`, `homeassistant/components/bosch_alarm/strings.json` och Lokalise API med direkt återläsning.

Status: samtliga 74 aktuella Lokalise-poster är radgranskade och återlästa. En korrigering är sparad och återläst.

| Nyckel | Befintlig text | Sparad text | Motivering |
|---|---|---|---|
| `entity::binary_sensor::panel_fault_user_code_tamper_since_rps_hang_up::name` | `Sabotage av användarkod sedan senaste RPS-anslutning` | `Sabotage av användarkod sedan den senaste RPS-anslutningen` | Korrekt bestämd form och konsekvens med övriga RPS-rader. |

Autentisering, panelanslutning, felstatusar, larmgrupper, dörrstatus, undantag och datum/tid-tjänsten är kontrollerade. Platshållarna `{model}`, `{host}` och `{target}` är bevarade. TMX-ledgern innehåller korrigeringen och är validerad.
