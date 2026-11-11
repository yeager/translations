# QGIS: PostGIS-raster och datatyper 103

Datum: 10 november 2026  
Resurs: `qgis-application`, språk `sv`  
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen granskar PostGIS-rasterleverantörens fel och metadata. C++-typnamnen
`byte`, `unsigned int`, `unsigned long`, `int`, `long`, `float` och `double`
bevaras. Funktionsnamnet `AddRasterConstraints`, EPSG, CRS, SQL och
platshållarna lämnas också oförändrade.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Invalid band number '%1` | `Ogiltigt antal band %1` | `Ogiltigt bandnummer %1` |
| `Requested extent is not valid` | `Begärd utsträckning är inte giltig.` | `Den begärda utbredningen är inte giltig` |
| `Cannot convert identified value to unsigned int` | `Kan inte konvertera identifierat värde till positivt heltal` | `Kan inte konvertera det identifierade värdet till unsigned int` |
| `Cannot convert identified value to unsigned long` | `Kan inte konvertera identifierat värde till positivt stort heltal` | `Kan inte konvertera det identifierade värdet till unsigned long` |
| `Cannot convert identified value to int` | `Kan inte konvertera identifierat värde till heltal` | `Kan inte konvertera det identifierade värdet till int` |
| `Cannot convert identified value to long` | `Kan inte konvertera identifierat värde till stort heltal` | `Kan inte konvertera det identifierade värdet till long` |
| `Cannot convert identified value to float` | `Kan inte konvertera identifierat värde till flyttal` | `Kan inte konvertera det identifierade värdet till float` |
| `Cannot convert identified value to double` | `Kan inte konvertera identifierat värde till dubbel` | `Kan inte konvertera det identifierade värdet till double` |
| `Unknown identified data type` | `Okänd identifierad datatyp` | `Okänd datatyp` |
| `Unable to create destination raster for tiles from %1: %2` | `Kan inte skapa mål-raster för kartrutor från %1: %2` | `Kan inte skapa målraster för rutor från %1: %2` |
| `Unable to resample and transform destination raster for tiles from %1: %2` | `Kan inte omsampla och transformera mål-raster för kartrutor från %1: %2` | `Kan inte sampla om och transformera målraster för rutor från %1: %2` |
| `Where Clause SQL` | `SQL Where-sats` | `SQL WHERE-sats` |
| `Overviews` | `Översiktskartor` | `Översikter` |
| `Primary Keys SQL` | `SQL primärnycklar` | `SQL-primärnycklar` |
| `Cannot create CRS from EPSG: '%1'` | `Kan inte skapa koordinatsystem från EPSG: '%1'` | `Kan inte skapa koordinatreferenssystem från EPSG: '%1'` |
| `Cannot get band count from value: '%1'` | `Kan inte få antalet band från värdet: '%1'` | `Kan inte hämta antalet band från värdet: '%1'` |
| `An error occurred while fetching raster metadata for %1, proceeding with (possibly very slow) raster data analysis: %2\nPlease consider adding raster constraints with PostGIS function AddRasterConstraints.` | `Ett fel uppstod vid hämtning av rastermetadata för %1, fortsätter med (möjligen mycket långsam) rasterdataanalys: %2\nÖvervägatt lägga till rasterinformation med PostGIS-funktionen AddRasterConstraints.` | `Ett fel uppstod vid hämtning av rastermetadata för %1. Rasterdataanalysen fortsätter, men kan vara mycket långsam: %2\nÖverväg att lägga till rasterbegränsningar med PostGIS-funktionen AddRasterConstraints.` |
| `An error occurred while fetching raster column` | `Ett fel inträffade vid hämtning av rasterkolumner` | `Ett fel inträffade vid hämtning av rasterkolumnen` |
| `Cannot get metadata from raster` | `Kan inte få metedata från raster` | `Kan inte hämta metadata från raster` |
| `PostgreSQL WHERE clause` | `PostgreSQL WHERE sats` | `PostgreSQL WHERE-sats` |
| `Error fetching overviews information: %1` | `Fel vid hämtning av översikts information: %1` | `Fel vid hämtning av översiktsinformation: %1` |
| `No overviews found, performances may be affected for %1` | `Inga översikter hittades, prestanda kan bli påverkad för %1` | `Inga översikter hittades. Prestandan kan påverkas för %1.` |

Ingen extern ändring har gjorts. Aktuella Transifex-enhetsidentifierare måste
hämtas och måltexterna jämföras före en separat deltafil kan skapas.
