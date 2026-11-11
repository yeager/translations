# QGIS: M3C2 och punktmolnsurval 255

Datum: 11 november 2026
Resurs: `qgis-application`, språk `sv`
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen granskar PDAL-verktyget för jämförelse av punktmoln. `M3C2`,
den utskrivna förklaringen av förkortningen och dimensionsnamnen är tekniska
namn och bevaras. `subsampling` är däremot en UI-etikett och översätts här
till `delurval`.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `This algorithm compares two point clouds using an M3C2 (Multiscale Model-to-Model Cloud Comparison) algorithm and outputs a subset (filtered using Poisson sampling, based on Subsampling cell size parameter ) of the original point cloud.` | `Denna algoritm jämför två punktmoln genom att använda- (Multiscale Model-to-Model Cloud Comparison) algoritmen och skapar en delmängd (filtrerad med Poisson-sampling, baserad på parametern Cellstorlek för subsampling) av det ursprungliga punktmolnet.` | `Denna algoritm jämför två punktmoln med en M3C2-algoritm (Multiscale Model-to-Model Cloud Comparison) och skapar en delmängd av det ursprungliga punktmolnet. Delmängden filtreras med Poisson-sampling utifrån parametern Cellstorlek för delurval.` |
| `The output point cloud will have several new dimensions: m3c2_distance, m3c2_uncertainty, m3c2_significant, m3c2_std_dev1, m3c2_std_dev2, m3c2_count1 and m3c2_count2.` | `Det nya punktmolnet kommer att ha flera nya dimensioner: m3c2_distance, m3c2_uncertainty, m3c2_significant, m3c2_std_dev1, m3c2_std_dev2, m3c2_count1 and m3c2_count2.` | `Utdatapunktmolnet kommer att ha flera nya dimensioner: m3c2_distance, m3c2_uncertainty, m3c2_significant, m3c2_std_dev1, m3c2_std_dev2, m3c2_count1 och m3c2_count2.` |
| `Compares two point clouds using M3C2 algorithm and outputs a subsample of the input point cloud containing additional dimensions describing the differences.` | `Jämför två punktmoln genom att använda) M3C2-algoritmen och skapar en delmängd av det ursprungliga punktmolnet med ytterligare dimensioner som beskriver skillnaderna.` | `Jämför två punktmoln med M3C2-algoritmen och skapar ett delurval av indatapunktmolnet med ytterligare dimensioner som beskriver skillnaderna.` |
| `Subsampling cell size` | `Cellstorlek för subsampling` | `Cellstorlek för delurval` |

Ingen extern ändring har gjorts. De rekommenderade texterna är lokala
kandidater tills de har jämförts mot aktuella Transifex-enheter vid en senare
uppladdning. Ändringarna är lokalt granskade och inte skickade externt.
