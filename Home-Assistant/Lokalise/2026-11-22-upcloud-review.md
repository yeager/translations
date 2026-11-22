# Home Assistant Core – UpCloud

Datum: 2026-11-22

Alla åtta UpCloud-strängar har kontrollerats rad för rad mot den aktuella
engelska källtexten och har även återlästs från Lokalise API. Ingen ändring
behövdes.

| Nyckel | Svenska |
| --- | --- |
| `component::upcloud::config::abort::already_configured` | Tjänsten är redan konfigurerad |
| `component::upcloud::config::error::cannot_connect` | Det gick inte att ansluta |
| `component::upcloud::config::error::invalid_auth` | Ogiltig autentisering |
| `component::upcloud::config::step::user::data::password` | Lösenord |
| `component::upcloud::config::step::user::data::username` | Användarnamn |
| `component::upcloud::options::step::init::data::scan_interval` | Uppdateringsintervall i sekunder, minst 30 |
| `component::upcloud::exceptions::authentication_failed::message` | Autentisering med UpCloud misslyckades |
| `component::upcloud::exceptions::cannot_connect::message` | Det gick inte att ansluta till UpCloud |

Kontroll: inga platshållare eller pluralformer berörs. Hunspell godkänner den
svenska texten; `UpCloud` är ett egennamn och därför en förväntad extern
ordlisteträff. Lokalise API visar i nuläget `is_reviewed=false` för raderna;
den kontrollflaggan kan inte sättas med den behörighet som projektets API-token
har (tidigare dokumenterat API-hinder), men innehållet är granskat.
