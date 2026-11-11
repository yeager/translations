# QGIS: svensk terminologi

Status: projektspecifik terminologilista för den radvisa svenska granskningen av QGIS Desktop på Transifex. Den är en separat granskningsartefakt; råexporter i `raw/` ändras aldrig.

Källor: QGIS egen [svenska dokumentation](https://docs.qgis.org/3.44/sv/docs/user_manual/map_views/map_view.html), etablerad QGIS-svenska i den aktuella Transifex-resursen samt svensk GIS-praxis. Produktnamn, formatnamn, API-namn, algoritmnamn och identifierare översätts inte om inte sammanhanget uttryckligen kräver en förklarande svensk text.

| Engelska | Svenska | Sammanhang | Anmärkning |
|---|---|---|---|
| processing | geobearbetning | QGIS Processing och dialoger | Inte ”bearbetning” när GIS-funktionen avses. |
| toolbox | verktygslåda | Panel med geobearbetningsverktyg | Bevarar etablerad QGIS-term. |
| history | historik | Tidigare körningar och åtgärder | ”Bearbetningshistorik” i Processing. |
| action | åtgärd | Användardefinierade QGIS-åtgärder | Inte alltid ett kommando; kan använda olika åtgärdstyper. |
| algorithm | algoritm | Geobearbetning | Använd ”verktyg” endast för UI-elementet. |
| solver | lösare | GRASS och numeriska ekvationssystem | Använd inte engelska `solver` i svensk UI-text. |
| shell | kommandorad | GRASS-fel och systeminstruktioner | Avser här ett kommandoradsskal. |
| mapset | GRASS-kartuppsättning | GRASS-providern | En särskild arbetskatalog under ett GRASS-projekt. Behåll `mapset` i kod, kommandon och miljövariabler. |
| space time vector dataset | rumtidsvektordataset | GRASS tidsdata | Avser registrerade vektorkartor över tid; skilj från raster- och 3D-rasterdataset. |
| binary | binärfil | GRASS-fel och systeminstruktioner | |
| feature | objekt | Geodata i lager | ”Funktion” endast när programfunktion avses. |
| field | fält | Attributtabell och data | Inte ”kolumn” om inte tabellvyn avses. |
| attribute | attribut | Attributtabell och uttryck | |
| layer | lager | Punkt-, linje-, polygon- och rasterlager | |
| vector layer | vektorlager | Geodatatyp | |
| vector export | vektorexport | GDAL-, OGR- och PostGIS-export | Avser export av geodataobjekt, inte export av ett specifikt UI-lager. |
| raster layer | rasterlager | Geodatatyp | |
| geometry | geometri | GIS-geometri | |
| geometry type | geometrityp | Vektorexport och datamodell | Skriv ihop. |
| non-linear geometry type | icke-linjär geometrityp | PostGIS- och GDAL-export | Bindestreck efter `icke`; huvudordet `geometrityp` skrivs ihop. |
| gap | glapp | Geometrikontroll av polygoners topologi | Avser ett topologiskt mellanrum mellan polygoner. I streckmönster och kodvärden behålls teknisk betydelse eller identifierare. |
| point, line, polygon | punkt, linje, polygon | Geometri | |
| boundary | gräns | Polygon- och områdesgeometri | ”Kant” vid fysisk eller visuell kant. |
| concave hull | konkavt hölje | Geobearbetning och geometri | Använd inte ”uteslutande polygon”. |
| convex hull | omslutande polygon | Geobearbetning och geometri | Etablerad QGIS-svenska. |
| spatial extent | geografisk utbredning | Koordinatmässigt område | Använd den kortare formen ”utbredning” när UI-utrymmet eller källkontexten kräver det. |
| coordinate reference system (CRS) | koordinatreferenssystem (CRS) | Projektion och dataegenskaper | |
| geographic information system (GIS) | geografiskt informationssystem (GIS) | Programinformation och allmän GIS-beskrivning | Gemener i löpande svensk text; behåll versaler bara när en officiell engelsk benämning citeras. |
| projection | projektion | Kartprojektion | |
| georeferencing | georeferering | Raster och kartor | |
| digitizing | digitalisering | Skapa eller ändra geometri | |
| snapping | snäppning | Redigeringsinställningar | Vedertagen QGIS-term. Blender använder i stället den projektspecifika termen ”fästning”. |
| vertex | brytpunkt | Linje- och polygongeometri | |
| waypoint | brytpunkt | GPSBabel och GPX | Följer de befintliga GPSBabel-etiketterna i QGIS. |
| route | rutt | GPSBabel och GPX | |
| track | spår | GPSBabel och GPX | |
| topology | topologi | Validering och redigering | |
| expression | uttryck | Uttrycksbyggaren | |
| variable | variabel | Uttryck och skript | |
| input | indata | Algoritmparameter | |
| output | utdata | Algoritmresultat | |
| parameter | parameter | Algoritm och inställning | |
| argument | argument | Uttrycksfunktioner | Kodnära namn som `strict` och `true` översätts inte. |
| wavelength | våglängd | Uttrycksfunktioner för vågformer | |
| maximum wavelength | maximal våglängd | Uttrycksfunktioner för vågformer | |
| project root name | projektets rotnamn | Projektvalidering | Inte `root-namn`. |
| processing model | geobearbetningsmodell | Model Designer | |
| model | modell | Model Designer | Översätt inte filändelser eller kodnamn. |
| extent | utbredning | Parameteretikett | ”Geografisk utbredning” när precision behövs. |
| zoom level | zoomnivå | Webbkarta och rutor | |
| tile | ruta | Webbkart- och rutmatrissammanhang | Undvik ”platta” i QGIS UI. |
| vector tile | vektorruta | Vektorrutslager och dataleverantörer | Följer QGIS-termen `ruta` för `tile`. |
| sprite | sprite | Vektorrutestilens resursformat | Behåll det tekniska namnet; använd `sprite-definition` och `spritebild` i UI-text. |
| tile matrix | rutmatris | WMTS och liknande | |
| metatile | metaruta | Rutrendning | |
| vector field | vektorfält | GIS-/attributterm | |
| raster pixel | bildpunkt | Rasterdata | |
| kernel radius | kärnradie | Rasterfilter och geobearbetning | `Kernel` avser filterkärnan i denna parameterkontext. |
| non-ground cell | icke-markcell | DTM-filter | Skriv med bindestreck för att undvika tvetydig läsning. |
| point cloud | punktmoln | Punktmolnslager och rendering | |
| M3C2 | M3C2 | PDAL-verktyg för jämförelse av punktmoln | Förkortningen och den utskrivna engelska betydelsen är tekniska namn. |
| subsampling | delurval | Punktmolnsbearbetning | Använd `Cellstorlek för delurval` för parametern `Subsampling cell size`. |
| comparison point cloud | jämförelsepunktmoln | M3C2-parametrar | Avser det andra punktmolnet i jämförelsen, inte åtgärden att jämföra lager. |
| half-length | halvlängd | M3C2-parametrar | Skriv ihop i tekniska parameteretiketter. |
| billboard | Billboard | 3D-punktsymbol | Tekniskt grafiknamn för kameravänd symbol; `skylt` ändrar betydelsen. |
| screen space error | skärmfel | 3D-punktmolnsrendering | UI-term för renderingsfelet i skärmrymden. |
| stroke | konturlinje | Symbologi | Används för en symbols kontur, inte en generell linje. |
| LAS point classification | LAS-klassificering av punkter | Punktmoln | ASPRS LAS-klasser visas som UI-etiketter. |
| wire - guard (shield) | topplina (skärm) | LAS-klass 13 | Kraftledningssammanhang. |
| wire - conductor (phase) | fasledare | LAS-klass 14 | Kraftledningssammanhang. |
| transmission tower | kraftledningsstolpe | LAS-klass 15 | Kraftledningssammanhang. |
| wire-structure connector (insulator) | ledningsfäste (isolator) | LAS-klass 16 | Omfattar isolator och anslutningsdetaljer. |
| bridge deck | brobana | LAS-klass 17 | Inte den bredare termen `bro`. |
| high noise | kraftigt brus | LAS-klass 18 | |
| COPC | COPC | Punktmolnsformat | Formatnamnet översätts inte. |
| band | band | Rasterdata | |
| nodata | inget data | Rasterdata | Behåll `NODATA` om det är ett datavärde eller identifierare. |
| profile | profil | Höjd- och terrängverktyg | |
| map canvas | kartvy | Huvudvyn för kartan | QGIS-dokumentationen använder ”2D-kartvy”. Behåll `QgsMapCanvas` i kod och API-text. |
| 3D map view | 3D-kartvy | 3D-gränssnitt | Bindestreck efter sifferförkortning. |
| tile resolution | rutupplösning | 3D-terrain och ruttjänster | Följer QGIS-termen `ruta` för `tile`. |
| map tile resolution | kartans rutupplösning | 3D-kartkonfiguration | Använd genitiv när kartan är bestämningen. |
| layout | layout | Layoutdesigner | |
| font family | typsnittsfamilj | Text- och layoutegenskaper | Följer de befintliga QGIS-etiketterna. |
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
| plugin | tillägg | QGIS användargränssnitt | `Insticksmodul` kan användas i teknisk dokumentation. Använd `plugin` endast om källan är ett egennamn. |
| plugin installer | installerare för Python-tillägg | Pluginhanteraren | Använd verbform i dialogtiteln för installation från ZIP. |
| plugin repository | centralkatalog | Pluginhanteraren | Etablerad i berörda QGIS-dialoger. Använd inte förråd i denna UI-kontext. |
| invalid plugin | ogiltigt tillägg | Pluginhanteraren | Skilj från tillägg som endast är trasiga eller inkompatibla. |
| experimental plugin | experimentellt tillägg | Pluginhanteraren | Varningstext, inte produktnamn. |
| deprecated plugin | föråldrat tillägg | Pluginhanteraren | Avser ett tillägg som inte längre underhålls. |
| provider | leverantör | Datakällor och autentisering | |
| driver | drivrutin | OGR- och formatfel | Avser formatdrivrutin i GDAL/OGR, inte en generell programkomponent. |
| SpatiaLite | SpatiaLite | Datakällor och feltexter | Produktnamn; följ officiell versalisering. |
| libspatialite | libspatialite | Diagnostik och biblioteksnamn | Biblioteksnamn behålls i gemen teknisk form. |
| autogenerate | generera automatiskt | UI-åtgärd i SpatiaLite-providern | Imperativ i menyalternativ och knappar, inte substantivet ”automatisk generering”. |
| ROWID | ROWID | SQLite- och SpatiaLite-diagnostik | SQL-identifierare; översätts inte. |
| script | skript | Python och uttryck | |
| API | API | Programgränssnitt | Översätt inte akronymen. |
| URI | URI | Datakällor och metadata | Skriv `URI:en` med kolon när svensk bestämd form behövs. |
| DXF | DXF | Filformat | Översätts inte. |
| CSV | CSV | Filformat | Översätts inte. |
| EPSG | EPSG | CRS-identifierare | Översätts inte. |
| EPSG Registry database version | EPSG-registrets databasversion | CRS-information | EPSG behålls som identifierare. |
| Proj String | Proj-sträng | CRS-definition | Produktnamnet och versaliseringen följer QGIS källtext. |
| GeographicLib version | GeographicLib-version | Bearbetningsinformation | Biblioteksnamnet översätts inte. |
| WMS, WMTS, WFS, WCS | WMS, WMTS, WFS, WCS | OGC-tjänster | Behåll protokoll- och standardnamn. |
| GeoPackage | GeoPackage | Filformat och datakälla | Behåll formatnamnet. |
| GeoJSON | GeoJSON | Filformat och datakälla | Behåll formatnamnet. |
| GPX | GPX | GPS-dataformat och datakälla | `GPX-datakälla` i QGIS-gränssnittet. |
| Nominatim geocoder | Nominatim-geokodare | Sökning och attribution | Produktnamnet Nominatim översätts inte. |
| share alike | delning på lika villkor | ODbL-attribution | Licensvillkor, inte generell UI-text. |
| coordinate | koordinat | Geodata och kartverktyg | |
| map unit | kartenhet | Mått i karta och digitalisering | |
| scale bar | skalstock | Kartelement | Inte ”skalrad”. |
| north arrow | nordpil | Kartelement | |
| north arrow SVG path | standardsökväg till SVG-filen för nordpil | Layoutens standardinställning | `SVG` är formatnamn. |
| bookmark | bokmärke | Sparad kartposition | ”Rumsligt bokmärke” när den tekniska betydelsen behöver förtydligas. |
| browser panel | panelen Bläddrare | QGIS-panel | Panelrubriken behandlas som produkttext. |
| layers panel | panelen Lager | QGIS-panel | Panelrubriken behandlas som produkttext. |
| layout manager | layouthanteraren | QGIS-dialog | |
| layout designer | layoutdesignern | QGIS-dialog | |
| layer style table | tabell för lagerstilar | Oracle- och datakällsfel | Skriv ut sammansättningen i feltext för bättre läsbarhet. |
| rule-based | regelbaserad | Symbologi och etiketter | Skriv ihop. |
| data-defined | datadefinierad | Egenskaper, symbologi och etiketter | Skriv ihop. |
| on the fly | i farten | CRS-omvandling | Använd bara i löpande hjälptetext, inte i tekniska nyckelnamn. |
| refresh | uppdatera | Visa om karta, lager eller data | ”Läs om” när källan uttryckligen avser omläsning från datakällan. |
| reload | läs om | Data från källa eller fil | Inte synonymt med ”uppdatera”. |
| database | databas | Datakällor och anslutningar | |
| database connection | databasanslutning | Datakällor och anslutningar | Skriv ihop. |
| thumbnail | miniatyr | Stil- och bildvyer | Använd `miniatyrstorlek` för `Thumbnail size`. |
| socket | socket | TCP- och UDP-feltexter | Teknisk nätverksterm kan behållas i QGIS-feltext. |
| spatially enabled | med rumsligt stöd | PostGIS-datakälla | Beskriver databasobjekt med rumsliga funktioner. |
| existing | befintlig | Datakällor, tabeller och lager | Undvik den engelsknära falska vännen ”existerande”. |
| authentication | autentisering | Säkerhet och datakällor | |
| authentication method | autentiseringsmetod | Säkerhet och datakällor | Inte ”verifieringsmetod”. |
| bucket | bucket | Objektlagring och molndatakällor | Etablerad teknisk term. Översätt inte till ”hink”. |
| secure token | säkerhetstoken | Autentisering | Sammanfogad form i UI-text. |
| account credentials | kontouppgifter | Autentisering | Produktnamn föreleds med bindestreck, exempelvis `MapTiler-kontouppgifter`. |
| relation edit widget | redigeringswidget för attributrelationer | Relaterade attribut och formulär | Samma term används i båda QGIS-widgetkontexterna. |
| certificate authority | certifikatutfärdare | TLS- och certifikatfel | Skriv ihop; undvik den felaktiga formen ”certifikat auktoritet”. |
| trusted certificate | betrott certifikat | TLS- och certifikatfel | ”Inte betrott” är inte samma sak som ”ogiltigt”. |
| credentials | inloggningsuppgifter | Säkerhet och datakällor | Inte ”autentiseringsuppgifter” i vanlig UI-text. |

## Tillämpning

- Kontrollera alltid sammanhang, kommenterar och skärmyta före en ändring. En UI-rubrik, en algoritmbeskrivning och en PyQGIS-API-text kan behöva olika register.
- Bevara platshållare, Qt-markörer som `&`, HTML/XML, filändelser, kommandon, namn på algoritmer och kodsymboler exakt.
- Översätt inte en term mekaniskt när den ingår i ett etablerat egennamn, en inställningsnyckel eller ett API. Lägg i stället en förklarande svensk formulering runt namnet när källtexten gör det möjligt.
- Använd inte tankstreck om inte källsträngen har ett sådant tecken.
- Avvikelser dokumenteras i granskningsbatchen med källsträng, kontext och motivering.
