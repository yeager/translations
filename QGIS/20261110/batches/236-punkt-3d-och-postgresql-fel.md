# QGIS: punktmönster, 3D och PostgreSQL-fel 236

Datum: 11 november 2026
Resurs: `qgis-application`, språk `sv`
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen täcker punktmönster, 3D-polygoner samt fel- och datatypsmeddelanden
från PostgreSQL-providern. `PostGIS`, `GEOS`, `SQL`, datatyper och
funktionsnamn bevaras; *schema* används som databasterm.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Ring` | `Cirkel` | `Ring` |
| `Transparent Stroke` | `Genomskinlig Linje` | `Genomskinlig konturlinje` |
| `Opaque Stroke` | `Opak kantlinje` | `Ogenomskinlig konturlinje` |
| `The point displacement renderer only applies to (single) point layers.\n'%1' is not a (single) point layer and cannot be displayed by the point displacement renderer.` | `Punktförskjutning kan endast användas på (enkla) punktlager.\n'%1' är inte ett (enkelt) punktlager och kan inte visas med punktförskjutning.` | `Återgivaren för punktförskjutning kan bara användas för enskilda punktlager.\n'%1' är inte ett enskilt punktlager och kan inte visas med den återgivaren.` |
| `Label font` | `Typsnitt etikett` | `Etikettens typsnitt` |
| `Stroke color` | `Linjefärg...` | `Konturlinjens färg` |
| `Point distance tolerance` | `Punktdistanstolerans` | `Tolerans för punktavstånd` |
| `Clip to Shape` | `Klipp till form` | `Klipp till formen` |
| `Marker Centroid Within Shape` | `Markörens tyngdpunkt inom form` | `Markörens tyngdpunkt inom formen` |
| `Marker Completely Within Shape` | `Markören helt inom form` | `Markören helt inom formen` |
| `Align Pattern to Feature` | `Justera mönster till objekt` | `Justera mönster efter objekt` |
| `Align Pattern to Map Extent` | `Justera mönster till kartutbredning` | `Justera mönster efter kartans utbredning` |
| `Both sides of the shapes are visible` | `Båda sidor av formerna är synliga` | `Båda sidorna av formerna är synliga` |
| `Only the back of the shapes is visible` | `Endast baksidan av formerna är synligt` | `Endast formernas baksidor är synliga` |
| `Only the front of the shapes is visible` | `Endast framsidan av formerna är synligt` | `Endast formernas framsidor är synliga` |
| `Cannot create relation. Unexpected tag '%1'` | `Kan inte skapa relation. Oväntad tagg '%1'` | `Det går inte att skapa relationen. Oväntad tagg '%1'.` |
| `Connection to database failed` | `Anslutning till databas misslyckades` | `Det gick inte att ansluta till databasen` |
| `Your PostGIS installation has no GEOS support. Feature selection and identification will not work properly. Please install PostGIS with GEOS support (http://geos.refractions.net)` | `Din PostGIS-installation har inget stöd för GEOS. Urval av objekt och identifiering kommer inte fungera ordentligt. Var vänlig installera PostGIS med GEOS-stöd (http://geos.refractions.net)` | `Din PostGIS-installation saknar stöd för GEOS. Objekturval och identifiering fungerar därför inte korrekt. Installera PostGIS med GEOS-stöd (http://geos.refractions.net).` |
| `Database connection was successful, but the accessible tables could not be determined.` | `Databasanslutningen lyckades, men anslutningsbara tabeller kunde inte bestämmas.` | `Databasanslutningen lyckades, men det gick inte att fastställa vilka tabeller som är åtkomliga.` |
| `Cannot set WriteOwner permission to cert: %0 to allow removing it` | `Kan inte sätta WriteOwner behörighet till cert: %0 för att tillåta borttagning` | `Kan inte ge certifikatet %0 behörigheten WriteOwner för att kunna ta bort det` |
| `Cannot remove cert: %0` | `Kan inte ta bort cert: %0` | `Kan inte ta bort certifikatet %0` |
| `Unsupported spatial column type %1` | `Rumslig kolumntyp %1 stöds ej` | `Den rumsliga kolumntypen %1 stöds inte` |
| `Unable to get list of spatially enabled tables from the database` | `Kan inte hämta lista med spatiala tabeller från databasen` | `Kan inte hämta listan över rumsligt aktiverade tabeller från databasen` |
| `Whole Number (smallint - 16bit)` | `Heltal (smallint - 16bit)` | `Heltal (smallint, 16 bitar)` |
| `Whole Number (integer - 32bit)` | `Heltal (integer - 32bit)` | `Heltal (integer, 32 bitar)` |
| `Whole Number (integer - 64bit)` | `Heltal (integer - 64bit)` | `Heltal (integer, 64 bitar)` |
| `Array of Number (integer - 32bit)` | `Matris av tal (integer - 32bit)` | `Matris med tal (integer, 32 bitar)` |
| `Array of Number (integer - 64bit)` | `Matris av tal (integer - 64bit)` | `Matris med tal (integer, 64 bitar)` |
| `Array of Number (double)` | `Matris av tal (double)` | `Matris med tal (double)` |
| `Array of Text` | `Matris av text` | `Matris med text` |
| `Text, fixed length (char)` | `Text, fixerad längd (text)` | `Text med fast längd (char)` |
| `Text, limited variable length (varchar)` | `Text, begränsad variabel längd (varchar)` | `Text med begränsad variabel längd (varchar)` |
| `Text, case-insensitive unlimited length (citext)` | `Text, skiftlägeskänslig, obegränsad längd (citext)` | `Text med obegränsad längd, utan skiftlägeskänslighet (citext)` |
| `Map (hstore)` | `Map (hstore)` | `Mappning (hstore)` |
| `%1 cursor states lost.\nSQL: %2\nResult: %3 (%4)` | `%1 markörstatus förlorade.\nSQL: %2\nResultat: %3 (%4)` | `%1 markörtillstånd har gått förlorade.\nSQL: %2\nResultat: %3 (%4)` |
| `connection still bad after reset.` | `anslutningen fortfarande bruten efter återställning.` | `anslutningen är fortfarande felaktig efter återställning.` |

Radbrytningar, platshållarna `%0` och `%1`–`%4`, URL:en, `SQL`, tekniska
datatyper samt `WriteOwner` ska bevaras oförändrade vid senare import. Ingen
extern ändring har gjorts.
