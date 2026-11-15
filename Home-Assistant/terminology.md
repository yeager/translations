# Home Assistant: svenska termer

Senast uppdaterad: 2026-11-14

Listan innehåller beslut som är kontrollerade i Home Assistants konkreta
entitets- och UI-kontext. Den är inte en generell ordlista och ersätter inte
källtextens sammanhang.

| Engelska | Svenska | Kontext och kommentar |
| --- | --- | --- |
| cloud services | molntjänster | HP Printer, binär sensors etikett för tillgängliga tjänster. |
| cloud registered | registrerad i molnet | HP Printer, registreringsstatus. |
| paper jam | pappersstopp | HP Printer, skrivarfel och räknarstatus. |
| scanner jam | pappersstopp i dokumentmataren | HP Printer, pappersstopp i dokumentmataren enligt komponentens dokumentation. |
| printed pages | utskrivna sidor | HP Printer, ackumulerad räknare. |
| copied pages | kopierade sidor | HP Printer, ackumulerad räknare. |
| scanned pages | skannade sidor | HP Printer, ackumulerad räknare. |
| faxed pages | faxade sidor | HP Printer, ackumulerad räknare. |
| scanned pages from glass | skannade sidor från skannerglaset | HP Printer, flatbäddsskannerns räknare; förtydligar att glaset är skannerns. |
| copied black and white pages | kopierade svartvita sidor | HP Printer, räknare för svartvita kopior. |
| copied color pages | kopierade färgsidor | HP Printer, räknare för färgkopior. |
| close door or cover | stäng luckan eller locket | HP Printer, aktiv åtgärdsstatus. |
| shutting down | stängs av | HP Printer, pågående status. |
| manufacturing date | tillverkningsdatum | HP Printer, informationsfält. |
| paper mispicks | pappersmatningsfel | HP Printer, räknare för misslyckade pappersmatningar. |
| scanner mispicks | matningsfel i dokumentmataren | HP Printer, räknare för misslyckade matningar i dokumentmataren. |
| faxed pages from document feeder | faxade sidor från dokumentmataren | HP Printer, faxräknare. |
| faxed pages from glass | faxade sidor från skannerglaset | HP Printer, faxräknare via skannerglaset. |
| faxed pages from computer | faxade sidor från datorn | HP Printer, faxräknare för datorutskick. |
| consumable installation date | installationsdatum för [färg] patron | HP Printer, datum då en bläck- eller tonerpatron installerades. |
| consumable level | nivå för [färg] patron | HP Printer, procentuell kvarvarande mängd för patronen. |
| consumable manufacturing date | tillverkningsdatum för [färg] patron | HP Printer, informationsfält. |
| consumable pages printed | utskrivna sidor med [färg] patron | HP Printer, ackumulerad patronräknare. |
| consumable pages remaining | återstående sidor för [färg] patron | HP Printer, uppskattning för patronen. |
| consumable warranty expiration date | garantins utgångsdatum för [färg] patron | HP Printer, informationsfält. |
| genuine refills | äkta påfyllningar för [färg] patron | HP Printer, diagnostisk ackumulerande räknare. |
| counterfeit refills | förfalskade påfyllningar för [färg] patron | HP Printer, diagnostisk ackumulerande räknare. |
| indoor humidity | luftfuktighet inomhus | Helty Cloud och andra klimatentiteter; egenskapsnamn. |
| indoor temperature | inomhustemperatur | Helty Cloud och andra klimatentiteter; egenskapsnamn. |
| outdoor temperature | utomhustemperatur | Helty Cloud och andra klimatentiteter; egenskapsnamn. |

## Status

De två molnstatusetiketterna, `scanner_jams`, fem räknaretiketter, tre
skrivarstatusvärden, tre matnings- och informationsfält samt tre faxräknare är
sparade i Lokalise och återlästa där. Övriga texter i batch 41–45 var redan
korrekta vid den oberoende verifieringen.

Batch 48 omfattar 30 sparade och återlästa patronfält för svart, cyan,
magenta, trefärg och gul patron. Påfyllningsräknare är medvetet utelämnade
i väntan på en tydligare betydelsekontroll. Den kontrollen är nu genomförd:
batch 50 omfattar tio sparade och återlästa diagnostiska
påfyllningsräknare.
