# Andra motgranskning: Blender Manual batch 18

Granskad fil: `blender-manual-sv-review-batch-20261104-18.po`
Underlag: råexportens `files/import_export/usd.rst:187–289` och lokala
`blender-ui-ui-sv.po`.

## Resultat

| Post | Bedömning | Exakt resultat |
| --- | --- | --- |
| `UsdGeomMesh`, `UsdVolVolume`, `UsdGeomPoints` | Godkänd | Kodnamn, RST-mål och de svenska formerna `meshobjekt`, `volymobjekt` och `punktmolnsobjekt` är korrekta. |
| `USD Shapes`, `Display Purpose`, `Material Purpose` | Godkänd | Rubrikerna återger avsedda USD-begrepp och URL/RST-markering är oförändrad. |
| `allPurpose` och `preview` | Godkänd | Normativa USD-värden är exakt bevarade; reservbeteendet är korrekt beskrivet. |
| `full` | Ändra | Avsluta meningen: `Försök att importera ``full``-material. Läs in ``allPurpose``- eller ``preview``-material, i den ordningen, som reserv.` |
| `Import USD Preview` | Ändra | Använd UI-exportens exakta namn: `Importera USD Preview`. |
| `Convert USD Preview Surface shaders …` | Ändra | Använd: `Konvertera USD Preview Surface-shaders till Principled BSDF-shadernätverk.` |
| Texturer, katalog, filnamnskollision och `Use Existing` | Godkänd | Svenskan är begriplig och tekniskt riktig; undantaget är att UI-katalogen har den mer specifika formen `Kollision mellan filnamn`, men batchens `Filnamnskollision` är korrekt svensk terminologi. |

## Särskild kontroll av USD Preview och `opacityThreshold`

`USD Preview` är ett synligt och etablerat UI-namn i lokala UI-exporten;
det ska alltså inte översättas till *USD-förhandsgranskning*. Samma export
belägger `Nätverk för USD Preview Surface` och `Principiell BSDF`.

Strängen om ``opacityThreshold`` hör inte till batch 18, men råexporten
visar att UI-strängarna ska lokaliseras som `Matematik`, `Runda`, `Alfa` och
`Principiell BSDF` när den posten behandlas i en senare batch. Kodvärdena
``opacityThreshold``, ``Round`` och uttrycket ``1 - (value < threshold)``
måste däremot behållas tekniskt oförändrade.

## Slutsats

Tolv poster godkänns. De tre angivna följdrättelserna krävs före
uppladdning. Inga råexporter eller PO-batchfiler har ändrats.
