# QGIS: MSSQL-laddning och stilfel 261

Datum: 11 november 2026
Resurs: `qgis-application`, språk `sv`
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen granskar feltexter från Microsoft SQL Server-datakällan. `MSSQL` och
det tekniska tabellnamnet `layer_styles` bevaras, medan `provider` återges som
datakälla enligt QGIS-terminologin.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Loading of the MSSQL provider failed` | `Laddning av MSSQL-datapluginet misslyckades` | `MSSQL-datakällan kunde inte läsas in.` |
| `Error connecting to database: %1` | `Fel vid anslutning till databas: %1` | `Fel vid anslutning till databasen: %1` |
| `Could not check if layer_styles table exists: %1` | `Kunde inte kontrollera om tabell layer_styles finns: %1` | `Det gick inte att kontrollera om tabellen layer_styles finns: %1` |
| `Checking for style failed: %1` | `Sökandet efter stil misslyckades: %1` | `Det gick inte att kontrollera stilen: %1` |
| `Unsupported type for field %1` | `Fälttyp för fält %1 ej stödd` | `Fälttypen för fältet %1 stöds inte.` |

Ingen extern ändring har gjorts. De rekommenderade texterna är lokala
kandidater tills de har jämförts mot aktuella Transifex-enheter vid en senare
uppladdning. Ändringarna är lokalt granskade och inte skickade externt.
