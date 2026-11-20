# Home Assistant Core – svensk granskning, sida 548

Datum: 2026-11-20  
Status: sparat och återläst i Lokalise

Granskade nycklar omfattar Plugwise. `Off-peak` och `peak` översätts konsekvent som `lågtrafik` respektive `högtrafik`; `point` avser ett punktvärde, inte en högsta punkt.

| Fullständig nyckel | Tidigare svenska | Sparad svenska | Motivering |
| --- | --- | --- | --- |
| `component::plugwise::entity::sensor::electricity_consumed_interval::name` | `Elförbrukning intervall` | `Elförbrukning per intervall` | Korrekt svensk relation. |
| `component::plugwise::entity::sensor::electricity_consumed_off_peak_cumulative::name` | `Elförbrukning off-peak kumulativt` | `Ackumulerad elförbrukning under lågtrafik` | Översatt tariffterm och naturlig livstids-/summaetikett. |
| `component::plugwise::entity::sensor::electricity_consumed_off_peak_interval::name` | `Elförbrukning off-peak intervall` | `Elförbrukning under lågtrafik per intervall` | Översatt tariffterm och korrekt relation. |
| `component::plugwise::entity::sensor::electricity_consumed_off_peak_point::name` | `Elförbrukning off-peak högsta punkt` | `Elförbrukning under lågtrafik, punktvärde` | `Point` är punktvärde, inte högsta punkt. |
| `component::plugwise::entity::sensor::electricity_consumed_peak_cumulative::name` | `Elförbrukning on-peak kumulativt` | `Ackumulerad elförbrukning under högtrafik` | Översatt tariffterm och naturlig summaetikett. |
| `component::plugwise::entity::sensor::electricity_consumed_peak_interval::name` | `Elförbrukning on-peak intervall` | `Elförbrukning under högtrafik per intervall` | Översatt tariffterm och korrekt relation. |
| `component::plugwise::entity::sensor::electricity_consumed_peak_point::name` | `Elförbrukning on-peak högsta punkt` | `Elförbrukning under högtrafik, punktvärde` | `Point` är punktvärde, inte högsta punkt. |
| `component::plugwise::entity::sensor::electricity_consumed_point::name` | `Elförbrukning högsta punkt` | `Elförbrukning, punktvärde` | `Point` är punktvärde, inte högsta punkt. |
| `component::plugwise::entity::sensor::electricity_produced_interval::name` | `Elproduktion intervall` | `Elproduktion per intervall` | Korrekt svensk relation. |
| `component::plugwise::entity::sensor::electricity_produced_off_peak_cumulative::name` | `Elproduktion off-peak kumulativt` | `Ackumulerad elproduktion under lågtrafik` | Översatt tariffterm och naturlig summaetikett. |
| `component::plugwise::entity::sensor::electricity_produced_off_peak_interval::name` | `Elproduktion off-peak intervall` | `Elproduktion under lågtrafik per intervall` | Översatt tariffterm och korrekt relation. |
| `component::plugwise::entity::sensor::electricity_produced_off_peak_point::name` | `Elproduktion off-peak högsta punkt` | `Elproduktion under lågtrafik, punktvärde` | `Point` är punktvärde, inte högsta punkt. |
| `component::plugwise::entity::sensor::electricity_produced_peak_cumulative::name` | `Elproduktion on-peak kumulativt` | `Ackumulerad elproduktion under högtrafik` | Översatt tariffterm och naturlig summaetikett. |
