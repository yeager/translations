# QGIS: atlasexport och täckningslager 181

Datum: 11 november 2026
Resurs: `qgis-application`, språk `sv`
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen granskar Processing-algoritmerna för att exportera en layoutatlas till
bild och PDF. Den följer det fastställda QGIS-begreppet `atlas` och använder
`täckningslager` för det lager som styr atlasens objekt. PNG, JPEG och PDF är
formatnamn och lämnas oförändrade.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Export atlas layout as image` | `Exportera kartbokslayout som bild` | `Exportera atlaslayout som bild` |
| `Exports an atlas layout as a set of images.` | `Exportera en kartbokslayout som en uppsättning av bilder.` | `Exporterar en atlaslayout som en uppsättning bilder.` |
| `This algorithm outputs an atlas layout as a set of image files (e.g. PNG or JPEG images).\n\nIf a coverage layer is set, the selected layout's atlas settings exposed in this algorithm will be overwritten. In this case, an empty filter or sort by expression will turn those settings off.` | `Denna algoritm skapar en uppsättning bildfiler (t.ex. PNG- eller JPEG-bilder) av en kartbokslayout.\n\nOm ett kartbokslager anges, kommer den valda kartbokens inställningar synliga i denna algoritm att skrivas över. I detta fall kommer ett tomt filter eller ett sorteringsuttryck att stänga av dessa inställningar.` | `Den här algoritmen skapar en uppsättning bildfiler, till exempel PNG- eller JPEG-bilder, från en atlaslayout.\n\nOm ett täckningslager anges skrivs den valda layoutens atlasinställningar som visas i den här algoritmen över. Ett tomt filter eller ett sorteringsuttryck stänger då av inställningarna.` |
| `Atlas layout` | `Kartbokslayout` | `Atlaslayout` |
| `Coverage layer` | `Kartbokslager` | `Täckningslager` |
| `Error setting atlas filter expression` | `Fel vid användande av filteruttryck för kartbok` | `Fel vid inställning av atlasens filteruttryck` |
| `Layout being export doesn't have an enabled atlas` | `Layout som ska exporteras har inte en aktiverad kartbok` | `Layouten som exporteras har ingen aktiverad atlas` |
| `Error setting atlas filename expression` | `Fel vid användande av uttryck för kartbokens filnamn` | `Fel vid inställning av uttrycket för atlasens filnamn` |
| `Error encountered while exporting atlas.` | `Fel uppstod under export av kartbok.` | `Ett fel uppstod när atlasen exporterades.` |
| `No atlas features found` | `Inga kartboksobjekt hittades` | `Inga atlasobjekt hittades` |
| `Selected layout does not have atlas functionality enabled` | `Vald layout har ingen kartboksfunktionalitet aktiverad. ` | `Atlasfunktionen är inte aktiverad för den valda layouten.` |
| `Export atlas layout as PDF (single file)` | `Exportera kartbokslayout som PDF (en fil)` | `Exportera atlaslayout som PDF, som en fil` |
| `Exports an atlas layout as a single PDF file.` | `Exporterar en kartbokslayout som en PDF-fil.` | `Exporterar en atlaslayout som en PDF-fil.` |
| `This algorithm outputs an atlas layout as a single PDF file.\n\nIf a coverage layer is set, the selected layout's atlas settings exposed in this algorithm will be overwritten. In this case, an empty filter or sort by expression will turn those settings off.` | `Denna algoritm skapar en PDF-fil av en kartbokslayout.\n\nOm ett kartbokslager anges, kommer den valda kartbokens inställningar synliga i denna algoritm att skrivas över. I detta fall kommer ett tomt filter eller ett sorteringsuttryck att stänga av dessa inställningar.` | `Den här algoritmen skapar en PDF-fil från en atlaslayout.\n\nOm ett täckningslager anges skrivs den valda layoutens atlasinställningar som visas i den här algoritmen över. Ett tomt filter eller ett sorteringsuttryck stänger då av inställningarna.` |
| `Successfully exported atlas to %1` | `Lyckades exportera kartbok till %1` | `Atlasen har exporterats till %1.` |
| `Export atlas layout as PDF (multiple files)` | `Exportera kartbokslayout som PDF (flera filer)` | `Exportera atlaslayout som PDF, som flera filer` |
| `Exports an atlas layout to multiple PDF files.` | `Exporterar en kartbokslayout som flera PDF-filer.` | `Exporterar en atlaslayout till flera PDF-filer.` |

Ingen extern ändring har gjorts. Aktuella Transifex-enhetsidentifierare måste
hämtas och måltexterna jämföras före en separat deltafil kan skapas.
