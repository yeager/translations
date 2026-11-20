# Home Assistant Core – svensk granskning, sida 508

Datum: 2026-11-20  
Status: sparat och återläst i Lokalise

Granskade nycklar omfattar Workday, Huisbaasje och AdGuard. `Lågtrafik`/`högtrafik` används för tariffperioderna (off-peak/peak); `importeffekt` och `exporteffekt` gör in-/utflödet entydigt.

| Fullständig nyckel | Tidigare svenska | Sparad svenska | Motivering |
| --- | --- | --- | --- |
| `component::workday::options::step::init::description` | `Ändra ytterligare alternativ för {name} konfigurerat för land {country}` | `Ändra ytterligare alternativ för {name}, som har konfigurerats för landet {country}` | Korrekt satskonstruktion och bestämd form. |
| `component::huisbaasje::entity::sensor::current_power_off_peak::name` | `Aktuell ineffekt off-peak` | `Aktuell importeffekt under lågtrafik` | Översatt tariffterm och tydlig fackterm. |
| `component::huisbaasje::entity::sensor::current_power_out_off_peak::name` | `Aktuell uteffekt off-peak` | `Aktuell exporteffekt under lågtrafik` | Översatt tariffterm och tydlig fackterm. |
| `component::huisbaasje::entity::sensor::current_power_out_peak::name` | `Aktuell uteffekt peak` | `Aktuell exporteffekt under högtrafik` | Översatt tariffterm och tydlig fackterm. |
| `component::huisbaasje::entity::sensor::current_power_peak::name` | `Aktuell ineffekt peak` | `Aktuell importeffekt under högtrafik` | Översatt tariffterm och tydlig fackterm. |
| `component::huisbaasje::entity::sensor::energy_consumption_off_peak_today::name` | `Elförbrukning off-peak i dag` | `Elförbrukning under lågtrafik i dag` | Översatt tariffterm. |
| `component::huisbaasje::entity::sensor::energy_consumption_peak_today::name` | `Elförbrukning peak i dag` | `Elförbrukning under högtrafik i dag` | Översatt tariffterm. |
| `component::huisbaasje::entity::sensor::energy_month::name` | `El aktuell månad` | `El denna månad` | Naturligt svenskt tidsuttryck. |
| `component::huisbaasje::entity::sensor::energy_production_off_peak_today::name` | `Elproduktion off-peak i dag` | `Elproduktion under lågtrafik i dag` | Översatt tariffterm. |
| `component::huisbaasje::entity::sensor::energy_production_peak_today::name` | `Elproduktion peak i dag` | `Elproduktion under högtrafik i dag` | Översatt tariffterm. |
| `component::huisbaasje::entity::sensor::energy_week::name` | `El aktuell vecka` | `El denna vecka` | Naturligt svenskt tidsuttryck. |
| `component::huisbaasje::entity::sensor::energy_year::name` | `El aktuellt år` | `El i år` | Naturligt svenskt tidsuttryck. |
| `component::huisbaasje::entity::sensor::gas_month::name` | `Gas aktuell månad` | `Gas denna månad` | Naturligt svenskt tidsuttryck. |
| `component::huisbaasje::entity::sensor::gas_week::name` | `Gas aktuell vecka` | `Gas denna vecka` | Naturligt svenskt tidsuttryck. |
| `component::huisbaasje::entity::sensor::gas_year::name` | `Gas aktuellt år` | `Gas i år` | Naturligt svenskt tidsuttryck. |
