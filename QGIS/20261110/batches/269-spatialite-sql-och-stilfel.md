# QGIS: SpatiaLite-SQL och stilfel 269

Datum: 11 november 2026
Resurs: `qgis-application`, språk `sv`
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen granskar SpatiaLite-providerns SQL-, metadata- och stilfel samt två
återanvända OGR-fel. `SpatiaLite`, `SpatialMetadata`, `SQL`, `URI`,
filändelser och platshållare bevaras. Rader med avslutande radbrytning ska
bevaras exakt vid senare import.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Error executing query %1: %2` | `Fel vid körning av fråga %1: %2` | `Fel när frågan %1 kördes: %2` |
| `Unable to initialize SpatialMetadata:\n` | `Kan inte initialisera SpatialMetadata:\n` | `Det gick inte att initiera SpatialMetadata:\n` |
| `Could not create a new database\n` | `Kunde inte skapa en ny databas\n` | `Det gick inte att skapa en ny databas\n` |
| `Unable to delete table %1\n` | `Kan inte radera tabell %1\n` | `Det gick inte att ta bort tabellen %1\n` |
| `Style with id %1 not found in %2 (Query: %3)` | `Stil med id %1 kunde inte hittas i %2 (Fråga: %3)` | `Stilen med ID %1 hittades inte i %2 (fråga: %3).` |
| `Error looking for style. The query was logged` | `Fel vid sökning efter stil- Frågan loggades` | `Fel vid sökning efter stil. Frågan loggades.` |
| `Unable to save layer style. It's not possible to create the destination table on the database.` | `Kan inte spara lagerstil. Det är inte möjligt att skapa tabellen i databasen.` | `Det gick inte att spara lagerstilen. Det går inte att skapa måltabellen i databasen.` |
| `URI %1 doesn't end with .shp or .dbf` | `URI %1 slutar inte med .shp eller .dbf` | `URI:en %1 slutar inte med .shp eller .dbf.` |
| `Cannot find layer %1.` | `Kan inte hitta lager %1.` | `Det gick inte att hitta lagret %1.` |
| `Cannot open %1 (%2).` | `Kan inte öppna %1 (%2).` | `Det gick inte att öppna %1 (%2).` |

Ingen extern ändring har gjorts. De rekommenderade texterna är lokala
kandidater tills de har jämförts mot aktuella Transifex-enheter vid en senare
uppladdning. Ändringarna är lokalt granskade och inte skickade externt.
