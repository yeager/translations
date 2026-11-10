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

Terminologi används från `terminology.md` samt diskussionsunderlaget `qgis-se-terminologi-for-diskussion.md`. Hittills har 472 av 36 514 unika strängar granskats i kontext: 195 tidigare kompletterade strängar, 276 unika korrigeringskandidater och en ytterligare sträng som bedömts korrekt utan ändring. Fem dubbla granskningsposter visade sig ha samma Transifex-ID och har slagits ihop vid beräkning och import. Återstår 36 042 strängar. Fullständig granskning av befintliga översättningar är påbörjad men ännu inte klar; statusen ovan avser endast att oöversatta strängar har kompletterats.

2026-11-10: Diskussionsunderlaget för Qgis.se utökades till 390 termer. Det
täcker QGIS huvudsakliga användargränssnitt, geodata, geometri, CRS,
redigering, symbologi, raster, 3D, tid, layout, geobearbetning, formulär,
metadata, datakällor, OGC-tjänster, säkerhet och nätverksanalys. Termer med
faktisk alternativ praxis är märkta `Öppen`; de är frågor för Qgis.se och inte
förutbestämda översättningar.

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
