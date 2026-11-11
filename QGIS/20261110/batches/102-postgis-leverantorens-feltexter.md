# QGIS: PostGIS-leverantörens feltexter 102

Datum: 10 november 2026  
Resurs: `qgis-application`, språk `sv`  
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen granskar feltexter från PostGIS-leverantören. SQL-nyckelord, `ctid`,
`hstore`, `topology.layer`, `NULL`, `SELECT` och platshållarna bevaras.
Terminologin följer den fastställda QGIS-termen `rumsligt index`.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Field %1 ignored, because of unsupported type %2` | `Fält %1 ignorerat eftersom typen %2 ej stöds` | `Fältet %1 ignorerades eftersom typen %2 inte stöds` |
| `Duplicate field %1 found\n` | `Duplicerat fält %1 funnet\n` | `Fältet %1 förekommer flera gånger\n` |
| `Unable to determine table access privileges for the %1 relation.\nThe error message from the database was:\n%2.\nSQL: %3` | `Kunde inte fastställa tabellprivilegier för %1 relationen.\nFelmeddelandet från databasen var:\n%2.\nSQL: %3` | `Kunde inte fastställa tabellbehörigheter för relationen %1.\nDatabasens felmeddelande var:\n%2.\nSQL: %3` |
| `Unable to execute the query.\nThe error message from the database was:\n%1.\nSQL: %2` | `Kunde inte köra fråga.\nFelmeddelandet från databasen var:\n%1.\nSQL: %2` | `Kunde inte köra frågan.\nDatabasens felmeddelande var:\n%1.\nSQL: %2` |
| `The table has no column suitable for use as a key. QGIS requires a primary key, a PostgreSQL oid column or a ctid for tables.` | `Tabellen har ingen kolumn som passar som nyckel. QGIS behöver en primärnyckel, en PostgreSQL oid kolumn eller ett ctid för tabeller.` | `Tabellen har ingen kolumn som kan användas som nyckel. QGIS kräver en primärnyckel, en PostgreSQL OID-kolumn eller ett ctid för tabellen.` |
| `Unique column '%1' doesn't have a NOT NULL constraint.` | `Unik kolumn '%1' har ingen NOT NULL begränsning.` | `Den unika kolumnen '%1' saknar en NOT NULL-begränsning.` |
| `Key field '%1' for view/query not found.` | `Nyckelfält '%1' för visning/fråga ej funnet.` | `Nyckelfältet '%1' för vyn/frågan hittades inte.` |
| `Primary key field '%1' for view/query not unique.` | `Primärnyckelfält '%1' ej unik för visning/fråga.` | `Primärnyckelfältet '%1' för vyn/frågan är inte unikt.` |
| `TopoGeometry columns with data referencing different topology layers are not supported (%1.%2.%3)` | `Kolumnerna TopoGeometry med data som refererar annat topologilager stöds inte (%1.%2.%3)` | `TopoGeometry-kolumner med data som refererar till olika topologilager stöds inte (%1.%2.%3)` |
| `Unexpected number of tuples from estimated extent query %1: %2 (1 expected).` | `Oväntat antal svar från fråga för uppskattad utsträckning %1: %2 (förväntade 1).` | `Oväntat antal rader från frågan om uppskattad utbredning %1: %2 (en förväntades).` |
| `Cannot find separator: %1` | `Kan inte hitta separator: %1` | `Kan inte hitta avgränsaren: %1` |
| `Error parsing array: %1` | `Fel vid tolkning av array: %1` | `Fel vid tolkning av matris: %1` |
| `Error parsing array, missing curly braces: %1` | `Fel vid tolkning av array, saknar klammerparanteser: %1` | `Fel vid tolkning av matris, klammerparenteser saknas: %1` |
| `Read attempt on an invalid PostgreSQL data source` | `Läsförsök på en ogiltig postgreSQL-datakälla` | `Läsförsök på en ogiltig PostgreSQL-datakälla` |
| `PostgreSQL WHERE clause` | `PostgreSQL WHERE sats` | `PostgreSQL WHERE-sats` |
| `No spatial index.` | `Inget spatialt index.` | `Inget rumsligt index.` |
| `Spatial index/indices exists (%1).` | `Spatialt index finns (%1).` | `Ett eller flera rumsliga index finns (%1).` |
| `Primary key is ctid - changing of existing features disabled (%1; %2)` | `Primärnyckel är ctid - ändring av befintliga objekt inaktiverad (%1; %2)` | `Primärnyckeln är ctid; ändring av befintliga objekt är inaktiverad (%1; %2)` |

Ingen extern ändring har gjorts. Aktuella Transifex-enhetsidentifierare måste
hämtas och måltexterna jämföras före en separat deltafil kan skapas.
