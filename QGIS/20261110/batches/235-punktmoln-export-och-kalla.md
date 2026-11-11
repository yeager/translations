# QGIS: punktmoln, export och källa 235

Datum: 11 november 2026
Resurs: `qgis-application`, språk `sv`
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen granskar dialogerna för att spara, filtrera, återge och lägga till
punktmoln. `CRS`, `HTTP(S)`, `URI`, `QQF`, `LAS/LAZ` och filändelser bevaras
som tekniska benämningar. *Renderer* återges som återgivare eller återgivning
utifrån gränssnittets funktion, och *dataset* som datamängd.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Save Point Cloud Layer As` | `Spara punktmolnslager som` | `Spara punktmolnslagret som` |
| `Overwrite File` | `Skriv över fil` | `Skriv över filen` |
| `Overwrite Layer` | `Skriv över lager` | `Skriv över lagret` |
| `Append to Layer` | `Lägg till i lager` | `Lägg till i lagret` |
| `Temporary Scratch Layer` | `Temporärt minneslager…` | `Temporärt minneslager` |
| `CRS` | `Referenskoordinatsystem` | `Koordinatreferenssystem` |
| `Extent` | `Utsträckning` | `Utbredning` |
| `Export points intersecting features from layer` | `Exportera punkter som skär objekt i lager` | `Exportera punkter som skär objekten i lagret` |
| `Add saved file to map` | `Lägg till sparad fil till kartan` | `Lägg till den sparade filen på kartan` |
| `Save Point Cloud Layer as…` | `Spara punktmolnslager som…` | `Spara punktmolnslagret som…` |
| `Save query to QQF file` | `Spara fråga till QQF-fil` | `Spara fråga i QQF-fil` |
| `Load query from QQF file` | `Läs in fråga från QQF-fil` | `Läs in fråga från en QQF-fil` |
| `Set provider filter on %1` | `Sätt datakällsfilter på %1` | `Ange datakällsfilter för %1` |
| `n/a` | `---` | `ej tillämpligt` |
| `Minimum: %1` | `Minimum: %1` | `Minsta: %1` |
| `Maximum: %1` | `Maximum: %1` | `Största: %1` |
| `Mean: %1` | `Medel: %1` | `Medelvärde: %1` |
| `"%1" not recognized as an available attribute.` | `"%1" är inte igenkänt som ett tillgängligt attribut.` | `"%1" känns inte igen som ett tillgängligt attribut.` |
| `The expression was successfully parsed.` | `Uttrycket lyckades tolkas.` | `Uttrycket tolkades utan fel.` |
| `Provider Specific Filter Expression` | `Specifikt filteruttryck för datakälla` | `Providerspecifikt filteruttryck` |
| `Customize label text` | `Anpassa etikettext` | `Anpassa etikettens text` |
| `Show Extents Only` | `Visa endast utsträckning` | `Visa endast utbredning` |
| `Show Extents Over Overview` | `Visa utsträckning över översikt` | `Visa utbredning över översikten` |
| `Renderer Settings` | `Renderingsinställningar` | `Inställningar för återgivning` |
| `This renderer doesn't implement a graphical interface.` | `Denna renderare har inget grafisk gränssnitt.` | `Den här återgivaren har inget grafiskt gränssnitt.` |
| `Layer Rendering` | `Lagerrendering` | `Lageråtergivning` |
| `Show tile labels` | `Visa rutiketter` | `Visa etiketter för rutor` |
| `Opacity` | `Opacitet` | `Ogenomskinlighet` |
| `Distance away from the original pixel to sample neighbors.` | `Avstånd från ursprungspixeln för att sampla grannar.` | `Avstånd från ursprungspixeln vid samplingen av angränsande pixlar.` |
| `Vertical exageration for hillshading` | `Vertikal förstoring för höjdskuggning` | `Vertikal överdrift för terrängskuggning` |
| `Use multidirectional lights instead of the specified azimuth for hillshading.` | `Använd flerriktat ljus istället för den angivna azimuten för höjdskuggning.` | `Använd flerriktat ljus i stället för den angivna azimuten för terrängskuggning.` |
| `Applies an expression to adjust the colors of the point cloud. The renderer base color is accessible as @value.` | `Använder ett uttryck för att justera färgerna i punktmolnet. Renderarens basfärg är tillgänglig som @value.` | `Tillämpar ett uttryck som justerar färgerna i punktmolnet. Återgivarens basfärg kan nås som @value.` |
| `Open Point Cloud Dataset` | `Öppna dataset för punktmoln` | `Öppna punktmolnsdatamängd` |
| `Invalid point cloud URL "%1", please make sure your URL ends with /ept.json, .copc.laz, .vpc or .vpz` | `Ogiltigt URL för punktmoln. "%1" Försäkra dig om att den slutar på /ept.json, .copc.laz, .vpc eller .vpz` | `Ogiltig punktmolns-URL "%1". Kontrollera att URL:en slutar med /ept.json, .copc.laz, .vpc eller .vpz.` |
| `Authentication` | `Verifiering` | `Autentisering` |
| `Protocol: HTTP(S), cloud, etc.` | `Protokoll: HTTP(S), cloud, etc.` | `Protokoll: HTTP(S), moln osv.` |
| `Point cloud dataset(s)` | `Dataset för punktmoln` | `Punktmolnsdatamängd(er)` |
| `Generating attributes statistics` | `Skapar statistik för attribut` | `Beräknar attributstatistik` |

Platshållaren `%1`, variabeln `@value`, URI-komponenterna och alla
filändelser ska bevaras oförändrade vid senare import. Ingen extern ändring
har gjorts.
