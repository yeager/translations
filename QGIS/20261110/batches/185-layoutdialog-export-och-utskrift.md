# QGIS: layoutdialog, export och utskrift 185

Datum: 11 november 2026
Resurs: `qgis-application`, språk `sv`
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen granskar layoutdesignerns mallar, export och utskrift. CRS, PDF, SVG,
Qt, DPI och HTML-markup är tekniska element som bevaras. Formuleringarna
skiljer tydligt mellan åtgärder, pågående förlopp och bekräftade resultat.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Error creating template file.` | `Fel vid skapande av mall-fil.` | `Det gick inte att skapa mallfilen.` |
| `Could not read template file.` | `Kunde inte läsa mall-fil.` | `Det gick inte att läsa mallfilen.` |
| `Duplicating layout…` | `Duplicera layout…` | `Duplicerar layout…` |
| `&lt;p&gt;The SVG export function in QGIS has several problems due to bugs and deficiencies in the underlying Qt SVG library. In particular, there are problems with layers not being clipped to the map bounding box.&lt;/p&gt;` | `&lt;p&gt;SVG exportfunktionen i QGIS har flera fel beroende på buggar och begränsningar i underliggande Qt SVG-bibliotek. Särskilt finns det problem med att lager inte klipps till kartramen.&lt;/p&gt;` | `&lt;p&gt;SVG-exportfunktionen i QGIS har flera problem på grund av fel och brister i det underliggande Qt SVG-biblioteket. Särskilt kan lager inte alltid klippas till kartans avgränsningsruta.&lt;/p&gt;` |
| `To create an image of %1x%2 requires about %3 of memory. Proceed?` | `Att skapa en bild med %1x%2 kräver ungefär %3 minne. Fortsätta?` | `Att skapa en bild på %1x%2 kräver cirka %3 minne. Vill du fortsätta?` |
| `Prefer Exporting Text as Text Objects` | `Föredra exportera text som objekt` | `Föredra att exportera text som textobjekt` |
| `One or more map items do not have a valid CRS set. This is required for geospatial PDF export.` | `Ett eller flera kartelement har inte ett giltigt koordinatsystem. Detta krävs för export till geospatial PDF.` | `Ett eller flera kartelement saknar ett giltigt koordinatreferenssystem. Detta krävs för geospatial PDF-export.` |
| `One or more map items are rotated. This is not supported for geospatial PDF export.` | `Ett eller flera kartelement är roterade. Detta stöds inte vid export ill geospatial PDF.` | `Ett eller flera kartelement är roterade. Detta stöds inte vid geospatial PDF-export.` |
| `Layout duplication failed.` | `Duplicering av Layout misslyckades.` | `Det gick inte att duplicera layouten.` |
| `Delete Layout` | `Radera Layout` | `Ta bort layout` |
| `Are you sure you want to delete the layout “%1”?` | `Är du säker att du vill radera layout "%1"?` | `Är du säker på att du vill ta bort layouten ”%1”?` |
| `Print layout` | `Utskriftslayout` | `Skriv ut layout` |
| `Memory Allocation Error` | `Minnesfel` | `Minnesallokeringsfel` |
| `Printing the layout resulted in a memory overflow.\n\nPlease try a lower resolution or a smaller paper size.` | `Utskrift av layouten resulterade i minnesproblem.\n\nVar vänlig prova en lägre upplösning eller en mindre pappersstorlek.` | `Utskrift av layouten resulterade i slut på minne.\n\nProva en lägre upplösning eller ett mindre pappersformat.` |
| `Export layout` | `Exporterar layout` | `Exportera layout` |
| `Successfully exported layout to &lt;a href=&quot;%1&quot;&gt;%2&lt;/a&gt;` | `Layout exporterad till &lt;a href=&quot;%1&quot;&gt;%2&lt;/a&gt;` | `Layouten har exporterats till &lt;a href=&quot;%1&quot;&gt;%2&lt;/a&gt;` |
| `Cannot write to %1.\n\nThis file may be open in another application.` | `Kan inte skriva till %1.\n\nFilen kanske är öppen i en annan applikation.` | `Det går inte att skriva till %1.\n\nFilen kan vara öppen i ett annat program.` |
| `Trying to create image %1 (%2×%3 @ %4dpi ) resulted in a memory overflow.\n\nPlease try a lower resolution or a smaller paper size.` | `Skapandet av bilden %1 (%2×%3 @ %4dpi ) orsakade brist på minne.\nVar vänlig försök med en lägre upplösning eller mindre pappersstorlek.` | `När bilden %1 (%2×%3 @ %4 dpi) skapades tog minnet slut.\n\nProva en lägre upplösning eller ett mindre pappersformat.` |
| `Undo History` | `Ångra Historik` | `Ångringshistorik` |
| `%1 Panel` | `%1 Panel` | `%1-panel` |
| `Successfully printed layout to %1.` | `Lyckades med utskrift av layout till %1.` | `Layouten har skrivits ut till %1.` |
| `Successfully printed layout.` | `Lyckades med utskrift av layout.` | `Layouten har skrivits ut.` |
| `Print Layout` | `Utskriftslayout` | `Skriv ut layout` |
| `Exporting the PDF resulted in a memory overflow.\n\nPlease try a lower resolution or a smaller paper size.` | `Export till PDF resulterade i ett minnesproblem.\n\nVar vänlig prova en lägre upplösning eller en mindre pappersstorlek.` | `PDF-exporten resulterade i slut på minne.\n\nProva en lägre upplösning eller ett mindre pappersformat.` |
| `Export to SVG` | `Exportera till SVG` | `Exportera som SVG` |

Ingen extern ändring har gjorts. Aktuella Transifex-enhetsidentifierare måste
hämtas och måltexterna jämföras före en separat deltafil kan skapas.
