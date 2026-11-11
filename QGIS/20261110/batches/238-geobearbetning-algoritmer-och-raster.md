# QGIS: geobearbetning, algoritmer och raster 238

Datum: 11 november 2026
Resurs: `qgis-application`, språk `sv`
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen granskar gränssnittet för geobearbetning, fältmappning och
rasterjustering. `Python`, `JSON`, `qgis_process`, `EPSG`, `WKT`, `PROJ` och
kommandoradssyntax bevaras exakt där de förekommer.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Connection to the database not available` | `Anslutning till databasen inte tillgänglig` | `Anslutningen till databasen är inte tillgänglig` |
| `Color Presets Ramp` | `Förinställd färggradient` | `Förinställda färggradienter` |
| `Delete selected field` | `Radera valt fält` | `Ta bort markerat fält` |
| `Load fields from template layer` | `Läs in fält från mall-lager` | `Läs in fält från mallager` |
| `Load fields from selected template layer` | `Läs in fält från valt mall-lager` | `Läs in fält från markerat mallager` |
| `an array of map items, each containing a 'name', 'type', 'aggregate' and 'input' value (and optional 'length' and 'precision' values).` | `en array med kartelement, som vart och ett innehåller ett värde för "namn", "typ", "aggregat" och "input" (och eventuellt värden för "längd" och "precision")` | `en matris med mappningsobjekt som vart och ett innehåller värdena 'name', 'type', 'aggregate' och 'input' samt valfria värden för 'length' och 'precision'.` |
| `Current settings cannot be specified as arguments to qgis_process (Pipe parameters as JSON to qgis_process instead)` | `Aktuella inställningar kan inte användas som argument för qgis_process ("Pipe":a parametrar som JSON till qgis_process istället)` | `De aktuella inställningarna kan inte anges som argument till qgis_process. Skicka i stället parametrarna som JSON via en pipeline till qgis_process.` |
| `Save Log to File` | `Spara logg till fil` | `Spara loggen i en fil` |
| `Warning: This algorithm is a potential security risk if executed with unchecked inputs, and may result in system damage or data leaks.` | `Varning: Denna algoritm är en potentiell säkerhetsrisk om den körs med okontrollerad indata och kan resultera i systemskada eller dataläckor.` | `Varning! Algoritmen kan innebära en säkerhetsrisk om den körs med okontrollerade indata och kan orsaka systemskador eller dataläckor.` |
| `Warning: This algorithm has known issues. The results must be carefully validated by the user.` | `Varning: Denna algoritm har kända problem. Resultaten måste valideras noga av användaren.` | `Varning! Algoritmen har kända problem. Användaren måste noggrant validera resultaten.` |
| `Message log truncated` | `Meddelandelogg tömd` | `Meddelandeloggen har trunkerats` |
| `Rescale values according to the cell size` | `Skala om värden efter cellstorlek` | `Skala om värden enligt cellstorleken` |
| `Nearest Neighbour` | `Närmaste granne` | `Närmaste granne-metoden` |
| `Bilinear (2x2 Kernel)` | `Bilinjär (2x2 kernel)` | `Bilinjär (2 × 2-kärna)` |
| `Cubic (4x4 Kernel)` | `Kubisk (4x4 kernel)` | `Kubisk (4 × 4-kärna)` |
| `Cubic B-Spline (4x4 Kernel)` | `Kubisk B-Kurva (4x4 kernel)` | `Kubisk B-spline (4 × 4-kärna)` |
| `Lanczos (6x6 Kernel)` | `Lanczos (6x6 kernel)` | `Lanczos (6 × 6-kärna)` |
| `Average` | `Medel` | `Medelvärde` |
| `Configure Raster…` | `Konfigurera raster…` | `Konfigurera rastret…` |
| `%n raster layer(s) selected` | `%n rasterlager valda` | `%n rasterlager valt` / `%n rasterlager valda` |
| `name of an annotation layer, or "main" for the main annotation layer` | `namn på ett anteckningslager, eller "main" för det huvudsakliga anteckningslagret` | `namnet på ett anteckningslager eller "main" för huvudanteckningslagret` |
| `Minimum value` | `Minimalt värde` | `Minsta värde` |
| `Maximum value` | `Maximalt värde` | `Största värde` |
| `Source CRS parameter` | `Parameter för källans koordinatsystem` | `Parameter för källans koordinatreferenssystem` |
| `Destination CRS parameter` | `Parameter för målets koordinatsystem` | `Parameter för målkoordinatreferenssystemet` |
| `Static source CRS` | `Statiskt koordinatsystem för källan` | `Statiskt koordinatreferenssystem för källan` |
| `Static destination CRS` | `Statiskt koordinatsystem för målet` | `Statiskt koordinatreferenssystem för målet` |
| `Proj coordinate operation string, e.g. '+proj=pipeline +step +inv...'` | `Textsträng för koordinathantering i proj t.ex. '+proj=pipeline +step +inv…'` | `PROJ-sträng för koordinatoperation, till exempel '+proj=pipeline +step +inv…'` |
| `string as EPSG code, WKT or PROJ format, or a string identifying a map layer` | `sträng som är en EPSG-kod, WKT eller PROJ-format, eller en sträng som identifierar ett kartlager` | `sträng i EPSG-kod, WKT- eller PROJ-format eller en sträng som identifierar ett kartlager` |
| `Provider connection parameter` | `Anslutningsparameter för källa` | `Anslutningsparameter för provider` |
| `Database schema parameter` | `Parameter för databasschema.` | `Parameter för databasschema` |
| `[Not selected]` | `[Ej vald]` | `[Inte vald]` |
| `datetime value, or a ISO string representation of a datetime` | `datumtid-värde eller en ISO-textsträng som representerar datumtid` | `datum- och tidsvärde eller en ISO-sträng som representerar datum och tid` |
| `date value, or a ISO string representation of a date` | `datum-värde eller en ISO-textsträng som representerar ett datum` | `datumvärde eller en ISO-sträng som representerar ett datum` |
| `time value, or a ISO string representation of a time` | `tid-värde eller en ISO-textsträng som representerar tid` | `tidsvärde eller en ISO-sträng som representerar en tid` |
| `QGIS Layer Style File` | `QGIS lagerstilfil` | `QGIS-lagerstilfil` |
| `Distance is in geographic degrees. Consider reprojecting to a projected local coordinate system for accurate results.` | `Avstånd är i grader. Överväg att transformera ditt lager till ett projicerat referenskoordinatsystem för mer exakta resultat.` | `Avståndet anges i geografiska grader. Överväg att omprojicera lagret till ett lokalt projicerat koordinatreferenssystem för att få exakta resultat.` |
| `Default unit type` | `Standard enhetstyp` | `Standardenhetstyp` |
| `years (365.25 days)` | `år (365.25 dagar)` | `år (365,25 dagar)` |
| `Maximum number of symbol blocks` | `Största antal symbolblock` | `Största antalet symbolblock` |
| ` [overridden name: %1]` | `[åsidosatt namn: %1]` | ` [åsidosatt namn: %1]` |
| `Clear Selection` | `Rensa valda` | `Rensa markeringen` |
| `Are you sure you want to delete all items` | `Är du säker på att du vill ta bort alla element?` | `Är du säker på att du vill ta bort alla objekt?` |

Pluralraden behöver båda svenska pluralformerna vid senare import. Kod,
kommandon och radens inledande blanksteg bevaras exakt. Ingen extern ändring
har gjorts.
