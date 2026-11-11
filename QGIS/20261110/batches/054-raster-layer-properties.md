# QGIS: rasterlageregenskaper 054

Datum: 10 november 2026  
Resurs: `qgis-application`, språk `sv`  
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`  
Källkod: `src/analysis/processing/qgsalgorithmrasterlayerproperties.cpp`

Rasteralgoritmens etiketter och korta hjälptexter granskas som en enhet. De
normaliserar QGIS etablerade termerna `utbredning`, `bildpunkt` och
`NoData-värde` samt rättar grammatik och dubbla blanksteg.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `extent,pixel,size,width,height` | `utsträckning,pixel,storlek,bredd,höjd` | `utbredning,bildpunkt,storlek,bredd,höjd` |
| `Band has a NoData value set` | `Band har  NoData-värden angivet` | `Bandet har ett NoData-värde angivet` |
| `Band NoData value` | `Bandets värde för NoData` | `Bandets NoData-värde` |
| `Returns basic properties of a given raster layer, including the extent, size in pixels and dimensions of pixels (in map units).` | `Returnerar grundläggande egenskaper för ett angivet rasterlager inklusive utsträckningen, storlek i pixlar och dimensioner för pixlar (i kartenheter).` | `Returnerar grundläggande egenskaper för ett angivet rasterlager, inklusive utbredningen, storlek i bildpunkter och bildpunkternas dimensioner (i kartenheter).` |
| `This algorithm returns basic properties of the given raster layer, including the extent, size in pixels and dimensions of pixels (in map units).\n\nIf an optional band number is specified then the NoData value for the selected band will also be returned.` | `Denna algoritm returnerar grundläggande egenskaper för ett angivet rasterlager, inklusive utsträckningen, storlek i pixlar och dimensioner för pixlar (i kartenheter).\n\nOm ett valfritt bandnummer anges så returneras  NoData-värdet för det valda bandet också.` | `Denna algoritm returnerar grundläggande egenskaper för det angivna rasterlagret, inklusive utbredningen, storlek i bildpunkter och bildpunkternas dimensioner (i kartenheter).\n\nOm ett valfritt bandnummer anges returneras även NoData-värdet för det valda bandet.` |
| `Number of bands in raster` | `Antal band i raster` | `Antal band i rastret` |

Den längre strängen måste vid en framtida uppladdning behålla sina två
radbrytningar. Ingen extern ändring har gjorts; Transifex-enheternas
identifierare behöver hämtas från den aktuella resursen innan en eventuell
deltafil kan skapas.
