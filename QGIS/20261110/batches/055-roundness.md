# QGIS: rundhet 055

Datum: 10 november 2026  
Resurs: `qgis-application`, språk `sv`  
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`  
Källkod: `src/analysis/processing/qgsalgorithmroundness.cpp:60`

Algoritmbeskrivningen för polygoners rundhet har stavfelet `mellen` och flera
onödigt tunga upprepningar. Den rekommenderade texten anger dessutom tydligt
att värdet lagras i det nya fältet:

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Calculates the roundness of each feature and stores it as a new field. The input vector layer must contain polygons.\n\nThe roundness of a polygon is defined as 4π × polygon area / perimeter². The roundness value varies between 0 and 1. A perfect circle has a roundness of 1, while a completely flat polygon has a roundness of 0.` | `Beräknar rundheten på varje objekt och sparar den i ett nytt fält. Indatalagret måste innehålla polygoner.\n\nRundheten av en polygon definieras som 4π × polygonarean / omkretsen². Värdet på rundheten varierar mellen 0 och 1. En perfekt cirkel har rundheten 1 medan en helt platt polygon har rundheten 0.` | `Beräknar rundheten för varje objekt och sparar värdet i ett nytt fält. Indatalagret måste innehålla polygoner.\n\nEn polygons rundhet definieras som 4π × polygonens area / omkrets². Rundhetsvärdet varierar mellan 0 och 1. En perfekt cirkel har rundhetsvärdet 1, medan en helt platt polygon har rundhetsvärdet 0.` |

Formeln, symbolerna `π` och `²` samt den obligatoriska radbrytningen bevaras.
Ingen extern ändring har gjorts; Transifex-enhetens identifierare behöver
hämtas från den aktuella resursen innan en eventuell deltafil kan skapas.
