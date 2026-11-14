# HP Printer: matningsfel och tillverkningsdatum, batch 46

Datum: 2026-11-14

Tre HP Printer-fält kontrollerades i Lokalise. Befintliga formuleringar för
matningsfel förtydligades med dokumentmataren som konkret kontext. Alla tre
sparades och återlästes separat.

| Nyckel | Källa | Svenska efter återläsning |
| --- | --- | --- |
| `component::hp_printer::entity::sensor::manufacturing_date::name` | Manufacturing date | Tillverkningsdatum |
| `component::hp_printer::entity::sensor::mispicks::name` | Paper mispicks | Pappersmatningsfel |
| `component::hp_printer::entity::sensor::scanner_mispicks::name` | Scanner mispicks | Matningsfel i dokumentmataren |

Kontroller före sparning: l10n-lint, individuell svlang-kontroll, Hunspell-sv,
diffkontroll och Gitleaks. `msgfmt` är inte tillämpligt eftersom Lokalise
hanterar JSON-nycklar, inte en PO-fil.
