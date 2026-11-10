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

Terminologi används från `terminology.md` samt diskussionsunderlaget `qgis-se-terminologi-for-diskussion.md`. Hittills har 463 av 36 514 strängar granskats i kontext, varav 267 är lokalt granskade korrigeringskandidater och en ytterligare sträng har bedömts korrekt utan ändring. Återstår 36 051 strängar. Fullständig granskning av befintliga översättningar är påbörjad men ännu inte klar; statusen ovan avser endast att oöversatta strängar har kompletterats.

## Översättningsminne

De verifierade QGIS-rättningarna har publicerats i [yeager/swedish-tm](https://github.com/yeager/swedish-tm), senast i commit [`87c5118`](https://github.com/yeager/swedish-tm/commit/87c5118). Uppdateringen omfattar sju kontextfria QGIS-termer i `sv-qgis.po` och `sv-qgis.tmx`, samt 267 kontextbevarade granskningsposter med 272 segment i den separata QGIS-katalogen. Posterna har status `local-reviewed-pending-upload`, eftersom Transifex bulk-PATCH ännu inte har godkänts av tjänsten.

2026-11-10: En samlad Transifex-batch med 35 verifierade ändringar skickades till den dokumenterade bulkändpunkten. Tjänsten svarade HTTP 500 med `server_error`; fyra representativa återläsningar bekräftade att ingen partiell ändring hade tillämpats. Efter batch 006 försöktes den samlade 44-strängarsbatchen på nytt och fick samma HTTP 500-svar. Återläsning av två nya och en tidigare kandidat bekräftade åter att ingen partiell ändring hade tillämpats. Batcherna 001 till 010 är arkiverade men ännu inte uppladdade.
