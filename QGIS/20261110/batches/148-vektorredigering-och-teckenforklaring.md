# QGIS: vektorredigering och teckenförklaring 148

Datum: 10 november 2026
Resurs: `qgis-application`, språk `sv`
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen granskar vektorlagers redigeringsbufferter, transaktioner och
teckenförklaringar. Platshållarna `%1`, `%2` och radbrytningarna bevaras.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `cannot add feature, wrong field count: layer: %1 feature: %2:` | `kan inte lägg atill fält, fel antal fält: lager %1 objekt %2:` | `kan inte lägga till objekt, fel antal fält: lager: %1, objekt: %2:` |
| `ERROR: %n attribute(s) not renamed` | `FEL: %n attribut ej omdöpt` / `FEL: %n attribut ej omdöpta` | `FEL: %n attribut döptes inte om` / `FEL: %n attribut döptes inte om` |
| `ERROR: the count of fields is incorrect after addition/removal of fields!` | `FEL: antalet fält är inte korrekt efter addering/borttagning av fält!` | `FEL: antalet fält är fel efter att fält har lagts till eller tagits bort!` |
| `Provider: %1` | `Dataplugin: %1` | `Dataleverantör: %1` |
| `SUCCESS: %1 attribute value(s) and %2 geometries changed.` | `RÄTT: %1 attributvärde(n) och %2 geometrier ändrades.` | `KLART: %1 attributvärden och %2 geometrier ändrades.` |
| `ERROR: %1 geometries not changed. Data provider '%2' does not have ChangeFeatures or ChangeGeometries capabilities` | `FEL: %1 geometrier ändrades inte. Datakällan "%2" har inte förmågan ChangeFeatures eller ChangeGeometries` | `FEL: %1 geometrier ändrades inte. Dataleverantören '%2' har inte stöd för ChangeFeatures eller ChangeGeometries.` |
| `ERROR: %1 attribute value change(s) not applied. Data provider '%2' does not have ChangeFeatures or ChangeAttributeValues capabilities` | `FEL: %1 ändringar av attributvärden tillämpades inte. Datakällan "%2" har inte förmågan ChangeFeatures eller ChangeGeometries` | `FEL: %1 ändringar av attributvärden tillämpades inte. Dataleverantören '%2' har inte stöd för ChangeFeatures eller ChangeAttributeValues.` |
| `SUCCESS: %n attribute value(s) changed.` | `RÄTT: %n attributvärde ändrades.` / `RÄTT: %n attributvärden ändrades.` | `KLART: %n attributvärde ändrades.` / `KLART: %n attributvärden ändrades.` |
| `SUCCESS: %n feature(s) deleted.` | `RÄTT: %n objekt togs bort.` / `RÄTT: %n objekt togs bort.` | `KLART: %n objekt togs bort.` / `KLART: %n objekt togs bort.` |
| `SUCCESS: %n feature(s) added.` | `RÄTT: %n objekt lades till.` / `RÄTT: %n objekt lades till.` | `KLART: %n objekt lades till.` / `KLART: %n objekt lades till.` |
| `Last error reported from data provider:\n%1` | `Senaste fel från dataleverantören:\n%1` | `Senaste fel som rapporterades av dataleverantören:\n%1` |
| `ERROR: %n feature(s) not added - provider doesn't support adding features.` | `FEL: %n objekt lades inte till.  Datakällan stödjer inte lägga till objekt.` | `FEL: %n objekt lades inte till. Dataleverantören har inte stöd för att lägga till objekt.` |
| `Can't rollback after start editing failure. Roll back detailed errors: %1` | `Kan inte rulla tillbaka efter att ha börjat redigera objekt. Tillbakarullningens detaljerade fel: %1` | `Kan inte återställa efter ett fel när redigeringen startades. Detaljerade återställningsfel: %1` |
| `ERROR: data source '%1', is not available for transactions.` | `FEL: datakälla '%1', kan inte använda transaktioner.` | `FEL: datakällan '%1' är inte tillgänglig för transaktioner.` |
| `ERROR: could not start a transaction on data provider '%1', detailed error: '%2'.` | `FEL:Kunde inte starta en transaktion på datakällan "%1", detaljerat fel: "%2"` | `FEL: Kunde inte starta en transaktion för dataleverantören '%1'. Detaljerat fel: '%2'.` |
| `ERROR: could not add layer '%1' to transaction on data provider '%2'.` | `FEL: Kunde in lägga till lager "%1" till transaktion på datakällan "%2".` | `FEL: Kunde inte lägga till lagret '%1' i transaktionen för dataleverantören '%2'.` |
| `WARNING: changes to layer '%1' were already sent to data provider and cannot be rolled back.` | `VARNING: ändringar på lager "%1" är redan skickade till datakälla och kan inte rullas tillbaka.` | `VARNING: ändringar i lagret '%1' har redan skickats till dataleverantören och kan inte återställas.` |
| `ERROR: could not commit a transaction, detailed error: '%1'.` | `FEL: Kunde inte posta en transaktion, detaljerat fel: "%1".` | `FEL: Kunde inte verkställa en transaktion. Detaljerat fel: '%1'.` |
| `Offset: %1` | `Offset: %1` | `Förskjutning: %1` |
| `Include automatically in print layout legend items` | `Inkludera automatiskt i utskriftslayouters teckenförklaringselement` | `Inkludera automatiskt i teckenförklaringsobjekt i utskriftslayouten` |
| `Legend Text Format` | `Format för legendtext` | `Textformat för teckenförklaring` |
| `Set Labels from Expression…` | `Använd uttryck för etikett…` | `Ange etiketter med uttryck…` |
| `Legend placeholder image` | `Bild för teckenförklaring` | `Platshållarbild för teckenförklaring` |
| `Invert Selection` | `Invertera valda` | `Invertera markering` |
| `Stop editing mode to enable this.` | `Avsluta redigeringsläge för att tillåta detta.` | `Avsluta redigeringsläget för att aktivera detta.` |
| `Not supported` | `Stöds ej` | `Stöds inte` |

Ingen extern ändring har gjorts. Aktuella Transifex-enhetsidentifierare måste
hämtas och måltexterna jämföras före en separat deltafil kan skapas.
