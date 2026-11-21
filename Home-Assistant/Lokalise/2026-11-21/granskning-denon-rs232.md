# Home Assistant Core – Denon RS-232

Datum: 2026-11-21

Alla 53 aktuella strängar jämfördes med Core `2fdaa177` och direkt återlästes från Lokalise. Konfiguration, samtliga ingångsetiketter och undantag kontrollerades. `{media_id}`, `{media_type}` och `{port}` är intakta.

| Nyckel | Befintlig text | Sparad text | Motivering |
| --- | --- | --- | --- |
| `config::step::user::data_description::device` | `Sökväg till serieporten att anslutas till` | `Sökväg till den serieport som ska användas för anslutning` | Idiomatisk och entydig svensk formulering. |
| `entity::media_player::receiver::state_attributes::source::state::mplay` | `Mediaspelare` | `Mediespelare` | Konsekvent svensk term. |

Ändringarna PUT-sparades och direkt återlästes. Det verifierade Core-TMX-minnet validerades efter uppdateringen till 2 049 poster.
