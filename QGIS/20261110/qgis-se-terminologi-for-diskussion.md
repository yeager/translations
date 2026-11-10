# QGIS: svensk terminologi för diskussion med Qgis.se

Status: diskussionsunderlag, 10 november 2026. Omfattar QGIS Desktop, svensk
användargränssnittstext, dokumentation och vanliga felmeddelanden. Det är inte
en auktoritativ ordlista för varje QGIS-sträng. Syftet är att få beslut om de
termer som behöver vara konsekventa innan en större svensk granskning skickas
upp.

## Så används listan

- **Fastställd**: etablerad i aktuell QGIS-svenska eller tydligt vedertagen
  GIS-svenska. Ändras bara med sakskäl.
- **Rekommenderad**: lämplig konsekvent huvudform. Invändningar och belägg
  välkomnas.
- **Öppen**: kräver ett beslut från svenska QGIS-användare eller fackfolk.
- Produktnamn, kodsymboler, filändelser, formatnamn, protokoll och
  identifierare översätts inte.

Källor som kontrollerats 2026-11-10: [QGIS 3.44, svenskt gränssnitt](https://docs.qgis.org/3.44/sv/docs/user_manual/introduction/qgis_gui.html), [vektoregenskaper](https://docs.qgis.org/3.44/sv/docs/user_manual/working_with_vector/vector_properties.html), [layout](https://docs.qgis.org/3.44/sv/docs/user_manual/print_composer/index.html) och [geobearbetning](https://docs.qgis.org/3.44/sv/docs/user_manual/processing/intro.html). Den lokala Transifex-exporten används som belägg för faktisk UI-kontext, inte som ensam språklig auktoritet.

## Grundläggande GIS och data

| Engelska | Rekommenderad svenska | Status | Kommentar |
|---|---|---|---|
| feature | objekt | Fastställd | GIS-objekt i lager. Använd inte funktion för geografiskt objekt. |
| feature id | objekt-id | Rekommenderad | Kort UI-form. `FID` behålls när det är fältnamn eller identifierare. |
| feature type | objekttyp | Rekommenderad | |
| field | fält | Fastställd | Attributfält. Kolumn avser främst tabellvyn. |
| attribute | attribut | Fastställd | |
| attribute table | attributtabell | Fastställd | |
| record | post | Rekommenderad | I databas- och tabellkontext. |
| value | värde | Fastställd | |
| null value | nullvärde | Rekommenderad | Behåll `NULL` när det är ett SQL-värde. |
| data type | datatyp | Fastställd | |
| data source | datakälla | Fastställd | |
| dataset | datamängd | Rekommenderad | Datauppsättning kan användas i mer formell dokumentation. |
| layer | lager | Fastställd | |
| group | grupp | Fastställd | Lagergrupp när precision krävs. |
| layer tree | lagerträd | Rekommenderad | |
| layer order | lagerordning | Rekommenderad | |
| vector layer | vektorlager | Fastställd | |
| raster layer | rasterlager | Fastställd | |
| mesh layer | nätlager | Rekommenderad | Avser mesh-data, inte bild- eller vägnät. |
| point cloud layer | punktmolnslager | Fastställd | |
| virtual layer | virtuellt lager | Rekommenderad | |
| temporary layer | tillfälligt lager | Rekommenderad | |
| memory layer | minneslager | Rekommenderad | Använd inte lager i minnet som fast namn. |
| joined layer | sammanfogat lager | Öppen | Skilj från sammanfogning av geometrier. |
| embedded layer | inbäddat lager | Rekommenderad | |
| selected feature | markerat objekt | Fastställd | |
| active layer | aktivt lager | Fastställd | |
| visible layer | synligt lager | Fastställd | |

## Geometri och topologi

| Engelska | Rekommenderad svenska | Status | Kommentar |
|---|---|---|---|
| geometry | geometri | Fastställd | |
| point | punkt | Fastställd | |
| line | linje | Fastställd | |
| linestring | linjesträng | Rekommenderad | Tekniskt objektnamn. |
| polygon | polygon | Fastställd | |
| multipoint | multipunkt | Rekommenderad | |
| multiline | multilinje | Öppen | Föreslås `multilinje`; befintliga översättningar bör kartläggas före beslut. |
| multipolygon | multipolygon | Rekommenderad | |
| geometry collection | geometrisamling | Rekommenderad | |
| vertex | brytpunkt | Fastställd | QGIS-användning, även för polygoners hörn. |
| node | nod | Rekommenderad | Använd brytpunkt i redigeringsverktyg när det är en vertex. |
| segment | segment | Fastställd | |
| ring | ring | Rekommenderad | Polygonens yttre eller inre ring. |
| hole | hål | Rekommenderad | Polygonhål i UI-text. |
| boundary | gräns | Fastställd | Kant när det handlar om visuell eller fysisk kant. |
| centroid | centroid | Rekommenderad | Tyngdpunkt kan vara begripligare i hjälptetext. |
| bounding box | begränsningsruta | Rekommenderad | `bounding box` kan behållas i API- och GDAL-text. |
| extent | utbredning | Fastställd | Geografisk utbredning när precision behövs. |
| spatial extent | geografisk utbredning | Fastställd | |
| envelope | omslutande rektangel | Öppen | Bör fastställas mot GDAL/GEOS-svenska. |
| convex hull | omslutande polygon | Fastställd | |
| concave hull | konkavt hölje | Fastställd | |
| buffer | buffert | Fastställd | |
| dissolve | upplös | Rekommenderad | Verb i geobearbetningsalgoritm. |
| clip | klipp | Rekommenderad | Verb. `Klipp ut` i förklarande text vid behov. |
| intersect | skär | Rekommenderad | Verb; skärning som substantiv. |
| union | union | Rekommenderad | Geometrisk operation, inte användargrupp. |
| difference | differens | Rekommenderad | Geometrisk operation. |
| symmetric difference | symmetrisk differens | Rekommenderad | |
| topology | topologi | Fastställd | |
| topological editing | topologisk redigering | Rekommenderad | |
| valid geometry | giltig geometri | Fastställd | |
| make valid | gör giltig | Rekommenderad | |
| self-intersection | självkorsning | Rekommenderad | |

## Koordinater, referenssystem och mätning

| Engelska | Rekommenderad svenska | Status | Kommentar |
|---|---|---|---|
| coordinate | koordinat | Fastställd | |
| coordinate pair | koordinatpar | Rekommenderad | |
| coordinate reference system (CRS) | koordinatreferenssystem (CRS) | Fastställd | |
| source CRS | källreferenskoordinatsystem | Rekommenderad | Kort `käll-CRS` där UI:t kräver det. |
| destination CRS | målreferenskoordinatsystem | Fastställd | Bevarar QGIS-term och skiljer från måldatum. |
| project CRS | projektets koordinatreferenssystem | Rekommenderad | |
| horizontal CRS | horisontellt koordinatreferenssystem | Rekommenderad | |
| vertical CRS | vertikalt koordinatreferenssystem | Rekommenderad | |
| compound CRS | sammansatt koordinatreferenssystem | Rekommenderad | |
| projection | projektion | Fastställd | |
| transformation | omvandling | Rekommenderad | Koordinatomvandling i förklarande text. |
| datum transformation | datumomvandling | Rekommenderad | |
| georeferencing | georeferering | Fastställd | |
| georeferencer | georefererare | Öppen | Kontrollera etablerat namn på QGIS-verktyget. |
| on-the-fly reprojection | dynamisk projektion | Öppen | Tidigare `i farten` är begripligt men mindre fackmässigt. |
| map unit | kartenhet | Fastställd | |
| distance | avstånd | Fastställd | |
| area | yta | Fastställd | Areal när mätenhet eller facktext kräver det. |
| bearing | bäring | Rekommenderad | |
| azimuth | azimut | Rekommenderad | |
| scale | skala | Fastställd | |
| scale denominator | skalnämnare | Rekommenderad | |
| scale bar | skalstock | Fastställd | |
| north arrow | nordpil | Fastställd | |

## Redigering och urval

| Engelska | Rekommenderad svenska | Status | Kommentar |
|---|---|---|---|
| editing | redigering | Fastställd | |
| digitizing | digitalisering | Fastställd | Skapa eller ändra geometri. |
| edit mode | redigeringsläge | Rekommenderad | |
| toggle editing | växla redigeringsläge | Rekommenderad | |
| add feature | lägg till objekt | Fastställd | |
| delete feature | ta bort objekt | Fastställd | |
| move feature | flytta objekt | Fastställd | |
| reshape feature | forma om objekt | Rekommenderad | |
| split feature | dela objekt | Fastställd | |
| merge features | slå samman objekt | Rekommenderad | |
| merge attributes | slå samman attribut | Rekommenderad | |
| tracing | följning | Öppen | Kräver skärmkontext och jämförelse med svensk CAD/GIS-praxis. |
| snapping | snäppning | Fastställd | QGIS-specifik term. Inte Blender-termen fästning. |
| snapping tolerance | snäppningstolerans | Rekommenderad | |
| snap to vertex | snäpp mot brytpunkt | Rekommenderad | |
| snap to segment | snäpp mot segment | Rekommenderad | |
| avoid intersections | undvik skärningar | Rekommenderad | |
| vertex tool | brytpunktsverktyg | Rekommenderad | |
| selection | markering | Fastställd | |
| select by expression | markera med uttryck | Rekommenderad | |
| select by location | markera efter plats | Öppen | `markera efter position` kan vara tydligare. |
| invert selection | invertera markering | Rekommenderad | |
| deselect | avmarkera | Fastställd | |

## Symbologi, etiketter och rendering

| Engelska | Rekommenderad svenska | Status | Kommentar |
|---|---|---|---|
| symbology | symbologi | Fastställd | |
| symbol | symbol | Fastställd | |
| symbol layer | symbollager | Rekommenderad | |
| renderer | renderare | Öppen | `renderare` är tydligt i teknisk UI-text men bör beslutas. |
| rendering | rendering | Fastställd | |
| style | stil | Fastställd | Lagerstil vid behov. |
| style manager | stilhanterare | Rekommenderad | |
| categorized | kategoriserad | Rekommenderad | |
| graduated | graderad | Rekommenderad | |
| rule-based | regelbaserad | Fastställd | |
| data-defined | datadefinierad | Fastställd | |
| opacity | opacitet | Rekommenderad | Genomskinlighet kan användas i hjälptetext. |
| blend mode | blandningsläge | Rekommenderad | |
| color ramp | färgramp | Rekommenderad | |
| color scheme | färgschema | Fastställd | |
| label | etikett | Fastställd | |
| labeling | etikettering | Rekommenderad | |
| callout | hänvisningslinje | Öppen | Valet kräver bildkontext. |
| diagram | diagram | Fastställd | |
| mask | mask | Fastställd | |
| shadow | skugga | Fastställd | |
| live update | direktuppdatering | Rekommenderad | |

## Raster, punktmoln och terräng

| Engelska | Rekommenderad svenska | Status | Kommentar |
|---|---|---|---|
| raster | raster | Fastställd | |
| pixel | bildpunkt | Fastställd | |
| band | band | Fastställd | |
| band set | banduppsättning | Rekommenderad | |
| no data | inget data | Rekommenderad | Behåll `NODATA` som värde eller identifierare. |
| resampling | omsampling | Rekommenderad | |
| hillshade | skuggrelief | Rekommenderad | |
| slope | lutning | Fastställd | |
| aspect | exponeringsriktning | Rekommenderad | |
| digital elevation model (DEM) | digital höjdmodell (DEM) | Fastställd | |
| terrain | terräng | Fastställd | |
| point cloud | punktmoln | Fastställd | |
| point cloud attribute | punktmolnsattribut | Rekommenderad | |
| classification | klassificering | Fastställd | |
| elevation | höjd | Fastställd | |
| profile | profil | Fastställd | |
| profile tool | profilverktyg | Rekommenderad | |
| COPC | COPC | Fastställd | Formatnamn. |

## Layout, kartproduktion och export

| Engelska | Rekommenderad svenska | Status | Kommentar |
|---|---|---|---|
| layout | layout | Fastställd | |
| layout designer | layoutdesignern | Fastställd | |
| layout manager | layouthanteraren | Fastställd | |
| layout item | layoutelement | Rekommenderad | |
| map item | kartelement | Rekommenderad | |
| legend | teckenförklaring | Fastställd | |
| legend item | teckenförklaringsobjekt | Öppen | Kan kortas till teckenförklaringselement. |
| map frame | kartbild | Öppen | Kontrollera svensk kartografisk praxis. |
| page | sida | Fastställd | |
| atlas | atlas | Fastställd | |
| atlas feature | atlasobjekt | Rekommenderad | |
| overview | översikt | Fastställd | |
| grid | rutnät | Fastställd | |
| graticule | gradnät | Rekommenderad | |
| export | export | Fastställd | `Exportera` som verb. |
| export as image | exportera som bild | Rekommenderad | |
| print | skriv ut | Fastställd | |
| template | mall | Fastställd | |
| report | rapport | Fastställd | |

## Geobearbetning och uttryck

| Engelska | Rekommenderad svenska | Status | Kommentar |
|---|---|---|---|
| processing | geobearbetning | Fastställd | QGIS Processing. |
| toolbox | verktygslåda | Fastställd | |
| processing toolbox | verktygslådan Geobearbetning | Rekommenderad | Namnform för panelen. |
| algorithm | algoritm | Fastställd | Verktyg endast för UI-elementet. |
| algorithm provider | algoritmleverantör | Rekommenderad | |
| model | modell | Fastställd | |
| processing model | geobearbetningsmodell | Fastställd | |
| model designer | modellbyggaren | Öppen | Jämför med etablerad QGIS-svenska innan beslut. |
| batch processing | batchbearbetning | Rekommenderad | |
| input | indata | Fastställd | |
| output | utdata | Fastställd | |
| parameter | parameter | Fastställd | |
| advanced parameter | avancerad parameter | Rekommenderad | |
| expression | uttryck | Fastställd | |
| expression builder | uttrycksbyggaren | Rekommenderad | |
| function | funktion | Fastställd | Funktionsnamn i kod lämnas orörda. |
| variable | variabel | Fastställd | |
| aggregate | aggregat | Rekommenderad | Aggregatfunktion i uttryckskontext. |
| condition | villkor | Fastställd | |
| filter | filter | Fastställd | Filtrera som verb. |
| query | fråga | Rekommenderad | SQL-fråga när kontexten är databas. |

## Databaser, tjänster och format

| Engelska | Rekommenderad svenska | Status | Kommentar |
|---|---|---|---|
| database | databas | Fastställd | |
| database connection | databasanslutning | Fastställd | |
| connection | anslutning | Fastställd | |
| schema | schema | Fastställd | Databasschema när det annars är oklart. |
| table | tabell | Fastställd | |
| view | vy | Fastställd | Databasvy när precision behövs. |
| query layer | frågelager | Rekommenderad | |
| primary key | primärnyckel | Fastställd | |
| foreign key | främmande nyckel | Rekommenderad | |
| transaction | transaktion | Fastställd | |
| transaction group | transaktionsgrupp | Rekommenderad | |
| service | tjänst | Fastställd | |
| web service | webbtjänst | Fastställd | |
| web map service | webbkarttjänst | Rekommenderad | Behåll WMS som standardnamn. |
| tile | ruta | Fastställd | Inte platta i QGIS UI. |
| tile matrix | rutmatris | Fastställd | |
| metatile | metaruta | Fastställd | |
| cache | cache | Rekommenderad | Cacha som verb bör undvikas i UI. |
| GeoPackage | GeoPackage | Fastställd | Formatnamn. |
| GeoJSON | GeoJSON | Fastställd | Formatnamn. |
| Shapefile | Shapefile | Fastställd | Formatnamn. |
| CSV | CSV | Fastställd | Formatnamn. |
| DXF | DXF | Fastställd | Formatnamn. |
| WMS, WMTS, WFS, WCS | WMS, WMTS, WFS, WCS | Fastställd | Protokoll- och standardnamn. |

## Gränssnitt, säkerhet och utvecklartext

| Engelska | Rekommenderad svenska | Status | Kommentar |
|---|---|---|---|
| map canvas | kartvy | Fastställd | `QgsMapCanvas` lämnas orört i kod och API. |
| browser panel | panelen Bläddrare | Fastställd | Panelrubrik. |
| layers panel | panelen Lager | Fastställd | Panelrubrik. |
| log messages panel | panelen Loggmeddelanden | Fastställd | Panelrubrik. |
| bookmark | bokmärke | Fastställd | Rumsligt bokmärke när betydelsen måste förtydligas. |
| refresh | uppdatera | Fastställd | Visa om karta, lager eller data. |
| reload | läs om | Fastställd | Läs på nytt från källa eller fil. |
| timeout | tidsgräns | Fastställd | |
| plugin | insticksmodul | Fastställd | Plugin bara om det är egennamn eller kodterm. |
| provider | leverantör | Fastställd | Datakällor och autentisering. |
| authentication | autentisering | Fastställd | |
| authentication method | autentiseringsmetod | Fastställd | Inte verifieringsmetod. |
| credentials | inloggningsuppgifter | Fastställd | Vanlig UI-text. |
| certificate authority | certifikatutfärdare | Fastställd | |
| trusted certificate | betrott certifikat | Fastställd | Inte samma sak som giltigt certifikat. |
| encryption | kryptering | Fastställd | |
| API | API | Fastställd | Akronymen översätts inte. |
| application programming interface | programgränssnitt | Rekommenderad | Endast när akronymen skrivs ut. |
| script | skript | Fastställd | |
| console | konsol | Fastställd | |
| debug | felsök | Rekommenderad | Felsökning som substantiv. |
| error | fel | Fastställd | |
| warning | varning | Fastställd | |
| shortcut | kortkommando | Öppen | Befintlig QGIS-svenska använder delvis genväg; välj en huvudform efter UI-granskning. |

## Beslut som behöver Qgis.se

1. **Snäppning**: behålls som QGIS-term för *snapping*. Bekräfta om svensk
   QGIS-gemenskap hellre vill använda `fästning` eller en annan form.
2. **Dynamisk projektion**: välj mellan `dynamisk projektion` och den mer
   direkta men mindre fackmässiga formen `projektion i farten` för
   *on-the-fly reprojection*.
3. **Renderare**: fastställ om `renderare` ska vara UI-term eller om QGIS ska
   beskriva effekten, till exempel `visningsmetod`.
4. **Kortkommando/genväg**: välj en huvudterm för *shortcut* och använd den
   konsekvent i menyer, konfliktdialoger och dokumentation.
5. **Select by location**: kontrollera om `markera efter plats` eller
   `markera efter position` är mest etablerat bland svenska GIS-användare.
6. **Tracing**: besluta term först efter skärmbild eller tydlig verktygskontext.
7. **Model Designer** och **Georeferencer**: kontrollera de faktiska svenska
   panel- och dialogtitlarna i en aktuell QGIS-byggnad före namnbyte.

## Stilregler

- Skriv sammansättningar: `databasanslutning`, `snäppningstolerans` och
  `punktmolnslager`.
- Bevara platshållare, XML/HTML, filändelser, funktionsnamn, kommandon och
  QGIS-klassnamn exakt.
- Skilj på en synlig UI-etikett och teknisk API-text. `QgsMapCanvas` är inte
  `kartvy`, men den omgivande förklaringen kan vara det.
- Använd svenska versalregler i löpande UI-text och inga tankstreck som inte
  finns i källsträngen.
