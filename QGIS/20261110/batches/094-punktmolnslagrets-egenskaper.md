# QGIS: punktmolnslagrets egenskaper 094

Datum: 10 november 2026  
Resurs: `qgis-application`, språk `sv`  
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen granskar metadata och egenskapsdialogen för punktmolnslager. Den
rättar den felaktiga komponentrubriken `Vector Tile Layer Properties`,
normaliserar ID-etiketter och använder `koordinatreferenssystem (CRS)`.
HTML-markupen bevaras.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Offset X` | `Offset X` | `Förskjutning X` |
| `Offset Y` | `Offset Y` | `Förskjutning Y` |
| `Project ID` | `ProjektID` | `Projekt-ID` |
| `System ID` | `SystemID` | `System-ID` |
| `Software ID` | `ProgramID` | `Program-ID` |
| `Restore Default` | `Återställ Standard` | `Återställ standard` |
| `Select transformation for the layer` | `Välj transformation för lager` | `Välj transformation för lagret` |
| `Vector Tile Layer Properties` | `Egenskaper för vektortile-lager` | `Egenskaper för punktmolnslager` |
| `Assigned Coordinate Reference System (CRS)` | `Tilldelat koordinatsystem (CRS)` | `Tilldelat koordinatreferenssystem (CRS)` |
| HTML-hjälpen för tilldelat CRS | Oidiomatisk svenska och inkonsekvent CRS-term | `<html><head/><body><p><span style=" font-weight:600;">Varken den ursprungliga datakällan ändras eller punkterna omprojiceras när du ändrar det här alternativet. I stället kan alternativet användas för att åsidosätta lagrets koordinatreferenssystem (CRS) i det här projektet om CRS:et inte kunde identifieras eller har identifierats fel.</span></p></body></html>` |
| `Note: The displayed statistics are estimated based on sampling data from the dataset and it is not guaranteed to be accurate!` | `Obs: Den visade statistiken är uppskattad med hjälp av stickprovsdata från datasetet och är inte garanterad att vara exakt!` | `Obs: Den visade statistiken bygger på stickprov från datauppsättningen och kanske inte är exakt.` |
| `Include automatically in print layout legend items` | `Inkludera automatiskt i utskriftslayouters teckenförklaringselement` | `Inkludera automatiskt i teckenförklaringsobjekt i utskriftslayouten` |

Ingen extern ändring har gjorts. Aktuella Transifex-enhetsidentifierare måste
hämtas och måltexterna jämföras före en separat deltafil kan skapas.
