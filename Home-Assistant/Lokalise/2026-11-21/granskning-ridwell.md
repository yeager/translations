# Home Assistant Core – Ridwell

Datum: 2026-11-21  
Källa: aktuell Core `2fdaa177`, `homeassistant/components/ridwell/strings.json`  
Status: samtliga 18 aktuella strängar granskade mot Lokalise och källtext.

Referenser, återautentiseringstext och resterande måltexter är korrekta.
Två valtexter behöver rättas:

| Nyckel | Befintlig text | Föreslagen text |
| --- | --- | --- |
| `component::ridwell::options::step::event::data::details::options::rotating_category` | `Roterar kategori` | `Roterande kategori` |
| `component::ridwell::options::step::event::data_description::details` | `Detaljer som inkluderas (inom parentes) efter evenemangssammanfattningen/titeln kan vara upphämtningsstat, namnet på nästa roterande kategori eller inga detaljer alls.` | `Detaljer som inkluderas (inom parentes) efter evenemangssammanfattningen/titeln kan vara upphämtningsstatus, namnet på nästa roterande kategori eller inga detaljer alls.` |

Förslagen är ännu inte sparade i Lokalise. De ska återläsas efter sparning
och därefter införas i den verifierade HA-TMX:en med Lokalise-ID.
