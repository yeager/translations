# QGIS: kortaste linjer 057

Datum: 10 november 2026  
Resurs: `qgis-application`, språk `sv`  
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`  
Källkod: `src/analysis/processing/qgsalgorithmshortestline.cpp`

Hjälptexten för kortaste linjer blandar ihop källager, objekt och
koordinatsystem samt använder engelsknära ordföljd. Texten och två tillhörande
UI-strängar granskas tillsammans:

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `This algorithm creates a line layer as the shortest line between the source and the destination layer. …` | `Denna algoritm skapar ett linjelager som den kortaste linjen mellan käll- och mållager. …` | `Denna algoritm skapar ett linjelager med de kortaste linjerna mellan käll- och mållagret. …` |
| `Maximum number of neighbors` | `Störst antal grannar` | `Maximalt antal grannar` |
| `An error occurred while calculating shortest line length` | `Ett fel inträffade när kortaste linjelängd beräknades` | `Ett fel inträffade när längden på den kortaste linjen beräknades` |

Den fullständiga rekommenderade hjälptesten är:

```text
Denna algoritm skapar ett linjelager med de kortaste linjerna mellan käll- och mållagret. Som standard tas endast det närmaste objektet i mållagret med. Antalet närmaste grannobjekt kan anges.

Om ett maximalt avstånd anges beaktas endast objekt som ligger närmare än detta avstånd.

Utdatan innehåller alla attribut från källagret, alla attribut från vart och ett av de närmaste grannobjekten samt ett ytterligare avståndsfält.

Denna algoritm använder enbart kartesiska avståndsberäkningar och beaktar inte geodetiska eller ellipsoida egenskaper vid beräkningen av närhet mellan objekt. Koordinatsystemet för mätning och utdata baseras på källagrets koordinatsystem.
```

Alla tre radbrytningarna ska bevaras vid en framtida uppladdning. Ingen extern
ändring har gjorts; Transifex-enheternas identifierare behöver hämtas från den
aktuella resursen innan en eventuell deltafil kan skapas.
