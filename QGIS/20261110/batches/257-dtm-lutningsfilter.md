# QGIS: DTM-lutningsfilter 257

Datum: 11 november 2026
Resurs: `qgis-application`, språk `sv`
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen granskar ett DTM-filter som klassificerar bildpunkter i en digital
höjdmodell. `DTM` och `DEM` behålls som etablerade förkortningar. `pixel`
följer QGIS-termen `bildpunkt`, och `kernel` avser filterkärnan.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `DTM filter (slope-based)` | `DTM-filter (lutningsbaserade)` | `DTM-filter (lutningsbaserat)` |
| `Filters a Digital Elevation Model in order to classify its cells into ground and object (non-ground) cells.` | `Filtrerar en digital höjdmodell (DEM) för att klassificera dess celler i mark- och objekt- (icke mark) celler.` | `Filtrerar en digital höjdmodell (DEM) för att klassificera dess celler som markceller eller objektceller (icke-markceller).` |
| `Kernel radius (pixels)` | `Kärnradie (pixel)` | `Kärnradie (bildpunkter)` |
| `The radius of the filter kernel (in pixels). Must be large enough to reach ground cells next to non-ground objects.` | `Radien av filterkärnan (i pixel). Måste vara stort nog att nå markceller bredvid icke-mark-objekt.` | `Filterkärnans radie i bildpunkter. Den måste vara tillräckligt stor för att nå markceller intill objekt som inte är mark.` |
| `The approximate terrain slope in %. The terrain slope must be adjusted to account for the ratio of height units vs raster pixel dimensions. Used to relax the filter criterium in steeper terrain.` | `Den approximativa lutningen i %. Terränglutningen måste justeras för att ta hänsyn till kvoten höjdenheter mot rasterpixelns dimensioner. Används för att försvaga filterkriteriet i brantare terräng.` | `Den uppskattade terränglutningen i procent. Terränglutningen måste justeras med hänsyn till förhållandet mellan höjdenheterna och rasterbildpunkternas dimensioner. Används för att mildra filterkriteriet i brantare terräng.` |

Ingen extern ändring har gjorts. De rekommenderade texterna är lokala
kandidater tills de har jämförts mot aktuella Transifex-enheter vid en senare
uppladdning. Ändringarna är lokalt granskade och inte skickade externt.
