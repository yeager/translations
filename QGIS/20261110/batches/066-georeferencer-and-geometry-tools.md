# QGIS: georefererare och geometriverktyg 066

Datum: 10 november 2026  
Resurs: `qgis-application`, språk `sv`  
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`  
Källkod: `src/core/actions/qgsaction.cpp`,
`src/analysis/georeferencing/qgsvectorwarper.cpp`,
`src/app/georeferencer/qgstransformsettingsdialog.cpp`,
`src/app/maptools/qgsmaptoolshapeellipsefoci.cpp` och
`src/core/proj/qgscoordinatereferencesystemutils.cpp`

Batchen rättar en versal i produktnamnet Python, två inställningsetiketter för
georefereraren, en geometrisk fackterm och österförkortningen i CRS-axlar.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Generic Python` | `Generisk python` | `Generisk Python` |
| `Last used folder for georeferencer destination files` | `Senast använda mapp för målfiler till georefereraren` | `Senast använda mapp för georefererarens målfiler` |
| `Last used folder for georeferencer PDF report files` | `Senast använda mapp för pdf-rapporer till georefereraren` | `Senast använda mapp för georefererarens PDF-rapportfiler` |
| `Ellipse from Foci` | `Ellips från foci` | `Ellips från brännpunkter` |
| Axeln `E` | `ÖÖ` | `Ö` |

`E` är den engelska förkortningen för öster och måste motsvaras av den svenska
förkortningen `Ö`; `ÖÖ` betyder inte öster. Ingen extern ändring har gjorts;
aktuella Transifex-enhetsidentifierare behöver hämtas innan en deltafil kan
skapas.
