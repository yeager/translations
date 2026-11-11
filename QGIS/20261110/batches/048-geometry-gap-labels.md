# QGIS: glappetiketter och sökord 048

Datum: 10 november 2026  
Resurs: `qgis-application`, språk `sv`  
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`  
Källkod: `src/analysis/processing/qgsalgorithmcheckgeometrygap.cpp` och
`src/analysis/processing/qgsalgorithmfixgeometrygap.cpp`

Den lokala terminologin från batch 047 tillämpas också på komponentens korta
etiketter. Bindestrecken i de befintliga formerna är inte motiverade av någon
egennamns- eller läsbarhetsregel; sammansättningarna skrivs ihop.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Gap errors` | `Glapp-fel` | `Glappfel` |
| `Gap features` | `Glapp-objekt` | `Glappobjekt` |
| `fix,fill,gap` | `fix,fyll,glapp` | `åtgärda,fyll,glapp` |

Sökordet `fix` ska vara svenskt eftersom det visas i QGIS egna
algoritmsökning. Ingen extern ändring har gjorts; Transifex-enheternas
identifierare behöver hämtas från den aktuella resursen innan en eventuell
deltafil kan skapas.
