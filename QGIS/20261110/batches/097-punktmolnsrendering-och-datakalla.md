# QGIS: punktmolnsrendering och datakälla 097

Datum: 10 november 2026  
Resurs: `qgis-application`, språk `sv`  
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen granskar återstående unika strängar i punktmolnsrenderarens dialog och
dialogen för att lägga till punktmolnsdata. Redan dokumenterade identiska
källsträngar, till exempel `Eye-Dome Lighting`, rutiketter och största
triangelsida, tas inte med på nytt. HTTP(S), filändelser och markeringsnyckeln
`&` bevaras.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `This renderer doesn't implement a graphical interface.` | `Denna renderare har inget grafisk gränssnitt.` | `Den här renderaren har inget grafiskt gränssnitt.` |
| `Overview switching scale` | `Skala för byte i översikt` | `Skala för byte av översikt` |
| `Sets the zoom level at which the individual point cloud files will get rendered instead of the overview or their extents.\n\nNormal means roughly when the point cloud extent no longer fits the map extent.\n\nSelect Earlier to switch at a smaller scale (zoomed out) or Later to switch at a larger scale (zoomed in). ` | `Ställer in zoomnivå vid vilken de enskilda punktmolnsfilerna kommer renderas i stället för översikten av dess utsträckningar.\n\nNormal betyder grovt när punktmolnsutsträckningen inte längre får plats i kartan.\n\nVälj Tidigare för att byta vid mindre skala (utzoomad) eller Senare för att byta vid större skala (inzoomad).` | `Anger den zoomnivå vid vilken de enskilda punktmolnsfilerna renderas i stället för översikten eller deras utbredningar.\n\nNormal innebär ungefär att punktmolnets utbredning inte längre ryms inom kartans utbredning.\n\nVälj Tidigare för att byta vid mindre skala (utzoomat) eller Senare för att byta vid större skala (inzoomat).` |
| `Adjusts how strong the added shading will be. Greater values mean stronger effect.` | `Justerar hur stark den tillagda skuggningen kommer bli. Större värden ger större effekt.` | `Justerar styrkan på den tillagda skuggningen. Ett högre värde ger starkare effekt.` |
| `Distance away from the original pixel to sample neighbors.` | `Avstånd från ursprungspixeln för att sampla grannar.` | `Avstånd från den ursprungliga pixeln vid sampling av grannar.` |
| `Vertical exageration for hillshading` | `Vertikal förstoring för höjdskuggning` | `Vertikal överhöjning för terrängskuggning` |
| `Use multidirectional lights instead of the specified azimuth for hillshading.` | `Använd flerriktat ljus istället för den angivna azimuten för höjdskuggning.` | `Använd flerriktat ljus i stället för den angivna azimuten för terrängskuggning.` |
| `Open Point Cloud Dataset` | `Öppna dataset för punktmoln` | `Öppna punktmolnsdatauppsättning` |
| `No layers selected.` | `Inga lager valda.` | `Inga lager har valts.` |
| `Invalid point cloud URL "%1", please make sure your URL ends with /ept.json, .copc.laz, .vpc or .vpz` | `Ogiltigt URL för punktmoln. "%1" Försäkra dig om att den slutar på /ept.json, .copc.laz, .vpc eller .vpz` | `Ogiltig URL för punktmoln: "%1". Kontrollera att URL:en slutar med /ept.json, .copc.laz, .vpc eller .vpz.` |
| `Bucket or container` | `Hink eller behållare` | `Bucket eller behållare` |
| `Authentication` | `Verifiering` | `Autentisering` |
| `Protoco&l: HTTP(S), cloud, etc.` | `Protokol&l: HTTP(S), cloud, etc.` | `Protokol&l: HTTP(S), moln osv.` |
| `Point cloud dataset(s)` | `Dataset för punktmoln` | `Punktmolnsdatauppsättning(ar)` |
| `Generating attributes statistics` | `Skapar statistik för attribut` | `Beräknar attributstatistik` |

Ingen extern ändring har gjorts. Aktuella Transifex-enhetsidentifierare måste
hämtas och måltexterna jämföras före en separat deltafil kan skapas.
