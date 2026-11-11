# QGIS: MSSQL-frågor och flerredigering 219

Datum: 11 november 2026
Resurs: `qgis-application`, språk `sv`
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen fortsätter granskningen av MSSQL-datakällan och rättar intilliggande
redigerings- och nätverksmeddelanden.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `If checked, QGIS will skip extent calculation when loading layers and thus speeds up loading time. This requires manually setting the extent in dedicated columns (qgis_xmin, qgis_xmax, qgis_ymin, qgis_ymax) in the geometry_columns metadata table.` | `Om alternativet är markerat kommer QGIS att hoppa över beräkning av utsträckning när lager laddas och därmed snabba upp inläsningstiden. Detta kräver manuell inställning av utsträckningen i avsedda kolumner (qgis_xmin, qgis_xmax, qgis_ymin, qgis_ymax) i metadatatabellen geometry_columns.` | `Om alternativet är markerat hoppar QGIS över beräkningen av utbredning när lager läses in, vilket förkortar inläsningstiden. Det kräver att utbredningen anges manuellt i de särskilda kolumnerna qgis_xmin, qgis_xmax, qgis_ymin och qgis_ymax i metadatatabellen geometry_columns.` |
| `If checked, QGIS will skip primary key calculation when loading views and thus speeds up loading time. This requires manually setting the primary key(s) name in a dedicated qgis_pkey column in the geometry_columns metadata table.` | `Om alternativet är markerat kommer QGIS att hoppa över beräkning av primärnyckel när vyer laddas och därmed snabba upp inläsningstiden. Detta kräver manuell inställning av namnet på primärnyckeln i en avsedd kolumn, qgis_pkey, i metadatatabellen geometry_columns.` | `Om alternativet är markerat hoppar QGIS över beräkningen av primärnyckel när vyer läses in, vilket förkortar inläsningstiden. Det kräver att namnet på primärnyckeln anges manuellt i den särskilda kolumnen qgis_pkey i metadatatabellen geometry_columns.` |
| `Invalid primary key from geometry_columns table for layer '%1', get primary key from the layer.` | `Ogiltig primärnyckel från tabellen geometry_columns för lager '%1', hämta primärnyckel från lagret.` | `Ogiltig primärnyckel från tabellen geometry_columns för lagret ”%1”. Hämtar primärnyckeln från lagret.` |
| `Key field '%1' for view/query not found.` | `Nyckelfält '%1' för visning/fråga ej funnet.` | `Nyckelfältet ”%1” för vyn eller frågan hittades inte.` |
| `Could not execute query: %1` | `Kunde inte köra fråga: %1` | `Det gick inte att köra frågan: %1` |
| `Could not fetch next query value: %1` | `Kunde inte hämta nästa frågevärde: %1` | `Det gick inte att hämta nästa frågevärde: %1` |
| `Invalid extent from geometry_columns table for layer '%1', get extent from the layer.` | `Ogiltig utsträckning från tabellen geometry_columns för lager '%1', hämta utsträckning från lagret.` | `Ogiltig utbredning från tabellen geometry_columns för lagret ”%1”. Hämtar utbredningen från lagret.` |
| `Only %1 of %2 features deleted` | `Endast %1 av %2 objekt raderades.` | `Endast %1 av %2 objekt togs bort.` |
| `SQL Server WHERE clause` | `SQL Server WHERE sats` | `SQL Server-WHERE-sats` |
| `Cannot connect to database: %1` | `Kan inte ansluta till databas: %1` | `Det går inte att ansluta till databasen: %1` |
| `Style does not exist` | `Stil finns inte` | `Stilen finns inte` |
| `Add MS SQL Server Table(s)` | `Lägg till MS SQL server-tabell(er)` | `Lägg till Microsoft SQL Server-tabell(er)` |
| `View` | `Visa` | `Vy` |
| `Select at id` | `Välj med id` | `Välj efter ID` |
| `Enter…` | `Skriv in…` | `Ange…` |
| `Disable 'Fast Access to Features at ID' capability to force keeping the attribute table in memory (e.g. in case of expensive views).` | `Stäng av 'Genväg till objekt vid ID' möjligheterna för att behålla attributtabellen i minnet (i händelse av koststamma visningar).` | `Inaktivera funktionen ”Snabb åtkomst till objekt via ID” för att tvinga attributtabellen att ligga kvar i minnet, till exempel för kostsamma vyer.` |
| `MS SQL Server query failed: %1` | `MS SQL Server-fråga misslyckades: %1` | `Microsoft SQL Server-frågan misslyckades: %1` |
| `Could not create savepoint (%1)` | `Kunde inte skapa sparningspunkt (%1)` | `Det gick inte att skapa sparpunkten (%1)` |
| `No Enhancement` | `Ingen förhöjning` | `Ingen kontrastförbättring` |
| `No Changes to Commit` | `Inga förändringar att spara ned` | `Inga ändringar att verkställa` |
| `Reset to Original Values` | `Återställ till standardvärden` | `Återställ till ursprungliga värden` |
| `HTTP fetch %1 failed with error %2` | `Hämtning av HTTP %1 misslyckades med fel %2` | `HTTP-hämtningen av %1 misslyckades med fel %2` |
| `Clear Log` | `Rensa logg` | `Rensa loggen` |

De tekniska tabell- och kolumnnamnen samt platshållarna `%1` och `%2` ska
bevaras oförändrade vid senare import. Ingen extern ändring har gjorts.
