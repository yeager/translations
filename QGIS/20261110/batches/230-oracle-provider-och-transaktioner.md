# QGIS: Oracle-provider och transaktioner 230

Datum: 11 november 2026
Resurs: `qgis-application`, språk `sv`
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen granskar Oracle-providerns databasfel, transaktioner och metadatarutiner.
SQL, Oracle, SRID, ROWID, SDO_GEOMETRY, ALL_TAB_COLUMNS och WKT bevaras som
tekniska namn.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Read attempt on an invalid oracle data source` | `Läsförsök på en ogiltig oracle-datakälla` | `Läsförsök på en ogiltig Oracle-datakälla` |
| `Unable to determine geometry column access privileges for column %1.%2.\nThe error message from the database was:\n%3.\nSQL: %4` | `Kunde inte fastställa åtkomsträttighet till geometrikolumnen på %1.%2.\nFelmeddelandet från databasen var:\n%3.\nSQL: %4` | `Det gick inte att fastställa åtkomsträttigheterna för geometrikolumnen %1.%2.\nFelmeddelandet från databasen var:\n%3.\nSQL: %4` |
| `Unable to determine table access privileges for the table %1.\nThe error message from the database was:\n%2.\nSQL: %3` | `Kunde inte fastställa åtkomsträttigheter på tabell %1.\nFelmeddelandet från databasen var:\n%2.\nSQL: %3` | `Det gick inte att fastställa åtkomsträttigheterna för tabellen %1.\nFelmeddelandet från databasen var:\n%2.\nSQL: %3` |
| `Unable to execute the query.\nThe error message from the database was:\n%1.\nSQL: %2` | `Kunde inte köra fråga.\nFelmeddelandet från databasen var:\n%1.\nSQL: %2` | `Det gick inte att köra frågan.\nFelmeddelandet från databasen var:\n%1.\nSQL: %2` |
| `Primary key field %1 not found in %2` | `Primärnyckelfält %1 inte funnet i %2` | `Primärnyckelfältet %1 hittades inte i %2` |
| `No primary key found, using ROWID.` | `Ingen primärnyckel hittad, använder ROWID.` | `Ingen primärnyckel hittades, använder ROWID.` |
| `Evaluation of default value failed` | `Evaluering av standardvärde misslyckades` | `Utvärdering av standardvärde misslyckades` |
| `Could not prepare get feature id statement` | `Kunde inte förbereda uttryck för att hämta objekt id` | `Det gick inte att förbereda satsen för att hämta objekt-ID` |
| `Could not prepare insert statement` | `Kunde inte förbereda uttryck för att lägga till` | `Det gick inte att förbereda infogningssatsen` |
| `Could not insert feature %1` | `Kunde inte skapa objekt %1` | `Det gick inte att infoga objekt %1` |
| `Could not retrieve feature id %1` | `Kunde inte hämta objekt id %1` | `Det gick inte att hämta objekt-ID %1` |
| `Could not commit transaction` | `Kunde inte utföra transaktionen` | `Det gick inte att verkställa transaktionen` |
| `Could not rollback transaction` | `Kunde inte ta tillbaka transaktionen` | `Det gick inte att återställa transaktionen` |
| `Adding attribute %1 failed` | `Skapande av attribut %1 misslyckades` | `Det gick inte att lägga till attribut %1` |
| `Setting comment on %1 failed` | `Skapande av kommentar på %1 misslyckades` | `Det gick inte att ange kommentaren för %1` |
| `Could not reload fields.` | `Kunde inte uppdatera fält.` | `Det gick inte att läsa in fälten på nytt.` |
| `Renaming column %1 to %2 failed` | `Namnbyte av kolumn %1 till %2 misslyckades` | `Det gick inte att byta namn på kolumnen %1 till %2` |
| `Oracle SQL WHERE clause` | `Oracle SQL WHERE sats` | `Oracle SQL WHERE-sats` |
| `Error discovering relations of %1: invalid layer` | `Fel vid upptäckande av relationer %1: ogiltigt lager` | `Fel när relationerna för %1 identifierades: ogiltigt lager` |
| `Could not determine geometry column name: No SDO_GEOMETRY results found for %1.%2 in ALL_TAB_COLUMNS` | `Kunde inte bestämma namnet på geometrikolumnen: Inga SDO_GEOMETRY resultat hittades för %1.%2 i ALL_TAB_COLUMNS` | `Det gick inte att fastställa geometrikolumnens namn: inga SDO_GEOMETRY-resultat hittades för %1.%2 i ALL_TAB_COLUMNS` |
| `Could not retrieve SRID of %1.%2 (%3): No matches found in all_sdo_geom_metadata` | `Kunde inte hämta SRID för %1.%2 (%3): Inga matchningar hittades i all_sdo_geom_metadata` | `Det gick inte att hämta SRID för %1.%2 (%3): inga träffar hittades i all_sdo_geom_metadata` |
| `Rebuild of spatial index failed.\nSQL: %1\nError: %2` | `Återuppbyggnad av spatialt index misslyckades.\nSQL: %1\nFel: %2` | `Det gick inte att bygga om det rumsliga indexet.\nSQL: %1\nFel: %2` |
| `Cannot insert geometry metadata for table '%1' and geometry column '%2'. Both needs to be uppercase` | `Kan inte infoga metadata för geometri för tabell '%1' och geometrikolumn '%2'. Båda behöver vara versaler.` | `Det går inte att infoga geometrimetadata för tabellen '%1' och geometrikolumnen '%2'. Båda måste skrivas med versaler.` |
| `No spatial index on column %1.%2.%3 found - expect poor performance.` | `Inget spatialt index för kolumn %1.%2.%3 funnet - dålig prestanda kan förväntas` | `Inget rumsligt index hittades för kolumnen %1.%2.%3. Prestandan kan bli låg.` |
| `Primary key field '%1' for view/query not unique.` | `Primärnyckelfält '%1' ej unik för visning/fråga.` | `Primärnyckelfältet '%1' är inte unikt för vyn eller frågan.` |
| `Key field '%1' for view/query not found.` | `Nyckelfält '%1' för visning/fråga ej funnet.` | `Nyckelfältet '%1' hittades inte för vyn eller frågan.` |
| `No key field for view/query given.` | `Inget nyckelfält för visning/fråga angivet.` | `Inget nyckelfält har angetts för vyn eller frågan.` |
| `Unable to execute the query to get foreign keys of %1.\nThe error message from the database was:\n%2.\nSQL: %3` | `Kunde inte köra fråga för att få främmande nycklar för %1.\nFelmeddelandet från databasen var:\n%2.\nSQL: %3` | `Det gick inte att köra frågan för att hämta främmande nycklar för %1.\nFelmeddelandet från databasen var:\n%2.\nSQL: %3` |
| `Could not retrieve extents: %1\nSQL: %2` | `Kunde inte hämta utbredning: %1\nSQL: %2` | `Det gick inte att hämta utbredningen: %1\nSQL: %2` |
| `Could not determine SRID of %1.\nThe error message from the database was:\n%2.\nSQL: %3` | `Kunde inte fastställa SRID på %1.\nFelmeddelandet från databasen var:\n%2.\nSQL: %3` | `Det gick inte att fastställa SRID för %1.\nFelmeddelandet från databasen var:\n%2.\nSQL: %3` |
| `Geometry type and srid for empty column %1 of %2 undefined.` | `Geometrityp och SRID för tom kolumn %1 av %2 odefinierad.` | `Geometrityp och SRID för den tomma kolumnen %1 i %2 är odefinierade.` |
| `Feature type or srid for %1 of %2 could not be determined or was not requested.` | `Objekttyp och SRID för %1 av %2 kunde inte fastställas eller efterfrågades inte.` | `Objekttyp eller SRID för %1 i %2 kunde inte fastställas eller begärdes inte.` |
| `Could not determine table existence.` | `Kunde inte bestämma existensen av tabell.` | `Det gick inte att fastställa om tabellen finns.` |
| `Table %1 already exists.` | `tabellen %1 existerar redan.` | `Tabellen %1 finns redan.` |
| `Could not determine new srid.` | `Kunde inte fastställa nytt referenskoordinatsystem` | `Det gick inte att fastställa nytt SRID.` |
| `Oracle SRID %1 not found.` | `Racle SRID %1 kunde inte hittas.` | `Oracle SRID %1 hittades inte.` |
| `Stop` | `Stopp` | `Stoppa` |
| `Disable 'Fast Access to Features at ID' capability to force keeping the attribute table in memory (e.g. in case of expensive views).` | `Stäng av 'Genväg till objekt vid ID' möjligheten för att behålla attributtabellen i minnet ( i händelse av kostsamma visningar).` | `Inaktivera funktionen 'Snabb åtkomst till objekt vid ID' för att tvinga fram att attributtabellen behålls i minnet, till exempel för resurskrävande vyer.` |
| `Connection to the database not available` | `Anslutning till databasen inte tillgänglig` | `Databasanslutningen är inte tillgänglig` |

Radbrytningar, apostrofer, platshållare och Oracle-specifika identifierare ska
bevaras oförändrade vid senare import. Ingen extern ändring har gjorts.
