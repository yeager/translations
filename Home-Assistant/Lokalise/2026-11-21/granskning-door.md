# Home Assistant Core – Door

Datum: 2026-11-21

Alla 32 aktuella strängar jämfördes med Core `2fdaa177` och direkt återlästes från Lokalise. Dörrtillstånd, triggers, villkor och valen för flera entiteter kontrollerades.

| Nyckel | Befintlig text | Sparad text | Motivering |
| --- | --- | --- | --- |
| `common::trigger_for_name` | `I åtminstone` | `I minst` | Korrekt svensk tidsfras. |
| `triggers::closed::fields::for::name` | `I åtminstone` | `I minst` | Direkt motsvarande triggerfält. |
| `triggers::opened::fields::for::name` | `I åtminstone` | `I minst` | Direkt motsvarande triggerfält. |
| `common::condition_for_name` | `I åtminstone` | `I minst` | Korrekt svensk tidsfras. |
| `conditions::is_closed::fields::for::name` | `I åtminstone` | `I minst` | Direkt motsvarande villkorsfält. |
| `conditions::is_open::fields::for::name` | `I åtminstone` | `I minst` | Direkt motsvarande villkorsfält. |

Ändringarna PUT-sparades och direkt återlästes. Det verifierade Core-TMX-minnet validerades efter uppdateringen till 2 083 poster.
