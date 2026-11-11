# QGIS: 3D-punktsymboler och punktmoln 092

Datum: 10 november 2026  
Resurs: `qgis-application`, språk `sv`  
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen granskar 3D-punktsymboler och punktmolnsrendering. `Billboard` är ett
tekniskt grafiknamn för en kameravänd symbol och behålls därför. `Screen space
error` översätts i UI som `skärmfel`; QGIS API beskriver det som ett felmått
som beräknas för renderingen. Radbrytningar och de två tomma raderna i den
längsta hjälpen bevaras.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `3D Model` | `3d-modell` | `3D-modell` |
| `Billboard` | `Skylt` | `Billboard` |
| `Billboard symbol` | `Skyltsymbol` | `Billboardsymbol` |
| `Maximum screen space error` | `Största fel, skärmavstånd` | `Maximalt skärmfel` |
| `Show bounding boxes` | `Visa begränsningsboxar` | `Visa begränsningsrutor` |
| `Contrast\nenhancement` | `Kontrast\nförhöjning` | `Kontrast-\nförbättring` |
| `The distance in pixels between the points of the smallest chunk to be rendered.\nRaising this value will result in a less detailed scene which can improve performance` | `Avståndet i pixlar mellan punkterna i den minsta bit som ska renderas.\nÖkning av detta värde kommer att resultera i mindre detaljerad scen som kan förbättra prestandan` | `Avståndet i pixlar mellan punkterna i den minsta del som ska renderas.\nEtt högre värde ger en mindre detaljerad scen och kan förbättra prestandan.` |
| `The maximum number of points that will be rendered simultaneously.\nRaising this value may allow missing chunks to be rendered while lowering it may improve performance` | `Det största antal punkter som kommer renderas samtidigt.\nÖkning av detta värde kan tillåta att saknade bitar renderas medan sänkning av det kan förbättra prestandan` | `Det högsta antal punkter som renderas samtidigt.\nEtt högre värde kan göra att saknade delar renderas, medan ett lägre värde kan förbättra prestandan.` |
| `Render as a Surface (Triangulate)` | `Rendera som yta (triangulera)` | `Rendera som en yta (triangulera)` |
| `Maximum Triangle Side Size in Horizontal Plan` | `Största triangelsida i horisontalplanet` | `Största längd på triangelsida i horisontalplanet` |
| `When zoomed out` | `När utzommad` | `När du har zoomat ut` |
| Hjälpen för `Overview switching scale` och `screen space error threshold` | Otydligt `skärmavståndsfel`, felaktiga begränsningsboxar och tung ordföljd | `Anger tröskelvärdet för skärmfelet då detaljerade 3D-rutor i punktmolnet renderas i stället för deras begränsningsrutor.\n\nNormal innebär att rutor växlar till detaljerad rendering när de upptar en märkbar del av skärmen.\n\nVälj Tidigare för att läsa in detaljerade rutor på större avstånd, när du har zoomat ut, eller Senare för att växla först när du har zoomat in mycket nära.` |

Ingen extern ändring har gjorts. Aktuella Transifex-enhetsidentifierare måste
hämtas och måltexterna jämföras före en separat deltafil kan skapas.
