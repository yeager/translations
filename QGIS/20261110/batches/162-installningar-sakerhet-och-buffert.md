# QGIS: inställningar, säkerhet och buffert 162

Datum: 10 november 2026
Resurs: `qgis-application`, språk `sv`
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen granskar 3D-inställningar, SSL-varningar, topologisk färgsättning och
buffertverktyget. SSL, CRS, URL, `color_id` och tekniska måttenheter bevaras.
HTML-markeringen i SSL-varningen ska vara oförändrad vid en senare deltafil.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| ` map units` | `kartenheter` | `kartenheter` |
| `Shadow bias` | `Skugg-bias` | `Skuggförskjutning` |
| `Number of smooth iterations. More iterations results in smoother geometries, at the expense of greatly increasing the number of vertices in those geometries.` | `Antal utjämningsupprepningar. Fler upprepningar ger jämnare geometrier på bekostnad av stor ökning av antalet brytpunkter i dessa geometrier.` | `Antal utjämningsiterationer. Fler iterationer ger jämnare geometrier, men ökar också antalet brytpunkter i geometrierna avsevärt.` |
| `Offset` | `Offset` | `Förskjutning` |
| `Offset from existing vertices at which to insert smoothed vertices. Larger values result in "looser" smoothing, smaller values result in "tight" smoothing.` | `Förskjutning från existerande brytpunkter där utjämnade brytpunkter kan skapas. Större värde ger en "lösare" utjämning, mindre värde ger en "tightare" utjämning.` | `Förskjutning från befintliga brytpunkter där utjämnade brytpunkter infogas. Större värden ger en lösare utjämning och mindre värden ger en tätare utjämning.` |
| `Convention` | `Konventionen` | `Konvention` |
| `When checked, the scene's lighting will reflect the skybox appearance` | `När markerad kommer scenens ljussättning återspegla skyboxens utseende` | `När alternativet är markerat återspeglar scenens ljussättning skyboxens utseende` |
| `Enable environmental lighting effects` | `Aktivera miljömässiga ljussättningseffekter` | `Aktivera omgivningsljuseffekter` |
| SSL-varningen | `värden du ansluter till` används i stället för värd. | `Ett eller flera SSL-fel uppstod när värden som du ansluter till verifierades. Granska följande fellista och klicka på Ignorera för att fortsätta eller Avbryt för att avbryta anslutningen.` med oförändrad omgivande HTML. |
| `Project CRS: %1` | `Projektets koordinatsystem: %1` | `Projektets koordinatreferenssystem: %1` |
| `Default CRS: %1` | `Standardkoordinatsystem: %1` | `Standardkoordinatreferenssystem: %1` |
| `Layer CRS: %1` | `Lagrets koordinatsystem: %1` | `Lagrets koordinatreferenssystem: %1` |
| `%3 request failed [error: %1 - url: %2]` | `%3 förfrågan misslyckades [fel: %1 - url: %2]` | `%3-begäran misslyckades [fel: %1, URL: %2]` |
| `%4 request error [status: %1 - reason phrase: %2] for %3` | `%4 förfrågningsfel [status: %1 - orsaksfras: %2] för %3` | `Fel i %4-begäran [status: %1, orsaksfras: %2] för %3` |
| `There is already a layout named “%1”.` | `Det finns redan en layout kallad "%1".` | `Det finns redan en layout med namnet ”%1”.` |
| `QGIS Development Server listening on http://%1:%2` | `QGIS Utvecklingsserver lyssnar på http://%1:%2` | `QGIS utvecklingsserver lyssnar på http://%1:%2` |
| `CTRL+C to exit` | `CTRL+C för avbryt` | `Avsluta med Ctrl+C` |
| `Assigns a color index to polygon features, so no adjacent polygons share the same color index.` | `Tilldelar ett färgindex till polygonobjekt så inga intilliggande polygoner delar samma färgindex.` | `Tilldelar polygonobjekt ett färgindex så att inga intilliggande polygoner har samma färgindex.` |
| Topologisk färgsättningshjälp | Har felaktig formulering i lägena för area och färgavstånd. | Översätt om med termerna `polygonobjekt`, `färgindex`, `intilliggande`, `färgsatt karta`, `tilldelad area` och `avstånd mellan färger`; bevara raden `color_id` exakt. |
| `Buffer` | `Buffer` | `Buffert` |
| `Variable distance buffer` | `Variabelt buffertavstånd` | `Buffert med variabelt avstånd` |
| `Computes a buffer area whose size is defined by an attribute.` | `Beräknar en buffertarea vars storlek definieras av ett attribut.` | `Beräknar en buffertzon vars storlek definieras av ett attribut.` |
| `This algorithm computes a buffer area for all the features in an input layer. The size of the buffer for a given feature is defined by an attribute, so it allows different features to have different buffer sizes.` | `Denna algoritm beräknar en buffertzon för varje objekt i ett lager. Buffertzonernas storlek definieras av ett attribut, så att olika objekt kan ha olika stora buffertzoner.` | `Den här algoritmen beräknar en buffertzon för alla objekt i ett indatalager. Buffertzonens storlek för varje objekt definieras av ett attribut, vilket gör att olika objekt kan ha olika stora buffertzoner.` |
| `number of bins` | `antal fack` | `Antal intervall` |
| `Generates a histogram with the values of the attribute of a vector layer.` | `Skapar ett histogram med värdena av ett attribut från ett vektorlager. ` | `Skapar ett histogram med värdena i ett attribut från ett vektorlager.` |

Ingen extern ändring har gjorts. Aktuella Transifex-enhetsidentifierare måste
hämtas och måltexterna jämföras före en separat deltafil kan skapas.
