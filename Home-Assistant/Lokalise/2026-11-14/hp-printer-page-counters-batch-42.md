# HP Printer: sidräknare, batch 42

Datum: 2026-11-14

Fyra lokalt kontextgranskade räknaretiketter söktes upp var för sig i Lokalise.
Samtliga var redan korrekta upstream, så inga ändringar sparades.

| Nyckel | Källa | Svenska efter återläsning |
| --- | --- | --- |
| `component::hp_printer::entity::sensor::total_pages::name` | Printed pages | Utskrivna sidor |
| `component::hp_printer::entity::sensor::copied_pages::name` | Copied pages | Kopierade sidor |
| `component::hp_printer::entity::sensor::scanned_pages::name` | Scanned pages | Skannade sidor |
| `component::hp_printer::entity::sensor::faxed_pages::name` | Faxed pages | Faxade sidor |

Kontroller före verifiering: l10n-lint, individuell svlang-kontroll,
Hunspell-sv, diffkontroll och Gitleaks. `msgfmt` är inte tillämpligt eftersom
Lokalise hanterar JSON-nycklar, inte en PO-fil.
