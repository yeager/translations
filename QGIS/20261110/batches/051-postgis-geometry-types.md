# QGIS: PostGIS och icke-linjära geometrityper 051

Datum: 10 november 2026  
Resurs: `qgis-application`, språk `sv`  
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`  
Källkod: `src/core/qgsvectorfilewriter.cpp:2809`

Inställningsbeskrivningen för PostGIS-export innehåller ett extra skiljetecken,
en felaktigt sammansatt term och en sats utan subjekt:

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Can be set to 2.0 or 2.2 for PostGIS 2.0/2.2 compatibility. Important to set it correctly if using non-linear geometry types` | `Kan ställas in till 2.0 eller 2.2. för kompatibilitet med PostGIS 2.0/2.2. Viktigt att ställa in rätt om icke-linjärageometri typer används` | `Kan ställas in på 2.0 eller 2.2 för kompatibilitet med PostGIS 2.0/2.2. Det är viktigt att ange rätt värde vid användning av icke-linjära geometrityper.` |

PostGIS och versionsnumren bevaras. `Icke-linjära geometrityper` följer svensk
avstavning och undviker den felaktiga formen `icke-linjärageometri typer`.
Ingen extern ändring har gjorts; Transifex-enhetens identifierare behöver
hämtas från den aktuella resursen innan en eventuell deltafil kan skapas.
