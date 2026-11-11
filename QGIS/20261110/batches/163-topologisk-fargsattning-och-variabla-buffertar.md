# QGIS: topologisk färgsättning och variabla buffertar 163

Datum: 10 november 2026
Resurs: `qgis-application`, språk `sv`
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen granskar topologisk färgsättning, variabla buffertar och
vektorhistogram. `color_id` är ett skapat attributnamn och ska behållas exakt.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `By feature count` | `Genom antal objekt` | `Efter antal objekt` |
| `By assigned area` | `Genom tilldelad area` | `Efter tilldelad area` |
| `By distance between colors` | `Genom avstånd mellan färger` | `Efter avstånd mellan färger` |
| `Assigns a color index to polygon features, so no adjacent polygons share the same color index.` | `Tilldelar ett färgindex till polygonobjekt så inga intilliggande polygoner delar samma färgindex.` | `Tilldelar polygonobjekt ett färgindex så att inga intilliggande polygoner har samma färgindex.` |
| Topologisk färgsättnings långa hjälptext | `medger`, `som ej rör varandra`, `tilldelar i färger` och flera onaturliga formuleringar. | `Den här algoritmen tilldelar polygonobjekt färgindex så att inga intilliggande polygoner har samma färgindex, samtidigt som antalet färger minimeras.\nDu kan ange ett valfritt minsta avstånd mellan objekt som får samma färg för att förhindra att närliggande, men icke angränsande, objekt får samma färg.\nVälj metod för färgtilldelningen. Standardmetoden försöker balansera antalet objekt per färgindex.\nLäget ”Efter tilldelad area” balanserar i stället den sammanlagda arean för objekt med varje färg. Det kan förhindra att stora objekt gör en färg alltför dominerande på en färgsatt karta.\nLäget ”Efter avstånd mellan färger” maximerar avståndet mellan objekt med samma färg och ger en jämnare färgfördelning över kartan.\nDu kan ange ett minsta antal färger. Färgindexet sparas i ett nytt attribut med namnet color_id.` |
| `The user expression {0} is not valid` | `Användaruttryck {0} är inte giltigt` | `Användaruttrycket {0} är inte giltigt` |
| `End cap style` | `Ändstil` | `Ändstil för linje` |
| `Join style` | `Ihopslagningsstil` | `Sammanfogningsstil` |
| `Buffer` | `Buffer` | `Buffert` |
| `Variable distance buffer` | `Variabelt buffertavstånd` | `Buffert med variabelt avstånd` |
| `Computes a buffer area whose size is defined by an attribute.` | `Beräknar en buffertarea vars storlek definieras av ett attribut.` | `Beräknar en buffertzon vars storlek definieras av ett attribut.` |
| `This algorithm computes a buffer area for all the features in an input layer. The size of the buffer for a given feature is defined by an attribute, so it allows different features to have different buffer sizes.` | `Denna algoritm beräknar en buffertzon för varje objekt i ett lager. Buffertzonernas storlek definieras av ett attribut, så att olika objekt kan ha olika stora buffertzoner.` | `Den här algoritmen beräknar en buffertzon för alla objekt i ett indatalager. Buffertzonens storlek för varje objekt definieras av ett attribut, vilket gör att olika objekt kan ha olika stora buffertzoner.` |
| `number of bins` | `antal fack` | `Antal intervall` |
| `This algorithm requires the Python “plotly” library. Please install this library and try again.` | `Denna algoritm kräver pythonbiblioteket &quot;plotly&quot;. Installera detta bibliotek och försök igen.` | `Den här algoritmen kräver Python-biblioteket ”plotly”. Installera biblioteket och försök igen.` |
| `Generates a histogram with the values of the attribute of a vector layer.` | `Skapar ett histogram med värdena av ett attribut från ett vektorlager. ` | `Skapar ett histogram med värdena i ett attribut från ett vektorlager.` |

Ingen extern ändring har gjorts. Aktuella Transifex-enhetsidentifierare måste
hämtas och måltexterna jämföras före en separat deltafil kan skapas.
