# HP Printer: svartvitt och färg, batch 44

Datum: 2026-11-14

Fyra färg- och svartviträknare kontrollerades var för sig i Lokalise. Två
fanns redan på korrekt svenska. Två tomma översättningar sparades och
återlästes separat.

| Nyckel | Källa | Svenska efter återläsning | Resultat |
| --- | --- | --- | --- |
| `component::hp_printer::entity::sensor::monochrome_pages::name` | Printed black and white pages | Utskrivna svartvita sidor | Redan korrekt. |
| `component::hp_printer::entity::sensor::color_pages::name` | Printed color pages | Utskrivna färgsidor | Redan korrekt. |
| `component::hp_printer::entity::sensor::copied_monochrome_pages::name` | Copied black and white pages | Kopierade svartvita sidor | Sparad och återläst. |
| `component::hp_printer::entity::sensor::copied_color_pages::name` | Copied color pages | Kopierade färgsidor | Sparad och återläst. |

Kontroller före sparning: l10n-lint, individuell svlang-kontroll, Hunspell-sv,
diffkontroll och Gitleaks. `msgfmt` är inte tillämpligt eftersom Lokalise
hanterar JSON-nycklar, inte en PO-fil.
