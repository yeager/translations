# QGIS: UI-stavning och kortkommandohjälp 067

Datum: 10 november 2026  
Resurs: `qgis-application`, språk `sv`  
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Fem tydliga fel har kontrollerats i algoritmhjälp och användargränssnitt:

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| COG-algoritmens rapporttext | `GoeTIFF` | `GeoTIFF` |
| Hjälptext för eliminering av polygoner | `sliver-poygoner` | `små sliverpolygoner` |
| Hjälptext för omklassning | `existerande rasterkartlager` | `befintliga rasterkartlager` |
| `This is here just to avoid shortcut conflicts, the shortcut is caught in QgsCustomization` | Engelska källtexten kvar | `Detta finns här endast för att undvika kortkommandokonflikter, eftersom kortkommandot hanteras i QgsCustomization.` |
| 3D-bloominställning | `storlekenpå` | `storleken på` |

Kodnamnet `QgsCustomization` och formatnamnet `GeoTIFF` bevaras. Ingen extern
ändring har gjorts; aktuella Transifex-enhetsidentifierare behöver hämtas innan
en deltafil kan skapas.
