# QGIS: lokalt granskade batcher som väntar på enhetsuppslag

Datum: 10 november 2026  
Resurs: `qgis-application`, språk `sv`

Detta index avser enbart lokalt granskade förslag vars Transifex-enheter ännu
inte har lästs från den aktuella resursen. Det är inte en uppladdningsfil och
de oförändrade råexporterna i `raw/` är fortsatt auktoritativa för den lokala
utgångspunkten.

| Batch | Omfattning | Status före nästa steg |
|---|---|---|
| 044 | GRASS `r.grow.distance` | Lokal granskning; slå upp enhet. |
| 045–046 | Export till kalkylblad | Lokal granskning; slå upp enheter. |
| 047–049 | Geometrikontroll för glapp | Lokal granskning; slå upp enheter och överför hela långttexter med radbrytningar. |
| 050–051 | Vektorexport och PostGIS | Lokal granskning; slå upp enheter. |
| 052–053 | GPSBabel och GPX | Lokal granskning; bevara platshållare och kommandotexternas avslutande blanksteg. |
| 054 | Rasterlageregenskaper | Lokal granskning; bevara den längre textens två radbrytningar. |
| 055 | Rundhet | Lokal granskning; bevara formelsymbolerna. |
| 056 | SQL-lager | Lokal granskning; bevara `%1`. |
| 057 | Kortaste linjer | Lokal granskning; bevara tre radbrytningar i hjälptesten. |
| 058 | ST-DBSCAN | Lokal granskning; slå upp enheter. |
| 059 | Standardvärden för layout | Lokal granskning; slå upp enheter. |
| 060 | LAS-klasser för punktmoln | Lokal granskning; slå upp enheter. |
| 061 | Geobearbetningsinställningar och API-hjälp | Lokal granskning; slå upp enheter och bevara kodsyntaxen. |
| 062 | Åtgärder och HTTP-överföring | Lokal granskning; bevara HTML, platshållare och HTTP-termer. |
| 063 | Kärn- och symbologietiketter | Lokal granskning; bevara `%1`. |
| 064 | Datakälle- och importdialoger | Lokal granskning; bevara `%1` och två avslutande radbrytningar. |
| 065 | Fel vid läsning av vektorrutepaket | Lokal granskning; bevara `%1`, citattecken och `gzip`. |
| 066 | Georefererare och geometriverktyg | Lokal granskning; slå upp enheter. |
| 067 | UI-stavning och kortkommandohjälp | Lokal granskning; bevara `QgsCustomization` och `GeoTIFF`. |
| 068 | Konsolens API-inställningar | Lokal granskning; bevara API och synlig inställningsetikett. |
| 069 | GDAL-, vektor- och skripttexter | Lokal granskning; bevara kodidentifierare och formatnamn. |
| 070 | Kartvy och dekorationsverktyg | Lokal granskning; `QgsMapCanvas` berörs inte. |
| 071 | Huvudfönstrets lager- och rasteråtgärder | Lokal granskning; bevara `QGIS` och OGR. |
| 072 | GRASS och formulärwidgets | Lokal granskning; bevara tekniska namn och `{}`. |
| 073 | Vektorrutor i bearbetningsverktyg | Lokal granskning; bevara `XYZ` och `MBTiles`. |
| 074 | Utbredning i bearbetningsverktyg | Lokal granskning; `GRASS` bevaras som produktnamn. |
| 075 | GRASS och geometrivalidering | Lokal granskning; bevara kommandon och parameteridentifierare. |
| 076 | Layout och teckenförklaring | Lokal granskning; bevara acceleratorn och `%1`. |
| 077 | Autentisering och certifikat | Lokal granskning; bevara säkerhetstermer och tekniska namn. |
| 078 | 3D-kartkonfiguration | Lokal granskning; bevara `FPS`, `skybox` och `Eye Dome`. |
| 079 | Eye Dome Lighting | Ingen deltafil; batch 078:s kandidat dras tillbaka enligt terminologilistan. |
| 080 | Status i geobearbetningsdialogen | Lokal granskning; bevara HTML, platshållare och radbrytning. |
| 081 | Anslutningsresultat | Lokal granskning; bevara platshållare och teknisk felinformation. |
| 082 | Tilläggshanterarens status och åtgärder | Lokal granskning; bevara `%1` och `%2`. |
| 083 | Tilläggshanterarens dialogetiketter | Lokal granskning; bevara radbrytningen i ett verktygstips. |
| 084 | Tilläggshanterarens hämtning och status | Lokal granskning; skilj förlopp från förfluten tid. |
| 085 | Tilläggshanterarens instruktioner | Lokal granskning; bevara HTML, `{}` och en radbrytning. |
| 086 | Centralkataloger och tilläggskategorier | Lokal granskning; bevara `%1`, länk och URL-prefix. |
| 087 | Tilläggsinstallation och beroenden | Lokal granskning; bevara `<b>` och `%s`. |
| 088 | Tilläggsinstallation, fel och filer | Lokal granskning; bevara `%s`, `{0}` och `__init__.py`. |
| 089 | Tilläggsnätverk och överföring | Lokal granskning; bevara versionsplatshållare och `200 OK`. |
| 090 | Tilläggshanterarens hjälptexter | Lokal granskning; bevara HTML, formatering och synliga UI-namn. |
| 091 | Tilläggsflödets korrekta status- och UI-texter | Kontrollbatch; ingen deltafil för dessa 14 texter. |
| 092 | 3D-punktsymboler och punktmoln | Lokal granskning; bevara radbrytningar och tomma rader i hjälptexten. |
| 093 | Punktmolnshöjd och vertikalt CRS | Lokal granskning; bevara HTML, `%1` och `%2`. |
| 094 | Punktmolnslagrets egenskaper | Lokal granskning; bevara HTML och CRS-termen. |
| 095 | Punktmolnsfrågor och rendering | Lokal granskning; bevara `%1`, radbrytning och tomma rader. |
| 096 | Punktmolnsexport och Spara som | Lokal granskning; bevara `%1` och dataförlustvarningarnas radbrytningar. |

Följ denna ordning inför en uppladdning:

1. Läs aktuell Transifex-enhet efter exakt källsträng och komponent.
2. Jämför den aktuella måltexten med batchens befintliga svenska så att en
   gammal råexport inte skriver över en senare rättning.
3. Bygg en separat deltafil med högst den etablerade batchgränsen.
4. Validera platshållare, HTML/XML, radbrytningar och avslutande blanksteg.
5. Skicka en batch per resurs och läs tillbaka varje accepterad enhet.

Ingen av batcherna i tabellen har laddats upp enbart genom att dokumenteras i
detta index.
