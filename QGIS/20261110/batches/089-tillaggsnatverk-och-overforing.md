# QGIS: tilläggsnätverk och överföring 089

Datum: 10 november 2026  
Resurs: `qgis-application`, språk `sv`  
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen granskar nätverksstatus och överföringsfel vid installation av
tillägg. Platshållarna `{minVersion}` och `{maxVersion}` samt det synliga
svaret `200 OK` bevaras. De två separata tidsgränsmeddelandena hålls som
separata enheter trots liknande rekommenderad svenska.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `If you haven't canceled the download manually, it was most likely caused by a timeout. In this case consider increasing the connection timeout value in QGIS options window.` | `Om du inte har avbrutit nedladdningen manuellt så kan det bero på en timeout. I detta fallet överväg att öka på inställningen för anslutningstimeout i QGIS inställningar.` | `Om du inte avbröt hämtningen manuellt beror det troligen på en tidsgräns. Överväg i så fall att höja tidsgränsen för anslutningen i QGIS-inställningarna.` |
| `Server response is 200 OK, but doesn't contain plugin metadata. This is most likely caused by a proxy or a wrong repository URL. You can configure proxy settings in QGIS options.` | `Svaret från servern är 200 OK, men innehåller ingen metadata för tillägg. Detta beror sannolikt på en proxy eller felaktig URL till centralkatalogen. Du kan konfigurera proxyinställningar i QGIS inställningarna.` | `Servern svarade 200 OK, men svaret innehåller inga metadata för tillägget. Det beror troligen på en proxy eller en felaktig URL till centralkatalogen. Du kan konfigurera proxyinställningarna i QGIS-inställningarna.` |
| `If you haven't canceled the download manually, it might be caused by a timeout. In this case consider increasing the connection timeout value in QGIS options.` | `Om du inte har avbrutit nedladdningen manuellt, så kan det bero på en timeout. I detta fallet överväg att öka på inställningen för anslutningstimeout i QGIS inställningar.` | `Om du inte avbröt hämtningen manuellt kan det bero på en tidsgräns. Överväg i så fall att höja tidsgränsen för anslutningen i QGIS-inställningarna.` |
| `Plugin designed for QGIS {minVersion} - {maxVersion}` | `Tillägg designat för QGIS {minVersion} - {maxVersion}` | `Tillägget är avsett för QGIS {minVersion} - {maxVersion}` |
| `Could not store plugin to the plugin directory:` | `Kunde inte lagra tillägg i biblioteket för tillägg:` | `Det gick inte att lagra tillägget i tilläggskatalogen:` |
| `Success` | `Lyckades` | `Klart` |
| `Host connected. Sending request…` | `Värd ansluten. Skickar förfrågan…` | `Ansluten till värden. Skickar begäran…` |
| `Closing connection…` | `Stänger anslutning…` | `Stänger anslutningen…` |
| `Idle` | `Stillastående` | `Vilande` |
| `Could not write to temporary folder.` | `Kunde inte skriva till temporär mapp.` | `Det gick inte att skriva till den tillfälliga mappen.` |
| `Failed to unzip the plugin package. Probably it's broken or missing from the repository.` | `Kunde inte packa upp tilläggspaket. Det är antagligen trasigt eller saknas i repot.` | `Det gick inte att packa upp tilläggspaketet. Det är troligen trasigt eller saknas i centralkatalogen.` |
| `Installing plugin:` | `Installerar plugin:` | `Installerar tillägg:` |

Ingen extern ändring har gjorts. Aktuella Transifex-enhetsidentifierare måste
hämtas och måltexterna jämföras före en separat deltafil kan skapas.
