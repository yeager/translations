# QGIS: PostgreSQL, diagram och tillägg 232

Datum: 11 november 2026
Resurs: `qgis-application`, språk `sv`
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen granskar PostgreSQL-val, diagramkontroller och tilläggshanteraren.
PostGIS, PostgreSQL, SSL, SRID, Python och interna identifierare behålls.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Don't resolve type of unrestricted columns (GEOMETRY)` | `slå inte upp typer med obegränsade kolumner (GEOMETRY)` | `Fastställ inte typen för obegränsade kolumner (GEOMETRY)` |
| `Session ROLE` | `Session ROLE` | `Sessions-ROLE` |
| `Also list raster overview tables` | `Lista också tabeller för rasterpyramider` | `Lista även översiktstabeller för raster` |
| `If specified, only tables from the matching schema will be fetched and listed for the provider` | `Om angett så hämtas och listas endast tabeller för matchande schema` | `Om ett schema anges hämtas och visas bara tabeller från det schemat i providern` |
| `Limit to tables from specific schema` | `Begränsa till tabeller från specifikt schema` | `Begränsa till tabeller från ett visst schema` |
| `Scanning tables for %1` | `Skannar av tabeller efter %1` | `Söker igenom tabeller efter %1` |
| `Spatial Type` | `Spatial typ` | `Rumslig typ` |
| `Check PK unicity` | `Kontrollera unik PK` | `Kontrollera primärnyckelns unikhet` |
| `Enable check for primary key unicity when loading views and materialized views. This option can make loading of large datasets significantly slower.` | `Kontrollera att primärnyckeln är unik vid laddning av vyer och materialiserade vyer. Detta val kan gör laddningen av stora dataset signifikant långsammare.` | `Kontrollera att primärnyckeln är unik när vyer och materialiserade vyer läses in. Det kan göra inläsningen av stora datamängder betydligt långsammare.` |
| `Specify a geometry type in the '%1' column` | `Välj en geometrityp i '%1' kolumnen` | `Ange en geometrityp i kolumnen '%1'` |
| `Enter a SRID into the '%1' column` | `Ange en SRID i '%1' kolumnen` | `Ange ett SRID i kolumnen '%1'` |
| `Select columns in the '%1' column that uniquely identify features of this layer` | `Välj kolumner i '%1' kolumnen som unikt identifierar objekt i detta lager` | `Välj de kolumner i '%1' som unikt identifierar objekt i lagret` |
| `This option is only available for views and materialized views.` | `Dett aval är endast tillgängligt för vyer och materialiserade vyer` | `Det här alternativet är bara tillgängligt för vyer och materialiserade vyer.` |
| `Select at id` | `Välj med id` | `Välj med ID` |
| `Specular color is disabled because material has no shininess` | `Speglande färg är inaktiverat för materialet har ingen glans` | `Speglande färg är inaktiverad eftersom materialet saknar glans` |
| `Animated Image From URL` | `Animerade bild från URL` | `Animerad bild från URL` |
| `Enter SVG URL` | `Skriv in URL:en till SVG ` | `Ange URL:en till SVG` |
| `Pie Chart Plot Properties` | `Egenskaper för pajdiagram` | `Egenskaper för cirkeldiagram` |
| `Category Labels` | `Kategorietikett` | `Kategorietiketter` |
| `Value Labels` | `Värdeetikett` | `Värdeetiketter` |
| `Pie Chart Plot Options` | `Alternativ för lpajdiagram` | `Alternativ för cirkeldiagram` |
| `Symbols list` | `Lista på symboler` | `Symbollista` |
| `Label font` | `Typsnitt etikett` | `Etiketttypsnitt` |
| `Change…` | `Ändra...` | `Ändra…` |
| `Zoom X Axis` | `Zooma X-axel` | `Zooma X-axeln` |
| `Plugin Dependencies Manager` | `Hanteraren för tilläggsberoende` | `Hanterare för tilläggsberoenden` |
| `Plugin dependencies for <b>%s</b>` | `Tilläggsberoende för <b>%s</b>` | `Tilläggsberoenden för <b>%s</b>` |
| `Installed` | `Installerade` | `Installerad` |
| `Available` | `Tillgänglig` | `Tillgängligt` |
| `Action` | `Kommando` | `Åtgärd` |
| `Fix manually` | `Fixa manuellt` | `Åtgärda manuellt` |
| `QGIS Python Plugin Installer` | `QGIS Installerare för Python-plugin` | `QGIS installationsprogram för Python-tillägg` |
| `Obsolete plugin:` | `Föråldrat plugin:` | `Föråldrat tillägg:` |
| `QGIS has detected an obsolete plugin that masks its more recent version shipped with this copy of QGIS. This is likely due to files associated with a previous installation of QGIS. Do you want to remove the old plugin right now and unmask the more recent version?` | `QGIS har upptäckt ett föråldrat plugin som döljer en nyare version som skeppas med denna kopia av QGIS. Detta beror troligen på en tidigare installation av QGIS. Vill du ta bort det gamla pluginprogrammet med en gång och på så sätt få fram den nyare versionen?` | `QGIS har upptäckt ett föråldrat tillägg som döljer den nyare version som följer med den här kopian av QGIS. Det beror troligen på filer från en tidigare QGIS-installation. Vill du ta bort det gamla tillägget nu och göra den nyare versionen tillgänglig?` |
| `Error reading repository:` | `Fel vid läsning av centralkatalog:` | `Fel vid läsning av förråd:` |
| `Are you sure you want to downgrade the plugin to the latest available version? The installed one is newer!` | `Är du säker på att du vill nedgradera detta plugin till den senast tillgängliga versionen? Den installerade versionen är nyare!` | `Är du säker på att du vill nedgradera tillägget till den senaste tillgängliga versionen? Den installerade versionen är nyare.` |
| `Plugin has disappeared` | `Plugin har försvunnit` | `Tillägget har försvunnit` |
| `The plugin is not compatible with this version of QGIS. It's designed for QGIS versions:` | `Detta plugin är inte kompatibelt med denna version av QGIS. Det är designat för QGIS-versioner:` | `Tillägget är inte kompatibelt med den här versionen av QGIS. Det är avsett för QGIS-versionerna:` |
| `The plugin depends on some components missing on your system. You need to install the following Python module in order to enable it:` | `Detta plugin är beroende av vissa komponenter som saknas på ditt system. Du behöver installera följande Python-moduler för att aktivera det:` | `Tillägget är beroende av komponenter som saknas på systemet. Installera följande Python-modul för att aktivera det:` |
| `The plugin is broken. Python said:` | `Detta plugin är trasigt. Python sa:` | `Tillägget är trasigt. Python angav:` |
| `Warning: this plugin isn't available in any accessible repository!` | `Varning: Detta plugin finns inte tillgängligt i någon centralkatalog!` | `Varning: Tillägget finns inte i något åtkomligt förråd!` |
| `Unable to add another repository with the same URL!` | `Du kan inte lägga till en till centralkatalog med samma URL!` | `Det går inte att lägga till ytterligare ett förråd med samma URL.` |

Markupen `<b>…</b>`, tekniknamn och interna identifierare ska bevaras
oförändrade vid senare import. Ingen extern ändring har gjorts.
