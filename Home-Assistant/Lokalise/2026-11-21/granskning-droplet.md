# Home Assistant Core – Droplet

Datum: 2026-11-21

Alla 22 aktuella strängar jämfördes med Core `2fdaa177` och direkt återlästes från Lokalise. Parkoppling, IP-adress, flödesvarningar och `{device_name}` kontrollerades.

| Nyckel | Befintlig text | Sparad text | Motivering |
| --- | --- | --- | --- |
| `config::step::confirm::data::code` | `Parnings kod` | `Parkopplingskod` | Korrekt svensk sammansättning och konsekvent med parallellt fält. |
| `config::step::user::title` | `Konfigurera Droplet-integration` | `Konfigurera Droplet-integrationen` | Fullständig svensk integrationsbenämning. |

Ändringarna PUT-sparades och direkt återlästes. Det verifierade Core-TMX-minnet validerades efter uppdateringen till 2 108 poster.
