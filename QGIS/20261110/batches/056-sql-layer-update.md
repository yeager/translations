# QGIS: uppdatering av SQL-lager 056

Datum: 10 november 2026  
Resurs: `qgis-application`, språk `sv`  
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`  
Källkod: `src/app/qgsapplayertreeviewmenuprovider.cpp:299–379`

Status- och feltexterna för SQL-lager innehåller talspråk, en stavmiss och
inkonsekventa sammansättningar. De granskas som en UI-enhet:

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Layer Update Success` | `Uppdatering av lager funkade` | `Lagret uppdaterades` |
| `The SQL layer was updated successfully` | `Det gick att uppdatera SQL-lagret` | `SQL-lagret uppdaterades.` |
| `layer is not valid, check the log messages for more information` | `lagret år inte giltigt, kolla loggmeddelanden för mer information` | `Lagret är inte giltigt. Kontrollera loggmeddelandena för mer information.` |
| `Layer Update Error` | `Uppdatering av lager, fel` | `Fel vid uppdatering av lager` |
| `Error updating the SQL layer: %1` | `Fel vid uppdatering av SQL-lager: %1` | `Fel vid uppdatering av SQL-lagret: %1` |
| `Error creating the SQL layer: %1` | `Fel vid skapande av SQL-lager: %1` | `Fel vid skapande av SQL-lagret: %1` |

Produkt- och tekniknamnet SQL och felplatshållaren `%1` bevaras. Ingen extern
ändring har gjorts; Transifex-enheternas identifierare behöver hämtas från den
aktuella resursen innan en eventuell deltafil kan skapas.
