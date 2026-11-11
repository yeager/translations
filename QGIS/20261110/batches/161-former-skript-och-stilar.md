# QGIS: former, skript och stilar 161

Datum: 10 november 2026
Resurs: `qgis-application`, språk `sv`
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen granskar formverktyg, regelbundna punkter, skriptredigeraren samt
stilalgoritmer. Python, QML, API, `import`, `from xxx`, `{}` och `{0}` är kod
eller platshållare och bevaras.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Diamonds` | `Ruter` | `Romber` |
| `Rotation field` | `Fält för rotation` | `Rotationsfält` |
| `Feature {} has empty width or height. Skipping…` | `Objekt {} har tom bredd eller höjd. Hoppar över…` | `Objekt {} saknar bredd eller höjd. Hoppar över…` |
| `Feature {} has empty angle. Skipping…` | `Objekt {} har tom vinkel. Hoppar över…` | `Objekt {} saknar vinkel. Hoppar över…` |
| `Creates rectangle, oval or diamond-shaped polygons from the input point layer.` | `Skapar rektangel-, oval- eller romb-formade polygoner av punktlagret i indata.` | `Skapar rektangulära, ovala eller rombformade polygoner från indatapunktlagret.` |
| `This algorithm creates rectangle, oval or diamond-shaped polygons from the input point layer using specified width, height and (optional) rotation values. Multipart inputs should be promoted to singleparts first.` | `Denna algoritm skapar rektangel-, oval- eller romb-formade polygoner av ett punktlager i indata med angiven bredd, höjd och (valfritt) rotationsvärden. Flerdelade geometrier i indata ska göras om till enkla först.` | `Den här algoritmen skapar rektangulära, ovala eller rombformade polygoner från indatapunktlagret med angiven bredd, höjd och valfria rotationsvärden. Flerdelade indata bör först omvandlas till enkeldelade geometrier.` |
| `Input extent` | `Utsträckning på indata` | `Indatautbredning` |
| `Initial inset from corner (LH side)` | `Startförskjutning från hörn (vänstersida)` | `Inledande indrag från hörn (vänster sida)` |
| `Apply random offset to point spacing` | `Lägg till slumpmässigt offset till punktavstånd` | `Tillämpa slumpmässig förskjutning på punktavståndet` |
| `Creates a point layer with a given number of regular points, all of them within a given extent.` | `Skapar ett punktlager med önskat antal regelbundna punkter, samtliga inom önskad geografisk utbredning.` | `Skapar ett punktlager med ett angivet antal regelbundna punkter, alla inom en angiven utbredning.` |
| `This algorithm creates a point layer with a given number of regular points, all of them within a given extent.` | `Denna algoritm skapar ett punktlager med önskat antal punkter, samtliga inom önskad geografisk utbredning.` | `Den här algoritmen skapar ett punktlager med ett angivet antal regelbundna punkter, alla inom en angiven utbredning.` |
| `Scripts folder(s)` | `Skriptmapp(ar)` | `Skriptmappar` |
| `There are unsaved changes in the script. Continue?` | `Det finns osparade ändringar i skriptet. Fortsätta?` | `Det finns osparade ändringar i skriptet. Vill du fortsätta?` |
| `Processing scripts (*.py *.PY)` | `Processkript (*.py *.PY)` | `Geobearbetningsskript (*.py *.PY)` |
| `No script found` | `Inga skript funna` | `Inget skript hittades` |
| `Could not import script algorithm '{}' from '{}'\n{}` | `Kunde inte importera skript-algoritm '{}' från '{}'\n{}` | `Det gick inte att importera skriptalgoritmen '{}' från '{}'\n{}` |
| `Styled` | `Formgiven` | `Formaterad` |
| `Set style for raster layer` | `Sätt stil för rasterlager` | `Ange stil för rasterlager` |
| `Applies the style from a QML file to a raster layer.` | `Applicerar stilen från en QML-fil till ett rasterlager.` | `Tillämpar stilen från en QML-fil på ett rasterlager.` |
| `This algorithm sets the style of a raster layer. The style must be defined in a QML file.` | `Denna algoritm anger stilen för ett rasterlager. Stilen måste definieras i en QML-fil.` | `Den här algoritmen anger stilen för ett rasterlager. Stilen måste vara definierad i en QML-fil.` |
| `Vector general` | `Generell vektor` | `Allmänt för vektorer` |
| `Set style for vector layer` | `Sätt stil för vektorlager` | `Ange stil för vektorlager` |
| `Specified path does not exist nor its parent:\n{0}` | `Angiven sökväg finns inte eller är inte förälder:\n{0}` | `Den angivna sökvägen och dess överordnade katalog finns inte:\n{0}` |
| `Specified path does not exist and parent is not writable:\n{0}` | `Angiven sökväg finns inte och förälder går inte att skriva till:\n{0}` | `Den angivna sökvägen finns inte och den överordnade katalogen är inte skrivbar:\n{0}` |
| `Auto-save script before running` | `Auto-spara skript innan det körs` | `Spara skript automatiskt före körning` |
| `Automatic parentheses insertion` | `Automatisk insättning av paranteser` | `Automatisk insättning av parenteser` |
| `Enable Object Inspector (switching between tabs may be slow)` | `Aktivera Objektkontroll (byte mellan flikar kan gå långsamt)` | `Aktivera objektgranskaren (växling mellan flikar kan gå långsamt)` |
| `From doc and APIs` | `från dokument och API` | `Från dokument och API:er` |
| `Autopep8 level` | `Autopep8 nivå` | `Autopep8-nivå` |
| Python-redigerarens externa kommandohjälp | Innehåller engelska `and`; tokennamnen och exempelkoden måste bevaras. | Översätt om med `token` → `platshållaren`, `and` → `och`; bevara all HTML, `&lt;file&gt;`, `&lt;line&gt;`, `&lt;col&gt;` och `kate -l …`. |
| `F1 works on hovered words` | `F1 fungerar på hovrade ord` | `F1 fungerar för ord som pekaren hålls över` |

Ingen extern ändring har gjorts. Aktuella Transifex-enhetsidentifierare måste
hämtas och måltexterna jämföras före en separat deltafil kan skapas.
