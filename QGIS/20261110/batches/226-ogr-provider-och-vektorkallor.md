# QGIS: OGR-provider och vektorkällor 226

Datum: 11 november 2026
Resurs: `qgis-application`, språk `sv`
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen granskar OGR-providerns felmeddelanden och dialogen för att välja
vektorkälla. OGR, GPKG, WKB, SQL, SQLite och URI är tekniska namn och lämnas
oförändrade.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `GPKG error searching for unique constraints on fields for table %1. (%2)` | `GPK-fel vid sökande efter unika begränsningar på fält i tabellen %1. (%2)` | `GPKG-fel vid sökning efter unika begränsningar för fält i tabellen %1. (%2)` |
| `Error retrieving next sequence value for %1` | `Fel vid hämtning av nästa värde i sekvens för %1` | `Fel vid hämtning av nästa sekvensvärde för %1` |
| `Feature has too many attributes (expecting %1, received %2)` | `Objektet har för många attribut (förväntade %1, tog emot %2)` | `Objektet har för många attribut (förväntar %1, tog emot %2)` |
| `wrong value for attribute %1 of feature %2: %3` | `fel värde på attribut %1 för objekt %2: %3` | `Fel värde för attribut %1 i objekt %2: %3` |
| `type %1 for attribute %2 not found` | `hittade ej typ %1 för attribut %2` | `Typen %1 för attributet %2 hittades inte` |
| `wrong data type for attribute %1 of feature %2: %3` | `fel datatyp på attribut %1 för objekt %2: %3` | `Fel datatyp för attribut %1 i objekt %2: %3` |
| `%1 query` | `%1 fråga` | `%1-fråga` |
| `wrong data type for attribute %1 of feature %2: Got %3, expected %4` | `fel datatyp på attribut %1 för objekt %2: Fick %3, förväntade %4` | `Fel datatyp för attribut %1 i objekt %2: fick %3, förväntade %4` |
| `type %1 for field %2 not found` | `hittade ej typ %1 för fält %2` | `Typen %1 för fältet %2 hittades inte` |
| `Cannot delete feature id column` | `Kan inte radera objekt-id kolumn` | `Det går inte att ta bort objekt-ID-kolumnen` |
| `OGR error renaming field %1: %2` | `OGR fel vid omdöpning av fält %1: %2` | `OGR-fel vid omdöpning av fält %1: %2` |
| `OGR error rolling back transaction: %1` | `OGR fel vid återställande av transaktion: %1` | `OGR-fel vid återställning av transaktionen: %1` |
| `Feature %1 for attribute update not found.` | `Hittade inte objekt %1 för attributuppdatering` | `Objekt %1 för attributuppdatering hittades inte.` |
| `Field %1 of feature %2 doesn't exist.` | `Fält %1 på objekt %2 existerar inte.` | `Fält %1 i objekt %2 finns inte.` |
| `OGR error setting feature %1: %2` | `OGR-fel vid skapande av objekt %1: %2` | `OGR-fel vid inställning av objekt %1: %2` |
| `OGR error setting geometry of feature %1: %2` | `OGR-fel vid skapande av geometri för objekt %1: %2` | `OGR-fel vid inställning av geometrin för objekt %1: %2` |
| `Possible corruption after REPACK detected. %1 still exists. This may point to a permission or locking problem of the original DBF.` | `Möjligt korrupt data efter REPACK upptäckt. %1 existerar fortfarande. Detta kan bero på ett rättighets- eller låsproblem med orginal-DBF-filen.` | `Möjliga skadade data efter REPACK har upptäckts. %1 finns fortfarande kvar. Det kan tyda på ett behörighets- eller låsproblem med den ursprungliga DBF-filen.` |
| `Original layer could not be reopened.` | `Orginallager kunde inte återöppnas.` | `Det ursprungliga lagret kunde inte öppnas igen.` |
| `OGR driver for '%1' not found (OGR error: %2)` | `OGR-drivrutinför '%1' hittades inte (OGR fel: %2)` | `OGR-drivrutinen för '%1' hittades inte (OGR-fel: %2)` |
| `ERROR: Failed to created default metadata file as %1. Check file permissions and retry.` | `FEL: Kunde inte skapa förvald metadatafil %1. Kontrollera filrättigheter och försök igen.` | `FEL: Det gick inte att skapa standardmetadatafilen %1. Kontrollera filbehörigheterna och försök igen.` |
| `Open OGR Supported Vector Dataset(s)` | `Öppna OGR Standardiserat Vektordataset` | `Öppna vektordatamängd(er) som stöds av OGR` |
| `Open an OGR Supported Vector Layer` | `Öppna ett vektorlager som OGR stödjer` | `Öppna ett vektorlager som stöds av OGR` |
| `Vector Dataset(s)` | `Vektordataset` | `Vektordatamängd(er)` |
| `No protocol URI entered.` | `Ingen protokoll-URI inskrivet.` | `Ingen protokoll-URI har angetts.` |
| `Protocol: HTTP(S), cloud, etc.` | `Protokoll: HTTP(S), cloud, etc.` | `Protokoll: HTTP(S), moln osv.` |
| `Authentication` | `Verifiering` | `Autentisering` |
| `Credential Options` | `Legitimeringsalternativ` | `Inloggningsalternativ` |
| `Consult <a href="%1">%2 driver help page</a> for detailed explanations on options` | `Titta på <a href="%1">%2 drivrutinens hjälpsida</a>ör detaljerad förklaring av alternativen` | `Se <a href="%1">hjälpsidan för drivrutinen %2</a> för detaljerade förklaringar av alternativen` |

Platshållarna `%1`, `%2`, `%3` och `%4` samt markupen i hjälplänken ska
bevaras oförändrade vid senare import. Ingen extern ändring har gjorts.
