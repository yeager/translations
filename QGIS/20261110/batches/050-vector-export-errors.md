# QGIS: feltexter vid vektorexport 050

Datum: 10 november 2026  
Resurs: `qgis-application`, språk `sv`  
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`  
Källkod: `src/core/qgsvectorfilewriter.cpp:3339` och `:4023`

Två feltexter från samma vektorexportör har en svensk form som döljer
handlingen eller saknar finit verb:

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Feature geometry failed to transform` | `Objektets geometri misslyckades att transformeras` | `Det gick inte att transformera objektets geometri.` |
| `Only %1 of %2 features written.` | `Endast %1 av %2 objekt skrivna.` | `Endast %1 av %2 objekt har skrivits.` |

Den första översättningen förklarar tydligt att transformeringen misslyckades,
utan att låta geometrin utföra handlingen. Den andra behåller Qt-platshållarna
`%1` och `%2` samt återställer svensk satsgrammatik. Ingen extern ändring har
gjorts; Transifex-enheternas identifierare behöver hämtas från den aktuella
resursen innan en eventuell deltafil kan skapas.
