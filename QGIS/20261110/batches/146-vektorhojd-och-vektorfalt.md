# QGIS: vektorhöjd och vektorfält 146

Datum: 10 november 2026
Resurs: `qgis-application`, språk `sv`
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen granskar vektorlagers höjdmodell och vektorfältsrendering. CRS,
Z-värden, 2D, 3D, HTML-radbrytningen och enhetsförkortningarna bevaras.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Elevation is relative to terrain height.` | `Höjdnivå är relativt terränghöjden.` | `Höjden är relativ till terränghöjden.` |
| `Any z values present in the features will be added to the terrain height.` | `Varje z-värde som finns i objekten kommer att läggas till terränghöjden.` | `Eventuella Z-värden i objekten läggs till terränghöjden.` |
| `Feature elevation will be taken directly from the terrain height.` | `Höjdnivå för objekten kommer att tas direkt från terränghöjden.` | `Objektens höjd hämtas direkt från terränghöjden.` |
| `Any existing z values present in the features will be ignored.` | `Varje z-värde som finns i objekten kommer att ignoreras.` | `Eventuella Z-värden i objekten ignoreras.` |
| `Feature elevation is relative to the terrain height at every vertex.` | `Objektets höjdnivå är relativ terränghöjden i varje brytpunkt.` | `Objektets höjd är relativ till terränghöjden vid varje brytpunkt.` |
| `The terrain will be sampled at every individual vertex before being added to the vertex's z value.` | `Terrängen kommer samplas i varje brytpunkt innan den läggs till brytpunktens z-värde.` | `Terrängen provtas vid varje brytpunkt innan den läggs till brytpunktens Z-värde.` |
| `Feature elevation is relative to the terrain height at feature's centroid only.` | `Objektets höjdnivå är relativ terränghöjden endast i objektets centroid.` | `Objektets höjd är relativ till terränghöjden endast vid objektets centroid.` |
| `The terrain will be sampled once at the feature's centroid, with the centroid height being added to each vertex's z value.` | `Terrängen kommer endast samplas i objektets centroid och denna höjd kommer sen att läggas till varje brytpunktens z-värde.` | `Terrängen provtas en gång vid objektets centroid och centroidens höjd läggs till varje brytpunkts Z-värde.` |
| `Layer coordinate reference system is set to a geographic 3D CRS (%1), so the vertical CRS cannot be manually specified.` | `Lagrets koordinatsystem är satt till ett geografiskt 3D-koordinatsystem (%1), så projektets vertikala koordinatsystem kan inte anges manuellt.` | `Lagrets koordinatreferenssystem är ett geografiskt 3D-CRS (%1), så lagrets vertikala CRS kan inte anges manuellt.` |
| `Layer coordinate reference system is set to a geocentric CRS (%1), so the vertical CRS cannot be manually specified.` | `Lagrets koordinatsystem är satt till ett geocentriskt koordinatsystem (%1), så projektets vertikala koordinatsystem kan inte anges manuellt.` | `Lagrets koordinatreferenssystem är ett geocentriskt CRS (%1), så lagrets vertikala CRS kan inte anges manuellt.` |
| `Layer coordinate reference system is set to a projected 3D CRS (%1), so the vertical CRS cannot be manually specified.` | `Lagrets koordinatsystem är satt till ett projicerat 3D-koordinatsystem (%1), så projektets vertikala koordinatsystem kan inte anges manuellt.` | `Lagrets koordinatreferenssystem är ett projicerat 3D-CRS (%1), så lagrets vertikala CRS kan inte anges manuellt.` |
| `Vector Elevation Properties` | `Höjdegenskaper vektor` | `Höjdegenskaper för vektorer` |
| `Extrusion controls how high features extend vertically above their base.` | `Extrudering kontrollerar hur högt objekt sträcker sig vertikalt ovanför dess bas.` | `Extrudering styr hur högt objekt sträcker sig vertikalt över sin bas.` |
| `If checked, then features will be shown in profile charts using the same symbols or colors as they use on 2D maps.` | `Om markerad kommer objekten att synas i profildiagrammet med samma symboler eller färger som de använder i 2D kartor.` | `När alternativet är markerat visas objekten i profildiagram med samma symboler eller färger som på 2D-kartor.` |
| `Respect layer's symbology` | `Används lagrets symbologi` | `Respektera lagrets symbologi` |
| `Wind Barbs` | `Vindtaggar` | `Vindflaggor` |
| `Streamlines Seeding Method` | `Metod för seedning av strömlinjer` | `Metod för att placera startpunkter för strömlinjer` |
| `X Spacing` | `X Mellanrum` | `X-avstånd` |
| `Y Spacing` | `Y Mellanrum` | `Y-avstånd` |
| `Defined by Min and Max` | `Definierad av min och max` | `Definierad av min. och max.` |
| `Max tail length` | `Max svanslängd` | `Största svanslängd` |
| `Select the units the data are in.<br>Values are converted to knots for rendering the wind barbs.` | `Välj enheterna som data är i.<br>Värdena konverteras till knop för rendering av vindtaggarna.` | `Välj enheterna som data anges i.<br>Värdena omvandlas till knop vid rendering av vindflaggorna.` |

Ingen extern ändring har gjorts. Aktuella Transifex-enhetsidentifierare måste
hämtas och måltexterna jämföras före en separat deltafil kan skapas.
