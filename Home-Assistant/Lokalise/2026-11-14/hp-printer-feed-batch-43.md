# HP Printer: ark, dokumentmatare och skannerglas, batch 43

Datum: 2026-11-14

Sju räknaretiketter kontrollerades var för sig i Lokalise. Tre svenska texter
var tomma eller för ospecifika och sparades därefter. Övriga var redan
idiomatiskt korrekta och lämnades oförändrade.

| Nyckel | Källa | Svenska efter återläsning | Resultat |
| --- | --- | --- | --- |
| `component::hp_printer::entity::sensor::simplex_sheets::name` | Printed single-sided sheets | Enkelsidigt utskrivna ark | Redan korrekt. |
| `component::hp_printer::entity::sensor::duplex_sheets::name` | Printed double-sided sheets | Dubbelsidigt utskrivna ark | Redan korrekt. |
| `component::hp_printer::entity::sensor::scanned_adf_pages::name` | Scanned pages from document feeder | Skannade sidor från dokumentmataren | Redan korrekt. |
| `component::hp_printer::entity::sensor::scanned_flatbed_pages::name` | Scanned pages from glass | Skannade sidor från skannerglaset | Sparad och återläst. |
| `component::hp_printer::entity::sensor::scanned_duplex_sheets::name` | Scanned double-sided sheets | Dubbelsidigt skannade ark | Redan korrekt. |
| `component::hp_printer::entity::sensor::copied_adf_pages::name` | Copied pages from document feeder | Kopierade sidor från dokumentmataren | Sparad och återläst. |
| `component::hp_printer::entity::sensor::copied_flatbed_pages::name` | Copied pages from glass | Kopierade sidor från skannerglaset | Sparad och återläst. |

`skannerglaset` är ett medvetet sammansatt fackord. svlang ger 10/10 och inga
språkproblem, men markerar ordet som ovanligt; Hunspell-sv saknar det också.
I den här konkreta räknarkontexten är termen tydligare än enbart `glaset`.

Kontroller före sparning: l10n-lint, individuell svlang-kontroll, Hunspell-sv,
diffkontroll och Gitleaks. `msgfmt` är inte tillämpligt eftersom Lokalise
hanterar JSON-nycklar, inte en PO-fil.
