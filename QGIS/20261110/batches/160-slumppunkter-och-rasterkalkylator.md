# QGIS: slumppunkter och rasterkalkylator 160

Datum: 10 november 2026
Resurs: `qgis-application`, språk `sv`
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen granskar geobearbetningsalgoritmer för slumpmässiga punkter,
rasterkalkylatorn och rasterhistogram. Kod och uttryck som `sin()`, `log10()`,
`layer_name@band number`, `DEM@1` och filsökvägen `path/to/my/rasterfile.tif`
måste bevaras oförändrade.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Random points along line` | `Slumpmässiga punkter längs linje` | `Slumpmässiga punkter längs en linje` |
| `Creates a point layer with a given number of points placed on the lines of the input layer.` | `Skapar ett nytt punktlager med givet antal punkter placerade på linjer i ett indatalager.` | `Skapar ett punktlager med ett angivet antal punkter placerade på linjerna i indatalagret.` |
| Beskrivningen av `Random points along line` | `sen`, `Euklidiskt` och otydlig ordföljd. | `Den här algoritmen skapar ett punktlager med ett angivet antal punkter placerade på linjerna i indatalagret.\nVarje punkts placering bestäms genom att slumpmässigt välja ett objekt, sedan ett segment i objektets linjegeometri och slutligen en slumpmässig position på segmentet. Du kan ange ett minsta avstånd mellan punkterna (euklidiskt avstånd).` |
| `Random points in layer bounds` | `Slumpvisa punkter i lagerutsträckning` | `Slumpmässiga punkter inom lagrets utbredning` |
| `Creates a new point layer with a given number of random points, all of them within the extent of a given layer.` | `Skapar ett nytt punktlager med önskat antal slumpvisa punkter, samtliga inom utbredningen av ett angivet lager.` | `Skapar ett nytt punktlager med ett angivet antal slumpmässiga punkter, alla inom utbredningen för ett angivet lager.` |
| `This algorithm creates a new point layer with a given number of random points, all of them within the extent of a given layer. A distance factor can be specified, to avoid points being too close to each other.` | `Denna algoritm skapar ett nytt punktlager med valt antal slumpmässiga punkter, samtliga inom utsträckningen av ett valt lager. En avståndsfaktor kan anges, för att undvika att punkter hamnar för nära varandra.` | `Den här algoritmen skapar ett nytt punktlager med ett angivet antal slumpmässiga punkter, alla inom utbredningen för ett angivet lager. Du kan ange en avståndsfaktor så att punkterna inte hamnar för nära varandra.` |
| `Random points inside polygons` | `Slumpmässiga punkter inuti polygoner` | `Slumpmässiga punkter inom polygoner` |
| `Skip feature {} as number of points for it is 0.` | `Hoppa över objekt {} eftersom antalet punkter för det är 0.` | `Hoppar över objekt {} eftersom antalet punkter är 0.` |
| Beskrivningen av `Random points inside polygons` | Saknar mellanrum mellan meningar och använder `datadefinerad åsidosättning`. | `Den här algoritmen skapar ett nytt punktlager med slumpmässiga punkter inom polygonerna i ett angivet lager. Antalet punkter i varje polygon kan anges som ett fast antal eller som ett densitetsvärde. Antals- eller densitetsvärdet kan också hämtas från ett attribut eller ett uttryck med funktionen ”datadefinierad åsidosättning”, så att det kan skilja sig mellan polygonerna i indatalagret. Du kan ange ett minsta avstånd så att punkterna inte hamnar för nära varandra.` |
| `Reference layer(s) (used for automated extent, cellsize, and CRS)` | `Referenslager (används för automatisk utbredning, cellstorlek och koordinatreferenssystem)` | `Referenslager (används för automatisk utbredning, cellstorlek och CRS)` |
| `Cell size (use 0 or empty to set it automatically)` | `Cellstorlek (använd 0 eller tom för automatisk inställning)` | `Cellstorlek (använd 0 eller lämna tomt för automatisk inställning)` |
| `Output extent` | `Utdataomfattning` | `Utdatautbredning` |
| `No reference layer selected nor CRS provided` | `Inget referenslager valt samt inget koordinatreferenssystem tillhandahållet` | `Inget referenslager har valts och inget CRS har angetts` |
| `No reference layer selected nor extent box provided` | `Inget referenslager valt samt ingen utbredningsram tillhandahållen` | `Inget referenslager har valts och ingen utbredningsruta har angetts` |
| `No reference layer selected nor cellsize value provided` | `Inget referenslager valt samt inget cellstorleksvärde tillhandahållet` | `Inget referenslager har valts och inget cellstorleksvärde har angetts` |
| `Output '%1' from algorithm '%2'` | `Utdata '%1' från algoritm '%2'` | `Utdata ”%1” från algoritmen ”%2”` |
| `Allows performing algebraic operations using raster layers.` | `Tillåter utförande av algebraiska operationer med rasterlager` | `Gör det möjligt att utföra algebraiska operationer med rasterlager.` |
| Rasterkalkylatorns hjälptext | Bristfällig kongruens, upprepade ord och felaktiga kodexempel (`lagernamn@bandnummer`). | Översätt på nytt med bevarade funktioner, citattecknen runt `layer_name@band number`, `DEM@1`, `path/to/my/rasterfile.tif` och `rasterfile.tif@1`; använd `utbredning`, `cellstorlek`, `utdata-CRS`, `lagerlista` och idiomatisk svensk meningsbyggnad. |
| `Band number` | `Band nummer` | `Bandnummer` |
| `number of bins` | `antal fack` | `Antal intervall` |
| `This algorithm requires the Python “plotly” library. Please install this library and try again.` | `Denna algoritm kräver pythonbiblioteket &quot;plotly&quot;. Installera detta bibliotek och försök igen.` | `Den här algoritmen kräver Python-biblioteket ”plotly”. Installera biblioteket och försök igen.` |
| `Generates a histogram with the values of a raster layer.` | `Skapar ett histogram med värdena från ett rasterlager. ` | `Skapar ett histogram med värdena i ett rasterlager.` |

Ingen extern ändring har gjorts. Aktuella Transifex-enhetsidentifierare måste
hämtas och måltexterna jämföras före en separat deltafil kan skapas.
