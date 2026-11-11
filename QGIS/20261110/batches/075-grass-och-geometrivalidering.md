# QGIS: GRASS och geometrivalidering 075

Datum: 10 november 2026  
Resurs: `qgis-application`, språk `sv`  
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen omfattar GRASS-parametrar och GEOS valideringsfel. Kommandon och
parameteridentifierare som `r.external`, `r.in.gdal`, `x_radius` och `y_radius`
bevaras. Termerna **ring** och **topologi** följer QGIS-terminologin.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Could not open GRASS algorithm: {0}` | `Kunde inte öppna GRASS-algoritm: {0}` | `Kunde inte öppna GRASS-algoritmen: {0}` |
| `Could not open GRASS algorithm: {0}\n{1}` | `Kunde inte öppna GRASS algoritm: {0}\n{1}` | `Kunde inte öppna GRASS-algoritmen: {0}\n{1}` |
| `You need to set either radius or x_radius and y_radius!` | `Du måste ange antingen radius eller x_radius och y_radius!` | `Du måste ange antingen radie eller x_radius och y_radius!` |
| `The start position must be inferior to the end position!` | `Startpositionen måste vara sämre än slutpositionen!` | `Startpositionen måste vara mindre än slutpositionen!` |
| `You can't use original Hargreaves flag and precipitation parameter together!` | `Du kan inte använda Hargreaves originalflagga och utskiljningsparameter tillsammans!` | `Du kan inte använda Hargreaves ursprungliga flagga och nederbördsparametern samtidigt!` |
| `For raster layers, use r.external (faster) instead of r.in.gdal` | `Använd r.external för rasterlager (snabbare) istället för r.in.gdal` | `Använd r.external för rasterlager (snabbare) i stället för r.in.gdal` |
| `For vector layers, use v.external (faster) instead of v.in.ogr` | `För vektorlager, använd v.external (snabbare) istället för v.in.ogr` | `Använd v.external för vektorlager (snabbare) i stället för v.in.ogr` |
| `Hole lies outside shell` | `Hål ligger utanför ytterkant` | `Hålet ligger utanför den yttre ringen` |
| `Holes are nested` | `Hål ligger på varandra` | `Hålen är nästlade` |
| `Interior is disconnected` | `Innandömet är avskiljt` | `Det inre området är inte sammanhängande` |
| `Nested shells` | `Skal ligger på varandra` | `De yttre ringarna är nästlade` |

Ingen extern ändring har gjorts. Aktuella Transifex-enhetsidentifierare måste
hämtas innan en separat deltafil kan skapas.
