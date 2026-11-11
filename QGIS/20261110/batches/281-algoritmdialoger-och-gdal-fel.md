# QGIS: algoritmdialoger och GDAL-fel 281

Datum: 11 november 2026
Resurs: `qgis-application`, språk `sv`
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen granskar dialoger för geobearbetning samt GDAL- och
FieldPyculator-fel. Kodnamn, platshållaren `{}` och filändelsen `.vrt`
bevaras exakt. `sliver polygons` beskrivs med den begripliga GIS-termen
`smala polygoner` i algoritmens hjälptetext.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Dissolve field` | `Lös ut fält` | `Upplösningsfält` |
| `Produce one feature for each geometry in any kind of geometry collection in the source file` | `Skapar ett objekt i vilken geometrisamling som helst i källfilen` | `Skapa ett objekt för varje geometri i alla typer av geometrisamlingar i källfilen` |
| `Processing options` | `Geobearbetning inställningar` | `Geobearbetningsinställningar` |
| `This algorithm combines selected polygons from the input layer with certain adjacent polygons by erasing their common boundary. The adjacent polygon can be either the one with the largest or smallest area or the one sharing the largest common boundary with the polygon to be eliminated.\nEliminate is normally used to get rid of sliver polygons, i.e. tiny polygons that are a result of polygon intersection processes where boundaries of the inputs are similar but not identical.` | `Denna algoritm kombinerar valda polygoner i indatalagret med vissa intilliggande polygoner genom att radera deras gemensamma gräns. Den intilliggande polygonen kan vara antingen den med störst eller minst area eller den som delar den största gemensamma gränsen med den som ska elimineras. Eliminera är vanligtvis använt för att bli av med sliver-poygoner, små polygoner som är ett resultat av processande av polygoner med skärning där gränserna i indata är lika men inte identiska.` | `Algoritmen sammanför valda polygoner i indatalagret med vissa intilliggande polygoner genom att ta bort deras gemensamma gräns. Den intilliggande polygonen kan vara den med störst eller minst yta eller den som delar den längsta gemensamma gränsen med polygonen som ska elimineras.\nEliminera används normalt för att ta bort smala polygoner, alltså mycket små polygoner som uppstår när polygoner skär varandra och indatagränserna är snarlika men inte identiska.` |
| `SQL result` | `SQL resultat` | `SQL-resultat` |
| `This algorithm can only be used with GDAL raster layers` | `Algoritmen kan bara användas med GDAL rasterlager` | `Algoritmen kan bara användas med GDAL-rasterlager` |
| `FieldPyculator code execute error. Field code block can't be executed!\n{0}\n{1}` | `FältPyculator kodkörningsfel. Fältkodblock kan inte köras!\n{0}\n{1}` | `Körningsfel i FieldPyculator-kod. Fältkodblocket kan inte köras!\n{0}\n{1}` |
| `FieldPyculator code execute error\nField code block does not return '{0}' variable! Please declare this variable in your code!` | `Exekveringsfel i FältPyculatorkod\nFältkodblock returnerar inte '{0}' variabel! Var vänlig deklarera denna variabel i din kod!` | `Körningsfel i FieldPyculator-kod\nFältkodblocket returnerar inte variabeln '{0}'. Deklarera variabeln i koden.` |
| `Advanced Python field calculator` | `Avancerad Python fältkalkylator` | `Avancerad Python-fältkalkylator` |
| `FieldPyculator code execute error. Global code block can't be executed!\n{0}\n{1}` | `FältPyculatorkod körningsfel. Globalt kodblock kan inte köras!\n{0}\n{1}` | `Körningsfel i FieldPyculator-kod. Det globala kodblocket kan inte köras!\n{0}\n{1}` |
| `This algorithm adds a new attribute to a vector layer, with values calculated by applying an expression to each feature. The expression is defined as a Python function.` | `Denna algoritm lägger till nya attribut till ett vektorlager, med värden skapade genom att tillämpa ett uttryckt för varje objekt. Uttrycket definieras som en Python-funktion.` | `Algoritmen lägger till ett nytt attribut i ett vektorlager med värden som beräknas genom att tillämpa ett uttryck på varje objekt. Uttrycket definieras som en Python-funktion.` |
| `Output filename must use a .vrt extension` | `Filnamn för utdata måste ha en .vrt ändelse` | `Filnamnet för utdata måste ha filändelsen .vrt` |
| `GDAL/OGR console call` | `GDAL/ORG konsol anrop` | `GDAL/OGR-konsolanrop` |
| `GDAL execution console output` | `Utdatakonsol för körning av GDAL` | `Konsolutdata från GDAL-körning` |
| `Process completed successfully` | `Process slutfördes` | `Processen slutfördes utan fel` |
| `Process returned error code {}` | `Process returnerade felkod {]` | `Processen returnerade felkoden {}` |

Ingen extern ändring har gjorts. De rekommenderade texterna är lokala
kandidater tills de jämförts mot aktuella Transifex-enheter i en senare
uppladdningsbatch.
