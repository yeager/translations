# QGIS: layoutrapport och vektorexport 186

Datum: 11 november 2026
Resurs: `qgis-application`, språk `sv`
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen granskar rapportexport, WMS-varningar och vektorexport i
layoutdesignern. WMS, WIDTH, HEIGHT, PDF och SVG bevaras som protokoll,
parametrar och formatnamn. `Path` i textvektorexport återges som `bana`.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Error: No coverage layer is set.` | `Fel: Inget kartbokslager är inställt.` | `Fel: Inget täckningslager har angetts.` |
| `Output file name expression is not valid. Canceling.\nEvaluation error: %1` | `Uttrycket för filnamnet för utdata är inte giltigt. Avbryter.\nUtvärderingsfel: %1` | `Uttrycket för utdatafilnamnet är inte giltigt. Avbryter.\nUtvärderingsfel: %1` |
| `Export Atlas as PDF` | `Exportera Kartbok som PDF` | `Exportera atlas som PDF` |
| `Rendering report…` | `Renderar rapport…` | `Återger rapport…` |
| `Export Report as SVG` | `Exportera Rapport som SVG` | `Exportera rapport som SVG` |
| `Error encountered while exporting report.` | `Fel uppstod under export av rapport.` | `Ett fel uppstod när rapporten exporterades.` |
| `Export Report as PDF` | `Exportera Rapport som PDF` | `Exportera rapport som PDF` |
| `Successfully printed report to %1.` | `Lyckades skriva ut rapport till %1.` | `Rapporten har skrivits ut till %1.` |
| `Successfully printed report.` | `Lyckades skriva ut rapport.` | `Rapporten har skrivits ut.` |
| `Error encountered while printing report.` | `Fel uppstod under utskrift av rapport.` | `Ett fel uppstod när rapporten skrevs ut.` |
| `Some WMS servers (e.g. UMN mapserver) have a limit for the WIDTH and HEIGHT parameter. Printing layers from such servers may exceed this limit. If this is the case, the WMS layer will not be printed` | `En del WMS-servrar (tex UMN mapserver) har begränsningar för parametrarna WIDTH och HEIGHT. Skriver du ut sådana lager kan de gränserna överskridas. Om så är fallet, skrivs WMS-lagret inte ut` | `Vissa WMS-servrar, till exempel UMN MapServer, har en gräns för parametrarna WIDTH och HEIGHT. Utskrift av lager från sådana servrar kan överskrida gränsen. I så fall skrivs inte WMS-lagret ut.` |
| `If you require a vector-based output file from QGIS it is suggested that you try exporting to PDF if the SVG output is not satisfactory.&lt;/p&gt;` | `Om du behöver en vektorbaserad utskrift från QGIS, föreslår vi att du försöker skriva till PDF, om du inte är nöjd med resultatet från SVG.&lt;/p&gt;` | `Om du behöver en vektorbaserad utdatafil från QGIS bör du prova att exportera till PDF om SVG-resultatet inte är tillfredsställande.&lt;/p&gt;` |
| `Composition Effects` | `Sammansättningseffekt` | `Layouteffekter` |
| `Advanced composition effects such as blend modes or vector layer transparency are enabled in this layout, which cannot be printed as vectors. Printing as a raster is recommended.` | `Avancerade kompositionseffekter som blandningsläge eller vektorlager opacitet är aktiverade för detta lager, vilka inte kan skrivas ut som vektorer. Utskrift som raster är rekommenderat.` | `Avancerade layouteffekter, som blandningslägen eller genomskinlighet för vektorlager, är aktiverade i layouten. De kan inte skrivas ut som vektorer. Utskrift som raster rekommenderas.` |
| `Force Vector` | `Tvinga vektoriserad utskrift` | `Tvinga vektoråtergivning` |
| `This layout has the &quot;Always export as vectors&quot; option enabled, but the layout contains effects such as blend modes or vector layer transparency, which cannot be printed as vectors. The generated file will differ from the layout contents.` | `Denna layout har &quot;Exportera alltid som vektor&quot; alternativet aktiverat, men layouten innehåller effekter som blandningsläge eller vektorlager opacitet, vilket inte kan skrivas ut som vektor. Den genererade filen kommer att skilja sig från layoutinnehållet.` | `Alternativet &quot;Exportera alltid som vektorer&quot; är aktiverat för layouten, men layouten innehåller effekter som blandningslägen eller genomskinlighet för vektorlager. De kan inte skrivas ut som vektorer. Den skapade filen kommer därför att skilja sig från layoutens innehåll.` |
| `Export Layout` | `Exporterar layout` | `Exportera layout` |
| `Always Export Text as Paths (Recommended)` | `Exportera alltid text som linjer (rekommenderas)` | `Exportera alltid text som banor (rekommenderas)` |
| `Always Export Text as Text Objects` | `Exportera alltid text som objekt` | `Exportera alltid text som textobjekt` |
| `Atlas feature %1 has no geometry — linked map extents cannot be updated` | `Atlasobjekt %1 har ingen geometri — länkad kartutsträckning kan inte uppdateras` | `Atlasobjektet %1 saknar geometri — kopplade kartutbredningar kan inte uppdateras` |
| `atlas` | `kartbok` | `atlas` |
| `&amp;Duplicate Layout…` | `&amp;Duplicera Layout…` | `&amp;Duplicera layout…` |
| `Delete Layout…` | `Radera Layout…` | `Ta bort layout…` |
| `Rename Layout…` | `Byt namn på Layout…` | `Byt namn på layout…` |
| `New Layout…` | `Ny Layout…` | `Ny layout…` |
| `&amp;Duplicate Report…` | `&amp;Duplicera Rapport…` | `&amp;Duplicera rapport…` |
| `Delete Report…` | `Radera Rapport…` | `Ta bort rapport…` |
| `Rename Report…` | `Byt namn på Rapport…` | `Byt namn på rapport…` |
| `New Report…` | `Ny Rapport…` | `Ny rapport…` |
| `The layout generated the following warnings. Please review and address these before proceeding with the layout export.` | `Layouten genererade följande varningar. Kontrollera och åtgärda dessa innan fortsättning av layoutexporten. ` | `Layouten gav följande varningar. Granska och åtgärda dem innan du fortsätter med layoutexporten.` |

Ingen extern ändring har gjorts. Aktuella Transifex-enhetsidentifierare måste
hämtas och måltexterna jämföras före en separat deltafil kan skapas.
