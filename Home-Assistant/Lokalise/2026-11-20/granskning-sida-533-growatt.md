# Home Assistant Core – svensk granskning, sida 533

Datum: 2026-11-20  
Status: sparat och återläst i Lokalise

Granskade nycklar omfattar Growatt Server. Korrekt befintliga nyckelreferenser lämnades oförändrade.

| Fullständig nyckel | Tidigare svenska | Sparad svenska | Motivering |
| --- | --- | --- | --- |
| `component::growatt_server::entity::sensor::storage_charge_storage_lifetime::name` | `Lagrad energi totalt livslängd` | `Ackumulerad lagrad energi` | Naturlig term för livstidstotal. |
| `component::growatt_server::entity::sensor::storage_current_1::name` | `PV1 ström till lagring` | `PV1-ström till lagring` | Korrekt bindestreck med förkortning. |
| `component::growatt_server::entity::sensor::storage_current_pv::name` | `Solel laddning ström` | `Ström för solladdning` | Korrekt svensk ordföljd och sammansättning. |
| `component::growatt_server::entity::sensor::storage_grid_amperage_input::name` | `Elnät laddning ström` | `Ström för laddning från elnätet` | Korrekt svensk ordföljd och relation. |
| `component::growatt_server::entity::sensor::storage_grid_charged_today::name` | `Elnät laddat i dag` | `Laddning från elnätet i dag` | Korrekt svensk relation. |
| `component::growatt_server::entity::sensor::storage_grid_discharge_today::name` | `Elnät urladdat i dag` | `Urladdning till elnätet i dag` | Korrekt svensk relation. |
| `component::growatt_server::entity::sensor::storage_grid_out_current::name` | `Elnät utström` | `Ström ut till elnätet` | Tydlig svensk mätetikett. |
| `component::growatt_server::entity::sensor::storage_load_percentage::name` | `Batterinivå` | `Lastprocent` | Källtexten avser last, inte batterinivå. |
