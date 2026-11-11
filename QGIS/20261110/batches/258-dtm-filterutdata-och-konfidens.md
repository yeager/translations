# QGIS: DTM-filterutdata och konfidens 258

Datum: 11 november 2026
Resurs: `qgis-application`, språk `sv`
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen fortsätter DTM-lutningsfiltret. Den skiljer filterkärnan från själva
filtret och använder konsekvent `konfidensintervall`, `höjdkriterium` och
`utdatalager` i parameter- och resultattexterna.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Choose whether to apply the filter kernel without modification or to use a confidence interval to relax or amplify the height criterium.` | `Välj huruvida att använda filterkärnan utan modifiering eller att använda ett konfidensintervall för att försvaga eller förstärka höjdkriteriet.` | `Välj om filterkärnan ska användas utan ändring eller om ett konfidensintervall ska användas för att mildra eller förstärka höjdkriteriet.` |
| `The standard deviation used to calculate a 5% confidence interval applied to the height threshold.` | `Standardavvikelsen som används för att beräkna 5%-konfidensintervallet applicerat på tröskelvärdet för höjd.` | `Standardavvikelsen som används för att beräkna ett konfidensintervall på 5 % för höjdtröskeln.` |
| `The filtered DEM containing only cells classified as ground.` | `Den filtrerade DEM innehållande endast celler klassificerade som mark.` | `Den filtrerade DEM:en innehåller endast celler som har klassificerats som mark.` |
| `Output layer (non-ground objects)` | `Utdatalager (icke-mark-objekt)` | `Utdatalager (objekt som inte är mark)` |
| `The non-ground objects removed by the filter.` | `Icke-mark-objekt borttagna av filtret.` | `Objekten som inte är mark och som har tagits bort av filtret.` |

Ingen extern ändring har gjorts. De rekommenderade texterna är lokala
kandidater tills de har jämförts mot aktuella Transifex-enheter vid en senare
uppladdning. Ändringarna är lokalt granskade och inte skickade externt.
