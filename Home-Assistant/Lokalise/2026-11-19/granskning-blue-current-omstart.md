# Blue Current och omstartsreferenser

Kontrollerat i Lokalise den 19 november 2026.

| Fullständig nyckel | Engelska | Svenska | Bedömning |
|---|---|---|---|
| `component::blue_current::entity::button::stop_charge_session::name` | Stop charge session | Avsluta laddningen | Behåll. |
| `component::blue_current::entity::button::reset::name` | Reset | Återställ | Behåll. |
| `component::blue_current::entity::button::reboot::name` | `[%key:common::action::reboot%]` | `[%key:common::action::reboot%]` | Behåll referensen. |

Målet `common::action::reboot` kontrollerades: ”Reboot” / ”Starta om”. Två ytterligare nycklar använde samma källreferens men hade vanlig svensk text ”Starta om”. Dessa återställdes till `[%key:common::action::reboot%]` och lästes tillbaka:

- `component::watergate::entity::button::reboot::name`
- `component::hassio::issues::issue_system_reboot_required::fix_flow::step::system_execute_reboot::submit`

Referensändringarna registreras separat från översättningsminnets textpar.
