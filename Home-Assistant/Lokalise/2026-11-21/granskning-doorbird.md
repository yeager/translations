# Home Assistant Core – DoorBird

Datum: 2026-11-21

Alla 41 aktuella strängar jämfördes med Core `2fdaa177` och direkt återlästes från Lokalise. Konfiguration, händelser, gamla kameraentiteter, Markdown och `{name}`, `{host}`, `{error}`, `{entity_id}`, `{entity_name}`, `{docs_url}` och `{items}` kontrollerades.

| Nyckel | Befintlig text | Sparad text | Motivering |
| --- | --- | --- | --- |
| `config::abort::not_doorbird_device` | `...inte en DoorBird` | `...inte en DoorBird-enhet` | Fullständig svensk produktnamnssats. |
| `entity::camera::last_ring::name` | `Senaste ringklocka` | `Senaste ringning` | Avser senaste ringhändelsen. |
| `entity::image::last_ring::name` | `Senaste ringklocka` | `Senaste ringning` | Samma etikett för bildentiteten. |
| `entity::event::doorbell::...::ring` | `Signal` | `Ringning` | Rätt händelsebetydelse. |
| `config::abort::not_ipv4_address` | `IPv4 adresser` | `IPv4-adresser` | Korrekt sammansättning. |
| `config::abort::wrong_device` | `MAC adress` | `MAC-adress` | Korrekt sammansättning. |

Ändringarna PUT-sparades och direkt återlästes. Det verifierade Core-TMX-minnet validerades efter uppdateringen till 2 089 poster.
