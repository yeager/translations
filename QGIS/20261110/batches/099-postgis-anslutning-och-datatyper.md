# QGIS: PostGIS-anslutning och datatyper 099

Datum: 10 november 2026  
Resurs: `qgis-application`, språk `sv`  
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen granskar anslutningsfel och typnamn från PostGIS-leverantören. Namnen
PostGIS, GEOS, SQL, `char`, `varchar`, `citext` och `hstore` bevaras som
tekniska namn. Platshållarna `%0` och `%1` samt radbrytningarna i respektive
felmeddelande bevaras.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Your PostGIS installation has no GEOS support. Feature selection and identification will not work properly. Please install PostGIS with GEOS support (http://geos.refractions.net)` | `Din PostGIS-installation har inget stöd för GEOS. Urval av objekt och identifiering kommer inte fungera ordentligt. Var vänlig installera PostGIS med GEOS-stöd (http://geos.refractions.net)` | `Din PostGIS-installation saknar stöd för GEOS. Objekturval och identifiering kommer inte att fungera korrekt. Installera PostGIS med stöd för GEOS (http://geos.refractions.net).` |
| `Database connection was successful, but the accessible tables could not be determined.` | `Databasanslutningen lyckades, men anslutningsbara tabeller kunde inte bestämmas.` | `Databasanslutningen lyckades, men de tillgängliga tabellerna kunde inte fastställas.` |
| `Cannot set WriteOwner permission to cert: %0 to allow removing it` | `Kan inte sätta WriteOwner behörighet till cert: %0 för att tillåta borttagning` | `Kan inte ange WriteOwner-behörighet för certifikatet %0 för att kunna ta bort det` |
| `Cannot remove cert: %0` | `Kan inte ta bort cert: %0` | `Kan inte ta bort certifikatet: %0` |
| `Unsupported spatial column type %1` | `Rumslig kolumntyp %1 stöds ej` | `Den rumsliga kolumntypen %1 stöds inte` |
| `Database connection was successful, but the accessible tables could not be determined.\nThe error message from the database was:\n%1` | `Databasanslutningen lyckades, men anslutningsbara tabeller kunde inte bestämmas. Felmeddelandet från databasen lyder:\n%1\n` | `Databasanslutningen lyckades, men de tillgängliga tabellerna kunde inte fastställas.\nDatabasens felmeddelande var:\n%1` |
| `Unable to get list of spatially enabled tables from the database` | `Kan inte hämta lista med spatiala tabeller från databasen` | `Kan inte hämta listan över tabeller med rumsligt stöd från databasen` |
| `Text, fixed length (char)` | `Text, fixerad längd (text)` | `Text med fast längd (char)` |
| `Text, limited variable length (varchar)` | `Text, begränsad variabel längd (varchar)` | `Text med begränsad variabel längd (varchar)` |
| `Text, case-insensitive unlimited length (citext)` | `Text, skiftlägeskänslig, obegränsad längd (citext)` | `Text med obegränsad längd, skiftlägesokänslig (citext)` |
| `Map (hstore)` | `Map (hstore)` | `Mappning (hstore)` |
| `Query could not be canceled [%1]` | `Fråga kunde inte avbrytas [%1]` | `Databasfrågan kunde inte avbrytas [%1]` |

Ingen extern ändring har gjorts. Aktuella Transifex-enhetsidentifierare måste
hämtas och måltexterna jämföras före en separat deltafil kan skapas.
