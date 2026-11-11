# QGIS: närhetsanalys, rasterisering och rutor 178

Datum: 11 november 2026
Resurs: `qgis-application`, språk `sv`
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen granskar närhetsanalys, rasterisering och GDAL:s rutindelning. NoData,
`gdal_rasterize`, `{}`, GDAL, CSV och CRS bevaras. `tile` översätts som
`ruta`, i enlighet med QGIS-terminologin.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Nodata value to use for the destination proximity raster` | `”Inget data”-värde att använda för närhetsrastret` | `NoData-värde för målnärhetsrastret` |
| `Proximity (raster distance)` | `Närhet (rasterdistans)` | `Närhet (rasteravstånd)` |
| `List of target pixels` | `Lista på målpixlar` | `Lista över målpixlar` |
| `Comma-separated list of pixel values in the source image to consider as target pixels. If not specified, all non-zero pixels will be considered target pixels.` | `Kommaseparerad lista av pixelvärden i källbilden som är att betrakta som målpixlar. Om inte angivet kommer alla icke noll pixlar att betraktas som målpixlar.` | `Kommaseparerad lista över pixelvärden i källbilden som ska betraktas som målpixlar. Om inga anges betraktas alla icke-nollpixlar som målpixlar.` |
| `The maximum distance to generate` | `Det största avståndet som kan skapas` | `Största avstånd som ska genereras` |
| `Value to apply to pixels within the maximum distance of target pixels` | `Värde att tilldela till pixlar som är inom maxavståndet från målpixlar` | `Värde som ska tilldelas pixlar inom det största avståndet från målpixlar` |
| `Value to apply to all pixels within the maximum distance of target pixels (including the target pixels) instead of a distance value` | `Värde att tilldela till alla pixlar som är inom maxavståndet från målpixlar (inklusive målpixlar) i stället för ett avståndsvärde` | `Värde som ska tilldelas alla pixlar inom det största avståndet från målpixlar, även målpixlarna, i stället för ett avståndsvärde` |
| `NoData value to use for the pixels beyond the maximum distance. If not provided, it will be set to the one from the output band, or ultimately to 65535.` | `NoData-värde att använda för pixlar bortanför största avståndet. Om inte angivet, kommer det att sättas till det från utdatabandet, eller i sista hand till 65535.` | `NoData-värde för pixlar bortom största avståndet. Om inget anges används värdet från utdatabandet, eller 65535 som sista utväg.` |
| `Field to use for a burn-in value` | `Fält att använda för värde att tilldela` | `Fält som ska användas för inbränningsvärde` |
| `A fixed value to burn` | `Ett fast värde att tilldela` | `Ett fast inbränningsvärde` |
| `Output raster size units` | `Enhet för utdatas rasterstorlek` | `Enheter för utdata-rastrets storlek` |
| `Width/Horizontal resolution` | `Bredd/Horisontal upplösning` | `Bredd/horisontell upplösning` |
| `Height/Vertical resolution` | `Höjd/Vertikal upplösning` | `Höjd/vertikal upplösning` |
| `Rasterize (vector to raster)` | `Rastrera (vektor till raster)` | `Rasterisera (vektor till raster)` |
| `Burn value extracted from the "Z" values of the feature` | `Bränn in värde extraherat från objektets ”Z”-värden` | `Bränn in ett värde hämtat från objektets Z-värden` |
| `Open options are not supported by gdal_rasterize version {} (requires GDAL version 3.7 or later)` | `Öppningsalternativ stöds inte av gdal_rasterize version {} (kräver GDAL version 3.7 eller senare)` | `Öppningsalternativ stöds inte av gdal_rasterize version {} (kräver GDAL-version 3.7 eller senare)` |
| `Input vector layer` | `Vektorlager med indata` | `Indatavektorlager` |
| `Input raster layer` | `Rasterlager med indata` | `Indatarasterlager` |
| `Add burn in values to existing raster values` | `Lägg till värden till befintliga rastervärden` | `Lägg till inbränningsvärden till befintliga rastervärden` |
| `Retile` | `Upprepa tile` | `Dela om till rutor` |
| `Input files` | `Indata-filer` | `Indatafiler` |
| `Overlap in pixels between consecutive tiles` | `Överlapp i pixlar mellan närliggande tiles` | `Överlappning i bildpunkter mellan intilliggande rutor` |
| `Number of pyramids levels to build` | `Antal pyramidnivåer att skapa` | `Antal pyramidnivåer som ska byggas` |
| `Use separate directory for each tiles row` | `Använd en katalog för varje tile-rad` | `Använd en separat katalog för varje rad med rutor` |
| `CSV file containing the tile(s) georeferencing information` | `CSV-fil som innehåller georefereringsinformation till tile(s)` | `CSV-fil som innehåller georefereringsinformation för rutorna` |

Ingen extern ändring har gjorts. Aktuella Transifex-enhetsidentifierare måste
hämtas och måltexterna jämföras före en separat deltafil kan skapas.
