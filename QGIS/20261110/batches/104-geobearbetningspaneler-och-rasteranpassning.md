# QGIS: geobearbetningspaneler och rasteranpassning 104

Datum: 10 november 2026  
Resurs: `qgis-application`, språk `sv`  
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen granskar geobearbetningspaneler och rasteranpassning. `qgis_process`,
JSON, Python, HTML och färgvärdena bevaras. I interpoleringsvalen används
matematiska namn som B-spline och Lanczos, medan `kernel` översätts som kärna.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Current settings cannot be specified as arguments to qgis_process (Pipe parameters as JSON to qgis_process instead)` | `Aktuella inställningar kan inte användas som argument för qgis_process ("Pipe":a parametrar som JSON till qgis_process istället)` | `De aktuella inställningarna kan inte anges som argument till qgis_process. Skicka i stället parametrarna som JSON till qgis_process via standardindata.` |
| `Message log truncated` | `Meddelandelogg tömd` | `Meddelandeloggen har trunkerats` |
| `Bilinear (2x2 Kernel)` | `Bilinjär (2x2 kernel)` | `Bilinjär (2x2-kärna)` |
| `Cubic (4x4 Kernel)` | `Kubisk (4x4 kernel)` | `Kubisk (4x4-kärna)` |
| `Cubic B-Spline (4x4 Kernel)` | `Kubisk B-Kurva (4x4 kernel)` | `Kubisk B-spline (4x4-kärna)` |
| `Lanczos (6x6 Kernel)` | `Lanczos (6x6 kernel)` | `Lanczos (6x6-kärna)` |
| `Area is in geographic degrees. Consider reprojecting to a projected local coordinate system for accurate results.` | `Area är i grader. Överväg att transformera ditt lager till ett projicerat referenskoordinatsystem för mer exakta resultat.` | `Arealen anges i geografiska grader. Överväg att projicera om lagret till ett projicerat lokalt koordinatreferenssystem för att få exakta resultat.` |
| `Algorithm %1 correctly executed…` | `Algoritm %1 exekverades korrekt…` | `Algoritmen %1 slutfördes korrekt…` |
| `Execution completed in %1 seconds` | `Beräkningen utfördes på %1 sekunder` | `Körningen slutfördes på %1 sekunder` |
| `Batch execution completed in %1 seconds` | `Batchbearbetning utfördes på %1 sekunder` | `Batchbearbetningen slutfördes på %1 sekunder` |
| `Warning: This algorithm is a potential security risk if executed with unchecked inputs, and may result in system damage or data leaks.` | `Varning: Denna algoritm är en potentiell säkerhetsrisk om den körs med okontrollerad indata och kan resultera i systemskada eller dataläckor.` | `Varning: Den här algoritmen kan innebära en säkerhetsrisk om den körs med okontrollerade indata och kan orsaka systemskador eller dataläckor.` |
| `color style string, e.g. #ff0000 or 255,0,0` | `färgkod som text, t.ex. #ff0000 or 255,0,0` | `Färgsträng, till exempel #ff0000 eller 255,0,0` |
| `Environment Settings` | `Mijöinställningar` | `Miljöinställningar` |

Ingen extern ändring har gjorts. Aktuella Transifex-enhetsidentifierare måste
hämtas och måltexterna jämföras före en separat deltafil kan skapas.
