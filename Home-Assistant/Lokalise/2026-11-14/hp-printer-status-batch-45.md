# HP Printer: skrivarstatus, batch 45

Datum: 2026-11-14

Tio driftstatusvärden kontrollerades var för sig i Lokalise. Tre tomma
översättningar sparades och återlästes separat. De andra sju var redan
korrekta.

| Nyckel | Källa | Svenska efter återläsning | Resultat |
| --- | --- | --- | --- |
| `component::hp_printer::entity::sensor::status::state::cancel_job` | Canceling job | Avbryter jobb | Redan korrekt. |
| `component::hp_printer::entity::sensor::status::state::close_door_or_cover` | Close door or cover | Stäng luckan eller locket | Sparad och återläst. |
| `component::hp_printer::entity::sensor::status::state::copying` | Copying | Kopierar | Redan korrekt. |
| `component::hp_printer::entity::sensor::status::state::in_power_save` | Power save | Energisparläge | Redan korrekt. |
| `component::hp_printer::entity::sensor::status::state::initializing` | Initializing | Initierar | Sparad och återläst. |
| `component::hp_printer::entity::sensor::status::state::processing` | Printing | Skriver ut | Redan korrekt. |
| `component::hp_printer::entity::sensor::status::state::ready` | Ready | Klar | Redan korrekt. |
| `component::hp_printer::entity::sensor::status::state::scan_processing` | Scanning | Skannar | Redan korrekt. |
| `component::hp_printer::entity::sensor::status::state::shutting_down` | Shutting down | Stängs av | Sparad och återläst. |
| `component::hp_printer::entity::sensor::status::state::tray_empty` | Paper tray empty | Pappersfacket är tomt | Redan korrekt. |

Kontroller före sparning: l10n-lint, individuell svlang-kontroll, Hunspell-sv,
diffkontroll och Gitleaks. `msgfmt` är inte tillämpligt eftersom Lokalise
hanterar JSON-nycklar, inte en PO-fil.
