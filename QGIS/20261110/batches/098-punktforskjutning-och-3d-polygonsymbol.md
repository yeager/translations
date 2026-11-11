# QGIS: punktförskjutning och 3D-polygonsymbol 098

Datum: 10 november 2026  
Resurs: `qgis-application`, språk `sv`  
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen granskar inställningarna för punktförskjutningsrenderaren och två
grammatiskt felaktiga visningsalternativ för 3D-polygonsymboler. Den bevarar
platshållaren `%1`, radbrytningen i felmeddelandet och det inledande
mellanslaget före enheten `mm`.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Ring` | `Cirkel` | `Ring` |
| `Concentric Rings` | `Koncentriska cirklar` | `Koncentriska ringar` |
| `Transparent Stroke` | `Genomskinlig Linje` | `Genomskinlig konturlinje` |
| `Opaque Stroke` | `Opak kantlinje` | `Ogenomskinlig konturlinje` |
| `The point displacement renderer only applies to (single) point layers. \n'%1' is not a (single) point layer and cannot be displayed by the point displacement renderer.` | `Punktförskjutning kan endast användas på (enkla) punktlager.\n'%1' är inte ett (enkelt) punktlager och kan inte visas med punktförskjutning.` | `Punktförskjutningsrenderaren kan endast användas för (enkla) punktlager.\n'%1' är inte ett (enkelt) punktlager och kan inte visas med punktförskjutningsrenderaren.` |
| `Label font` | `Typsnitt etikett` | `Etikettens typsnitt` |
| `Stroke width` | `Linjebredd` | `Konturlinjebredd` |
| `Stroke color` | `Linjefärg...` | `Konturlinjefärg` |
| ` mm` | `mm` | ` mm` |
| `Point distance tolerance` | `Punktdistanstolerans` | `Tolerans för punktavstånd` |
| `Only the back of the shapes is visible` | `Endast baksidan av formerna är synligt` | `Endast baksidan av formerna är synlig` |
| `Only the front of the shapes is visible` | `Endast framsidan av formerna är synligt` | `Endast framsidan av formerna är synlig` |

Ingen extern ändring har gjorts. Aktuella Transifex-enhetsidentifierare måste
hämtas och måltexterna jämföras före en separat deltafil kan skapas.
