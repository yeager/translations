# QGIS: standardvärden för layout 059

Datum: 10 november 2026  
Resurs: `qgis-application`, språk `sv`  
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`  
Källkod: `src/core/layout/qgslayout.cpp`

Två inställningar anger standardvärden för nya layouter. Den befintliga svenska
texten gör den första sammansättningen felaktigt till två ord och den andra
kan läsas som en katalog med flera SVG-norrpilar, inte som en sökväg till den
SVG-fil som används som nordpil.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Default font family for new layout items` | `Standard typsnittsfamilj för nya layoutelement` | `Typsnittsfamilj som används som standard för nya layoutelement` |
| `Default north arrow SVG path` | `Standardsökväg för SVG-norrpilar` | `Standardsökväg till SVG-filen för nordpil` |

`Typsnittsfamilj` följer de befintliga QGIS-etiketterna för `Font family`.
`Nordpil` är QGIS etablerade term för kartelementet, och `SVG` behålls som
formatnamn. Ingen extern ändring har gjorts; Transifex-enheternas identifierare
behöver hämtas från den aktuella resursen innan en eventuell deltafil kan
skapas.
