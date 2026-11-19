# Sparad ändring för Sofar

Sparad och återläst i Lokalise 2026-11-19 efter kontroll mot tidigare granskningsrapport.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::sofar::config::step::reconfigure::data::unit_id` | Modbus unit ID | Modbus enhets-ID | Modbus-enhets-ID |

Bindestrecket markerar den svenska sammansättningen.

## Synkroniseringsresultat

Sparade och återlästa i Lokalise 2026-11-19 efter jämförelse med tidigare granskningsrapport.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::sofar::entity::sensor::sync_rtc_result::state::operation_in_progress` | Operation in progress | Operation pågår | Åtgärd pågår |
| `component::sofar::entity::sensor::sync_rtc_result::state::operation_failed_controller_refused_to_respond` | Operation failed: controller refused to respond | Åtgärden misslyckades: styrenheten svarade inte | Åtgärden misslyckades: styrenheten vägrade svara |

Den senare texten skiljer avvisat svar från det separata tillståndet utan svar.

## Nätstatus och programvara

Sparade och återlästa i Lokalise 2026-11-19 efter jämförelse med tidigare granskningsrapport.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::sofar::entity::sensor::system_state::state::grid_connected` | Grid connected | Nät anslutet | Ansluten till elnätet |
| `component::sofar::entity::sensor::software_version::name` | Software version | Mjukvaruversion | Programvaruversion |

Nätstatusen förtydligas och programvara används som svensk term för software.

## Total reaktiv effekt

Sparade och återlästa i Lokalise 2026-11-19 efter jämförelse med tidigare granskningsrapport.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::sofar::entity::sensor::reactive_power_output_total::name` | Reactive power output total | Reaktiv effekt utgång totalt | Total reaktiv uteffekt |
| `component::sofar::entity::sensor::reactive_power_offgrid_total::name` | Reactive power off-grid total | Reaktiv effekt off-grid totalt | Total reaktiv effekt vid ödrift |

De svenska benämningarna skiljer utgående effekt från effekt vid ödrift. Övriga effektförslag återstår.

## Reaktiv uteffekt per fas

Sparade och återlästa i Lokalise 2026-11-19 efter jämförelse med tidigare granskningsrapport.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::sofar::entity::sensor::reactive_power_output_l1::name` | Reactive power output L1 | Reaktiv effekt utgång L1 | Reaktiv uteffekt L1 |
| `component::sofar::entity::sensor::reactive_power_output_l2::name` | Reactive power output L2 | Reaktiv effekt utgång L2 | Reaktiv uteffekt L2 |
| `component::sofar::entity::sensor::reactive_power_output_l3::name` | Reactive power output L3 | Reaktiv effekt utgång L3 | Reaktiv uteffekt L3 |

Fasbeteckningarna bevarades och uttrycket följer den sparade termen för total reaktiv uteffekt.

## Effektfaktor per utgång

Sparade och återlästa i Lokalise 2026-11-19 efter jämförelse med tidigare granskningsrapport.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::sofar::entity::sensor::power_factor_output_l1::name` | Power factor output L1 | Effektfaktor utgång L1 | Effektfaktor för utgång L1 |
| `component::sofar::entity::sensor::power_factor_output_l2::name` | Power factor output L2 | Effektfaktor utgång L2 | Effektfaktor för utgång L2 |
| `component::sofar::entity::sensor::power_factor_output_l3::name` | Power factor output L3 | Effektfaktor utgång L3 | Effektfaktor för utgång L3 |

Fasbeteckningarna bevarades och relationen till utgången tydliggjordes.

## Spänning vid ödrift per fas

Sparade och återlästa i Lokalise 2026-11-19 efter jämförelse med tidigare granskningsrapport.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::sofar::entity::sensor::offgrid_voltage_l1::name` | Off-grid voltage L1 | Off-grid spänning L1 | Spänning vid ödrift L1 |
| `component::sofar::entity::sensor::offgrid_voltage_l2::name` | Off-grid voltage L2 | Off-grid spänning L2 | Spänning vid ödrift L2 |
| `component::sofar::entity::sensor::offgrid_voltage_l3::name` | Off-grid voltage L3 | Off-grid spänning L3 | Spänning vid ödrift L3 |

Fasbeteckningarna bevarades och termen följer den tidigare sparade ödriftsbenämningen.
