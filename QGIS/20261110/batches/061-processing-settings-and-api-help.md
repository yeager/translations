# QGIS: inställningar och API-hjälp för geobearbetning 061

Datum: 10 november 2026  
Resurs: `qgis-application`, språk `sv`  
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`  
Källkod: `src/core/processing/qgsprocessing.cpp` och
`src/core/processing/qgsprocessingparametermeshdataset.h`

Granskningen omfattar inställningstexter och de korta hjälptexter som visas för
meshparametrars Python-liknande värden. Kodsyntaxen och PyQGIS-klassnamnen
bevaras exakt. I användargränssnittet används den etablerade termen
`utdata`; i utvecklarhjälpen översätts den förklarande texten men inte
`list[int]`, `dict{}` eller QGIS-klassnamnen.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Prefer filename as layer name` | `Föredra filnamn som lagernamn` | `Använd helst filnamnet som lagernamn` |
| `Override temporary output folder path` | `Åsidosätt temporär utdatakatalog` | `Åsidosätt sökvägen till den temporära utdatakatalogen` |
| `This algorithm drops existing primary keys or FID values and regenerates them in output layers.` | `Denna algoritm slänger befintliga primärnycklar eller FID-värden och återskapar dem i utdatalager.` | `Denna algoritm tar bort befintliga primärnycklar eller FID-värden och skapar dem på nytt i utdatalagren.` |
| `This algorithm may drop existing primary keys or FID values and regenerate them in output layers, depending on the input parameters.` | `Denna algoritm kan slänga befintliga primärnycklar eller FID-värden och återskapar dem i utdatalager, beroende på indataparametrar.` | `Beroende på indataparametrarna kan denna algoritm ta bort befintliga primärnycklar eller FID-värden och skapa dem på nytt i utdatalagren.` |
| `This algorithm uses ellipsoid based measurements and respects the current ellipsoid settings.` | `Denna algoritm använder ellipsoid-baseade mätningar och tar hänsyn till aktuella ellipsoid-inställningar.` | `Denna algoritm använder ellipsoidbaserade mätningar och tar hänsyn till de aktuella ellipsoidinställningarna.` |
| `list[int]: list of dataset group indexes, see QgsProcessingParameterMeshDatasetGroups docs` | `list[int]: lista på index för datasetsgrupper, se QgsProcessingParameterMeshDatasetGroups dokumantation` | `list[int]: lista över index för datamängdsgrupper, se dokumentationen för QgsProcessingParameterMeshDatasetGroups` |
| `dict{}: dictionary, see QgsProcessingParameterMeshDatasetTime docs` | `dict{}: dictionary, se QgsProcessingParameterMeshDatasetTime dokumentation` | `dict{}: ordbok, se dokumentationen för QgsProcessingParameterMeshDatasetTime` |

Ingen extern ändring har gjorts; aktuella Transifex-enhetsidentifierare behöver
hämtas innan en deltafil kan skapas.
