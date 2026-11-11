# QGIS: OGR-feltexter och metadata 264

Datum: 11 november 2026
Resurs: `qgis-application`, språk `sv`
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen granskar OGR-providerns felkategorier, metadata och filgränser.
Kommandot `ulimit -n number_of_files`, XML och SRS bevaras som tekniska namn.
`URI` behandlas som en identifierare och skrivs med versaler i svensk text.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Too many files opened (%1). Cannot open %2. You may raise the limit with the 'ulimit -n number_of_files' command before starting QGIS.` | `För många filer öppna (%1). Kan inte öppna %2. Du kan öka gränsen med kommandot "ulimit -n number_of_files" innan du startar QGIS.` | `För många filer är öppna (%1). Det gick inte att öppna %2. Du kan höja gränsen med kommandot 'ulimit -n number_of_files' innan QGIS startas.` |
| `Too many files opened (%1). Cannot open %2` | `För många filer öppna (%1). Kan inte öppna %2` | `För många filer är öppna (%1). Det gick inte att öppna %2.` |
| `Error updating style` | `Fel vid uppdatering av stil` | `Det gick inte att uppdatera stilen.` |
| `Invalid style identifier` | `Otillåten lageridentifierare` | `Ogiltig stilidentifierare.` |
| `No style corresponding to style identifier` | `Ingen stil överensstämmer med stilidentifieraren` | `Det finns ingen stil som motsvarar stilidentifieraren.` |
| `Storing metadata for the specified uri is not supported` | `Att spara metadata till den angivna uri stöds inte` | `Det går inte att lagra metadata för den angivna URI:en.` |
| `Not enough data to deserialize` | `Inte tillräckligt med data för avserialisering` | `För lite data för avserialisering.` |
| `Unsupported operation` | `Operationen stöds ej` | `Åtgärden stöds inte.` |
| `Corrupt data` | `Korrupt data` | `Skadade data.` |
| `Failure` | `Misslyckades` | `Fel` |
| `Unsupported SRS` | `Vald SRS stöds ej` | `SRS stöds inte.` |

Ingen extern ändring har gjorts. De rekommenderade texterna är lokala
kandidater tills de har jämförts mot aktuella Transifex-enheter vid en senare
uppladdning. Ändringarna är lokalt granskade och inte skickade externt.
