# HP Printer: molnstatus, batch 40

Datum: 2026-11-14

Två korta statusetiketter i Home Assistants HP Printer-integrering har granskats
i komponentens källfil, kontrollerats mot termbasen och sparats i Lokalise.

| Nyckel | Källa | Svenska |
| --- | --- | --- |
| `component::hp_printer::entity::binary_sensor::cloud_services::name` | Cloud services | Molntjänster |
| `component::hp_printer::entity::binary_sensor::cloud_registered::name` | Cloud registered | Registrerad i molnet |

`cloud_services` är en binär sensors etikett för molntjänster. `cloud_registered`
anger registreringsstatus och behöver därför en fullständig svensk statusfras,
inte bara en sammansättning.

Kontroller:

- Lokalise: båda sparade och återlästa separat i redigeraren.
- l10n-lint: godkänd.
- svlang: 10,0/10, inga problem.
- Hunspell-sv: inga okända ord.
- Gitleaks: inga hemligheter.
- msgfmt: ej tillämpligt; Lokalise-nycklar, inte en PO-fil.

Status: sparad upstream i Lokalise och verifierad genom separat återläsning.
