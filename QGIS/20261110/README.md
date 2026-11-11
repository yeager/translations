# QGIS: svensk Transifex-granskning 2026-11-10

Källa: Transifex-projektet `qgis/QGIS`, resursen `qgis-application`, språk `sv`.

- Projektets aktuella stabila release verifierad: QGIS 4.2.3, 25 september 2026. Aktuell LTR är 3.44.15.
- Stabilgrenarna `release-3_44-qgis-application`, `release-4_0-qgis-application` och `release-4_2-qgis-application` har inga oöversatta svenska strängar.
- Huvudgrenen hade 195 oöversatta strängar vid start. Efter tio granskade batcher återstår 0.
- Batcherna omfattar 195 strängar i menyer, geobearbetningsfunktioner, lagerfel, konvertering av uttryck, WMS-konfiguration, OAPIF, projektmallar, rastervektorer, tidszoner och gränssnittstext. Samtliga sparades via Transifex API och lästes tillbaka efteråt.
- `raw/` innehåller två oförändrade JSON-exportsidor för de strängar som var oöversatta före den andra batchen, inklusive källkontext.
- Tidigare lokala helfiler användes enbart som historisk referens. De laddades inte upp eftersom de är äldre än den aktuella Transifex-resursen.
- Gitleaks på QGIS-arkivet godkändes. `l10n-lint` på den äldre historiska PO-filen rapporterade 47 fel och 2 443 varningar, vilket bekräftar att den inte får användas som uppladdningskälla.

Status: samtliga tio batcher är uppladdade och mottagna. Transifex visar 0 oöversatta strängar i huvudgrenen samt i stabilgrenarna 3.44, 4.0 och 4.2. Ingen ändring gjordes i stabilgrenarna.

## Pågående fullständig granskning

Efter kompletteringen begärdes en radvis granskning av också redan översatta strängar. En oförändrad källsnapshot från QGIS huvudgren finns i `raw/qgis-application-sv-github-master.ts`; den innehåller 36 407 meddelanden, varav 149 är markerade som ofärdiga i just den källsnapshoten. Den aktuella, oförändrade Transifex-exporten finns i `raw/qgis-application-sv-transifex-live-20261110.ts`; den har 36 515 XML-meddelanden, medan resursens API-attribut `string_count` är 36 514. Transifex huvudresurs är därmed inte identisk med GitHub-snapshoten. Den aktuella Transifex-resursen är auktoritativ för ändringar och uppladdning.

Terminologi används från `terminology.md` samt diskussionsunderlaget `qgis-se-terminologi-for-diskussion.md`. Hittills har 4 677 av 36 514 unika strängar granskats i kontext: 195 tidigare kompletterade strängar, 4 464 unika korrigeringskandidater och 18 ytterligare strängar som bedömts korrekta utan ändring. Fem dubbla granskningsposter visade sig ha samma Transifex-ID och har slagits ihop vid beräkning och import. Återstår 31 837 strängar. Fullständig granskning av befintliga översättningar är påbörjad men ännu inte klar; statusen ovan avser endast att oöversatta strängar har kompletterats.

`local-review-archive.md` är revisionsregistret för batcherna 044–254 och
deras lokala commits. Det markerar uttryckligen vad som ännu inte har laddats
upp till Transifex.

`deltas/qgis-application-sv-pending-269-274.json` är ett maskinläsbart
granskningsmanifest för de senaste batcherna. Det är inte en uppladdningsfil:
varje rad måste först slås upp mot aktuell Transifex-enhet och dess måltext.

`deltas/qgis-application-sv-pending-253-274.json` är den sammanhängande,
validerade manifestfilen för batch 253–274 med 160 kandidater. Den ersätter
inte den mindre filen, men är det primära underlaget inför nästa samlade
Transifex-delta.

`deltas/qgis-application-sv-pending-253-276.json` är den aktuella primära
manifestfilen. Den omfattar batch 253–276 och 171 kandidater; den tidigare
253–274-filen bevaras som ett arkiverat mellanläge.

