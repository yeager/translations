# QGIS: datakälle- och importdialoger 064

Datum: 10 november 2026  
Resurs: `qgis-application`, språk `sv`  
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`  
Källkod: `src/gui/qgsdataitemguiproviderutils.cpp` och
`src/providers/hana/qgshanaprimarykeys.cpp`

Felen finns i bekräftelse- och felmeddelanden för datakällor, import och
databasvyer. Formuleringarna görs idiomatiska med korrekt bestämd form, utan
att ändra fråga, felallvar eller tekniska beteckningar.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Are you sure you want to remove the connection to “%1”?` | `Är du säker att du vill ta bort anslutningen till "%1"?` | `Är du säker på att du vill ta bort anslutningen till "%1"?` |
| `Are you sure you want to remove the connection to %1?` | `Är du säker att du vill ta bort anslutningen till %1?` | `Är du säker på att du vill ta bort anslutningen till %1?` |
| `Import failed.` | `Import misslyckades.` | `Importen misslyckades.` |
| `Failed to set new table comment!\n\n` | `Misslyckades att lagra tabellkommentar\n\n` | `Det gick inte att ange den nya tabellkommentaren!\n\n` |
| `Failed to import layer!\n\n` | `Kunde inte importera lager!\n\n` | `Det gick inte att importera lagret!\n\n` |
| `Key field '%1' for view/query not found.` | `Nyckelfält '%1' för visning/fråga ej funnet.` | `Nyckelfältet '%1' för vyn/frågan hittades inte.` |
| `Keys for view/query undefined. Some functionality might not be available.` | `Nycklar för vy/fråga odefinierade. Viss funktionalitet kanske inte är tillgänglig.` | `Nycklar för vyn/frågan är inte definierade. Viss funktionalitet kanske inte är tillgänglig.` |
| `No key field for view/query given.` | `Inget nyckelfält för visning/fråga angivet.` | `Inget nyckelfält för vyn/frågan har angetts.` |

De två avslutande radbrytningarna i båda importfelen och platshållaren `%1`
bevaras exakt. Ingen extern ändring har gjorts; aktuella
Transifex-enhetsidentifierare behöver hämtas innan en deltafil kan skapas.
