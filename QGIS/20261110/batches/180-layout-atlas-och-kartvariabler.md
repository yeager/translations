# QGIS: layout, atlas och kartvariabler 180

Datum: 11 november 2026
Resurs: `qgis-application`, språk `sv`
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen granskar uttrycksvariabler för kartlayout, atlas och karta. DPI,
EPSG:4326, Proj4 och WKT behålls som tekniska namn. `composition` återges
enligt QGIS nuvarande användarterm `kartlayout`, och CRS som
`koordinatreferenssystem`.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Composition page height in mm (or specified custom units).` | `Kompositionens sidhöjd i mm (eller specificerade anpassade enheter).` | `Kartlayoutens sidhöjd i mm, eller angivna egna enheter.` |
| `Composition page width in mm (or specified custom units).` | `Kompositionens sidbredd i mm (eller specificerade anpassade enheter).` | `Kartlayoutens sidbredd i mm, eller angivna egna enheter.` |
| `Array of Y coordinate of the top of each page.` | `Array med Y koordinat för toppen av varje sida.` | `Matris med Y-koordinaten för överkanten på varje sida.` |
| `Current atlas coverage layer ID.` | `Nuvarande kartbokslager ID.` | `ID för det aktuella täckningslagret för atlasen.` |
| `Current atlas coverage layer name.` | `Nuvarande kartbokslagernamn.` | `Namn på det aktuella täckningslagret för atlasen.` |
| `Total number of features in atlas.` | `Totalt antal objekt i atlas.` | `Totalt antal objekt i atlasen.` |
| `Current atlas feature number.` | `Nuvarande kartboksobjektnummer.` | `Nummer för det aktuella atlasobjektet.` |
| `Current atlas file name.` | `Nuvarande kartboksfilnamn.` | `Filnamn för den aktuella atlasen.` |
| `Current atlas page name.` | `Nuvarande kartboks sidnamn.` | `Sidnamn för den aktuella atlasen.` |
| `Current atlas feature (as feature object).` | `Nuvarande kartboksobjekt (som objekt).` | `Aktuellt atlasobjekt (som objekt).` |
| `Current atlas feature ID.` | `Nuvarande kartboksobjekts ID.` | `ID för det aktuella atlasobjektet.` |
| `Current atlas feature geometry.` | `Nuvarande kartboksobjekts geometri.` | `Geometri för det aktuella atlasobjektet.` |
| `layout item unique ID.` | `Layoutobjekt unikt ID.` | `Layoutobjektets unika ID.` |
| `Left position of layout item (in mm).` | `Vänster position för layoutobjekt (i mm).` | `Vänster position för layoutobjektet, i mm.` |
| `Top position of layout item (in mm).` | `Övre position för layoutobjekt (i mm).` | `Övre position för layoutobjektet, i mm.` |
| `Width of layout item (in mm).` | `Bredd på layoutobjekt (i mm).` | `Bredd för layoutobjektet, i mm.` |
| `Height of layout item (in mm).` | `Höjd på layoutobjekt (i mm).` | `Höjd för layoutobjektet, i mm.` |
| `Geometry representing the current extent of the map.` | `Geometri som representerar aktuell kartutsträckning.` | `Geometri som representerar kartans aktuella utbredning.` |
| `Center of map.` | `Kartans centrum.` | `Kartans mittpunkt.` |
| `Coordinate reference system of map (e.g., 'EPSG:4326').` | `Kordinatsystem för kartan (t.ex. EPSG:4326)` | `Kartans koordinatreferenssystem, t.ex. ”EPSG:4326”.` |
| `Coordinate reference system of the map (full definition).` | `Koordinatsystem för kartan (hela definitionen)` | `Kartans koordinatreferenssystem (fullständig definition).` |
| `Acronym of the coordinate reference system of the map.` | `Akronym för koordinatsystemet för kartan.` | `Förkortning för kartans koordinatreferenssystem.` |
| `Acronym of the ellipsoid of the coordinate reference system of the map.` | `Akronym för ellipsoiden för koordinatsystemets för kartan.` | `Förkortning för ellipsoiden i kartans koordinatreferenssystem.` |
| `List of map layer IDs visible in the map.` | `Lista på kartlagerID som är synliga i kartan.` | `Lista över kartlager-ID:n som är synliga på kartan.` |
| `List of map layers visible in the map.` | `Lista på kartlager som är synliga i kartan.` | `Lista över kartlager som är synliga på kartan.` |
| `Start of the map's temporal time range (as a datetime value)` | `Start för kartans temporala tidsintervall (som ett datumtid-värde)` | `Start för kartans temporala tidsspann, som datum/tid-värde.` |
| `End of the map's temporal time range (as a datetime value)` | `Slut för kartans temporala tidsintervall (som ett datumtid-värde)` | `Slut för kartans temporala tidsspann, som datum/tid-värde.` |
| `Current frame number during animation playback` | `Aktuellt bildnummer under uppspelning av animnation` | `Aktuellt bildnummer under uppspelning av animation.` |
| `Last cursor position on the canvas in the project's geographical coordinates.` | `Sista muspekarposition på kartytan i projektets geografiska koordinater.` | `Senaste muspekarposition på kartytan i projektets geografiska koordinater.` |
| `Last cursor position on the canvas in the current layers's geographical coordinates. QGIS Server: When used in a maptip expression for a raster layer, this variable holds the GetFeatureInfo position.` | `Senaste position för pekaren på kartan i det aktiva lagrets geografiska koordinater. QGIS Server: När det används i karttips-uttryck för rasterlager, innehåller variabeln positionen för GetFeatureInfo.` | `Senaste muspekarposition på kartytan i det aktuella lagrets geografiska koordinater. QGIS Server: När variabeln används i ett karttipsuttryck för ett rasterlager innehåller den GetFeatureInfo-positionen.` |

Ingen extern ändring har gjorts. Aktuella Transifex-enhetsidentifierare måste
hämtas och måltexterna jämföras före en separat deltafil kan skapas.
