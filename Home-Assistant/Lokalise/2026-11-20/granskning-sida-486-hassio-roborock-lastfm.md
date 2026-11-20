# Home Assistant Core — granskning sida 486 (Hass.io, Roborock, IMAP och Last.fm)

Datum: 2026-11-20  
Status: dokumenterade förslag; **inte sparade i Lokalise**

| Fullständig nyckel | Befintlig svenska | Föreslagen svenska | Motivering |
|---|---|---|---|
| `component::hassio::issues::issue_mount_mount_failed::title` | `Nätverkslagringsenheten misslyckades` | `Det gick inte att montera nätverkslagringsenheten` | Gör felorsaken tydlig och idiomatisk i stället för att låta enheten själv ”misslyckas”. |
| `component::roborock::entity::sensor::filter_time_left::name` | `Filtertid kvar` | `Återstående tid för filtret` | Fullständig och idiomatisk sensorbenämning. |
| `component::roborock::entity::sensor::main_brush_time_left::name` | `Huvudborste tid kvar` | `Återstående tid för huvudborsten` | Rätt svensk ordföljd och bestämd form. |
| `component::roborock::entity::sensor::sensor_time_left::name` | `Sensortid kvar` | `Återstående tid för sensorn` | Fullständig och idiomatisk sensorbenämning. |
| `component::roborock::entity::sensor::side_brush_time_left::name` | `Sidoborste tid kvar` | `Återstående tid för sidoborsten` | Rätt svensk ordföljd och bestämd form. |
| `component::lastfm::config::step::friends::data::users` | `Last.fm användarnamn` | `Last.fm-användarnamn` | Bindestreck behövs när ett egennamn med punkt inleder en svensk sammansättning. |
| `component::lastfm::config::step::user::data::main_user` | `Last.fm användarnamn` | `Last.fm-användarnamn` | Bindestreck behövs när ett egennamn med punkt inleder en svensk sammansättning. |

Övriga 13 nycklar på sidan granskades utan dokumenterat ändringsförslag. Binärsensorutlösarna uttrycker korrekt start och stopp av laddning; Hass.io-platshållare, IMAP-mallen och Last.fm:s API-länk bevaras.
