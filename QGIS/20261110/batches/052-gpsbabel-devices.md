# QGIS: GPSBabel-enheter och GPX-objekt 052

Datum: 10 november 2026  
Resurs: `qgis-application`, språk `sv`  
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`  
Källkod: `src/analysis/processing/qgsalgorithmgpsbabeltools.cpp`

GPSBabel-algoritmerna använder redan QGIS svenska benämningar *brytpunkt*,
*rutt* och *spår* i sina parameteretiketter. Felmeddelanden och kommandoetiketter
har däremot engelska rester, böjningsfel och förlorade avslutande blanksteg.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Unknown GPSBabel device “%1”. Valid devices are: %2` | `Okänt GPSBabel-ehet "%1". Giltiga enheter är: %2` | `Okänd GPSBabel-enhet ”%1”. Giltiga enheter är: %2` |
| `Unknown port “%1”. Valid ports are: %2` | `Okänt port "%1". Giltiga portar är: %2` | `Okänd port ”%1”. Giltiga portar är: %2` |
| `Download command: ` | `Kommando för nerladdning` | `Nedladdningskommando: ` |
| `Upload GPS data to device` | `Ladda upp GPS-data till enhet` | `Ladda upp GPS-data till en GPS-enhet` |
| `The GPSBabel format “%1” does not support waypoints.` | `GPSBabel-formatet "%1" stödjer inte waypoints.` | `GPSBabel-formatet ”%1” stöder inte brytpunkter.` |
| `The GPSBabel format “%1” does not support routes.` | `GPSBabel-formatet "%1" stödjer inte routes.` | `GPSBabel-formatet ”%1” stöder inte rutter.` |
| `The GPSBabel format “%1” does not support tracks.` | `GPSBabel-formatet "%1" stödjer inte tracks.` | `GPSBabel-formatet ”%1” stöder inte spår.` |
| `Upload command: ` | `Kommando för uppladdning` | `Uppladdningskommando: ` |

Kommandoetiketterna ska innehålla ett avslutande blanksteg precis som
källsträngarna; det måste bevaras i en framtida deltafil även om Markdown-tabellen
inte kan göra det synligt. Produktnamnet GPSBabel och platshållarna `%1` och
`%2` bevaras. Ingen extern ändring har gjorts; Transifex-enheternas
identifierare behöver hämtas från den aktuella resursen innan en eventuell
deltafil kan skapas.