`deltas/qgis-application-sv-pending-253-277.json` är den nuvarande primära
manifestfilen. Den omfattar batch 253–277 och 175 kandidater; den tidigare
253–276-filen bevaras som ett arkiverat mellanläge.

`deltas/qgis-application-sv-pending-253-278.json` är den nuvarande primära
manifestfilen. Den omfattar batch 253–278 och 182 kandidater; den tidigare
253–277-filen bevaras som ett arkiverat mellanläge.

`deltas/qgis-application-sv-pending-253-279.json` är den nuvarande primära
manifestfilen. Den omfattar batch 253–279 och 185 kandidater.

`deltas/qgis-application-sv-pending-280.json` innehåller en ny kandidat
från den lokala granskningen av den exporterade Transifex-filen. Även denna
manifestfil är endast ett granskningsunderlag och saknar Transifex-enhets-ID:n.

`scripts/extract-review-manifest.mjs` bygger och validerar ett sådant manifest
från ett angivet sammanhängande batchintervall. Verktyget avbryter om en
källsträng inte återfinns i den oförändrade Transifex-exporten.

2026-11-11: Batch 253 rättar kvarvarande SpatiaLite-fel och en åtgärdstext.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 254 rättar tabellformatering, miniatyrer och TCP-fel.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 255 rättar M3C2-verktygets punktmolnstexter och normaliserar
`subsampling` till `delurval`. Ändringarna är lokalt granskade och inte
skickade externt.

2026-11-11: Batch 256 rättar M3C2-parameteretiketter, mätfel och hjälptexter.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 257 rättar DTM-lutningsfiltrets cell-, kärn- och terrängtexter.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 258 rättar DTM-lutningsfiltrets konfidens- och utdatahjälp.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 259 rättar GRASS-providerns kartuppsättnings- och
katalogfel. Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 260 rättar GPX-datakällan och GRASS-providerns feltexter.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 261 rättar MSSQL-datakällans laddnings- och stilfel.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 262 rättar SAP HANA-datakällans schema- och CRS-fel.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 263 rättar OGR-providerns datakälls- och drivrutinstexter.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 264 rättar OGR-providerns felkategorier, metadata och
filgränser. Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 265 rättar OGR-providerns status- och fältexporttexter.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 266 rättar Oracle-providerns datakälls-, lager- och
metadatafel. Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 267 rättar Oracle-providerns stiltabeller och SQL-fel.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 268 rättar PostgreSQL-providerns markör-, lager- och
lagerstilsfel. Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 269 rättar SpatiaLite-providerns SQL-, metadata- och
stilfel. Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 270 rättar statusfältets kartutbrednings- och
koordinattexter. Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 271 rättar tidsnavigeringens lägesval och direktuppdatering.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 272 rättar textformatets grundval och radinställningar.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 273 rättar etikettrotation och visningsinställningar.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 274 rättar etikettens skalregler och dubbletthantering.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Källsträngarna för två koordinatrader i batch 270 korrigerades
efter validering mot råexporten. De är kartkoordinater, inte kartutbredningar.
Manifestet uppdaterades samtidigt. Ändringarna är lokala och inte skickade
externt.

2026-11-11: Batch 275 rättar vektorfältets enhets-, skala- och partikeltexter.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 276 rättar startfel för vektorredigering och transaktioner.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 277 rättar QGIS programinformation och konsekvent svensk
versalhantering. Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 278 rättar GRASS rumtidsdata och rasterbeskrivningar.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 279 rättar GRASS provtagning och indelning.
2026-11-11: Batch 280 granskar rasterklippning och Cloud Optimized GeoTIFF.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 281 granskar algoritmdialoger samt GDAL- och FieldPyculator-fel.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 282 granskar GRASS-raster och nätverksparametrar.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 286 rättar bearbetningsalgoritmen `Interpolate (Data metrics)`.
I denna kontext betyder `data metrics` datamått, inte datanätverk. Ändringen är
lokalt granskad och inskickad som Transifex-förslag. Kontot saknar behörighet
att tillämpa ändringen direkt.

