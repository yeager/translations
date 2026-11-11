# QGIS: WMS-T och XYZ 159

Datum: 10 november 2026
Resurs: `qgis-application`, språk `sv`
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen granskar tidsstyrda WMS-lager, XYZ-anslutningar och återförsök för
ruthämtning. WMS-T, WMTS, XYZ, XML, DPI och URI bevaras. HTML-markering och
tekniska identifierare som `tileRequest` måste bevaras vid en senare deltafil.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `%n tile request(s) in background` | `%n tile-förfrågningar i bakgrunden` / `%n tile-förfrågningar i bakgrunden` | `%n rutbegäran i bakgrunden` / `%n rutbegäranden i bakgrunden` |
| `, %n cache hit(s)` | `, %n cache-träff(ar)` / `, %n cache-träff(ar)` | `, %n cacheträff` / `, %n cacheträffar` |
| `, %n cache misses.` | `, %n cache miss.` / `, %n cache missar.` | `, %n cachemiss.` / `, %n cachemissar.` |
| `Tile request error (Title: %1; Error: %2; URL: %3)` | `Mosaik-fel (Titel: %1; Fel: %2; URL: %3)` | `Fel i rutbegäran (Titel: %1; Fel: %2; URL: %3)` |
| `Tile request error (Status: %1; Content-Type: %2; Length: %3; URL: %4)` | `Mosaik-fel (Status: %1; Innehållstyp: %2; Längd: %3; URL: %4)` | `Fel i rutbegäran (Status: %1; Innehållstyp: %2; Längd: %3; URL: %4)` |
| `Not logging more than 100 request errors.` | `Loggar ej mer än 100 förfrågningsfel.` | `Loggar inte fler än 100 förfrågningsfel.` |
| `Tile request max retry error. Failed %1 requests for tile %2 of tileRequest %3 (url: %4)` | `'Tile' begäran nådde maximalt antal omfrågninar. Misslyckades %1 begäran för 'tile' %2 av 'tileRequest' %3 (url: %4)` | `Rutbegäran nådde högsta antalet återförsök. %1 begäranden misslyckades för ruta %2 i tileRequest %3 (URL: %4)` |
| `repeat tileRequest %1 tile %2(retry %3)` | `upprepa 'tileRequest' %1 'tile' %2(försök %3)` | `upprepa tileRequest %1, ruta %2 (återförsök %3)` |
| `No reference time is reported in the layer's capabilities.` | `Det finns ingen referenstid rapporterad i lagrets capabilities.` | `Ingen referenstid har rapporterats i lagrets funktioner.` |
| `Reported reference time extent: <i>%1</i>` | `Rapporterad utbredning av referenstid: <i>%1</i>` | `Rapporterad utbredning för referenstid: <i>%1</i>` |
| `Closest Match to Start of Range` | `Närmsta matchning med början av intervallet` | `Närmaste matchning till början av intervallet` |
| `Closest Match to End of Range` | `Närmsta matchning med slutet av intervallet` | `Närmaste matchning till slutet av intervallet` |
| `WMS-T Settings` | `WMS-T Inställningar` | `WMS-T-inställningar` |
| `Static WMS-T Temporal Range` | `Tidsintervall i Statisk WMS-T` | `Statiskt tidsintervall för WMS-T` |
| WMS-T-hjälptexten om `Dynamic Temporal Control` | Språkligt korrekt men saknar kommatecken efter inledande infinitivfras. | `Alternativen för statisk WMS-T är inaktiverade eftersom lagret använder <span style=" font-weight:600;">Dynamisk tidskontroll</span>. Aktivera dem genom att först inaktivera <span style=" font-weight:600;">Dynamisk tidskontroll</span>.` med oförändrad omgivande HTML. |
| WMS-T-hjälptexten om lagrets funktioner och tidsintervall | Använder `förmågorna`, `annonserade` och `lager-tidsintervall`. | `Om det här lagrets funktioner flyttas utanför tidsintervallet återställs intervallet till lagrets angivna standardtidsintervall.` med oförändrad omgivande HTML. |
| `Set end same as start` | `Ställ in slut till samma som start` | `Ange samma slut som start` |
| `Ignore time components (use dates only)` | `Ignorera tidskomponent (använd endast datum)` | `Ignorera tidskomponenter (använd endast datum)` |
| `If checked the time component of temporal queries will be discarded and only the date component will be used in server requests` | `Om markerad kommer tidskomponenten att förkastas och endast datumkomponenten användas i tidsförfrågningar till server` | `Om alternativet är markerat ignoreras tidskomponenten i tidsfrågor och endast datumkomponenten används i serverbegäranden.` |
| `XYZ Connection` | `XYZ Anslutning` | `XYZ-anslutning` |
| `Connection Properties` | `Kopplingsegenskaper` | `Anslutningsegenskaper` |
| `Are you sure you want to remove the %1 connection and all associated settings?` | `Är du säker att du vill ta bort anslutningen %1 och alla tillhörande inställningar?` | `Är du säker på att du vill ta bort anslutningen %1 och alla tillhörande inställningar?` |
| `High (512x512 / 192 DPI)` | `High (512x512 / 192 DPI)` | `Hög (512x512 / 192 DPI)` |

Ingen extern ändring har gjorts. Aktuella Transifex-enhetsidentifierare måste
hämtas och måltexterna jämföras före en separat deltafil kan skapas.
