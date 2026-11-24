# IAMMETER: exporterad energi och effektfaktor

| Fullständig nyckel | Befintlig svenska | Sparad svenska | Motivering |
| --- | --- | --- | --- |
| `component::iammeter::entity::sensor::export_grid_a::name` | `Nätexport A` | `Exporterad energi till elnätet A` | Sensorn har energienhet och energiklass; formuleringen anger att energin exporteras till elnätet. |
| `component::iammeter::entity::sensor::export_grid_b::name` | `Nätexport B` | `Exporterad energi till elnätet B` | Samma riktning och storhet för fas B. |
| `component::iammeter::entity::sensor::export_grid_c::name` | `Nätexport C` | `Exporterad energi till elnätet C` | Samma riktning och storhet för fas C. |
| `component::iammeter::entity::sensor::pf_a::name` | `PF A` | `Effektfaktor A` | Källkoden anger sensor device class `power_factor`; svensk term skrivs ut. |
| `component::iammeter::entity::sensor::pf_b::name` | `PF B` | `Effektfaktor B` | Samma sensorstorhet för fas B. |
| `component::iammeter::entity::sensor::pf_c::name` | `PF C` | `Effektfaktor C` | Samma sensorstorhet för fas C. |

Källtext och enheter kontrollerades i aktuell Iammeter `strings.json` och `sensor.py`. Sex poster sparades/återlästes i Lokalise och synkades till snapshot, PO och TMX. Övriga 15 namn i komponentbatchen verifierades som befintliga och lämnades oförändrade.
