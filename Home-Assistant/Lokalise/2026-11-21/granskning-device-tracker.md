# Home Assistant Core – Device Tracker

Datum: 2026-11-21

Alla 70 aktuella strängar jämfördes med Core `2fdaa177` och direkt återlästes från Lokalise. Tillstånd, äldre `see`-tjänsten, automatiseringar, issues och platshållarna `{entity_name}`, `{entity_id}`, `{zone}` och `{docs_url}` kontrollerades.

| Nyckel | Befintlig text | Sparad text | Motivering |
| --- | --- | --- | --- |
| `common::trigger_for_name` | `I åtminstone` | `I minst` | Korrekt svensk tidsfras. |
| `triggers::entered_home::fields::for::name` | `I åtminstone` | `I minst` | Direkt motsvarande triggerfält. |
| `triggers::left_home::fields::for::name` | `I åtminstone` | `I minst` | Direkt motsvarande triggerfält. |

Ändringarna PUT-sparades och direkt återlästes. Det verifierade Core-TMX-minnet validerades efter uppdateringen till 2 056 poster.
