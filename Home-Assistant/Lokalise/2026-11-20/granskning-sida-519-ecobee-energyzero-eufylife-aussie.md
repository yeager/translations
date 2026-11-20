# Home Assistant Core – svensk granskning, sida 519

Datum: 2026-11-20  
Status: sparat och återläst i Lokalise

Granskade nycklar omfattar ecobee, EnergyZero, eufyLife BLE och Aussie Broadband. Övriga befintliga mätetiketter lämnades oförändrade.

| Fullständig nyckel | Tidigare svenska | Sparad svenska | Motivering |
| --- | --- | --- | --- |
| `component::ecobee::entity::number::ventilator_min_type_away::name` | `Ventilator minsta tid borta` | `Ventilatorns minsta drifttid i bortaläge` | Korrekt genitiv, huvudord och lägesnamn. |
| `component::ecobee::entity::number::ventilator_min_type_home::name` | `Ventilator minsta tid hemma` | `Ventilatorns minsta drifttid i hemläge` | Korrekt genitiv, huvudord och lägesnamn. |
| `component::energyzero::entity::sensor::highest_price_time::name` | `Högsta marknadspris tidpunkt` | `Tidpunkt för högsta marknadspris` | Naturlig svensk ordföljd. |
| `component::energyzero::entity::sensor::lowest_price_time::name` | `Lägsta marknadspris tidpunkt` | `Tidpunkt för lägsta marknadspris` | Naturlig svensk ordföljd. |
| `component::energyzero::entity::sensor::percentage_of_max::name` | `Marknadsprocent av högsta` | `Marknadspris i procent av högsta priset` | Tydliggör både storhet och jämförelsevärde. |
| `component::aussie_broadband::entity::sensor::billing_cycle_length::name` | `Faktureringsperiod` | `Faktureringsperiodens längd` | `Length` saknades i måltexten. |
| `component::aussie_broadband::entity::sensor::billing_cycle_remaining::name` | `Återstående faktureringsperiod` | `Återstående del av faktureringsperioden` | Korrekt innebörd: återstående del, inte en annan period. |
| `component::aussie_broadband::entity::sensor::data_used::name` | `Använd data` | `Använd datamängd` | Korrekt svensk substantivfras. |
