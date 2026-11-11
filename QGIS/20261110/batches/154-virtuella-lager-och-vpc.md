# QGIS: virtuella lager och VPC 154

Datum: 10 november 2026
Resurs: `qgis-application`, språk `sv`
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen granskar dialogen för virtuella lager och fel från den virtuella
punktmolnsleverantören. SQL, SQLite, SpatiaLite, QLR, SRID, VPC och VPZ är
format- eller tekniknamn och bevaras. HTML-markeringen och exempelkoden i
hjälptexten måste också vara oförändrade vid en senare deltafil.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Error while executing feature count request : %1` | `Fel vid körning av objektsräkningsförfrågan : %1` | `Fel när begäran om objektantal kördes: %1` |
| `Checkbox 'Unique identifier column' is checked, but no field given` | `Kryssrutan &quot; Kolumn för unik identifierare&quot; är markerad, men inget fält är angett` | `Kryssrutan ”Kolumn för unik identifierare” är markerad, men inget fält har angetts` |
| `The unique identifier field <b>%1</b> was not found in list of fields:<ul>%2</ul>` | `Fältet för unik identifierare <b>%1</b> hittades inte i lista på fält:<ul>%2</ul>` | `Fältet för unik identifierare <b>%1</b> hittades inte i listan över fält:<ul>%2</ul>` |
| `No CRS defined, are you sure you want to create a layer without a crs?` | `Inget koordinatsystem definierat. Är du säker du vill skapa ett lager utan ett koordinatsystem?` | `Inget koordinatreferenssystem har angetts. Är du säker på att du vill skapa ett lager utan CRS?` |
| `A virtual layer of this name already exists, would you like to overwrite it?` | `En virtuellt lager med detta namn finns redan, vill du skriva över det?` | `Ett virtuellt lager med det här namnet finns redan. Vill du skriva över det?` |
| `Embedded layers can be added to have SQL queries with layers that are independent from layers loaded by the current QGIS project.\nIn particular, saving a virtual layer with embedded layers to a QLR file can be done to reuse its definition in another project.` | `Inbäddade lager kan läggas till för att ha SQL frågor med lager som är oberoende från lager inlästa av det aktuella QGIS projektet.\nExempelvis, att spara ett virtuellt lager med inbäddade lager till en QLR fil kan göras för att återvinna dess definition i ett annat projekt.` | `Du kan lägga till inbäddade lager för SQL-frågor med lager som är oberoende av de lager som har lästs in i det aktuella QGIS-projektet.\nDu kan särskilt spara ett virtuellt lager med inbäddade lager i en QLR-fil och återanvända dess definition i ett annat projekt.` |
| `Import layer definition from loaded layers of the current project` | `Importera lagerdefinitioner ur laddade lager från det aktuella projektet` | `Importera lagerdefinition från inlästa lager i det aktuella projektet` |
| SQL-hjälptexten | Ofullständig och innehåller bland annat `kommentater`, felaktiga typnamn och saknar förklaringen av `tablename.geometry`. | Översätt hela hjälptexten på nytt med bevarad HTML, `tablename.geometry`, `/*:type*/`, `/*:gtype:srid*/` och SQL-exemplet. |
| `CRS` | `Referenskoordinatsystem` | `Koordinatreferenssystem` |
| `Browse for Layer` | `Bläddra efter lager` | `Bläddra efter lager…` |
| `Could not create temporary folder` | `Kunde inte skapa temporär mapp.` | `Kunde inte skapa tillfällig mapp` |
| `VPZ file does not contain any VPCs` | `VPZ-filen innehåller inte några VPCer` | `VPZ-filen innehåller inga VPC-filer` |
| `VPZ file contains multiple VPCs` | `VPZ-filen innehåller flera VPCer` | `VPZ-filen innehåller flera VPC-filer` |
| `Indexed VTPK (tilemap is present)` | `Indexerad VTPK (tilemap finns)` | `Indexerad VTPK (rutmapp finns)` |
| `Flat VTPK (no tilemap)` | `Platt VTPK (ingen tilemap)` | `Platt VTPK (ingen rutmapp)` |
| `Tile detail levels` | `Tile detaljnivåer` | `Rutornas detaljnivåer` |
| `Select VTPK Dataset` | `Välj VTPK dataset` | `Välj VTPK-datamängd` |
| `Error when parsing GetFeature response` | `Fel vid tolkning av GetFeature svar` | `Fel vid tolkning av GetFeature-svar` |

Ingen extern ändring har gjorts. Aktuella Transifex-enhetsidentifierare måste
hämtas och måltexterna jämföras före en separat deltafil kan skapas.
