# QGIS: projektmetadata, server och tillit 243

Datum: 11 november 2026
Resurs: `qgis-application`, språk `sv`
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen granskar projektets metadata, serverinställningar, sensorinställningar
och projektförtroendedialog. `WMS`, `WFS`, `WCS`, `WMTS`, `CRS`, `URL`, `URI`,
`ICC`, `GetFeatureInfo`, `GetCapabilities` och `GetMap` bevaras som API-termer.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Automatically sets the number of decimal places to use when displaying coordinates` | `Sätter automatiskt antal decimaler som används när koordinater visas` | `Anger automatiskt antalet decimaler som ska användas när koordinater visas` |
| `Manually set the number of decimal places to use when displaying coordinates` | `Sätt manuellt antal decimaler som används när koordinater visas` | `Ange manuellt antalet decimaler som ska användas när koordinater visas` |
| `WMS/WFS/WCS Server Configuration` | `WMS/WFS/WCS Serverkonfiguration` | `Serverkonfiguration för WMS/WFS/WCS` |
| `General Settings` | `Generella inställningar` | `Allmänna inställningar` |
| `Open folder containing the project` | `Öppna mapp där projektet finns` | `Öppna mappen som innehåller projektet` |
| `Set the project home path` | `Ange projektets sökväg` | `Ange projektets hemkatalog` |
| `Save to file` | `Spara till fil` | `Spara i fil` |
| `Ask for datum transformation if several are available (defined in global setting)` | `Fråga efter datumtransformation när flera finns tillgängliga (definierade i globala inställningar)` | `Fråga efter datumtransformation om flera är tillgängliga, enligt den globala inställningen` |
| `Opacity` | `Opacitet` | `Ogenomskinlighet` |
| `The contact person e-mail for the service.` | `E-post till kontaktpersonen för tjänsten` | `Kontaktpersonens e-postadress för tjänsten.` |
| `The contact person name for the service.` | `Namn på kontaktperson för tjänsten` | `Kontaktpersonens namn för tjänsten.` |
| `The title should be brief yet descriptive enough to identify this service.` | `Titeln bör vara kortfattad men så beskrivande att det går att identifiera tjänsten.` | `Titeln bör vara kort men tillräckligt beskrivande för att identifiera tjänsten.` |
| `List of keywords separated by comma to help catalog searching.` | `Lista med sökord separerade med kommatecken för att assistera katalogsökning.` | `Lista över nyckelord, separerade med kommatecken, som underlättar katalogsökning.` |
| `Fees applied to the service.` | `Avgifter som tillämpas för tjänsten.` | `Avgifter för tjänsten.` |
| `Access constraints applied to the service.` | `Åtkomstbegränsningar appliceras för tjänsten.` | `Åtkomstbegränsningar för tjänsten.` |
| `A name used to identify the root layer. The short name is a text string used for machine-to-machine communication.` | `Ett namn som används för att identifiera rotlagret. Kortnamnet är en textsträng som används för kommunikation maskin-till-maskin.` | `Ett namn som används för att identifiera rotlagret. Kortnamnet är en sträng som används för maskin-till-maskin-kommunikation.` |
| `Add new CRS` | `Lägg till nytt referenssystem` | `Lägg till nytt koordinatreferenssystem` |
| `Fetch all CRS's from layers` | `Hämta alla koordinatreferenssystem från lager` | `Hämta alla koordinatreferenssystem från lagren` |
| `Service language` | `Servicespråk` | `Tjänstspråk` |
| `Metadata URL` | `Metadata URL` | `Metadata-URL` |
| `URL mime/type` | `URL mime/typ` | `URL MIME-typ` |
| `Minimum scale` | `Minimumskala` | `Minsta skala` |
| `Advertised URL` | `Utannonsera URL` | `Annonserad URL` |
| `CRS restrictions` | `Referenskoordinatsystemsbegränsningar` | `Begränsningar av koordinatreferenssystem` |
| `Speed up project loading by skipping data checks in PostgreSQL layers. Useful in QGIS server context or project with huge database views or materialized views.` | `Snabbar upp projektladdningen genom att hoppa över datakontroller i PostgreSQL-lager. Användbart i QGIS server eller projekt med stora databasvyer eller materialiserade vyer.` | `Snabbar upp inläsningen av projekt genom att hoppa över datakontroller i PostgreSQL-lager. Användbart i QGIS Server eller projekt med stora databasvyer eller materialiserade vyer.` |
| `Maximum features for Atlas print requests` | `Max antal objekt för förfrågningar av atlasutskrift` | `Högsta antal objekt för atlasutskriftsförfrågningar` |
| `Scenario &2 - INSPIRE related fields using embedded service metadata` | `Scenario &2 - INSPIRE-relaterat fält använder inbäddad tjänsts metadata` | `Scenario &2: INSPIRE-relaterade fält använder inbäddade tjänstemetadata` |
| `Scenario &1 - INSPIRE related fields using referenced external service metadata` | `Scenario %1 - INSPIRE-relaterat fält använder externt refererad tjänsts metadata` | `Scenario &1: INSPIRE-relaterade fält använder refererade externa tjänstemetadata` |
| `GetCapabilities response would skip name attribute for group items while leaving title attribute as is, thus showing the group but making it impossible to include the whole group (rather than it's elements) in subsequent GetMap request LAYERS parameter.` | `GetCapabiliies-svaret kommer skippa namnattributet för grupper medan titelattributet lämnas som det är, därigenom visas gruppen men gör det omöjligt att inkludera hela gruppen (i stället för dess innehåll) i efterkommande GetMap-förfrågningars LAYER-parameter.` | `GetCapabilities-svaret hoppar över namnattributet för gruppobjekt men lämnar titelattributet oförändrat. Gruppen visas då, men det går inte att inkludera hela gruppen i parametern LAYERS i efterföljande GetMap-förfrågningar, utan bara dess element.` |
| `Skip name attribute for groups` | `Skippa namnattribut för grupper` | `Hoppa över namnattribut för grupper` |
| `Quality for JPEG and WebP images (from 0 to 100; 0 - smaller size, 100 - better quality)` | `Kvalitet på JPEG- och WebP-bilder (från 0 till 100; 0 - mindre storlek, 100 - bättre kvalitet)` | `Kvalitet för JPEG- och WebP-bilder, från 0 till 100: 0 ger mindre filstorlek och 100 bättre kvalitet` |
| `Style Databases` | `Stil-databaser` | `Stildatabaser` |
| `Add existing style database` | `Lägg till befintlig stil-databas` | `Lägg till befintlig stildatabas` |
| `Create new style database` | `Skapa ny stil-databas` | `Skapa ny stildatabas` |
| `Load an ICC profile file and attach it to the project. Color model will be updated accordingly.` | `Läs in en ICC-profil-fil och koppla den till projektet. Färgmodellen kommer uppdateras därefter.` | `Läs in en ICC-profil och koppla den till projektet. Färgmodellen uppdateras därefter.` |
| `For distance, area and angle calculations` | `För avstånd-, area- och vinkelberäkningar` | `För beräkning av avstånd, area och vinkel` |
| `Set Project Full Extent` | `Ställ in projektets hela utsträckning` | `Ange projektets fullständiga utbredning` |
| `When connected, a sensor will passively capture data in the background. The latest captured data can be accessed within expressions using the sensor_data('sensor name') function.` | `När den är inkopplad kommer en sensor att passivt fånga data i bakgrunden. Den senaste fångade data kan kommas åt i uttryck genom att använda funktionen  sensor_data('sensor name')` | `När en sensor är ansluten samlar den passivt in data i bakgrunden. De senast insamlade uppgifterna kan nås i uttryck med funktionen sensor_data('sensor name').` |
| `Do you trust the author(s) of this project?` | `Litar du på författaren av detta projekt?` | `Litar du på projektets författare?` |
| `Double-click on a list item to preview the script.` | `Dubbelklicka på en i listan för att förhandsgranska skriptet.` | `Dubbelklicka på ett objekt i listan för att förhandsgranska skriptet.` |
| `Return to list` | `Återvänd till lista` | `Återgå till listan` |
| `The current project file path is ’%1’.` | `Sökvägen för aktuellt projekt är '%1'.` | `Sökvägen till den aktuella projektfilen är ’%1’.` |
| `Apply decision to all projects in folder ’%1’` | `Applicera beslut för alla projekt i mappen '%1'` | `Tillämpa beslutet på alla projekt i mappen ’%1’` |
| `The current project URI is ’%1’.` | `URI för aktuellt projekt är '%1'.` | `URI:n för det aktuella projektet är ’%1’.` |

Acceleratorerna `&1` och `&2`, API-namn, MIME-typer, platshållaren `%1`,
HTML-markupen samt sensorfunktionen med dess argument ska bevaras oförändrade
vid senare import. Ingen extern ändring har gjorts.
