# QGIS: WCS-svar och täckningar 157

Datum: 10 november 2026
Resurs: `qgis-application`, språk `sv`
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen granskar WCS-hämtning, tjänstefel och information om täckningar.
WCS, GetCapabilities, UpdateSequence, CRS, DTD, DOM, RasterIO, URL och
Content-Transfer-Encoding bevaras som protokoll- eller API-termer. `coverage`
översätts här konsekvent med `täckning`, enligt det aktuella QGIS-underlaget.
Platshållarna och radbrytningarna i diagnostiktexter måste bevaras.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Expected 2 parts, %1 received` | `Förväntade 2 delar, %2 mottogs` | `Förväntade 2 delar, %1 togs emot` |
| `Cannot parse multipart response: %1` | `Kan inte tolka multipart svar: %1` | `Det går inte att tolka svar i flera delar: %1` |
| `Content-Transfer-Encoding %1 not supported` | `Kodad innehållsöverföring (CTE) %1 stöds ej` | `Content-Transfer-Encoding %1 stöds inte` |
| `Not logging more than 100 request errors.` | `Loggar ej mer än 100 förfrågningsfel.` | `Loggar inte fler än 100 förfrågningsfel.` |
| `Cannot calculate extent` | `Kan inte beräkna omfång` | `Det går inte att beräkna utbredningen` |
| `Received coverage has wrong extent %1 (expected %2)` | `Mottagen täckning har fel omfång %1 (förväntade %2)` | `Den mottagna täckningen har fel utbredning %1 (förväntad %2)` |
| `Received coverage has wrong size %1 x %2 (expected %3 x %4)` | `Mottagen täckning har fel storlek %1 x %2 (förväntade %3 x %4)` | `Den mottagna täckningen har fel storlek %1 × %2 (förväntad %3 × %4)` |
| `No data received` | `Ingen data mottagen` | `Inga data togs emot` |
| `Dom Exception` | `Dom undantag` | `DOM-undantag` |
| `Could not get WCS Service Exception at %1 at line %2 column %3\n\nResponse was:\n\n%4` | `Kunde inte hämta WCS Service Undantag vid %1 på rad %2 kolumn %3\n\nSvaret var:\n\n%4` | `Det gick inte att hämta WCS-tjänstundantaget vid %1 på rad %2, kolumn %3\n\nSvaret var:\n\n%4` |
| `Service Exception` | `Fel på tjänst` | `Tjänstundantag` |
| `Value of (optional) UpdateSequence parameter in GetCapabilities request is equal to current value of service metadata update sequence number.` | `Värdet på (frivilliga) UpdateSequence-parameter i GetCapabilities-förfrågan är samma som nuvarande värde på 'service metadata update' sekvensnummer.` | `Värdet på den valfria parametern UpdateSequence i GetCapabilities-begäran är samma som tjänstmetadatauppdateringens aktuella sekvensnummer.` |
| `Value of (optional) UpdateSequence parameter in GetCapabilities request is greater than current value of service metadata update sequence number.` | `Värdet på (frivilliga) UpdateSequence-parameter i GetCapabilities-förfrågan är större än nuvarande värde på 'service metadata update' sekvensnummer.` | `Värdet på den valfria parametern UpdateSequence i GetCapabilities-begäran är större än tjänstmetadatauppdateringens aktuella sekvensnummer.` |
| `No other exceptionCode specified by this service and server applies to this exception.` | `Ingen annan 'exceptionCode' angiven av denna tjänst och servern tillämpas på detta undantag.` | `Ingen annan exceptionCode som angetts av tjänsten och servern gäller för det här undantaget.` |
| `Operation request contains an output CRS that can not be used within the output format.` | `Beräkningsbegäran innehåller ett utgående CRS som inte kan användas i det utgående formatet.` | `Åtgärdsbegäran innehåller ett utdata-CRS som inte kan användas i utdataformatet.` |
| `Operation request specifies to "store" the result, but not enough storage is available to do this.` | `Beräkningsbegäran anger att "lagra" resultatet, men det finns inte tillräckligt mycket lagringsutrymme för att göra detta.` | `Åtgärdsbegäran anger att resultatet ska ”lagras”, men det finns inte tillräckligt med lagringsutrymme.` |
| `(No error code was reported)` | `(Ingen felkod)` | `(Ingen felkod rapporterades)` |
| `composed error message '%1'.` | `sammansatt felmeddelande '%1'.` | `sammansatt felmeddelande ”%1”.` |
| `Native CRS` | `Ursprungligt referenskordinatsystem` | `Ursprungligt koordinatreferenssystem` |
| `Native Bounding Box` | `Ursprunglig begränsningsbox` | `Ursprunglig begränsningsruta` |
| `WGS 84 Bounding Box` | `WGS 84 begränsningsbox` | `Begränsningsruta för WGS 84` |
| `Available in CRS` | `Tillgänglig i referenskoordinatsystem` | `Tillgänglig i koordinatreferenssystem` |
| `Available in format` | `Tillgänglig i format` | `Tillgänglig i formatet` |
| `Cache Stats` | `Cache statistik` | `Cache-statistik` |
| `Online Resource` | `Online-resurser` | `Resurs på nätet` |
| `Get Coverage Url` | `Hämta täcknings Url` | `URL för GetCoverage` |
| `And %n more coverage(s)` | `Och ytterligare %n coverage(s)` / `Och ytterligare %n coverage(s)` | `Och ytterligare %n täckning` / `Och ytterligare %n täckningar` |
| `RasterIO error: ` | `RasterIO fel:` | `RasterIO-fel:` |

Ingen extern ändring har gjorts. Aktuella Transifex-enhetsidentifierare måste
hämtas och måltexterna jämföras före en separat deltafil kan skapas.
