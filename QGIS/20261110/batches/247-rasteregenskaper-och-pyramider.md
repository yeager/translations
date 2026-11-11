# QGIS: rasteregenskaper och pyramider 247

Datum: 11 november 2026
Resurs: `qgis-application`, språk `sv`
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen granskar rasterlagrets egenskapsdialog, med fokus på pyramidfiler,
dataleverantörsfel och återgivningsinställningar. `GDAL`, `JPEG`, `libtiff`,
`WMS`, `WMTS`, `URI` och platshållarna `%1` och `%2` bevaras.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Could not insert provider into layer pipe (provider: %1, URI: %2)` | `Kunde inte lägga till datakällan i lagrets pipe; (datakälla: %1, URI: %2)` | `Kunde inte lägga till dataleverantören i lagerpipelinen (dataleverantör: %1, URI: %2).` |
| `By creating lower resolution copies of the data (pyramids) performance can be considerably improved as QGIS selects the most suitable resolution to use depending on the level of zoom.` | `Genom att skapa kopior med lägre upplösning (pyramider) kan prestanda avsevärt förbättras, genom att  QGIS väljer den lämpligaste upplösningen beroende på zoom-nivå.` | `Genom att skapa kopior av data med lägre upplösning, så kallade pyramider, kan prestandan förbättras avsevärt. QGIS väljer den lämpligaste upplösningen utifrån zoomnivån.` |
| `Please note that building internal pyramids may alter the original data file and once created they cannot be removed!` | `Den ursprungliga datafilen kan ändras när du bygger pyramider, och de kan ej tas bort efter de har skapats.` | `Observera att interna pyramider kan ändra den ursprungliga datafilen och inte kan tas bort när de har skapats.` |
| `The file was not writable. Some formats do not support pyramid overviews. Consult the GDAL documentation if in doubt.` | `Filen var inte skrivbar. Vissa format stödjer inte pyramider. Kontrollera med GDAL-dokumentation om du är osäker.` | `Filen var inte skrivbar. Vissa format stöder inte pyramidöversikter. Läs GDAL-dokumentationen om du är osäker.` |
| `Building pyramid overviews is not supported on this type of raster.` | `Denna typ av raster stödjer ej att bygga pyramider.` | `Den här rastertypen stöder inte pyramidöversikter.` |
| `Building internal pyramid overviews is not supported on raster layers with JPEG compression and your current libtiff library.` | `Nuvarande libtiff-bibliotek stödjer inte att bygga pyramider från lager med JPEG-kompression.` | `Din aktuella libtiff-version stöder inte interna pyramidöversikter för rasterlager med JPEG-komprimering.` |
| `Render type` | `Renderingstyp` | `Återgivningstyp` |
| `Advertise as background layer` | `Annonsera som bakgrundslager` | `Ange som bakgrundslager` |
| `There are no raster attribute tables associated with this data source.

If the current symbology can be converted to an attribute table you can create a new attribute table using the context menu available in the layer tree or the button below.

You can also import an existing raster attribute table from a VAT.DBF file and associate it with a raster band.` | `Det finns ingen attributtabell för raster associerad för denna datakälla.

Om den nuvarande symbologin kan konverteras ill en attributtabell kan du skapa en ny attributtabell genom att använda kontextmenyn tillgänglig i lagerträdet eller knappen nedan.

Du kan också importera en befintlig attributtabell för raster från en VAT.DBF-fil och associera den med ett rasterband.` | `Det finns inga rasterattributtabeller kopplade till den här datakällan.

Om den aktuella symbologin kan konverteras till en attributtabell kan du skapa en ny attributtabell via kontextmenyn i lagerträdet eller med knappen nedan.

Du kan även importera en befintlig rasterattributtabell från en VAT.DBF-fil och koppla den till ett rasterband.` |

Ingen extern ändring har gjorts. De rekommenderade texterna är lokala
kandidater tills de har jämförts mot aktuella Transifex-enheter vid en senare
uppladdning.
