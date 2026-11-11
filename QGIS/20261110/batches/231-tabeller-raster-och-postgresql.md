# QGIS: tabeller, raster och PostgreSQL 231

Datum: 11 november 2026
Resurs: `qgis-application`, språk `sv`
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen granskar tabellkolumner, paletterade raster och början av
PostgreSQL-anslutningarna. SQL-lägena, PostgreSQL, filformatet `.clr` och
namnen på interna register behålls.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `[Action Widget]` | `[Kommando Widget]` | `[Åtgärdskomponent]` |
| `Organize Table columns` | `Organisera tabellkolumner` | `Ordna tabellkolumner` |
| `Hide All` | `Göm alla` | `Dölj alla` |
| `Hides all the fields and actions in the table` | `Gömmer alla fält och kommandon i tabellen` | `Döljer alla fält och åtgärder i tabellen` |
| `Displays all the fields and actions in the table` | `Visar alla fält och kommandon i tabellen` | `Visar alla fält och åtgärder i tabellen` |
| `Toggles visibility of the selected fields and actions` | `Växlar synlighet för valda fält och kommandon` | `Växlar synligheten för de valda fälten och åtgärderna` |
| `Connection failed` | `Anslutningen avbröts` | `Anslutningen misslyckades` |
| `Last modified time` | `Senast ändrad tid` | `Tidpunkt för senaste ändring` |
| `Last modified user` | `Senast ändrad användare` | `Senast ändrad av` |
| `View` | `Visa` | `Vy` |
| `Materialized view` | `Uppkommen visning` | `Materialiserad vy` |
| ` (srid %1)` | ` (srid %1)` | ` (SRID %1)` |
| ` (unknown srid)` | `(okänd srid)` | ` (okänt SRID)` |
| `Change Color…` | `Ändra färg….` | `Ändra färg…` |
| `Change Opacity…` | `Ändra opacitet…` | `Ändra ogenomskinlighet…` |
| `Load Classes from Layer` | `Läs in klasser från lager` | `Läs in klasser från lagret` |
| `Load Color Table from File` | `Läs in färgkarta från fil` | `Läs in färgtabell från fil` |
| `Load Color Table` | `Läs in färgkarta` | `Läs in färgtabell` |
| `Opacity` | `Opacitet` | `Ogenomskinlighet` |
| `Change color opacity [%]` | `Ändra färgopacitet [%]` | `Ändra färgens ogenomskinlighet [%]` |
| `Could not interpret file as a raster color table.` | `Kunde inte tolka fil som en rasterfärgstabell.` | `Det gick inte att tolka filen som en rasterfärgtabell.` |
| `The classification band was changed from %1 to %2.\nShould the existing classes be deleted?` | `Klassificeringsbandet ändrades från %1 till %2.\nSkall existerande klasser tas bort?` | `Klassificeringsbandet ändrades från %1 till %2.\nSka de befintliga klasserna tas bort?` |
| `Add values manually` | `Lägg till värden för hand` | `Lägg till värden manuellt` |
| `Delete All` | `Radera alla` | `Ta bort alla` |
| `Hide text` | `Göm text` | `Dölj text` |
| `Paste Transformations` | `Klista in transformationer` | `Klistra in transformationer` |
| `Untwine executable not found %1` | `Körbar fil för Untwine hittades inte %1` | `Den körbara filen för Untwine hittades inte: %1` |
| `Another indexing process is running (or finished with crash) for file %1` | `En annan indexeringsprocess kör (eller avslutades med krasch) för filen %1` | `En annan indexeringsprocess körs för filen %1 eller avslutades med en krasch` |
| `Append georeference information` | `Lägg till georefereringsinformation` | `Lägg till georeferensinformation` |
| `Export RDF metadata (title, author, etc.)` | `Exportera RDF metadata (titel, författare, etc.)` | `Exportera RDF-metadata (titel, författare osv.)` |
| `Disables tiled rendering of raster layers. This setting may improve the export quality in some circumstances, at the cost of much greater memory usage during exports.` | `Inaktiverar rutbaserad rendering av rasterlager. Denna inställning kan förbättra exportkvalitén under vissa omständigheter, till priset av mycket högre minnesanvändning under exporter.` | `Inaktiverar rutbaserad återgivning av rasterlager. Inställningen kan i vissa fall förbättra exportkvaliteten, men använder då betydligt mer minne vid export.` |
| `Uncheck layers to avoid exporting vector feature information for those layers, and optionally set the group name to allow multiple layers to be joined into a single logical PDF group. Layers can be dragged and dropped to rearrange their order in the generated Geospatial PDF table of contents.` | `Bocka av lager för att undvika att vektorobjektsinformation exporteras för dessa lager och ange eventuellt gruppnamn för att tillåta att flera lager förenas till en logisk PDF-grupp. Lager kan dras och släppas för att ordna om  dem i den skapade geospatial  PDF:ens innehållsförteckning.` | `Avmarkera lager för att inte exportera vektorobjektsinformation för dem. Du kan ange ett gruppnamn för att förena flera lager till en logisk PDF-grupp. Dra och släpp lager för att ändra deras ordning i innehållsförteckningen i den skapade geospatiala PDF-filen.` |
| `disable` | `tillåt ej` | `inaktivera` |
| `verify-ca` | `verifiera ca` | `verifiera CA` |
| `verify-full` | `verifiera komplett` | `verifiera fullständigt` |
| `Saving Passwords` | `Sparar lösenord` | `Spara lösenord` |
| `Connection failed - consult message log for details.` | `Anslutning misslyckades - se meddelandelogg för detaljer.` | `Anslutningen misslyckades. Se meddelandeloggen för mer information.` |
| `Authentication` | `Verifiering` | `Autentisering` |
| `When searching for spatial tables that are not in the geometry_columns tables, restrict the search to tables that are in the public schema (for some databases this can save lots of time)` | `Sökning för rumsliga tabeller som inte finns i tabellen geometri_kolumner begränsa sökningen till tabeller som finns i det allmäna schemat (för vissa databaser sparar detta mycket tid)` | `När rumsliga tabeller som saknas i geometry_columns söks, begränsa sökningen till tabeller i schemat public. För vissa databaser kan detta spara mycket tid.` |
| `Only look in the 'public' schema` | `Leta bara i 'public' schema` | `Sök bara i schemat 'public'` |

Platshållare, radbrytningar, ellips, registeridentifierare och formatnamn ska
bevaras oförändrade vid senare import. Ingen extern ändring har gjorts.
