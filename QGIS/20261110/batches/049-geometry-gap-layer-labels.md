# QGIS: lageretiketter för glapp 049

Datum: 10 november 2026  
Resurs: `qgis-application`, språk `sv`  
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`  
Källkod: `src/analysis/processing/qgsalgorithmcheckgeometrygap.cpp` och
`src/analysis/processing/qgsalgorithmfixgeometrygap.cpp`

Två lageretiketter i samma arbetsflöde granskas tillsammans:

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Neighbors layer` | `Lager för grannar` | `Grannlager` |
| `Gaps-filled layer` | `Glappfyllt lager` | `Lager med fyllda glapp` |

`Grannlager` följer den redan använda QGIS-formen `Glapplager`. Den andra
etiketten beskriver resultatlagret tydligt utan den svårtolkade sammansättningen
`glappfyllt`. Ingen extern ändring har gjorts; Transifex-enheternas
identifierare behöver hämtas från den aktuella resursen innan en eventuell
deltafil kan skapas.
