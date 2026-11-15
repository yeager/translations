# Home Assistant Core – Teslemetry, väder och Bosch SHC

Datum: 2026-11-15

Femton kontextgranskade svenska texter sparades via Lokalise API. Batchen
omfattar batteristyrning för Powerwall, platsval i väderintegrationer samt
sensoranslutningar i Bosch Smart Home Controller.

Samtliga poster återlästes med `is_unverified=false`. Kontroller: JSON,
l10n-lint, svlang, Hunspell, git-diff och Gitleaks. `msgfmt` är inte
tillämpligt eftersom batchen är JSON för Lokalise API.

Detta bekräftar lokal granskning, arkivering och sparning i Lokalise, men inte
upstream-granskning, merge eller release.