2026-11-11: Terminologilistan kompletterades med SpatiaLite, libspatialite,
`ROWID`, miniatyr och socket från batch 253–254. Uppdateringen är lokal och
används vid fortsatt granskning.

2026-11-10: Diskussionsunderlaget för Qgis.se utökades till 402 termer. Det
täcker QGIS huvudsakliga användargränssnitt, geodata, geometri, CRS,
redigering, symbologi, raster, 3D, tid, layout, geobearbetning, formulär,
metadata, datakällor, OGC-tjänster, säkerhet och nätverksanalys. Termer med
faktisk alternativ praxis är märkta `Öppen`; de är frågor för Qgis.se och inte
förutbestämda översättningar.

2026-11-10: Batch 167 rättar mallade linjer, omformning och vektorfält.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 168 rättar topologikontrollens panel och felmeddelanden.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 169 rättar uttryck, höjdkurvor och kartytans utbredning.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 170 rättar GDAL-verktygens rutor och rastertexter.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 171 rättar GDAL-rasterkalkylatorns parametrar.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 172 rättar GRASS-modulernas grundläggande parametrar.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 173 rättar GRASS-modulernas visning och export.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 174 rättar GRASS-modulernas import och interpolering.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 175 rättar GRASS-modulernas datamängder, regioner och topologi.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 176 rättar GRASS-modulernas tid och vektoranalyser.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 177 rättar OGR-konvertering, skuggning och pansharp.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 178 rättar närhetsanalys, rasterisering och rutindelning.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 179 rättar QGIS-variabler och projektmetadata.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 180 rättar layout, atlas och kartvariabler.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 181 rättar atlasexport och täckningslager.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 182 rättar atlaspanelen och dess inställningar.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 183 rättar attributtabeller i layoutdesignern.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 184 rättar atlasåtgärder och export i layoutdesignern.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 185 rättar layoutdesignerns mallar, export och utskrift.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 186 rättar layoutrapporter och vektorexport.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 187 rättar höjdprofil och hjälplinjer i layoutdesignern.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 188 rättar teckenförklaringen i layoutdesignern.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 189 rättar kartklippning i layoutdesignern.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 190 rättar kartrutnät i layoutdesignern.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 191 rättar kartobjekt och atlasstyrning i layoutdesignern.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 192 rättar kartyta och markör i layoutdesignern.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 193 rättar skalstock i layoutdesignern.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 194 rättar layoutelement, sidor och former.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 195 rättar layouttabellens färgsättning och inställningar.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 196 rättar 3D-ljus och linjediagram.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 197 rättar linjediagram, linjära referenser och rasterattributtabeller.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 198 rättar sökare, validering och anslutningar.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 199 rättar kartyta och koordinatreferenssystem.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 200 rättar kartlager och koordinatreferenser.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 201 rättar lagerstilar, uppdateringar och servermetadata.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 202 rättar stilkategorier och kartexport.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 203 rättar kartexport, kartteman och digitalisering.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 204 rättar redigeringsverktyg och nätredigering.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 205 rättar objektmatrisen och identifieringsverktyget.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 206 rättar etikettflytt och förskjutningsverktyg.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 207 rättar punkt- och topologiverktyg.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 208 rättar delning, maskning och mätning.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 209 rättar mätning, minneslager och 3D-nät.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 210 rättar nätkalkylatorn och datamängdsgrupper.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 211 rättar nätredigering och höjdegenskaper.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 212 rättar nätlageregenskaper och vertikal utvärdering.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 213 rättar nättransformation och meddelandelogg.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 214 rättar metadatabeskrivning och åtkomst.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 215 rättar metadataomfattning och modellredigerare.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 216 rättar modellfiler och körning.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 217 rättar modellcanvas och komponenter.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 218 rättar MSSQL-anslutningar och geometri.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 219 rättar MSSQL-frågor och flerredigering.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 220 rättar ArcGIS-anslutningar och GeoPackage.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 221 rättar GeoPackage-fält och HTTP-anslutning.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 222 rättar minneslager, nät och SpatiaLite.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 223 rättar SpatiaLite och vektortabeller.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 224 rättar OWS-cache och OAPIF.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 225 rättar OAPIF och offlineredigering.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 226 rättar OGR-providern och vektorkällor.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 227 rättar inställningar och miljövariabler.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 228 rättar inställningar för CRS och digitalisering.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 229 rättar mätningar, projekttillit och Oracle-anslutningar.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 230 rättar Oracle-providerns transaktioner och metadatafel.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 231 rättar tabellkolumner, raster och PostgreSQL-anslutningar.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 232 rättar PostgreSQL, diagram och tilläggshanteraren.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 233 rättar tilläggsinstalleraren och förrådshanteringen.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 234 rättar punktmolnens 3D- och höjdinställningar.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 235 rättar punktmolnens export-, filter- och källdialoger.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 236 rättar punktmönster, 3D-objekt och PostgreSQL-fel.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 237 rättar PostgreSQL-projektlagring, raster och tidsfält.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 238 rättar geobearbetningens algoritmer, raster och parametrar.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 239 rättar geobearbetningens inmatning, utdata och fältparametrar.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 240 rättar geobearbetningens modeller, nätdata och flervalsdialoger.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 241 rättar geobearbetningens skript och projektmeddelanden.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 242 rättar projektets höjdinställningar och egenskaper.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 243 rättar projektmetadata, server och tillit.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-11: Batch 235 har justerats lokalt så att rekommendationen använder
`etikettens text` i stället för en sammansättning med tre likadana konsonanter.
Ändringen är arkiverad och inte skickad externt.

