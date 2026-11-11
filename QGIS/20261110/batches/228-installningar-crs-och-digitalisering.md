# QGIS: inställningar, CRS och digitalisering 228

Datum: 11 november 2026
Resurs: `qgis-application`, språk `sv`
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen fortsätter granskningen av inställningsdialogen, med fokus på CRS,
nätverk, projektformat och digitalisering. De etablerade QGIS-termerna
`snäppning`, `koordinatreferenssystem`, `kartyta` och `konturlinje` används.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Snap tolerance` | `Snappningstolerans` | `Snäppningstolerans` |
| `Default snapping tolerance` | `Standardtolerans` | `Standardtolerans för snäppning` |
| `Search radius for vertex edits` | `Sökradie för nodredigeringar` | `Sökradie för brytpunktsredigering` |
| `Show markers only for selected features` | `Visa markör bara för valda objekt` | `Visa markörer endast för valda objekt` |
| `Join style` | `Ihopslagningsstil` | `Sammanfogningsstil` |
| `In some cases more than one GDAL driver can be used to load the same raster format. Use the list below to specify which to use.` | `I vissa fall kan mer en ett GDAL-dataplugin användas för att öppna samma rasterformat. Använd listan nedanför för att välja vilken som ska användas.` | `I vissa fall kan mer än en GDAL-drivrutin användas för att läsa in samma rasterformat. Använd listan nedan för att ange vilken som ska användas.` |
| `When a new layer is created, or when a layer is loaded that has no CRS` | `När ett nytt lager skapas, eller när ett lager läggs till kartfönstret som inte har något definierat koordinatsystem` | `När ett nytt lager skapas eller ett lager utan koordinatreferenssystem läses in` |
| `Timeout for network requests (ms)` | `Tidsbegränsning på nätverksförfrågan (ms)` | `Tidsgräns för nätverksbegäranden (ms)` |
| `Default expiration period for WMS-C/WMTS tiles (hours)` | `Standardperiod för giltighet av WMS-C/WMTS tiles (timmar)` | `Standardgiltighetstid för WMS-C/WMTS-rutor (timmar)` |
| `Host` | `Dator` | `Värd` |
| `Proxy type` | `Mellanvärdstyp` | `Proxytyp` |
| `Default uses system's proxy` | `Default använder systemets proxy` | `Standard använder systemets proxy` |
| `Use CRS from first layer added` | `Använd koordinatsystem från först tillagda lager` | `Använd koordinatreferenssystemet från det första lagret som läggs till` |
| `If checked, QGIS project news is shown on the welcome page on startup` | `Om markerad visas QGIS projektnyheter på välkomstsidan vid start` | `Om rutan är markerad visas QGIS-projektnyheter på välkomstsidan vid start` |
| `Default CRS for layers` | `Standardkoordinatsystem för lager` | `Standardkoordinatreferenssystem för lager` |
| `UI theme` | `UI-tema` | `Gränssnittstema` |
| `Set Current Project as Default` | `Sätt nuvarande projekt som standardmall` | `Ange aktuellt projekt som standard` |
| `The auxiliary data will be kept in a separate .qgd data file which must be distributed along with the .qgs project file.` | `Extra data kommer spara si en separat .qgd fil som måste distribueras tillsammans med .qgs projektfilen.` | `Hjälpdata sparas i en separat .qgd-datafil som måste distribueras tillsammans med .qgs-projektfilen.` |
| `Prompt for sublayers when opening` | `Fråga efter underlager vid öppnande` | `Fråga efter underlager vid öppning` |
| `Localized data paths for basemaps, logos, etc. (in order of preference)` | `Lokala datasökvägar för baskartor, logotyper, etc. (i preferensordning)` | `Lokala datasökvägar för baskartor, logotyper osv. (i prioritetsordning)` |
| `Raise selected localized data path priority` | `Höj prioritet för vald lokal datasökväg` | `Höj prioriteten för den valda lokala datasökvägen` |
| `Lower selected localized data path priority` | `Sänk prioritet för vald datasökväg` | `Sänk prioriteten för den valda lokala datasökvägen` |
| `Hidden Browser Paths` | `Dold sökväg för datakällor` | `Dolda sökvägar i datakällpanelen` |
| `Default Map Appearance (overridden by project properties)` | `Standardutseende i kartfönster (projektinställningar har större vikt)` | `Standardutseende för kartan (åsidosätts av projektegenskaper)` |
| `Predefined Scales` | `Fördefinerade skalor` | `Fördefinierade skalor` |
| `Curve Offset Tool` | `Kurvoffset-verktyg` | `Kurvförskjutningsverktyg` |
| `Grid and Guide Defaults` | `Standard för rutnät och hjälplinjer` | `Standardinställningar för rutnät och hjälplinjer` |
| `In some cases more than one GDAL driver can be used to load the same vector format. Use the list below to specify which to use.` | `I vissa fall kan mer en ett GDAL-datakällan användas för att öppna samma vektorformat. Använd listan nedanför för att välja vilken som ska användas.` | `I vissa fall kan mer än en GDAL-drivrutin användas för att läsa in samma vektorformat. Använd listan nedan för att ange vilken som ska användas.` |
| `Cache Settings` | `Cache-inställningar` | `Cacheinställningar` |
| `Accuracy Warnings` | `Noggranhetsvarningar` | `Noggrannhetsvarningar` |
| `If the inherent inaccuracy in a selected CRS exceeds this threshold a warning message will be shown` | `Om det inneboende osäkerheten i ett valt koordinatsystem överstiger detta tröskelvärde kommer ett varningsmeddelande visas` | `Om den inneboende osäkerheten i ett valt koordinatreferenssystem överstiger detta tröskelvärde visas ett varningsmeddelande` |
| `Default snapping type` | `Standard snappningstyp` | `Standardtyp för snäppning` |
| `Show feature count for newly added layers` | `Visa objektantal för nya tillagda lager` | `Visa objektantal för nyligen tillagda lager` |
| `Separator` | `avskiljare` | `Avgränsare` |
| `Font <i>(QGIS restart required)</i>` | `Typsnitt <i>(Kräver omstart av QGIS</i>` | `Typsnitt <i>(QGIS måste startas om)</i>` |
| `QGZ Bundled project format` | `QGZ Packat projektformat` | `QGZ-format för paketerade projekt` |
| `Saved in a clear text, does not embed auxiliary data` | `Sparas i klartext, bäddar inte in extra data` | `Sparas som klartext och bäddar inte in hjälpdata` |
| `Specify the cache size in megabytes. Clear the value to enable smart cache size, which sets the maximum cache size based on available space.` | `Ange cachestorleken i megabytes. Rensa värdet för att aktivera smart cachestorlek som sätter största cachestorlek baserat på tillgängligt utrymme.` | `Ange cachestorleken i megabyte. Rensa värdet för att aktivera smart cachestorlek, som anger högsta cachestorlek utifrån tillgängligt utrymme.` |

CRS, WMS-C, WMTS, GDAL, QGZ, filändelser och markupen `<i>…</i>` ska
bevaras oförändrade vid senare import. Ingen extern ändring har gjorts.
