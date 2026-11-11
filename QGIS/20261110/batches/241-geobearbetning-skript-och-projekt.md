# QGIS: geobearbetning, skript och projekt 241

Datum: 11 november 2026
Resurs: `qgis-application`, språk `sv`
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen granskar geobearbetningens raster- och skriptdialoger samt projektets
läsnings- och felmeddelanden. `WMS`, `DPI`, `CRS`, `ZIP`, `QGIS`, `DEM` och
filformatnamn bevaras.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `path to layer destination` | `sökväg till lagrets destination` | `sökväg till lagrets mål` |
| `If set, gives the algorithm a hint on the reference scale that should be used to retrieve an image from the WMS server` | `Om angiven ges algoritmen en antydan om referensskalan som borde användas då en bild hämtas från WMS-servern` | `Om alternativet anges får algoritmen en uppgift om vilken referensskala som ska användas för att hämta en bild från WMS-servern` |
| `If set, gives the algorithm a hint on the DPI used by the WMS server` | `Om angiven ges algoritmen en antydan om DPI som används av WMS-servern` | `Om alternativet anges får algoritmen en uppgift om den DPI som WMS-servern använder` |
| `Not set` | `Inte satt` | `Inte angivet` |
| `Save colors to file` | `Spara färger till fil` | `Spara färgerna i en fil` |
| `Relief colors definition` | `Definition av relieffärger` | `Definition av relieffärgerna` |
| `string of the format 'min,max,red,green,blue' for each relief color, joined by a ; delimiter` | `sträng i formatet 'min, max, röd, grön, blå' för varje relieffärg, sammankopplad med ett ; som avgränsare` | `sträng i formatet 'min,max,red,green,blue' för varje relieffärg, sammanfogade med avgränsaren ;` |
| `Increase Font Size` | `Öka fontstorlek` | `Öka teckenstorleken` |
| `Decrease Font Size` | `Minska fontstorlek` | `Minska teckenstorleken` |
| `Find && Replace` | `Hitta && Ersätt` | `Sök och ersätt` |
| `No regions defined` | `Inga regioner har angetts` | `Inga områden har angetts` |
| `%1 regions defined` | `%1 regioner har angetts` | `%1 områden har angetts` |
| `Tile extent max zoom level definition` | `Definition av maximal zoomnivå för rututbredning` | `Definition av högsta zoomnivå för rututbredning` |
| `string of the format 'zoom:xmin,ymin,xmax,ymax [crs]', joined by a '::|::' delimiter` | `sträng med formatet ”zoom:xmin,ymin,xmax,ymax [crs]”, sammanfogad med avgränsaren ”::|::”` | `sträng i formatet 'zoom:xmin,ymin,xmax,ymax [crs]', sammanfogad med avgränsaren '::|::'` |
| `Show Timeouts` | `Visa timeouter` | `Visa tidsgränsöverskridanden` |
| `Loading layer %1` | `Läser in lager %1` | `Läser in lagret %1` |
| `Load layer source` | `Läs in lagerkälla` | `Läs in lagrets källa` |
| `Add layer to project` | `Lägg till lager till projekt` | `Lägg till lager i projektet` |
| `Reading project file` | `Läser projektfil` | `Läser projektfilen` |
| `Project Variables Invalid` | `Projektvariabler ogiltiga` | `Ogiltiga projektvariabler` |
| `Loading selective masking source sets` | `Läser in set för selektiv maskning` | `Läser in källuppsättningar för selektiv maskning` |
| `Loading snapping settings` | `Läser in snappningsinställningar` | `Läser in snäppningsinställningar` |
| `Updating CRS` | `Uppdaterar koordinatsystem` | `Uppdaterar koordinatreferenssystem` |
| `Unable to save project to storage %1` | `Kunde inte spara projekt till %1` | `Det gick inte att spara projektet i lagringen %1` |
| `Unable to save attachments archive` | `Går inte att spara bifogat arkiv` | `Det går inte att spara bilagearkivet` |
| `Unable to create backup file %1` | `Kan inte skapa backupfil %1` | `Det går inte att skapa säkerhetskopian %1` |
| `Unable to save to file %1` | `Kan ej spara till fil %1` | `Det går inte att spara i filen %1` |
| `Transaction mode can be changed only if all layers are not editable.` | `Transaktionsläge kan bara ämdras om alla lager inte är redigerbara.` | `Transaktionsläget kan bara ändras om inga lager är redigerbara.` |
| `Unable to unzip file '%1'` | `Kunde inte packa upp fil '%1'` | `Det gick inte att packa upp filen '%1'` |
| `Cannot read unzipped qgs project file` | `Kan ej läsa okomprimerad projektfil` | `Kan inte läsa den uppackade QGS-projektfilen` |
| `Unable to write temporary qgs file` | `Kunde inte skriva till temporär qgs-fil` | `Det gick inte att skriva den temporära QGS-filen` |
| `Unable to save auxiliary storage file ('%1'). The project has been saved but the latest changes to auxiliary data cannot be recovered. It is recommended to reload the project.` | `Kunde inte spara filen med kompletterande lagring ('%1'). Projektet har spats men de senaste ändringarna i kompletterade data kan inte återskapas. Det rekommenderas att ladda om projektet.` | `Det gick inte att spara filen för kompletterande lagring ('%1'). Projektet har sparats, men de senaste ändringarna av kompletterande data kan inte återställas. Vi rekommenderar att du läser in projektet på nytt.` |
| `%1 is not writable. Please adjust permissions (if possible) and try again.` | `%1 är inte skrivbar. Justera rättigheter (om möjligt) och försök igen.` | `%1 är inte skrivbar. Justera behörigheterna om möjligt och försök igen.` |
| `Unable to save to file %1. Your project may be corrupted on disk. Try clearing some space on the volume and check file permissions before pressing save again.` | `Kunde inte spara till fil %1. Ditt projekt kan vara felaktigt sparat. Försök frigöra disk-utrymme och kontrollera filrättigheter innan du försöker igen.` | `Det gick inte att spara i filen %1. Projektet kan vara skadat på disken. Frigör utrymme på volymen och kontrollera filbehörigheterna innan du sparar igen.` |
| `Mesh` | `Mesh` | `Nät` |
| `Project Vertical CRS` | `Projektets vertikala koordinatsystem` | `Projektets vertikala koordinatreferenssystem` |
| `Project coordinate reference system is set to a compound CRS (%1), so the project's vertical CRS is the vertical component of this CRS (%2).` | `Projektets koordinatsystem är satt till ett sammansatt koordinatsystem (%1), så projektets vertikala koordinatsystem är den vertikala komponenten av detta (%2).` | `Projektets koordinatreferenssystem är ett sammansatt CRS (%1), så projektets vertikala CRS är den vertikala komponenten i detta CRS (%2).` |
| `Project coordinate reference system is set to a geographic 3D CRS (%1), so the vertical CRS cannot be manually specified.` | `Projektets koordinatsystem är satt till ett geografiskt 3D-koordinatsystem (%1), så projektets vertikala koordinatsystem kan inte anges manuellt.` | `Projektets koordinatreferenssystem är ett geografiskt 3D-CRS (%1), så vertikalt CRS kan inte anges manuellt.` |

Tekniska protokoll, filformat, platshållare `%1`, citattecken och
avgränsarsträngen `::|::` ska bevaras vid senare import. Ingen extern ändring
har gjorts.
