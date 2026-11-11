# QGIS: export to spreadsheet 045

Datum: 10 november 2026  
Resurs: `qgis-application`, språk `sv`  
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`, rad 22981  
Källkod: `src/analysis/processing/qgsalgorithmexporttospreadsheet.cpp:137`

Beskrivningen av geobearbetningsalgoritmen granskades tillsammans med den
kortare beskrivningen på raden efter. Den befintliga texten har två tydliga
grammatikfel: `exportera` saknar finit verbform och `till till` är en oavsiktlig
upprepning.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `This algorithm collects a number of existing layers and exports them to a spreadsheet document.\n\nOptionally the layers can be appended to an existing spreadsheet as additional sheets.\n\n` | `Denna algoritm samlar ett antal befintliga lager och exportera dem till ett kalkylarks-dokument.\n\nDet går att välja om lagren ska läggas till till ett befintligt kalkylark som extra blad.\n\n` | `Algoritmen samlar ett antal befintliga lager och exporterar dem till ett kalkylbladsdokument.\n\nLagren kan även läggas till som ytterligare blad i ett befintligt kalkylark.\n\n` |

Rättningen bevarar de två avslutande radbrytningarna, använder QGIS-termerna
*lager*, *exportera* och *befintlig* och följer den närliggande, redan korrekta
korttexten. Ingen extern ändring har gjorts; Transifex-enhetens identifierare
måste hämtas från den aktuella resursen innan en eventuell uppladdningsbatch
kan skapas.