2026-11-11: Batch 244 rättar CRS-väljaren och datadefinierade egenskaper.
Ändringarna är lokalt granskade och inte skickade externt.

## Översättningsminne

De verifierade QGIS-rättningarna finns i [yeager/swedish-tm](https://github.com/yeager/swedish-tm). Uppdateringen omfattar sju kontextfria QGIS-termer i `sv-qgis.po` och `sv-qgis.tmx`, samt 281 kontextbevarade granskningsposter med 286 segment i den separata QGIS-katalogen. Efter den verifierade Transifex-importen har 212 granskningsposter, som motsvarar 207 unika Transifex-strängar, status `upstream-import-verified`. Resterande 69 unika strängar har status `local-reviewed-pending-upload`. Bland dem finns 68 låsta, granskade strängar och en förberedd men ännu inte sparad rättning i Transifex.

2026-11-10: En samlad Transifex-batch med 35 verifierade ändringar skickades till den dokumenterade bulkändpunkten. Tjänsten svarade HTTP 500 med `server_error`; fyra representativa återläsningar bekräftade att ingen partiell ändring hade tillämpats. Efter batch 006 försöktes den samlade 44-strängarsbatchen på nytt och fick samma HTTP 500-svar. Återläsning av två nya och en tidigare kandidat bekräftade åter att ingen partiell ändring hade tillämpats. Batcherna 001 till 010 är arkiverade men ännu inte uppladdade.

2026-11-10: Transifex API:s dokumenterade bulkprofil användes med högst 150
strängar per anrop. Den första förkontrollen gav 41 och den andra 26 explicita
`permission_denied`-svar för redan granskade strängar. Efter att de låsta
strängarna filtrerats bort accepterade Transifex 108 respektive 93 unika
översättningar. Fyra dubbletter normaliserades och lästes tillbaka. Tre
separata GET-kontroller bekräftade slutvärde och ursprunget `API`; de importerade
strängarna är ännu inte markerade som granskade i Transifex. Deltafilerna och
det exakta uppladdningsutfallet finns i batch 038.

2026-11-10: Batch 039 rättade tre oblockerade stavfel i datum- och
terrängsträngar. Transifex accepterade alla tre via API och direkta
återläsningar bekräftade svensk måltext samt ursprunget `API`.

2026-11-10: Batch 040 rättade två oavsiktliga ordupprepningar. Transifex
accepterade båda via API och direkta återläsningar bekräftade svensk måltext
samt ursprunget `API`. Batch 041 ersatte den för snäva metadataetiketten
`Län` med `Administrativt område`. Transifex accepterade ändringen och den
inloggade redigeraren bekräftade sedan måltext, kontext, hash och upphov.

2026-11-10: Batch 042 dokumenterar den låsta WCS-etiketten `Native CRS`.
Rekommendationen `Ursprungligt koordinatreferenssystem` rättar både stavfelet
och QGIS-terminologin, men den befintliga översättningen är granskad och kan
inte ändras med aktuell behörighet.

2026-11-10: Batch 043 rättar uttrycksfunktionens hjälptext för
`map_prefix_keys`. Ändringen är lokalt arkiverad och förberedd i
Transifex-redigeraren, men inte sparad upstream ännu.

2026-11-10: Batch 044 dokumenterar en lokal rättning av den dubblerade
GRASS-parameteretiketten `Input input raster layer`. Den rekommenderade
svenska texten är `Indatarasterlager`; ingen extern ändring har gjorts.

2026-11-10: Batch 045 rättar beskrivningen av algoritmen för export till
kalkylblad. Ändringen är lokalt arkiverad; ingen extern ändring har gjorts.

2026-11-10: Batch 046 rättar felmeddelandet för export utan valda lager.
Ändringen är lokalt arkiverad; ingen extern ändring har gjorts.

2026-11-10: Batch 047 normaliserar `gap` till `glapp` i QGIS
geometrikontroll och rättar 16 relaterade texter. Terminologin är uppdaterad;
ändringarna är lokalt arkiverade och inte skickade externt.

2026-11-10: Batch 048 normaliserar de korta glappetiketterna och dess
algoritmsökord. Ändringarna är lokalt arkiverade och inte skickade externt.

2026-11-10: Batch 049 rättar två lageretiketter i glapparbetsflödet.
Ändringarna är lokalt arkiverade och inte skickade externt.

2026-11-10: Batch 050 rättar två feltexter vid vektorexport. Ändringarna är
lokalt arkiverade och inte skickade externt.

2026-11-10: Batch 051 rättar PostGIS-inställningen för icke-linjära
geometrityper. Ändringen är lokalt arkiverad och inte skickad externt.

2026-11-10: Terminologin kompletterades med `geometrityp`, `icke-linjär
geometrityp` och `vektorexport` för QGIS vektorexportflöden.

2026-11-10: Batch 052 rättar GPSBabels enhets- och GPX-texter och kompletterar
terminologin med GPSBabels användning av `waypoint`, `route` och `track`.
Ändringarna är lokalt arkiverade och inte skickade externt.

2026-11-10: Batch 053 rättar GPSBabels konverteringshjälp, korttext,
kommandoetikett och svenska sökord. Ändringarna är lokalt arkiverade och inte
skickade externt.

2026-11-10: Batch 054 rättar rasterlageregenskapernas etiketter, sökord och
hjälptexter. Ändringarna är lokalt arkiverade och inte skickade externt.

2026-11-10: Batch 055 rättar algoritmbeskrivningen för rundhet. Ändringen är
lokalt arkiverad och inte skickad externt.

2026-11-10: Batch 056 rättar status- och feltexter för SQL-lager. Ändringarna
är lokalt arkiverade och inte skickade externt.

2026-11-10: Batch 057 rättar hjälptesten och UI-etiketter för algoritmen
Kortaste linjer. Ändringarna är lokalt arkiverade och inte skickade externt.

2026-11-10: Batch 058 rättar rubrik och parametertexter för ST-DBSCAN.
Ändringarna är lokalt arkiverade och inte skickade externt.

2026-11-10: `pending-local-review-index.md` samlar batcherna 044–058 som
väntar på uppslag av aktuella Transifex-enheter innan en deltafil kan skapas.

2026-11-10: Batch 059 rättar två standardinställningar för layoutelement.
Ändringarna är lokalt arkiverade och inte skickade externt.

2026-11-10: Batch 060 rättar LAS-klasserna för punktmoln. Ändringarna är
lokalt arkiverade och inte skickade externt.

2026-11-10: Batch 061 rättar geobearbetningsinställningar och API-hjälp.
Ändringarna är lokalt arkiverade och inte skickade externt.

2026-11-10: Batch 062 rättar QGIS-åtgärder och HTTP-etiketter. Ändringarna är
lokalt arkiverade och inte skickade externt.

2026-11-10: Batch 063 rättar kärn- och symbologietiketter. Ändringarna är
lokalt arkiverade och inte skickade externt.

2026-11-10: Batch 064 rättar datakälle- och importdialoger. Ändringarna är
lokalt arkiverade och inte skickade externt.

2026-11-10: Batch 065 rättar feltexter för läsning av vektorrutepaket.
Ändringarna är lokalt arkiverade och inte skickade externt.

2026-11-10: Batch 066 rättar inställningar för georefereraren,
geometriverktyg och en CRS-axelförkortning. Ändringarna är lokalt arkiverade
och inte skickade externt.

2026-11-10: Batch 067 rättar UI-stavning och en kortkommandohjälptext.
Ändringarna är lokalt arkiverade och inte skickade externt.

2026-11-10: Batch 068 rättar konsolens API-inställningar. Ändringarna är
lokalt arkiverade och inte skickade externt.

2026-11-10: Batch 069 rättar GDAL-, vektor- och skripttexter. Ändringarna är
lokalt arkiverade och inte skickade externt.

2026-11-10: Batch 070 normaliserar *map canvas* till kartvy i
dekorationernas verktygstips. Ändringarna är lokalt granskade och inte
skickade externt.

2026-11-10: Batch 071 rättar lager- och rasteråtgärder i huvudfönstret.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 072 rättar GRASS-felmeddelanden och formulärwidgets.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 073 normaliserar vektorrutor i bearbetningsverktygen.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 074 normaliserar utbredning i bearbetningsverktygen.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 075 rättar GRASS-parametrar och GEOS valideringsfel.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 076 normaliserar layout- och teckenförklaringstexter.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 077 rättar autentisering och certifikatstatus.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 078 rättar etiketter i 3D-kartkonfigurationen.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 079 drar tillbaka den lokala kandidaten för `Eye Dome
Lighting`. Det tekniska namnet behålls enligt terminologilistan; ingen
översättningsändring ska skickas externt.

2026-11-10: Batch 080 rättar status och åtgärder i geobearbetningsdialogen.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 081 rättar resultat och fel för datakällsanslutningar.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 082 rättar tilläggshanterarens statusrader och
åtgärdsbeskrivningar. Ändringarna är lokalt granskade och inte skickade
externt.

2026-11-10: Batch 083 rättar tilläggshanterarens filter, knappar och
hjälptext. Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 084 rättar tilläggshanterarens hämtning, status och
feltexter. Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 085 rättar tilläggshanterarens instruktioner och
säkerhetsvarning. Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 086 rättar centralkataloger och tilläggskategorier.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 087 rättar tilläggsinstallation och beroendehantering.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 088 rättar installationsfel, ZIP-filer och katalogåtgärder.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 089 rättar nätverksstatus och överföringsfel för tillägg.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 090 rättar tilläggshanterarens kontextbundna hjälptexter.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 091 dokumenterar 14 korrekta status- och UI-texter och
avslutar den lokala granskningen av QGIS tilläggsflöde. Ingen extern ändring
har gjorts för de oförändrade texterna.

2026-11-10: Batch 092 rättar 3D-punktsymboler och punktmolnsrendering.
Terminologin kompletteras med `Billboard` och den öppna UI-termen `skärmfel`.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 093 rättar punktmolnshöjd och vertikala CRS-inställningar.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 094 rättar punktmolnslagrets metadata och egenskaper.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 095 rättar punktmolnsfrågor och rendering. `Eye Dome
Lighting` behålls som tekniskt namn. Ändringarna är lokalt granskade och inte
skickade externt.

2026-11-10: Batch 096 rättar punktmolnsexport och Spara som-dialogen.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 124 rättar nätåtergivning och rapportlayouter.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 125 rättar riktextredigerarens filfilter och regelbaserad
rendering. Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 126 rättar Spatialite-fel, SQL-frågebyggaren,
skalinställningar och sökfrågor. Ändringarna är lokalt granskade och inte
skickade externt.

2026-11-10: Batch 127 rättar SensorThings-anslutningar och bevarar
SensorThings API-entiteter som synliga tekniska namn. Ändringarna är lokalt
granskade och inte skickade externt.

2026-11-10: Batch 128 rättar SensorThings-filter, seriella portar och några
symbologi- och geometrikontroller. Ändringarna är lokalt granskade och inte
skickade externt.

2026-11-10: Batch 129 rättar symbologi och normaliserar QGIS-termen
`snäppning`. Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 130 rättar snäppning, fältegenskaper och SpatiaLite-dialoger.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 131 rättar SpatiaLite-felhantering och STAC-katalogernas
svenska UI-text. Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 132 rättar diagram, statistik, statusfält och stilhantering.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 133 rättar stilhanteraren och symbolbiblioteket.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 134 rättar stilhanterarens valideringar, pluralformer och
stildatabaser. Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 135 rättar stilbibliotek, textsubstitutioner och SVG-export.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 136 rättar 3D-symboler, animation, symbolbuffertar och
tabelleditorn. Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 137 rättar tabelleditorns pluralformer, aktivitetsstatus och
linjesymbolernas instruktioner. Ändringarna är lokalt granskade och inte
skickade externt.

2026-11-10: Batch 138 rättar tidsnavigering, JSON-validering och textformat.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 139 rättar etikettplacering och texttypografi.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 140 rättar textformatets layout, buffert och
etikettplacering. Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 141 rättar etikettplacering, hinder, maskning och
skalgränser. Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 142 rättar rutindelade scener, tjänsteanslutningar och
3D-lager. Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 143 rättar scendata och georefereringens
transformationsinställningar. Ändringarna är lokalt granskade och inte
skickade externt.

2026-11-10: Batch 144 rättar georeferering, GPS-åtgärder och
användarprofiler. Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 145 rättar värdekartor, vektorleverantörens funktioner och
höjdinställningar. Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 146 rättar vektorlagers höjdmodell och
vektorfältsrendering. Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 147 rättar vektorlager, 3D-inställningar och digitalisering.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 148 rättar vektorredigering, transaktioner och
teckenförklaringar. Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 149 rättar lageregenskaper, attributkopplingar och
datakällenotiser. Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 150 rättar förenkling, karttips och vektorexport.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 151 rättar vektorexport och tidsstyrning.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 152 rättar vektorrutor, anslutningar och rendererfel.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 153 rättar vektorrutor, export och brytpunktsredigeraren.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 154 rättar virtuella lager, VPC-filer och VTPK-terminologi.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 155 rättar WFS-svar, parserfel och förfrågningar.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 156 rättar WFS- och WMS-anslutningar.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 157 rättar WCS-svar, tjänstefel och täckningsinformation.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 158 rättar WMS-fel, rutlager och rutmatrisuppsättningar.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 159 rättar WMS-T, XYZ och fel vid ruthämtning.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 160 rättar slumppunkter, rasterkalkylator och histogram.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 161 rättar former, skript och stilalgoritmer.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 162 rättar inställningar, säkerhet och buffertverktyg.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 163 rättar topologisk färgsättning och variabla buffertar.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 164 rättar diagram och symbolplacering.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 165 rättar fyllningar, gradienter och markörer.
Ändringarna är lokalt granskade och inte skickade externt.

2026-11-10: Batch 166 rättar SVG-symboler, sensorer och linjesymboler.
Ändringarna är lokalt granskade och inte skickade externt.
