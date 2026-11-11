# QGIS: nätlageregenskaper och vertikal utvärdering 212

Datum: 11 november 2026
Resurs: `qgis-application`, språk `sv`
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen rättar felstavade datamängder, enhetliggör `mesh` till `nät` och
förtydligar tids- och höjdinställningar i nätlagrets egenskaper.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Find Closest Dataset Before Requested Time` | `Hitta närmsta datset före begärd tid` | `Hitta närmaste datamängd före den begärda tiden` |
| `Find Closest Dataset From Requested Time (After or Before)` | `Hitta närmsta datset från begärd tid (efter eller före)` | `Hitta närmaste datamängd till den begärda tiden (efter eller före)` |
| `Restore Default` | `Återställ Standard` | `Återställ standard` |
| `Rendering` | `Rendering` | `Återgivning` |
| `Assigned Coordinate Reference System (CRS)` | `Tilldelat koordinatsystem (CRS)` | `Tilldelat koordinatreferenssystem (CRS)` |
| `Changing this option does not modify the original data source or perform any reprojection of the mesh. Rather, it can be used to override the layer's CRS within this project if it could not be detected or has been incorrectly detected.` | `Att ändra detta alternativ modifierar inte originaldata eller utför någon omprojicering av trådmodellen (mesh). I stället kan det användas för att åsidosätta lagrets koordinatsystem i projektet om det inte kunde detekteras eller har blivit felaktigt detekterat.` | `Om du ändrar detta alternativ ändras inte den ursprungliga datakällan och nätet omprojiceras inte. Alternativet kan i stället användas för att åsidosätta lagrets koordinatreferenssystem i det här projektet om det inte kunde identifieras eller har identifierats felaktigt.` |
| `Simplify Mesh` | `Förenkla mesh` | `Förenkla nät` |
| `Provider Time Settings` | `Inställningar av tid för källan` | `Dataleverantörens tidsinställningar` |
| `Default time unit of mesh data provider is hour, change to override the time unit` | `Standardenhet för tid för mesh-data är timme, ändra för att åsidosätta tidsenheten` | `Dataleverantörens standardtidsenhet för nätdata är timme. Ändra för att åsidosätta tidsenheten.` |
| `Reference time used to render mesh dataset when using temporal range or temporal animation` | `Referenstid som används för att rendera mesh-dataset när tidintervall tidsanimering används` | `Referenstid som används för att återge nätets datamängd när ett tidsintervall eller en tidsanimering används` |
| `Reload from provider` | `Läs in på nytt från datakälla` | `Läs in igen från dataleverantören` |
| `Dataset matching method` | `Datasetets matchningsmetod` | `Metod för att matcha datamängder` |
| `Method for selection of temporal mesh dataset from a range time` | `Metod för val av tids-mesh-dataset från ett tidsintervall` | `Metod för att välja en tidsberoende datamängd för nätet från ett tidsintervall` |
| `Always treat as a static dataset even if the temporal navigation is on` | `Behandla alltid som ett statiskt dataset även om tidsnavigeringen är på` | `Behandla alltid som en statisk datamängd även om tidsnavigering är aktiverad` |
| `Treat as Static Dataset` | `Behandla som statiskt dataset` | `Behandla som statisk datamängd` |
| `Always take reference time from data source` | `Ta alltid referenstid från datakälla` | `Hämta alltid referenstiden från datakällan` |
| `Include automatically in print layout legend items` | `Inkludera automatiskt i utskriftslayouters teckenförklaringselement` | `Inkludera automatiskt i teckenförklaringsobjekt i utskriftslayouter` |
| `Invalid mesh definition, vertex definition does not contain x, y` | `Ogiltig meshdefinition, nod-definition innehåller inte x, y` | `Ogiltig nätdefinition: noddefinitionen innehåller inte x, y` |
| `Invalid mesh definition, vertex index must be positive value` | `Ogiltig meshdefinition, nod-index måste vara positiva värden` | `Ogiltig nätdefinition: nodindex måste vara ett positivt värde` |
| `Invalid mesh definition, missing vertex id defined in face` | `Ogiltig meshdefinition, saknat nod-id i yta` | `Ogiltig nätdefinition: nod-id saknas i ytan` |
| `Invalid mesh definition, edge must contain at least 2 vertices` | `Ogiltig meshdefinition, kant måste innehålla minst 2 brytpunkter` | `Ogiltig nätdefinition: kanten måste innehålla minst två noder` |
| `Invalid mesh definition, unable to read mesh with both edges and faces` | `Ogiltig meshdefinition, kan inte läsa mesh med både kanter och ytor` | `Ogiltig nätdefinition: det går inte att läsa ett nät med både kanter och ytor` |
| `Invalid type definition, must be Vertex/Edge/Face Vector/Scalar Name` | `Ogiltig typdefinition, måste vara Nod/Kant/Yta Vektor/Skalär Namn` | `Ogiltig typdefinition: måste vara Nod/Kant/Yta Vektor/Skalär Namn` |
| `Invalid dataset definition, dataset scalar values must be x` | `Ogiltig datasetdefinition, dataset skalärvärde måste vara x` | `Ogiltig datamängdsdefinition: skalärvärden måste vara x` |
| `Dataset defined on vertices has {} values, but mesh {}` | `Dataset definierade på noder har {} värden, men mesh {}` | `Datamängden som definierats på noder har {} värden, men nätet har {}` |
| `Dataset defined on faces has {} values, but mesh {}` | `Dataset definierade på ytor har {} värden, men mesh {}` | `Datamängden som definierats på ytor har {} värden, men nätet har {}` |
| `Dataset defined on edges has {} values, but mesh {}` | `Dataset definierade på kanter har {} värden, men mesh {}` | `Datamängden som definierats på kanter har {} värden, men nätet har {}` |
| `Display the value from a vertical layer from the top (surface). The level is truncated to the maximum number of vertical layers for particular face.` | `Visa värdet från ett vertikalt lager från toppen (ytan). Nivån är trunkerad till största antal vertikala lagar för den enskilda rutan.` | `Visa värdet från ett vertikalt lager räknat från toppen (ytan). Nivån begränsas till det högsta antalet vertikala lager för den aktuella ytan.` |
| `Height averaging method averages the values based on range defined relative to bed elevation. The range is defined in the same length units as defined by model (e.g. meters)` | `Djupmedelvärdesmetoden tar medelvärden baserat på ett intervall definierat relativt bottennivå. Intervallet är definierat med samma längdenheter som modellen definierats med (t.ex. meter)` | `Höjdmedelvärdesmetoden beräknar medelvärdet utifrån ett intervall som definieras relativt bottennivån. Intervallet anges i samma längdenheter som modellen, till exempel meter.` |
| `Example: Elevation -0.5 to -2.5` | `Exampel: Höjd -0.5 till -2.5` | `Exempel: höjd -0.5 till -2.5` |
| `Elevation averaging method averages the values based on range defined absolute value to the model's datum. The range is defined in the same length units as defined by model (e.g. meters). The elevation will be truncated at the surface and bed levels.` | `Höjdmedelvärdesmetoden tar medelvärden baserat på ett intervall definierat relativt modellens datum. Intervallet är definierat med samma längdenheter som modellen definierats med (t.ex. meter). Höjden kommer truneras vid yt- och bottennivåerna.` | `Höjdmedelvärdesmetoden beräknar medelvärdet utifrån ett intervall som anges som ett absolut värde i förhållande till modellens datum. Intervallet anges i samma längdenheter som modellen, till exempel meter. Höjden begränsas av yt- och bottennivåerna.` |
| `Depth (relative to surface)` | `Djup (relativt till ytan)` | `Djup (relativt ytan)` |
| `Height (relative to bed level)` | `Höjd (relativt till grundnivå)` | `Höjd (relativt bottennivån)` |

De långa raderna som innehåller HTML behåller exakt samma markup i en eventuell
senare importdeltafil. Ingen extern ändring har gjorts.
