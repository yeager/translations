# Home Assistant Core, svenska: tomma etiketter 2026-11-15

## Omfattning

Granskning av samtliga svenska översättningar som innehöll orden `Tom` eller
`Tomt` i Lokalise-projektet Home Assistant Core.

## Resultat

Elva pluralnycklar hade den engelska källtexten `{\"one\":\"\",\"other\":\"\"}`
men den svenska översättningen `{\"one\":\"Tom\",\"other\":\"Tomma\"}`.
De återställdes via Lokalise API till avsiktligt tomma pluralvärden.

Berörda nycklar:

- `component::arcam_fmj::config::error`
- `component::firmata::config::step`
- `component::rfxtrx`
- `component::rfxtrx::config::error`
- `component::rfxtrx::config::step`
- `component::dsmr::config::error`
- `component::dsmr::config::step`
- `component::roku::config::step::discovery_confirm::data`
- `component::kraken::config::error`
- `component::kraken::config::step::user::data`
- `component::switchbot::config::error`

## Verifiering

- Lokalise API läste tillbaka samtliga elva svenska värden som tomma.
- En ny fullständig API-sökning över 3 866 nycklar fann 0 svenska träffar på
  orden `Tom` eller `Tomt`.

## Status

Ändringarna är sparade direkt i Lokalise. Ingen upstream-PR krävs eftersom
Lokalise är projektets etablerade översättningskanal.
