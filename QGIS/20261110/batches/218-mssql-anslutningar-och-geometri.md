# QGIS: MSSQL-anslutningar och geometri 218

Datum: 11 november 2026
Resurs: `qgis-application`, språk `sv`
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen granskar Microsoft SQL Server-datakällan. SQL-termerna `schema`,
`geometry_columns`, `DSN` och tabellkolumnnamn bevaras där de är tekniska
identifierare.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Sockets cannot be connected` | `Kopplingar kan inte redigeras` | `Anslutningspunkterna kan inte anslutas` |
| `Either the sockets are incompatible or there is a circular dependency` | `Antingen är kopplingen inte kompatibel eller så finns det ett cirkelberoende` | `Antingen är anslutningspunkterna inkompatibla eller så finns det ett cirkulärt beroende` |
| `Unlink %1: %2` | `Avlänka %1: %2` | `Ta bort länk mellan %1 och %2` |
| `Pan` | `Flytta vy` | `Panorera` |
| `Show Non-spatial Tables` | `Visa icke-spatiala tabeller` | `Visa icke-rumsliga tabeller` |
| `Table Operations` | `Tabelloperationer` | `Tabellåtgärder` |
| `Truncate Table` | `Trunkera Tabell` | `Töm tabell` |
| `Delete %1` | `Radera %1` | `Ta bort %1` |
| `%1 deleted successfully.` | `%1 raderades.` | `%1 togs bort.` |
| `Unable to create schema %1\n%2` | `Kan inte skapa schema %1\n%2` | `Det gick inte att skapa schema %1\n%2` |
| `Table truncated successfully.` | `Trunkering av tabell lyckades.` | `Tabellen tömdes.` |
| `%1: Not a vector layer!` | `%1: Är inte ett vektorlager!` | `%1: Är inte ett vektorlager.` |
| `Import to MS SQL Server database` | `Importera till MS SQL Server-databas` | `Importera till Microsoft SQL Server-databas` |
| `Failed to import some layers!` | `Misslyckades med att importera vissa lager!` | `Det gick inte att importera vissa lager.` |
| `%1: Not a valid layer!` | `%1: Är inte ett giltigt lager!` | `%1: Är inte ett giltigt lager.` |
| `SQL Server Import` | `SQL Server import` | `SQL Server-import` |
| `Should the existing connection %1 be overwritten?` | `Vill du att existerande anslutning '%1' ska skrivas över?` | `Ska den befintliga anslutningen ”%1” skrivas över?` |
| `Error opening connection` | `Fel vid öppnande av anslutning` | `Fel när anslutningen öppnades` |
| `Use extent from geometry_columns table` | `Använd utsträckning från tabellen geometry_columns` | `Använd utbredning från tabellen geometry_columns` |
| `Extent columns (qgis_xmin, qgis_ymin, qgis_xmax, qgis_ymax) not found.` | `Utsträckningskolumner (qgis_xmin, qgis_ymin, qgis_xmax, qgis_ymax) hittades inte.` | `Utbredningskolumnerna (qgis_xmin, qgis_ymin, qgis_xmax, qgis_ymax) hittades inte.` |
| `Extent columns found.` | `Utbredningskolumner hittades.` | `Utbredningskolumnerna hittades.` |
| `Host` | `Dator` | `Värd` |
| `If checked, tables without a geometry column attached will also be shown in the available table lists.` | `Om markerad så visas även tabeller utan geometrikolumn i listan över tillgängliga tabeller.` | `Om alternativet är markerat visas även tabeller utan geometrikolumn i listorna över tillgängliga tabeller.` |
| `If checked, only estimated table metadata will be used. This avoids a slow table scan, but may result in incorrect layer properties such as layer extent.` | `Om markerad så används bara uppskattad tabellmetadata. Genom detta undviks långsam tabellsökning, men kan resultera i oriktiga lageregenskaper såsom lagerutbredning.` | `Om alternativet är markerat används bara uppskattade tabellmetadata. Det undviker en långsam tabellgenomsökning, men kan ge felaktiga lageregenskaper, till exempel lagerutbredning.` |
| `If checked, all handling of records with invalid geometry will be disabled. This speeds up the provider, however, if any invalid geometries are present in a table then the result is unpredictable and may include missing records. Only check this option if you are certain that all geometries present in the database are valid, and any newly added geometries or tables will also be valid.` | `Om markerad, så avaktiveras all hantering av poster ogiltig geometri. Detta snabbar upp datakällan men om det finns ogiltiga geometrier i tabellen så blir resultatet oförutsägbart och kan innehålla saknade poster. Kryssa bara för detta val om du är säker på att alla geometrier i databasen är giltiga och alla nya geometrier och tabeller också kommer vara giltiga.` | `Om alternativet är markerat inaktiveras all hantering av poster med ogiltig geometri. Det snabbar upp dataleverantören, men om en tabell innehåller ogiltiga geometrier blir resultatet oförutsägbart och poster kan saknas. Markera bara alternativet om du är säker på att alla geometrier i databasen är giltiga och att nya geometrier eller tabeller också kommer att vara giltiga.` |
| `Connection name` | `Namn på anslutning` | `Anslutningsnamn` |
| `Use estimated table parameters` | `Använd estimerade tabellparametrar` | `Använd uppskattade tabellparametrar` |
| `Use layer extent from geometry_columns table` | `Använd lagerutsträckning från tabellen geometry_columns` | `Använd lagerutbredning från tabellen geometry_columns` |

Radbrytningen och platshållarna i felmeddelandet om schema ska bevaras vid
senare import. Ingen extern ändring har gjorts.
