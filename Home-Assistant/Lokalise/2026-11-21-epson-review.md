# Core — Epson

Datum: 2026-11-21

Alla 13 Epson-strängar hämtades från Lokalise och granskades mot aktuell källtext. Två ändringar sparades direkt och lästes tillbaka.

| Nyckel | Före | Efter | Motivering |
| --- | --- | --- | --- |
| `component::epson::config::step::user::data_description::host` | `Värdnamn eller IP-adress för din Epson-projektor.` | `Värdnamnet, IP-adressen eller serieporten för din Epson-projektor.` | Återställer borttappad serieport och samordnar bestämd form. |
| `component::epson::selector::connection_type::options::serial` | `Serienummer` | `Seriell` | `Serial` är anslutningstyp, inte ett serienummer. |

Home Assistant-TMX uppdaterades och validerades efter ändringen.
