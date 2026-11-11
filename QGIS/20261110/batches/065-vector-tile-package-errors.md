# QGIS: fel vid läsning av vektorrutepaket 065

Datum: 10 november 2026  
Resurs: `qgis-application`, språk `sv`  
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`  
Källkod: `src/core/vectortile/qgsvtpktiles.cpp`

Strängarna visas när QGIS läser ett vektorrutepaket. Den befintliga svenska
texten ersätter felaktigt en stildefinition med en lagerdefinitionsfil och
lämnar `tile` samt `bundle` oöversatta. `sprite` behålls som det tekniska
namnet i vektorrutestilens format.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Error reading style definition: '%1'` | `Fel vid läsning av lagerdefinitionsfil: "%1"` | `Fel vid läsning av stildefinition: "%1"` |
| `Error reading sprite definition: '%1'` | `Fel vid läsning av definition för "sprite": "%1"` | `Fel vid läsning av sprite-definition: "%1"` |
| `Error reading sprite image: '%1'` | `Fel vid läsning av bild för "sprite": "%1"` | `Fel vid läsning av spritebild: "%1"` |
| `Error extracting bundle contents as gzip: %1` | `Fel vid extrahering av bundle-innehåll som gzip: %1` | `Fel vid extrahering av paketinnehåll som gzip: %1` |
| `Error reading tile: '%1'` | `Fel vid läsning av tile: '%1'` | `Fel vid läsning av ruta: '%1'` |

Platshållaren `%1`, citattecknen i de berörda källsträngarna och formatnamnet
`gzip` bevaras. Ingen extern ändring har gjorts; aktuella
Transifex-enhetsidentifierare behöver hämtas innan en deltafil kan skapas.
