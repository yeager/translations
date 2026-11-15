# Home Assistant Core – Govee, Matter och Ecovacs

Datum: 2026-11-15

Femton kontextgranskade strängar sparades via Lokalise API. Batchen avslutar
den aktuella gruppen med Govee-effekter och omfattar även Matter-persienner,
Bosch LED-ljusstyrka och Ecovacs moppfunktioner.

Samtliga poster återlästes med `is_unverified=false`. Kontroller: JSON,
l10n-lint, svlang, Hunspell, git-diff och Gitleaks. `msgfmt` är inte
tillämpligt eftersom batchen är JSON för Lokalise API.

Detta bekräftar lokal granskning, arkivering och sparning i Lokalise, men inte
upstream-granskning, merge eller release.
