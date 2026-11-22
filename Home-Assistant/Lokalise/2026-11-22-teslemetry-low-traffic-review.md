# Teslemetry: laddning under lågtrafik

Granskad 22 november 2026 mot aktuell källtext och svenska Lokalise-värden via
API. Sex relaterade service- och feltexter använde kvarlämnat engelskt
`off-peak` eller inkonsekvent `off peak`. De har standardiserats till
`lågtrafik`, Home Assistants etablerade term för tariffperioden.

| Fullständig nyckel | Tidigare text | Sparad text |
| --- | --- | --- |
| `component::teslemetry::exceptions::set_scheduled_departure_off_peak::message` | Sluttid för laddning off-peak krävs vid aktivering | Sluttid för laddning under lågtrafik krävs vid aktivering |
| `component::teslemetry::services::set_scheduled_departure::fields::end_off_peak_time::name` | Off-peak sluttid | Sluttid för laddning under lågtrafik |
| `component::teslemetry::services::set_scheduled_departure::fields::off_peak_charging_enabled::description` | Aktivera off peak-laddning. | Aktivera laddning under lågtrafik. |
| `component::teslemetry::services::set_scheduled_departure::fields::off_peak_charging_enabled::name` | Off peak-laddning aktiverad | Laddning under lågtrafik aktiverad |
| `component::teslemetry::services::set_scheduled_departure::fields::off_peak_charging_weekdays_only::description` | Aktivera off peak-laddning endast på vardagar. | Aktivera laddning under lågtrafik endast på vardagar. |
| `component::teslemetry::services::set_scheduled_departure::fields::off_peak_charging_weekdays_only::name` | Off peak-laddning endast vardagar | Laddning under lågtrafik endast på vardagar |

## Verifiering

- Samtliga sex ändringar sparades via Lokalise API och lästes tillbaka
  ordagrant.
- `svlang check` gav 10,0/10 för samtliga formuleringar.
- `hunspell-sv` gav inga stavningsavvikelser.
- `lågtrafik` följer befintlig Home Assistant-terminologi för *off-peak* i
  bland annat Plugwise och Huisbaasje.
- HA-TMX-validatorn: `valid: 3332 entries` efter uppdateringen
  (`swedish-tm`-commit `469da67`).

Ingen platshållare, kodreferens eller oavslutad referens berörs av denna
rättning.
