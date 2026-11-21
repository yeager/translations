# Home Assistant Core – Ridwell

Datum: 2026-11-21  
Källa: aktuell Core `2fdaa177`, `homeassistant/components/ridwell/strings.json`  
Status: samtliga 18 aktuella strängar granskade mot Lokalise och källtext.

Referenser, återautentiseringstext och resterande måltexter är korrekta.
Två valtexter behöver rättas:

| Nyckel | Befintlig text | Föreslagen text |
| --- | --- | --- |
| `component::ridwell::selector::conf_calendar_title::options::rotating_category` | `Roterar kategori` | `Roterande kategori` |
| `component::ridwell::options::step::init::data_description::conf_calendar_title` | `Detaljer som inkluderas (inom parentes) efter evenemangssammanfattningen/titeln kan vara upphämtningsstat, namnet på nästa roterande kategori eller inga detaljer alls.` | `Detaljer som inkluderas (inom parentes) efter evenemangssammanfattningen/titeln kan vara upphämtningsstatus, namnet på nästa roterande kategori eller inga detaljer alls.` |

Korrigeringarna är sparade och återlästa via Lokalise API 2026-11-21 och
ingår i den verifierade HA-TMX:en med översättnings-ID `6930939222` och
`6930938966`.
