# QGIS: OGR-datakälla och drivrutin 263

Datum: 11 november 2026
Resurs: `qgis-application`, språk `sv`
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen granskar OGR-providerns skapande- och formattexter. `OGR`, `OGDI`,
`MapInfo` och fältnamnet `overwrite` är tekniska namn. Här avser `driver` en
formatdrivrutin och blir därför `drivrutin`, inte `dataplugin`.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Unable to create the datasource. %1 exists and overwrite flag is false.` | `Kan inte skapa datakällan. %1 existerar och överskrivningsflaggan är satt till nej.` | `Det gick inte att skapa datakällan. %1 finns redan och överskrivningsflaggan är falsk.` |
| `Unable to get driver %1` | `Kan inte hämta dataplugin %1` | `Det gick inte att hämta drivrutinen %1.` |
| `Layer %2 of %1 exists and overwrite flag is false.` | `Lager %2 av %1 finns redan och överskrivningsflaggan är satt till nej.` | `Lager %2 i %1 finns redan och överskrivningsflaggan är falsk.` |
| `Mapinfo File` | `Mapinfo File` | `MapInfo-fil` |
| `OGDI Vectors` | `OGDI Vectors` | `OGDI-vektorer` |

Ingen extern ändring har gjorts. De rekommenderade texterna är lokala
kandidater tills de har jämförts mot aktuella Transifex-enheter vid en senare
uppladdning. Ändringarna är lokalt granskade och inte skickade externt.
