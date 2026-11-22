# Rympro: fullständig svensk granskning

Granskad 22 november 2026 mot aktuell källtext och aktuella svenska
översättningar i Lokalise via API. Samtliga elva strängar i komponenten
`rympro` har lästs från Lokalise. Inga nya ändringar behövdes.

| Fullständig nyckel | Aktuell svensk text |
| --- | --- |
| `component::rympro::config::abort::already_configured` | Enheten är redan konfigurerad |
| `component::rympro::config::error::cannot_connect` | Det gick inte att ansluta |
| `component::rympro::config::error::invalid_auth` | Ogiltig autentisering |
| `component::rympro::config::error::unknown` | Oväntat fel |
| `component::rympro::config::step::user::data::email` | E-post |
| `component::rympro::config::step::user::data::password` | Lösenord |
| `component::rympro::entity::sensor::total_consumption::name` | Total förbrukning |
| `component::rympro::entity::sensor::monthly_forecast::name` | Månadsprognos |
| `component::rympro::config::abort::reauth_successful` | Återautentisering lyckades |
| `component::rympro::entity::sensor::daily_consumption::name` | Daglig förbrukning |
| `component::rympro::entity::sensor::monthly_consumption::name` | Månadsförbrukning |

## Verifiering

- Lokalise API: alla elva svenska översättningar hämtades direkt vid
  granskningen.
- `förbrukning` används konsekvent för energikonsumtion och `månadsprognos`
  anger tydligt prognosperioden.
- `Återautentisering` följer Home Assistants etablerade terminologi.

Ingen osäker fråga eller oavslutad referens återstår för komponenten.
