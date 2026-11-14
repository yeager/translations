# HP Printer: faxräknare, batch 47

Datum: 2026-11-14

Tre tomma faxräknare kontrollerades och sparades i Lokalise. Varje måltext
återlästes sedan separat.

| Nyckel | Källa | Svenska efter återläsning |
| --- | --- | --- |
| `component::hp_printer::entity::sensor::faxed_adf_pages::name` | Faxed pages from document feeder | Faxade sidor från dokumentmataren |
| `component::hp_printer::entity::sensor::faxed_flatbed_pages::name` | Faxed pages from glass | Faxade sidor från skannerglaset |
| `component::hp_printer::entity::sensor::faxed_pc_pages::name` | Faxed pages from computer | Faxade sidor från datorn |

Kontroller före sparning: l10n-lint, individuell svlang-kontroll, Hunspell-sv,
diffkontroll och Gitleaks. `msgfmt` är inte tillämpligt eftersom Lokalise
hanterar JSON-nycklar, inte en PO-fil.
