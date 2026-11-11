# QGIS: ST-DBSCAN-klustring 058

Datum: 10 november 2026  
Resurs: `qgis-application`, språk `sv`  
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`  
Källkod: `src/analysis/processing/qgsalgorithmstdbscanclustering.cpp`

ST-DBSCAN-algoritmens rubrik och två parametertexter granskas. Förkortningen
behålls, medan dess svenska sammansättning och tidsdimension förtydligas:

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `ST-DBSCAN clustering` | `ST-DBSCAN klustring` | `ST-DBSCAN-klustring` |
| `Clusters spatiotemporal point features using a time and density based scan algorithm.` | `Klustrar spatiotemporala punktobjekt med en tids- och densitetsbaserad skanningsalgoritm` | `Klustrar rumtidsbaserade punktobjekt med en skanningsalgoritm som baseras på tid och täthet.` |
| `Maximum time duration between clustered points` | `Största tidsavstånd mellan klustrade punkter` | `Längsta tidsintervall mellan klustrade punkter` |

`Tidsavstånd` ersätts eftersom parametern avser en tidslängd eller ett intervall,
inte ett avstånd. Ingen extern ändring har gjorts; Transifex-enheternas
identifierare behöver hämtas från den aktuella resursen innan en eventuell
deltafil kan skapas.
