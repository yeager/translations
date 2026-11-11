# QGIS: GPSBabel-konvertering 053

Datum: 10 november 2026  
Resurs: `qgis-application`, språk `sv`  
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`  
Källkod: `src/analysis/processing/qgsalgorithmgpsbabeltools.cpp:91–121`

GPSBabels konverteringsverktyg granskas i samma kontext som batch 052.
Åtgärden använder QGIS etablerade GPS-termer från den lokala terminologin.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `This algorithm uses the GPSBabel tool to convert GPX features from one type to another (e.g. converting all waypoint features to a route feature).` | `Denna algoritm använder verktyget GPSBabel för att konvertera GPX-objekt från en typ till en annan (T.ex. konvertera alla waypoint-objekt till route-objekt).` | `Denna algoritm använder verktyget GPSBabel för att konvertera GPX-objekt från en typ till en annan, till exempel genom att konvertera alla brytpunktsobjekt till ett ruttobjekt.` |
| `Converts GPX features from one type to another.` | `Konvertera GPX-objekt från en typ till en annan.` | `Konverterar GPX-objekt från en typ till en annan.` |
| `Conversion command: ` | `Konverteringskommando:` | `Konverteringskommando: ` |
| `gps,tools,babel,tracks,waypoints,routes,gpx,import,export,export,device,serial` | `gps,verktyg,babel,tracks,waypoints,routes,gpx,importera,exportera,enhet,seriell` | `gps,verktyg,babel,spår,brytpunkter,rutter,gpx,importera,exportera,enhet,seriell` |

Kommandoetiketten ska ha ett avslutande blanksteg eftersom efterföljande
kommando visas direkt efter etiketten. Sökorden ska vara svenska sökord, medan
produktnamnet GPSBabel och formatnamnet GPX bevaras. Ingen extern ändring har
gjorts; Transifex-enheternas identifierare behöver hämtas från den aktuella
resursen innan en eventuell deltafil kan skapas.
