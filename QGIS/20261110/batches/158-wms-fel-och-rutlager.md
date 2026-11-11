# QGIS: WMS-fel och rutlager 158

Datum: 10 november 2026
Resurs: `qgis-application`, språk `sv`
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen granskar WMS-providerens fel, kapacitetsuppgifter och rutlager.
WMS, WMTS, WMS-C, XYZ, GetMap, GetFeatureInfo, GetLegendGraphic, MBTiles,
EPSG, CRS, SRS och URI bevaras. `tile` översätts med `ruta` i allmän UI-text;
etablerade API- och formatnamn behålls.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Cannot set CRS` | `Kan inte sätta referenskoordinatsystem` | `Det går inte att ange koordinatreferenssystemet` |
| `Setup tile capabilities` | `Ställ in tile egenskaper för tjänst` | `Ställ in tjänstens rutfunktioner` |
| `Cannot open MBTiles database` | `Kan inte öppna databas för MBTiles` | `Det går inte att öppna MBTiles-databasen` |
| `Retrieve server capabilities` | `Hämta egenskaper för tjänst` | `Hämta serverns funktioner` |
| `Number of layers and styles don't match` | `Antal lager och stil överensstämmer ej` | `Antalet lager och stilar stämmer inte överens` |
| `Number of tile layers must be one` | `Antal 'tile' lager måste vara ett` | `Antalet rutlager måste vara ett` |
| `Tile layer not found` | `'Tile' lager kan inte hittas` | `Rutlagret hittades inte` |
| `Tile layer or tile matrix set not found` | `'Tile' lager eller 'tile' matrisuppsättning kan inte hittas` | `Rutlagret eller rutmatrisuppsättningen hittades inte` |
| `, %n cache misses.` | `, %n cache miss.` / `, %n cache missar.` | `, %n cachemiss.` / `, %n cachemissar.` |
| `Warning: Bbox placeholder EPSG:%1 does not match current CRS %2` | `Varning: Platshållare för Bbox EPSG:%1 matchar inte aktuellt koordinatsystem %2` | `Varning: Bbox-platshållaren EPSG:%1 stämmer inte överens med aktuellt CRS %2` |
| `Dom Exception` | `DOM fel` | `DOM-undantag` |
| `Service Exception` | `Fel på tjänst` | `Tjänstundantag` |
| `GetMap request is for a Layer not offered by the server, or GetFeatureInfo request is for a Layer not shown on the map.` | `GetMap-förfrågan är för ett lager som serven inte tillhandahåller, eller GetFeatureInfo-anropet är avsett för ett lager som inte är med på kartan.` | `GetMap-begäran gäller ett lager som servern inte erbjuder, eller GetFeatureInfo-begäran gäller ett lager som inte visas på kartan.` |
| `GetFeatureInfo request is applied to a Layer which is not declared queryable.` | `GetFeatureInfo-förfrågan ställdes till ett lager som inte är definerat som frågbart.` | `GetFeatureInfo-begäran riktades till ett lager som inte är definierat som frågbart.` |
| `Value of (optional) UpdateSequence parameter in GetCapabilities request is equal to current value of service metadata update sequence number.` | `Värdet på (frivilliga) UpdateSequence-parameter i GetCapabilities-förfrågan är samma som nuvarande värde på 'service metadata update' sekvensnummer.` | `Värdet på den valfria parametern UpdateSequence i GetCapabilities-begäran är samma som tjänstmetadatauppdateringens aktuella sekvensnummer.` |
| `Value of (optional) UpdateSequence parameter in GetCapabilities request is greater than current value of service metadata update sequence number.` | `Värdet på (frivilliga) UpdateSequence-parameter i GetCapabilities-förfrågan är större än nuvarande värde på 'service metadata update' sekvensnummer.` | `Värdet på den valfria parametern UpdateSequence i GetCapabilities-begäran är större än tjänstmetadatauppdateringens aktuella sekvensnummer.` |
| `Request is for an optional operation that is not supported by the server.` | `Förfrågan gäller en frivillig operation som servern inte stödjer.` | `Begäran gäller en valfri åtgärd som servern inte stöder.` |
| `Request contains a time value that does not match any available layer in the server.` | `Förfrågan innehåller tidsvärden som inte matchar något tillgängligt lager i servern.` | `Begäran innehåller ett tidsvärde som inte stämmer överens med något lager som finns på servern.` |
| `Request contains some parameter values that do not match any available layer in the server` | `Förfrågan innehåller någon parameter som inte matchar något tillgängligt lager i servern.` | `Begäran innehåller parametervärden som inte stämmer överens med något lager som finns på servern.` |
| `Available in CRS` | `Tillgänglig i referenskoordinatsystem` | `Tillgänglig i koordinatreferenssystem` |
| `(and %n more)` | `(och %1 till)` / `(och %1 till)` | `(och %n till)` / `(och %n till)` |
| `Available in style` | `Tilgänglig med stil` | `Tillgänglig med stil` |
| `LegendURLs` | `Url till teckenförklaring` | `Teckenförklarings-URL:er` |
| `Tile Layer Properties` | `Egenskaper mosaiklager` | `Egenskaper för rutlager` |
| `Cache Stats` | `Cache statistik` | `Cache-statistik` |
| `Get feature info request error (Title: %1; Error: %2; URL: %3)` | `'Get feature info' begäran fel (Titel: %1; Fel: %2; URL: %3)` | `Fel i GetFeatureInfo-begäran (Titel: %1; Fel: %2; URL: %3)` |
| `Tile templates` | `Mosaik-mall` | `Rutmallar` |
| `FeatureInfo templates` | `FeatureInfo-mall` | `GetFeatureInfo-mallar` |
| `Tileset Properties` | `Tileset-inställningar` | `Rutuppsättningens egenskaper` |
| `Tile mode` | `'Tile' läge` | `Rutläge` |
| `Invalid tile mode` | `Otillåtet 'tile' läge` | `Ogiltigt rutläge` |
| `Bounding Box` | `Begränsningsbox` | `Begränsningsruta` |
| `Selected tile matrix set ` | `Vald 'tile' matrisuppsättning` | `Vald rutmatrisuppsättning ` |
| `Tile size [px]` | `'Tile' storlek [px]` | `Rutstorlek [px]` |
| `Tile size [mu]` | `'Tile' storlek [mu]` | `Rutstorlek [mu]` |
| `%n missing row(s)` | `%n saknade rad(er)` / `%n saknade rad(er)` | `%n saknad rad` / `%n saknade rader` |
| `%n missing column(s)` | `%n saknade kolumn(er)` / `%n saknade kolumn(er)` | `%n saknad kolumn` / `%n saknade kolumner` |
| `Context not fully specified (extent was defined but width and/or height was not).` | `Innehåll inte fullständigt angivet (utsträckning är definierat men bredd och/eller höjd är det inte).` | `Kontexten är inte fullständigt angiven (utbredningen har angetts, men bredden och/eller höjden saknas).` |
| `Map getfeatureinfo error %1: %2` | `Kartans 'getfeatureinfo' fel %1: %2` | `Fel i kartans GetFeatureInfo %1: %2` |
| `Cannot parse getfeatureinfo: %1` | `Kan inte tolka getfeatureinfo: %1` | `Det går inte att tolka GetFeatureInfo: %1` |
| `%1 of %2 bytes of GetLegendGraphic downloaded.` | `%1 av %2 bytes av 'GetLegendGraphic' hämtad.` | `%1 av %2 byte av GetLegendGraphic har hämtats.` |

Ingen extern ändring har gjorts. Aktuella Transifex-enhetsidentifierare måste
hämtas och måltexterna jämföras före en separat deltafil kan skapas.
