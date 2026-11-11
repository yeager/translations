# QGIS: rasterattributtabeller och datakälla 245

Datum: 11 november 2026
Resurs: `qgis-application`, språk `sv`
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen granskar felmeddelanden och fältnamn i rasterattributtabellen samt
rasterdatakällans gränssnitt. `GFU_AlphaMax` och talen `0-255` är
maskinläsbara namn och värden och bevaras.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Error creating Raster Attribute Table table: %1.` | `Fel vid skapande av attributtabell för raster: %1` | `Fel när rasterattributtabellen skapades: %1.` |
| `Error creating Raster Attribute Table table: could not add rows.` | `Fel vid skapande av attributtabell för raster: kunde inte lägga till rader.` | `Fel när rasterattributtabellen skapades: kunde inte lägga till rader.` |
| `Error reading Raster Attribute Table table from file: number of fields and number of attributes do not match.` | `Fel vid läsning av attributtabell för raster från fil: antal fält och antal attribut matchar inte.` | `Fel vid läsning av rasterattributtabellen från fil: antalet fält och attribut stämmer inte överens.` |
| `The attribute table has no MinMax nor a pair of Min and Max fields.` | `Attributtabellen har inget MinMax och inte heller ett par fält för min och max.` | `Attributtabellen har varken ett MinMax-fält eller ett par fält för min och max.` |
| `Alpha` | `Alpha` | `Alfa` |
| `Alpha Minimum` | `Alpha minimum` | `Alfaminimum` |
| `Alpha Maximum` | `Alpha maximum` | `Alfamaximum` |
| `Maximum Count` | `Största antal` | `Maximalt antal` |
| `Class Minimum Value` | `Klass min-värde` | `Klassens minimivärde` |
| `Class Maximum Value` | `Klass max-värde` | `Klassens maximivärde` |
| `Maximum GFU value(equals to GFU_AlphaMax+1 currently)` | `Största GFU-värde (lika med GFU_AlphaMax + 1 för närvarande)` | `Högsta GFU-värdet (motsvarar för närvarande GFU_AlphaMax + 1)` |
| `Attribute Table Write Error` | `Skrivning till attributtabell misslyckades` | `Fel när attributtabellen sparades` |
| `The raster attribute table is not set.` | `Attributtabell för raster är inte satt.` | `Rasterattributtabellen är inte angiven.` |
| `The attribute table does not seem to be valid and it may produce an unusable symbology, validation errors:<br>%1<br>` | `Attributtabellen verkar ogiltig och kan komma att framställa en oanvändbar symbologi, valideringsfel: <br>%1<br>` | `Attributtabellen verkar vara ogiltig och kan ge en oanvändbar symbologi. Valideringsfel:<br>%1<br>` |
| `The existing symbology for the raster will be replaced by a new symbology from the attribute table and any unsaved changes to the current symbology will be lost, do you want to proceed?` | `Den befintliga symbologin för rastret kommer att ersättas med ny symbologi från attributtabellen och alla osparade ändringar för aktuell symbologi kommer förloras, vill du fortsätta?` | `Rastrets befintliga symbologi ersätts med ny symbologi från attributtabellen. Osparade ändringar i den aktuella symbologin går förlorade. Vill du fortsätta?` |
| `The classification returned no classes.` | `Klassificeringen skapade inga klasser` | `Klassificeringen gav inga klasser.` |
| `Error adding color column` | `Fel vid tilläggning av färgkolumn` | `Fel när färgkolumnen lades till` |
| `Error adding new column` | `Fel vid tilläggning av ny kolumn ` | `Fel när en ny kolumn lades till` |
| `Error adding row` | `Fel vid tilläggning av ny rad ` | `Fel när en rad lades till` |

Ingen extern ändring har gjorts. De rekommenderade texterna är lokala
kandidater tills de har jämförts mot aktuella Transifex-enheter vid en senare
uppladdning.
