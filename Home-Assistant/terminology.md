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

## Status

De två molnstatusetiketterna, `scanner_jams` och räknaren för skannerglaset
är sparade i Lokalise och återlästa där. `jams` och sex övriga räknaretiketter
var redan korrekta vid den oberoende verifieringen. Återstående räknare väntar
på upstream-sparning och separat återläsning.
