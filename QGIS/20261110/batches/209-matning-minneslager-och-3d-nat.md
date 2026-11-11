# QGIS: mätning, minneslager och 3D-nät 209

Datum: 11 november 2026
Resurs: `qgis-application`, språk `sv`
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen granskar mätning, minneslagrets feltexter och 3D-nätets inställningar.
`CRS`, `QGIS` och platshållarna `%1` till `%4` bevaras. `mesh` normaliseras
till `nät` och `dataset` till `datamängd` i gränssnittet.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `No map projection set, so area is calculated using Cartesian calculations.` | `Ingen kartprojektion satt, area beräknas därför med kartesiska beräkningar.` | `Ingen kartprojektion är angiven, så arean beräknas kartesiskt.` |
| `Both project CRS (%1) and measured area are in degrees, so area is calculated using Cartesian calculations in square degrees.` | `Både projektets koordinatsystem (%1) och uppmätt area är i grader, så mätningen beräknas med kartesiska beräkningar i kvadrat-grader.` | `Både projektets CRS (%1) och den uppmätta arean anges i grader, så arean beräknas kartesiskt i kvadratgrader.` |
| `Project ellipsoidal calculation is selected.` | `Projektets ellipsodberäkning är vald.` | `Projektets ellipsoidiska beräkning är vald.` |
| `Project ellipsoidal calculation is not selected.` | `Projektets ellipsodialberäkning är inte vald.` | `Projektets ellipsoidiska beräkning är inte vald.` |
| `No map projection set, so distance is calculated using Cartesian calculations.` | `Ingen kartprojektion satt, så avstånd beräknas med kartesiska beräkningar.` | `Ingen kartprojektion är angiven, så avståndet beräknas kartesiskt.` |
| `Distance is calculated in %1, based on project CRS (%2).` | `Avstånd beräknas i %1, baserat på projektets koordinatsystem (%2).` | `Avståndet beräknas i %1 utifrån projektets CRS (%2).` |
| `Measurements copied to clipboard` | `Mätningar kopierade till urklipp` | `Mätningarna har kopierats till urklippet` |
| `Area is calculated in %1, based on project CRS (%2).` | `Area beräknas i %1, baserat på projektets koordinatsystem (%2).` | `Arean beräknas i %1 utifrån projektets CRS (%2).` |
| `map units` | `kartenheter` | `kartenheter` |
| `Unsupported typeName '%1'. Will be handled as string.` | `Typnamn "%1" stöds inte. Kommer hanteras som textsträng.` | `Typnamnet ”%1” stöds inte. Det hanteras som en sträng.` |
| `Feature has too many attributes (expecting %1, received %2)` | `Objektet har för många attribut (förväntade %1, tog emot %2)` | `Objektet har för många attribut, förväntade %1 men fick %2` |
| `Could not add feature with geometry type %1 to layer of type %2` | `Kunde inte lägga till objekt med geometritypen %1 i lager av typ %2` | `Kunde inte lägga till objekt med geometritypen %1 i ett lager av typ %2` |
| `Take attributes from selected feature` | `Ta attribut från valda objekt` | `Ta attribut från markerat objekt` |
| `Remove feature from selection` | `Ta bort attribut från valt` | `Ta bort objekt från markeringen` |
| `Sub renderer` | `Subrenderare` | `Underåtergivare` |
| `Both sides of the mesh are visible` | `Båda sidor av mesh är synliga` | `Båda sidorna av nätet är synliga` |
| `Only the back of the mesh is visible` | `Endast baksidan av mesh är synligt` | `Endast nätets baksida är synlig` |
| `Only the front of the mesh is visible` | `Endast framsidan av mesh är synligt` | `Endast nätets framsida är synlig` |
| `Rendering Color Settings` | `Renderingsinställningar för färg` | `Färginställningar för återgivning` |
| `Level of detail can only be set when mesh simplification is enabled (see Rendering tab in the Mesh Layer Properties)` | `Detaljeringsnivå kan bara ställas in när mesh-förenkling är aktiverad (se renderingsflik i mesh-lagrets egenskaper)` | `Detaljeringsnivå kan bara anges när nätförenkling är aktiverad, se fliken Återgivning i nätlagrets egenskaper.` |
| `Dataset group for vertical value` | `Datasetsgrupp för vertikalt värde` | `Datamängdsgrupp för vertikalt värde` |
| `Dataset value relative to vertices Z value` | `Datasetsvärde relativt till brytpunkters Z-värde` | `Datamängdsvärde relativt till brytpunkternas Z-värde` |

För HTML-varningen om felaktiga mätresultat ska exakt befintlig markup och
menyidentifieraren `Settings:Project Properties` bevaras i en senare deltafil.
Ingen extern ändring har gjorts.
