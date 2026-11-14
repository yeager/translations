# HP Printer: anslutningar, batch 49

Datum: 2026-11-14

Tre tomma binära sensoretiketter kontrollerades och sparades i Lokalise.
Varje måltext återlästes separat efter sparning.

| Nyckel | Källa | Svenska efter återläsning |
| --- | --- | --- |
| `component::hp_printer::entity::binary_sensor::ethernet::name` | Ethernet | Ethernet |
| `component::hp_printer::entity::binary_sensor::usb::name` | USB | USB |
| `component::hp_printer::entity::binary_sensor::wifi::name` | Wi-Fi | Wi-Fi |

Den generella statusetiketten var redan korrekt som "Status" vid kontrollen.

Kontroller före sparning: l10n-lint, individuell svlang-kontroll,
Hunspell-sv, diffkontroll och Gitleaks. `msgfmt` är inte tillämpligt eftersom
Lokalise hanterar JSON-nycklar, inte en PO-fil.
