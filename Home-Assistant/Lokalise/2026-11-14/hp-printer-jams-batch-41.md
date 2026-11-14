# HP Printer: pappersstopp, batch 41

Datum: 2026-11-14

Två etiketter i Home Assistants HP Printer-integrering kontrollerades direkt i
Lokalise efter lokal språk- och kontextgranskning.

| Nyckel | Källa | Svenska | Resultat |
| --- | --- | --- | --- |
| `component::hp_printer::entity::sensor::jams::name` | Paper jams | Pappersstopp | Fanns redan korrekt och återlästes utan ändring. |
| `component::hp_printer::entity::sensor::scanner_jams::name` | Scanner jams | Pappersstopp i dokumentmataren | Sparades och återlästes separat. |

HP Printers dokumentation anger att `scanner_jams` avser pappersstopp i
dokumentmataren. Formuleringen skiljer därför den från den generella
skrivaretiketten `jams`.

Kontroller före sparning: l10n-lint, individuell svlang-kontroll, Hunspell-sv,
diffkontroll och Gitleaks. `msgfmt` är inte tillämpligt eftersom Lokalise
hanterar JSON-nycklar, inte en PO-fil.
