# QGIS: uttryck, höjdkurvor och kartutbredning 169

Datum: 10 november 2026
Resurs: `qgis-application`, språk `sv`
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen granskar uttrycksfunktioner, höjdkurvor och värden från kartytans
utbredning. `NULL` samt lägesnamnen `AddFeatureMode`, `SingleEditMode`,
`MultiEditMode`, `SearchMode`, `AggregateSearchMode` och `IdentifyMode` är
programidentifierare och bevaras. `mesh`, `vector tile` och `plugin` följer
den fastställda QGIS-terminologin.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Color of symbols within a cluster, or NULL if symbols have mixed colors.` | `Färger på symboler inom ett kluster, eller NULL om symboler har blandade färger.` | `Färgen på symbolerna i ett kluster, eller NULL om symbolerna har olika färger.` |
| `Attribute name (if not set, no elevation attribute is attached)` | `Attributnamn (Om det inte anges, så skapas inget attribut med höjd)` | `Attributnamn (om inget anges läggs inget höjdattribut till)` |
| `Offset from zero relative to which to interpret intervals` | `Förskjutning från noll för intervallen.` | `Förskjutning från noll som intervallen ska tolkas relativt` |
| `Attribute name for minimum elevation of contour polygon` | `Attributnamn för minsta höjd av höjdkurvspolygon` | `Attributnamn för lägsta höjd i höjdkurvspolygonen` |
| `Attribute name for maximum elevation of contour polygon` | `Attributnamn för högsta höjd av höjdkurvspolygon` | `Attributnamn för högsta höjd i höjdkurvspolygonen` |
| `What the form is used for, like AddFeatureMode, SingleEditMode, MultiEditMode, SearchMode, AggregateSearchMode or IdentifyMode as string.` | `När formuläret används till, AddFeatureMode, SingleEditMode, MultiEditMode, SearchMode, AggregateSearchMode eller IdentifyMode som text.` | `Anger vad formuläret används till, till exempel AddFeatureMode, SingleEditMode, MultiEditMode, SearchMode, AggregateSearchMode eller IdentifyMode, som text.` |
| `Maximum x-value from full canvas extent (including all layers).` | `Största x-värde från kartfönstrets hela utbredning (inklusive alla lager).` | `Största x-värdet i kartytans fulla utbredning (inklusive alla lager).` |
| `Maximum y-value from full canvas extent (including all layers).` | `Största y-värde från kartfönstrets hela utbredning (inklusive alla lager).` | `Största y-värdet i kartytans fulla utbredning (inklusive alla lager).` |
| `Minimum x-value from full canvas extent (including all layers).` | `Minsta x-värde från kartfönstrets hela utbredning (inklusive alla lager).` | `Minsta x-värdet i kartytans fulla utbredning (inklusive alla lager).` |
| `Minimum y-value from full canvas extent (including all layers).` | `Minsta y-värde från kartfönstrets hela utbredning (inklusive alla lager).` | `Minsta y-värdet i kartytans fulla utbredning (inklusive alla lager).` |
| `Mesh` | `Mesh` | `Nät` |
| `Vector Tile` | `Vector Tile` | `Vektorruta` |
| `Plugin` | `Plugin` | `Tillägg` |
| `Tiled Scene` | `Tiled Scene` | `Rutindelad scen` |

Ingen extern ändring har gjorts. Aktuella Transifex-enhetsidentifierare måste
hämtas och måltexterna jämföras före en separat deltafil kan skapas.
