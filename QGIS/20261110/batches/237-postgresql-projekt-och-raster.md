# QGIS: PostgreSQL-projekt och raster 237

Datum: 11 november 2026
Resurs: `qgis-application`, språk `sv`
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen granskar PostgreSQL-providerns projektlagring, rasterfel och tidsfält.
SQL, `PostGIS`, `EPSG`, `ctid`, `oid`, `NoData`, `AddRasterConstraints` och
databasscheman är tekniska termer och bevaras.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Truncate Table` | `Trunkera Tabell` | `Töm tabell` |
| `Import Projects to Schema “%1”` | `Importera projekt till schema "%1#` | `Importera projekt till schemat “%1”` |
| `Add selected project or projects from folder` | `Lägg till valda projekt eller projekt från mapp` | `Lägg till markerade projekt från en mapp` |
| `Add Project File…` | `Lägg till projektfil...` | `Lägg till projektfil…` |
| `Add Projects from Folder…` | `Lägg till projekt från mapp...` | `Lägg till projekt från mapp…` |
| `Select Projects from Folder` | `Välj projekt från mapp` | `Välj projekt från en mapp` |
| `Add Projects from Folder Recursively…` | `Lägg till projekt från mapp rekursivt…` | `Lägg till projekt rekursivt från en mapp…` |
| `Select Projects from Folder Recursively` | `Välj projekt från mapp rekursivt` | `Välj projekt rekursivt från en mapp` |
| `Load project from PostgreSQL` | `Öppna projekt från PostgreSQL` | `Läs in projekt från PostgreSQL` |
| `Connection failed` | `Anslutningen avbröts` | `Anslutningen misslyckades` |
| `Failed to get schemas` | `Misslyckades med att hämta scheman` | `Det gick inte att hämta scheman` |
| `Overwrite project` | `Skriv över projekt` | `Skriv över projektet` |
| `Do you really want to remove the project "%1"?` | `Vill du verkligen ta bort projektet  "%1"?` | `Vill du verkligen ta bort projektet "%1"?` |
| `Enable versioning of QGIS projects` | `Aktivera versionshantering av QGIS-projekt ` | `Aktivera versionshantering för QGIS-projekt` |
| `Do you want to enable versioning of QGIS projects in the schema “%1”?\nThis will create a new table in the schema and store older versions of QGIS projects there.` | `Vill du aktivera versionshantering av QGIS-projekt i schemat "%1"? \nDetta kommer skapa en ny tabell i schemat och lagra äldre versioner av QGIS-projekt där.` | `Vill du aktivera versionshantering för QGIS-projekt i schemat “%1”?\nDet skapar en ny tabell i schemat där äldre versioner av QGIS-projekt lagras.` |
| `Project Versions for “%1” in Schema “%2”` | `Projektversioner av "%1" i schema "%2"` | `Projektversioner för “%1” i schema “%2”` |
| `Modified Time` | `Ändrad tid` | `Ändringstid` |
| `FAILURE: Field %1 not found.` | `FEL: Fält %1 hittades inte.` | `FEL: Fältet %1 hittades inte.` |
| `Field %1 ignored, because of unsupported type %2` | `Fält %1 ignorerat eftersom typen %2 ej stöds` | `Fältet %1 ignorerades eftersom typen %2 inte stöds` |
| `Duplicate field %1 found` | `Duplicerat fält %1 funnet` | `Dubblettfältet %1 hittades` |
| `Unable to determine table access privileges for the %1 relation.\nThe error message from the database was:\n%2.\nSQL: %3` | `Kunde inte fastställa tabellprivilegier för %1 relationen.\nFelmeddelandet från databasen var:\n%2.\nSQL: %3` | `Det gick inte att fastställa tabellbehörigheterna för relationen %1.\nFelmeddelandet från databasen var:\n%2.\nSQL: %3` |
| `Unable to execute the query.\nThe error message from the database was:\n%1.\nSQL: %2` | `Kunde inte köra fråga.\nFelmeddelandet från databasen var:\n%1.\nSQL: %2` | `Det gick inte att köra frågan.\nFelmeddelandet från databasen var:\n%1.\nSQL: %2` |
| `The table has no column suitable for use as a key. QGIS requires a primary key, a PostgreSQL oid column or a ctid for tables.` | `Tabellen har ingen kolumn som passar som nyckel. QGIS behöver en primärnyckel, en PostgreSQL oid kolumn eller ett ctid för tabeller.` | `Tabellen saknar en kolumn som kan användas som nyckel. QGIS kräver en primärnyckel, en PostgreSQL-oid-kolumn eller ctid.` |
| `Unique column '%1' doesn't have a NOT NULL constraint.` | `Unik kolumn '%1' har ingen NOT NULL begränsning.` | `Den unika kolumnen '%1' saknar begränsningen NOT NULL.` |
| `Key field '%1' for view/query not found.` | `Nyckelfält '%1' för visning/fråga ej funnet.` | `Nyckelfältet '%1' för vy/fråga hittades inte.` |
| `Primary key field '%1' for view/query not unique.` | `Primärnyckelfält '%1' ej unik för visning/fråga.` | `Primärnyckelfältet '%1' för vy/fråga är inte unikt.` |
| `Keys for view/query undefined.` | `Nyckel för visning/fråga odefinierad.` | `Nycklarna för vy/fråga är odefinierade.` |
| `No key field for view/query given.` | `Inget nyckelfält för visning/fråga angivet.` | `Inget nyckelfält har angetts för vy/fråga.` |
| `Cannot create CRS from EPSG: '%1'` | `Kan inte skapa koordinatsystem från EPSG: '%1'` | `Kan inte skapa ett koordinatreferenssystem från EPSG: '%1'` |
| `Unsupported data type: '%1'` | `Inget stöd för datatyp: '%1'` | `Datatypen '%1' stöds inte` |
| `Cannot get extent from raster` | `Kan inte få utsträckning från raster` | `Kan inte hämta utbredningen från rastret` |
| `An error occurred while fetching raster metadata for table %1: %2\nSQL: %3` | `Ett fel uppstod vid hämtning av metadata för raster för tabell %1: %2\nSQL: %3` | `Ett fel uppstod när rastermetadata hämtades för tabell %1: %2\nSQL: %3` |
| `An error occurred while fetching raster metadata for %1, proceeding with (possibly very slow) raster data analysis: %2\nPlease consider adding raster constraints with PostGIS function AddRasterConstraints.` | `Ett fel uppstod vid hämtning av rastermetadata för %1, fortsätter med (möjligen mycket långsam) rasterdataanalys: %2\nÖvervägatt lägga till rasterinformation med PostGIS-funktionen AddRasterConstraints.` | `Ett fel uppstod när rastermetadata hämtades för %1. Fortsätter med rasterdataanalys, som kan vara mycket långsam: %2\nÖverväg att lägga till rasterbegränsningar med PostGIS-funktionen AddRasterConstraints.` |
| `Multiple raster column detected, using the first one` | `Flera olika rasterkolumner hittades, använder den första` | `Flera rasterkolumner upptäcktes. Den första används.` |
| `Cannot get metadata from raster` | `Kan inte få metedata från raster` | `Kan inte hämta metadata från rastret` |
| `PostgreSQL WHERE clause` | `PostgreSQL WHERE sats` | `PostgreSQL WHERE-sats` |
| `Cannot convert NoData value '%1' to double, default to: %2` | `Kan inte konvertera NoData-värdet '%1' till double, standardvärde till: %2` | `Kan inte konvertera NoData-värdet '%1' till double. Använder standardvärdet %2.` |
| `No overviews found, performances may be affected for %1` | `Inga översikter hittades, prestanda kan bli påverkad för %1` | `Inga översikter hittades. Prestandan för %1 kan påverkas.` |
| `Temporal capabilities` | `Tidsegenskaper (capabilities)` | `Tidsfunktioner` |
| `If the dataset contains multiple rasters belonging to a time series, specify the field that contains the time information, the type of the field can be any type that can be converted to a timestamp.` | `Om datasetet innehåller fler raster som tillhör tidsserier, ange fältet som innehåller tidsinformationen, typen för fältet kan vara vad som helst som kan konverteras till tidsstämpel.` | `Om datamängden innehåller flera raster som ingår i en tidsserie anger du fältet med tidsinformationen. Fälttypen kan vara vilken typ som helst som kan konverteras till en tidsstämpel.` |

Platshållarna `%1`–`%3`, radbrytningarna, tekniska termer och smarta citattecken
ska bevaras oförändrade vid senare import. Ingen extern ändring har gjorts.
