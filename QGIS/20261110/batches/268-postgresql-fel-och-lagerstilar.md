# QGIS: PostgreSQL-fel och lagerstilar 268

Datum: 11 november 2026
Resurs: `qgis-application`, språk `sv`
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen granskar PostgreSQL-providerns fel vid markörhämtning, borttagning och
lagerstilar. `PostgreSQL`, `SQL`, `layer_styles`, `SELECT` och platshållarna
bevaras. Radbrytningar i tre felmeddelanden ska bevaras vid senare import.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `no result buffer` | `ingen resultatbuffer` | `Ingen resultatbuffert.` |
| `Fetching from cursor %1 failed\nDatabase error: %2` | `Hämtning från %1 misslyckades\nDatabasfel: %2` | `Det gick inte att hämta från markören %1.\nDatabasfel: %2` |
| `Unable to delete layer %1: \n%2` | `Kan inte radera lager %1:\n%2` | `Det gick inte att ta bort lagret %1:\n%2` |
| `Unable to delete schema %1: \n%2` | `Kan inte radera schema %1: \n%2` | `Det gick inte att ta bort schemat %1:\n%2` |
| `Unable to delete view %1: \n%2` | `Kan inte radera vy %1: \n%2` | `Det gick inte att ta bort vyn %1:\n%2` |
| `Creation of fields failed:\n%1` | `Skapandet av fält misslyckades:\n%1` | `Det gick inte att skapa fälten:\n%1` |
| `Connection to database failed using username: %1` | `Anslutning till databas misslyckades med användarnamn: %1` | `Databasanslutningen misslyckades med användarnamnet %1.` |
| `Error executing query: %1` | `Fel vid körning av fråga: %1` | `Fel när frågan kördes: %1` |
| `Save style in database` | `Spara stil i databas` | `Spara stilen i databasen` |

Ingen extern ändring har gjorts. De rekommenderade texterna är lokala
kandidater tills de har jämförts mot aktuella Transifex-enheter vid en senare
uppladdning. Ändringarna är lokalt granskade och inte skickade externt.
