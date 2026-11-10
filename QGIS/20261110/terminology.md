# QGIS: svensk terminologi

Status: projektspecifik terminologilista för den radvisa svenska granskningen av QGIS Desktop på Transifex. Den är en separat granskningsartefakt; råexporter i `raw/` ändras aldrig.

Källor: QGIS egen [svenska dokumentation](https://docs.qgis.org/3.44/sv/docs/user_manual/map_views/map_view.html), etablerad QGIS-svenska i den aktuella Transifex-resursen samt svensk GIS-praxis. Produktnamn, formatnamn, API-namn, algoritmnamn och identifierare översätts inte om inte sammanhanget uttryckligen kräver en förklarande svensk text.

| Engelska | Svenska | Sammanhang | Anmärkning |
|---|---|---|---|
| processing | geobearbetning | QGIS Processing och dialoger | Inte ”bearbetning” när GIS-funktionen avses. |
| toolbox | verktygslåda | Panel med geobearbetningsverktyg | Bevarar etablerad QGIS-term. |
| history | historik | Tidigare körningar och åtgärder | ”Bearbetningshistorik” i Processing. |
| algorithm | algoritm | Geobearbetning | Använd ”verktyg” endast för UI-elementet. |
| feature | objekt | Geodata i lager | ”Funktion” endast när programfunktion avses. |
| field | fält | Attributtabell och data | Inte ”kolumn” om inte tabellvyn avses. |
| attribute | attribut | Attributtabell och uttryck | |
| layer | lager | Punkt-, linje-, polygon- och rasterlager | |
| vector layer | vektorlager | Geodatatyp | |
| raster layer | rasterlager | Geodatatyp | |
| geometry | geometri | GIS-geometri | |
| point, line, polygon | punkt, linje, polygon | Geometri | |
| boundary | gräns | Polygon- och områdesgeometri | ”Kant” vid fysisk eller visuell kant. |
| concave hull | konkavt hölje | Geobearbetning och geometri | Använd inte ”uteslutande polygon”. |
| convex hull | omslutande polygon | Geobearbetning och geometri | Etablerad QGIS-svenska. |
| spatial extent | geografisk utbredning | Koordinatmässigt område | Använd den kortare formen ”utbredning” när UI-utrymmet eller källkontexten kräver det. |
| coordinate reference system (CRS) | koordinatreferenssystem (CRS) | Projektion och dataegenskaper | |
| projection | projektion | Kartprojektion | |
| georeferencing | georeferering | Raster och kartor | |
| digitizing | digitalisering | Skapa eller ändra geometri | |
| snapping | snäppning | Redigeringsinställningar | Vedertagen QGIS-term. Blender använder i stället den projektspecifika termen ”fästning”. |
| vertex | brytpunkt | Linje- och polygongeometri | |
| topology | topologi | Validering och redigering | |
| expression | uttryck | Uttrycksbyggaren | |
| variable | variabel | Uttryck och skript | |
| input | indata | Algoritmparameter | |
| output | utdata | Algoritmresultat | |
| parameter | parameter | Algoritm och inställning | |
| processing model | geobearbetningsmodell | Model Designer | |
| model | modell | Model Designer | Översätt inte filändelser eller kodnamn. |
| extent | utbredning | Parameteretikett | ”Geografisk utbredning” när precision behövs. |
| zoom level | zoomnivå | Webbkarta och rutor | |
| tile | ruta | Webbkart- och rutmatrissammanhang | Undvik ”platta” i QGIS UI. |
| tile matrix | rutmatris | WMTS och liknande | |
| metatile | metaruta | Rutrendning | |
| vector field | vektorfält | GIS-/attributterm | |
| raster pixel | bildpunkt | Rasterdata | |
| point cloud | punktmoln | Punktmolnslager och rendering | |
| COPC | COPC | Punktmolnsformat | Formatnamnet översätts inte. |
| band | band | Rasterdata | |
| nodata | inget data | Rasterdata | Behåll `NODATA` om det är ett datavärde eller identifierare. |
| profile | profil | Höjd- och terrängverktyg | |
| map canvas | kartvy | Huvudvyn för kartan | QGIS-dokumentationen använder ”2D-kartvy”. Behåll `QgsMapCanvas` i kod och API-text. |
| layout | layout | Layoutdesigner | |
| legend | teckenförklaring | Kartlayout | |
| scale | skala | Kart- och layoutegenskap | |
| label | etikett | Kartetiketter | |
| rendering | rendering | Visning och export | |
| symbology | symbologi | Lagerstil | |
| export | export | Verb och substantiv | ”Exportera” som verb. |
| import | import | Verb och substantiv | ”Importera” som verb. |
| encoding | kodning | Text- och filkodning | |
| Unicode | Unicode | Teckenkodning och uttryck | Behåll egennamnet med versalt U. |
| Unicode code | Unicode-kod | Uttryck och teckenfunktioner | Skriv med bindestreck. |
| log messages panel | panelen Loggmeddelanden | Felsökning | Produktnamnet i panelrubriken behålls. |
| plugin | insticksmodul | QGIS-tillägg | Använd ”plugin” endast om källan är ett egennamn. |
| plugin repository | centralkatalog | Pluginhanteraren | Etablerad i berörda QGIS-dialoger. Använd inte förråd i denna UI-kontext. |
| provider | leverantör | Datakällor och autentisering | |
| script | skript | Python och uttryck | |
| API | API | Programgränssnitt | Översätt inte akronymen. |
| DXF | DXF | Filformat | Översätts inte. |
| CSV | CSV | Filformat | Översätts inte. |
| EPSG | EPSG | CRS-identifierare | Översätts inte. |
| WMS, WMTS, WFS, WCS | WMS, WMTS, WFS, WCS | OGC-tjänster | Behåll protokoll- och standardnamn. |
| GeoPackage | GeoPackage | Filformat och datakälla | Behåll formatnamnet. |
| GeoJSON | GeoJSON | Filformat och datakälla | Behåll formatnamnet. |
| coordinate | koordinat | Geodata och kartverktyg | |
| map unit | kartenhet | Mått i karta och digitalisering | |
| scale bar | skalstock | Kartelement | Inte ”skalrad”. |
| north arrow | nordpil | Kartelement | |
| bookmark | bokmärke | Sparad kartposition | ”Rumsligt bokmärke” när den tekniska betydelsen behöver förtydligas. |
| browser panel | panelen Bläddrare | QGIS-panel | Panelrubriken behandlas som produkttext. |
| layers panel | panelen Lager | QGIS-panel | Panelrubriken behandlas som produkttext. |
| layout manager | layouthanteraren | QGIS-dialog | |
| layout designer | layoutdesignern | QGIS-dialog | |
| rule-based | regelbaserad | Symbologi och etiketter | Skriv ihop. |
| data-defined | datadefinierad | Egenskaper, symbologi och etiketter | Skriv ihop. |
| on the fly | i farten | CRS-omvandling | Använd bara i löpande hjälptetext, inte i tekniska nyckelnamn. |
| refresh | uppdatera | Visa om karta, lager eller data | ”Läs om” när källan uttryckligen avser omläsning från datakällan. |
| reload | läs om | Data från källa eller fil | Inte synonymt med ”uppdatera”. |
| database | databas | Datakällor och anslutningar | |
| database connection | databasanslutning | Datakällor och anslutningar | Skriv ihop. |
| existing | befintlig | Datakällor, tabeller och lager | Undvik den engelsknära falska vännen ”existerande”. |
| authentication | autentisering | Säkerhet och datakällor | |
| authentication method | autentiseringsmetod | Säkerhet och datakällor | Inte ”verifieringsmetod”. |
| certificate authority | certifikatutfärdare | TLS- och certifikatfel | Skriv ihop; undvik den felaktiga formen ”certifikat auktoritet”. |
| trusted certificate | betrott certifikat | TLS- och certifikatfel | ”Inte betrott” är inte samma sak som ”ogiltigt”. |
| credentials | inloggningsuppgifter | Säkerhet och datakällor | Inte ”autentiseringsuppgifter” i vanlig UI-text. |

## Tillämpning

- Kontrollera alltid sammanhang, kommenterar och skärmyta före en ändring. En UI-rubrik, en algoritmbeskrivning och en PyQGIS-API-text kan behöva olika register.
- Bevara platshållare, Qt-markörer som `&`, HTML/XML, filändelser, kommandon, namn på algoritmer och kodsymboler exakt.
- Översätt inte en term mekaniskt när den ingår i ett etablerat egennamn, en inställningsnyckel eller ett API. Lägg i stället en förklarande svensk formulering runt namnet när källtexten gör det möjligt.
- Använd inte tankstreck om inte källsträngen har ett sådant tecken.
- Avvikelser dokumenteras i granskningsbatchen med källsträng, kontext och motivering.
