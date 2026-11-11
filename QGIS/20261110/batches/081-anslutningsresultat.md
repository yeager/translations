# QGIS: anslutningsresultat 081

Datum: 10 november 2026  
Resurs: `qgis-application`, språk `sv`  
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen granskar datakällors anslutningsresultat. Den skiljer ett misslyckat
anslutningsförsök från en avbruten anslutning, eftersom det är olika diagnoser.
Platshållarna `{0}`, `%1`, `%2` och `%3` bevaras.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `File {0} exists. Overwrite?` | `Filen {0} finns redan. Skriva över?` | `Filen {0} finns redan. Vill du skriva över den?` |
| `{0} exists.  Overwrite?` | `{0} finns redan. Skriva över?` | `{0} finns redan. Vill du skriva över den?` |
| `Connection {0} exists. Overwrite?` | `Anslutningen {0} finns redan. Skriva över?` | `Anslutningen {0} finns redan. Vill du skriva över den?` |
| `Connection to database failed` | `Anslutning till databas misslyckades` | `Databasanslutningen misslyckades.` |
| `Connection to database failed using username: %1` | `Anslutning till databas misslyckades med användarnamn: %1` | `Databasanslutningen misslyckades med användarnamnet %1.` |
| `Connection failed: %1` | `Anslutning misslyckades: %1` | `Anslutningen misslyckades: %1` |
| `Connection failed` | `Anslutningen avbröts` | `Anslutningen misslyckades` |
| `Connection to %1 was successful.` | `Anslutning till %1 lyckades.` | `Anslutningen till %1 lyckades.` |
| `Database connection was successful, but the accessible tables could not be determined.` | `Databasanslutningen lyckades, men anslutningsbara tabeller kunde inte bestämmas.` | `Databasanslutningen lyckades, men det gick inte att avgöra vilka tabeller som är åtkomliga.` |
| `Connection failed %1s ago - skipping retry` | `Anslutning misslyckades efter %1 s - skippar nya försök` | `Anslutningen misslyckades för %1 s sedan; nytt försök hoppas över.` |
| `Connection failed - consult message log for details.` | `Anslutning misslyckades - se meddelandelogg för detaljer.` | `Anslutningen misslyckades. Läs meddelandeloggen för detaljer.` |
| `Connection error: %1 returned %2 [%3]` | `Anslutningsfel: %1 returnerade %2 [%3]` | `Anslutningsfel: %1 returnerade %2 [%3]` |

Den sista raden är granskad utan ändring för att bekräfta att samtliga
platshållare och den tekniska felinformationen redan är korrekt bevarade.
Ingen extern ändring har gjorts. Aktuella Transifex-enhetsidentifierare måste
hämtas innan en separat deltafil kan skapas.
