# Streamlabs Water: fullständig svensk granskning

Granskad 22 november 2026 mot aktuell källtext och aktuella svenska
översättningar i Lokalise via API. Samtliga 14 strängar i komponenten
`streamlabswater` har lästs från Lokalise. Inga platshållare eller pluralformer
förekommer.

## Rättningar sparade i Lokalise

| Fullständig nyckel | Tidigare text | Sparad text | Motivering |
| --- | --- | --- | --- |
| `component::streamlabswater::services::set_away_mode::description` | Ställer in hemma/borta-läget för en Streamlabs vattenmonitor. | Ställer in hemma/borta-läget för en Streamlabs Water Monitor. | Produktnamnet ska bevaras. |
| `component::streamlabswater::entity::sensor::daily_usage::name` | Daglig användning | Daglig vattenförbrukning | Anger tydligt vad sensorn mäter. |
| `component::streamlabswater::entity::sensor::monthly_usage::name` | Månatlig användning | Månatlig vattenförbrukning | Anger tydligt vad sensorn mäter. |
| `component::streamlabswater::entity::sensor::yearly_usage::name` | Årlig användning | Årlig vattenförbrukning | Anger tydligt vad sensorn mäter. |

Ändringarna verifierades genom läsning efter skrivning i Lokalise. De fyra
posterna finns också i det validerade HA-minnet i `swedish-tm`.

## Kontrollerade utan ändring

| Fullständig nyckel | Aktuell svensk text |
| --- | --- |
| `component::streamlabswater::services::set_away_mode::fields::away_mode::description` | Hemma eller borta. |
| `component::streamlabswater::services::set_away_mode::fields::away_mode::name` | Bortaläge |
| `component::streamlabswater::services::set_away_mode::name` | Ställ in bortaläge |
| `component::streamlabswater::config::abort::already_configured` | Enheten är redan konfigurerad |
| `component::streamlabswater::config::error::cannot_connect` | Det gick inte att ansluta |
| `component::streamlabswater::config::error::unknown` | Oväntat fel |
| `component::streamlabswater::config::step::user::data::api_key` | API-nyckel |
| `component::streamlabswater::services::set_away_mode::fields::location_id::description` | Plats-ID för Streamlabs Water Monitor. |
| `component::streamlabswater::services::set_away_mode::fields::location_id::name` | Plats-ID |
| `component::streamlabswater::entity::binary_sensor::away_mode::name` | Bortaläge |

## Verifiering

- Lokalise API: samtliga 14 svenska översättningar hämtades direkt efter
  rättningarna och motsvarar tabellerna ovan.
- `svlang check`: 10,0/10 för de ändrade formuleringarna. Verktyget markerar
  endast produktnamnet `Streamlabs Water` som ovanligt, vilket är väntat och
  korrekt.
- `hunspell-sv`: endast orden i produktnamnet saknas i ordlistan.
- Terminologi: `vattenförbrukning` är mer specifikt och naturligt än
  `användning` för vattenmätning.

Ingen osäker fråga eller oavslutad referens återstår för komponenten.
