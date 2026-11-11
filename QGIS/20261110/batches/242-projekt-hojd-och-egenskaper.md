# QGIS: projekt, höjd och egenskaper 242

Datum: 11 november 2026
Resurs: `qgis-application`, språk `sv`
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen granskar projektets höjdinställningar, projekthem och egenskaper.
`DEM`, `CRS`, `WMS`, `WCS`, `URL`, `XML`, `QGIS`, `PostgreSQL` och tekniska
metadatafält behålls enligt gränssnittets och standardernas benämningar.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Not set` | `Inte satt` | `Inte angivet` |
| `DEM (Raster Layer)` | `DEM (Rasterlager)` | `DEM (rasterlager)` |
| `Mesh` | `Mesh` | `Nät` |
| `An elevation layer must be selected for a DEM terrain` | `Ett lager med höjder måste väljas för en DEM-terräng` | `Ett höjdlager måste väljas för en DEM-terräng` |
| `An elevation layer must be selected for a mesh terrain` | `Ett lager med höjder måste väljas för en mesh-terräng` | `Ett höjdlager måste väljas för en nätterräng` |
| `Upper elevation range must be greater than the lower one` | `Övre höjdnivå måste vara större än den lägre` | `Den övre höjdgränsen måste vara större än den undre` |
| `Mesh layer` | `Mesh-lager` | `Nätlager` |
| `Maximum elevation of interest` | `Största höjd av intresse` | `Högsta relevanta höjd` |
| `Minimum elevation of interest` | `Lägsta höjd av intresse` | `Lägsta relevanta höjd` |
| `When set, these heights define the upper and lower elevation limits for the area of interest in this project.` | `När det är angivet, definierar dessa höjder det övre och lägre begränsningarna för höjder av intresse i detta projekt.` | `När de anges definierar dessa höjder den övre och undre höjdgränsen för intresseområdet i projektet.` |
| `Vertical Reference System` | `Vertikalt koordinatsystem` | `Vertikalt referenssystem` |
| `Set Project Home…` | `Ange projektets sökväg` | `Ange projektets hemkatalog…` |
| `Select Project Home Directory` | `Ange projektets sökväg` | `Välj projektets hemkatalog` |
| `Open Project` | `Öppna projekt` | `Öppna projektet` |
| `Could not read project file` | `Kunde inte läsa projektfil` | `Det gick inte att läsa projektfilen` |
| `Recursive embedding is not supported. It is not possible to embed layers / groups from the current project.` | `Rekursiv inbäddning stöds inte. Det är inte möjligt att bädda in lager/grupper från aktuellt projekt.` | `Rekursiv inbäddning stöds inte. Det går inte att bädda in lager eller grupper från det aktuella projektet.` |
| `Coordinate System Restriction` | `Koordinatsystemrestriktion` | `Begränsning av koordinatsystem` |
| `No coordinate systems selected. Disabling restriction.` | `Inga koordinatsystem valda. Avaktiverar restriktion.` | `Inga koordinatsystem har valts. Begränsningen inaktiveras.` |
| `Easting, Northing (Longitude, Latitude)` | `Öst, Norr (Longitud, Latitud)` | `Östlig, nordlig (longitud, latitud)` |
| `Northing, Easting (Latitude, Longitude)` | `Norr, Öst (Latitud, Longitud)` | `Nordlig, östlig (latitud, longitud)` |
| `Yards` | `Yards` | `Yard` |
| `Miles` | `Miles` | `Engelska mil` |
| `Automatic Transaction Groups` | `Automatiska trasaktionsgrupper` | `Automatiska transaktionsgrupper` |
| `Automatic transactional editing means that on supported datasources (postgres databases) the edit state of all tables that originate from the same database are synchronized and executed in a server side transaction.` | `Automatiska transaktionsredigering innebär att, på stödda datakällor (postgres-databaser), redigeringstillståndet för alla tabeller som kommer från samma databas synkroniseras och körs i en transaktion på serversidan.` | `Automatisk transaktionsredigering innebär att redigeringsläget för alla tabeller från samma databas synkroniseras och utförs i en transaktion på serversidan när datakällan har stöd för det, till exempel PostgreSQL.` |
| `Buffered transactional editing means that all editable layers in the buffered transaction group are toggled synchronously and all edits are saved in a local edit buffer. Saving changes is executed within a single transaction on all layers (per provider).` | `Buffrad transaktionsredigering innebär att alla redigerbara lager i den buffrade transaktionsgruppen växlas synkroniserat och alla redigeringar sparas i en lokal redigeringsbuffert. Att spara förändringar körs inom en transaktion på alla lager (per datakälla).` | `Buffrad transaktionsredigering innebär att alla redigerbara lager i den buffrade transaktionsgruppen växlas synkront och att alla ändringar sparas i en lokal redigeringsbuffert. När ändringarna sparas utförs en enda transaktion för alla lager per provider.` |
| `Layers are in edit mode. Stop edit mode on all layers to toggle transactional editing.` | `Lager är i redigeringsläge. Avsluta redigeringsläge på alla lager för att växla transaktionsredigering.` | `Lager är i redigeringsläge. Avsluta redigeringsläget för alla lager för att växla transaktionsredigering.` |
| `Edits are buffered locally and sent to the provider when toggling layer editing mode.` | `Redigeringar är buffrade lokalt och skickas till datakällan när redigeringsläget för lagret ändras.` | `Ändringar buffras lokalt och skickas till providern när lagrets redigeringsläge växlas.` |
| `Scale denominator` | `Skalavgränsare` | `Skalnämnare` |
| `XML files (*.xml *.XML)` | `XML-filer (*.xml *XML)` | `XML-filer (*.xml *.XML)` |
| `Select %1 from pull-down menu to adjust radii` | `Välj %1 från rullgardinsmenyn för att justera radie` | `Välj %1 i rullgardinsmenyn för att justera radierna` |
| `The text you entered is not a valid scale.` | `Texten du skrev in har inte en giltig skala.` | `Texten du angav är inte en giltig skala.` |
| `Coordinate Reference System` | `Koordinaternas referenssystem` | `Koordinatreferenssystem` |
| `Checking this setting avoids visible edge artifacts when rendering this project as separate map tiles. Rendering performance will be degraded.` | `Kryssa i denna inställning för undvikande av synliga kantartefakter vid rendering av detta projekt som separata kartrutor. Renderingsprestanda kommer att försämras.` | `När inställningen är markerad undviks synliga kantartefakter när projektet återges som separata kartrutor. Återgivningen blir långsammare.` |
| `Toggle Selection` | `Växla valda` | `Växla markering` |
| `Show spatial layers only` | `Visa endast spatiala lager` | `Visa endast rumsliga lager` |
| `Online resource` | `Onlineresurser` | `Nätresurs` |
| `E-Mail` | `E-Mail` | `E-post` |
| `Add geometry to feature response` | `Inkludera geometri till förfrågningsvar` | `Lägg till geometri i objektsvaret` |
| `Use layer ids as names` | `Använd lager-id som namn` | `Använd lager-ID som namn` |

`CRS`, `WMS`, `WCS`, `DEM`, filmasker och platshållaren `%1` ska bevaras
oförändrade vid senare import. Ingen extern ändring har gjorts.
