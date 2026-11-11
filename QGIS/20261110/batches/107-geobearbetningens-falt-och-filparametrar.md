# QGIS: geobearbetningens fält- och filparametrar 107

Datum: 10 november 2026  
Resurs: `qgis-application`, språk `sv`  
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen granskar fältmappning, versionsrader och filparametrar i
geobearbetningen. Biblioteksnamnen QGIS, Qt, Python, GDAL, GEOS, PROJ, PDAL,
SFCGAL och GeographicLib bevaras. Konfigurationsnycklar som `name`, `type`
och `expression` ska inte översättas.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `QGIS code revision: %1` | `QGIS kodrevision: %1` | `QGIS-kodrevision: %1` |
| `SFCGAL version: %1` | `SFCGAL version: %1` | `SFCGAL-version: %1` |
| `GeographicLib version: %1.%2.%3` | `GeographicLib version: %1.%2.%3` | `GeographicLib-version: %1.%2.%3` |
| `%1 version: %2` | `%1 version: %2` | `%1-version: %2` |
| `Invert fields selection` | `Invertera valda fält` | `Invertera fältmarkeringen` |
| `an array of map items, each containing a 'name', 'type' and 'expression' values (and optional 'length' and 'precision' values).` | `en array med kartelement, som vart och ett innehåller ett värde för "namn", "typ", "uttryck" och "input" (och eventuellt värden för "längd" och "precision")` | `en matris med mappningsposter, där varje post innehåller värdena 'name', 'type' och 'expression' samt eventuellt 'length' och 'precision'.` |
| `Default field name, or ; separated list of field names for multiple field parameters` | `Förvalt fältnamn, eller en semikolonserparerad lista på multipla fältparametrar` | `Standardfältnamn, eller en semikolonseparerad lista med fältnamn för parametrar som accepterar flera fält` |
| `selected field names as an array of names, or semicolon separated string of options (e.g. 'fid;place_name')` | `valda fältnamn som en array av namn eller semikolonseparerad textsträng av  alternativ (t.ex. 'fid;place_name')` | `valda fältnamn som en matris med namn eller en semikolonseparerad sträng med alternativ (till exempel 'fid;place_name')` |
| `path to file destination` | `sökväg till filens destination` | `sökväg till fildestinationen` |
| `HTML Files (*.html *.htm)` | `HTML-filer(*.html *.htm)` | `HTML-filer (*.html *.htm)` |
| `string representing a path to a file or folder` | `textsträng som representerar sökväg till en fil eller mapp` | `sträng som representerar en sökväg till en fil eller mapp` |
| `path to folder destination` | `sökväg till mappens destination` | `sökväg till mappdestinationen` |

Ingen extern ändring har gjorts. Aktuella Transifex-enhetsidentifierare måste
hämtas och måltexterna jämföras före en separat deltafil kan skapas.
