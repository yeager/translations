# HomeWizard: etiketter per fas

Sparat direkt i Lokalise och verifierat genom API-läsning efter skrivning.

| Nyckel | Tidigare | Sparad svensk text |
|---|---|---|
| `component::homewizard::entity::sensor::active_current_phase_a::name` | `Ström fas {phase}` | `Ström, fas {phase}` |
| `component::homewizard::entity::sensor::active_power_phase_w::name` | `Effektfas {phase}` | `Effekt, fas {phase}` |
| `component::homewizard::entity::sensor::active_voltage_phase_v::name` | `Spänning fas {phase}` | `Spänning, fas {phase}` |
| `component::homewizard::entity::sensor::active_apparent_power_phase_va::name` | `Skenbar effekt fas {phase}` | `Skenbar effekt, fas {phase}` |
| `component::homewizard::entity::sensor::active_power_factor_phase::name` | `Effektfaktor fas {phase}` | `Effektfaktor, fas {phase}` |
| `component::homewizard::entity::sensor::active_reactive_power_phase_var::name` | `Reaktiv effekt fas {phase}` | `Reaktiv effekt, fas {phase}` |

Källa för den verifierade TM-posten: `yeager/swedish-tm`, manifestet `Home-Assistant/2026-11-22-homewizard-phase-labels-verified.json`.
