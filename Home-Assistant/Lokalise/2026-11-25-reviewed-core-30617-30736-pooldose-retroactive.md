# Retroaktiv terminologisynk – PoolDose Proportional (2026-11-25)

## Ändringar

Granskningen av `component::pooldose::entity::select::ph_type_dosing_method::state::proportional` visade att **Proportionell** är den etablerade tekniska formen för proportional dosering; minnet hade `Proportionerlig`. Eftersom fem PoolDose-nycklar använder samma källmål synkades mål och fyra ytterligare alias i Lokalise. Samtliga fem uppdateringar kontrollerades mot live-API.

| Fullständig nyckel | Källtext (EN) | Befintlig svenska | Sparad svenska |
|---|---|---|---|
| `component::pooldose::entity::sensor::peristaltic_ph_dosing::state::proportional` | Proportional | Proportionerlig | Proportionell |
| `component::pooldose::entity::select::cl_type_dosing_method::state::proportional` | Proportional | Proportionerlig | Proportionell |
| `component::pooldose::entity::select::orp_type_dosing_method::state::proportional` | Proportional | Proportionerlig | Proportionell |
| `component::pooldose::entity::sensor::peristaltic_cl_dosing::state::proportional` | Proportional | Proportionerlig | Proportionell |
| `component::pooldose::entity::sensor::peristaltic_orp_dosing::state::proportional` | Proportional | Proportionerlig | Proportionell |

Kanonisk Home Assistant Core-TM uppdaterades för alla nycklar med Lokalise-ID. Underlag: `2026-11-25-reviewed-core-30617-30736-pooldose-retroactive.json`.
