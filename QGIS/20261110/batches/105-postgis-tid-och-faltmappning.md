# QGIS: PostGIS-tid och fältmappning 105

Datum: 10 november 2026  
Resurs: `qgis-application`, språk `sv`  
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen granskar tidsinställningar för PostGIS-raster samt fältmappning i
geobearbetningspaneler. HTML-markeringen, tidskontrollens etablerade namn och
de tekniska nycklarna `name`, `type`, `aggregate`, `input`, `length` och
`precision` bevaras.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Temporal capabilities` | `Tidsegenskaper (capabilities)` | `Tidsegenskaper` |
| `If the dataset contains multiple rasters belonging to a time series, specify the field that contains the time information, the type of the field can be any type that can be converted to a timestamp.` | `Om datasetet innehåller fler raster som tillhör tidsserier, ange fältet som innehåller tidsinformationen, typen för fältet kan vara vad som helst som kan konverteras till tidsstämpel.` | `Om datauppsättningen innehåller flera raster som ingår i en tidsserie, anger du fältet som innehåller tidsinformationen. Fältets typ kan vara vilken typ som helst som kan konverteras till en tidsstämpel.` |
| `<html><head/><body><p>A default value can be specified and it will be used when the temporal controller is not requesting any particular time.</p><p>It is recommended to set a default temporal value here instead of using a provider filter because the provider filter will still be active when using the temporal controller while this default value will be ignored.</p></body></html>` | `<html><head/><body><p>Ett standardvärde kan anges och används när tidskontrollen inte begär någon speciell tid.</p><p>Det är rrekommenderat att ange ett standardvärde för tid här i stället för att använda ett filter för datakällan eftersom filtret kommer fortfarande att vara aktivt när tidskontrollen används medan standardvärdet kommer att ignoreras.</p></body></html>` | `<html><head/><body><p>Ett standardvärde kan anges och används när tidskontrollen inte begär en viss tid.</p><p>Vi rekommenderar att du anger ett standardvärde för tid här i stället för att använda ett leverantörsfilter. Leverantörsfiltret är fortfarande aktivt när tidskontrollen används, medan standardvärdet då ignoreras.</p></body></html>` |
| `Default time` | `Standardvärde för tid` | `Standardtid` |
| `Connection to the database not available` | `Anslutning till databasen inte tillgänglig` | `Databasanslutningen är inte tillgänglig` |
| `Load fields from template layer` | `Läs in fält från mall-lager` | `Läs in fält från mallager` |
| `Load fields from selected template layer` | `Läs in fält från valt mall-lager` | `Läs in fält från valt mallager` |
| `Do you want to reset the field mapping?` | `Vill du återställa fältkopplingarna?` | `Vill du återställa fältmappningen?` |
| `an array of map items, each containing a 'name', 'type', 'aggregate' and 'input' value (and optional 'length' and 'precision' values).` | `en array med kartelement, som vart och ett innehåller ett värde för "namn", "typ", "aggregat" och "input" (och eventuellt värden för "längd" och "precision")` | `en matris med mappningsposter, där varje post innehåller värdena 'name', 'type', 'aggregate' och 'input' samt eventuellt 'length' och 'precision'.` |

Ingen extern ändring har gjorts. Aktuella Transifex-enhetsidentifierare måste
hämtas och måltexterna jämföras före en separat deltafil kan skapas.
