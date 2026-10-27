# Cacti Monitor — svensk förslagsgranskning, 2026-10-21

Samtliga tolv externa Weblate-förslag granskades rad för rad.

Godtagna och sparade förbättringar:

- `Thresholds` → `Tröskelvärden`
- `Not Set` → `Ej inställt`

Avvisade förslag försämrade etablerade tekniska termer, hade felaktiga mellanslag eller lämnade engelska ord kvar. Tre förslag ändrade PHP-platshållaren `%d` till `% d` och skulle därför ha brutit formatet. Den automatiska återanvändningskontrollen för `Tröskelvärden` avfärdades efter sakgranskning: samma ord är korrekt för de relaterade källsträngarna.

Efter granskningen gav både `has:suggestion` och `has:check` inga aktiva träffar. Komponenten är 100 % översatt (311 av 311 strängar).

## Aktuell källkontroll 2026-10-27

Den kompletterande komponentfilen `cacti-monitor-sv-granskning-20261026.po`
har jämförts rad för rad med den aktuella katalogen på `develop` (SHA-256
`36d821b9c3f077afe32110828ec8ad6304ec4927da91f80bf9c3ceb0c188b481`).
Alla tolv poster finns kvar och skiljer sig fortfarande från uppströms
måltext; ingen var redan rättad eller saknades. Filen är därmed en komplett
komponentvis fil med tolv kvarvarande rättelser och är inte inskickad.

Den passerar `msgfmt`, `l10n-lint` (0 fel och 0 varningar), `svlang`,
Hunspell-granskning och Gitleaks. Hunspell-träffarna är Cacti-, Syslog- och
CSS-termer, samt den korrekta sammansättningen ”siduppdateringar”.
