# Home Assistant Core – Govee-ljuseffekter, del tre

Datum: 2026-11-15

Femton ytterligare Govee-effektnamn har översatts och återlästs via Lokalise
API med `is_unverified=false`. Namnet `Marquee` behålls, eftersom den korta
källsträngen inte säkert anger vilken typ av effekt som avses.

Kontroller: JSON, l10n-lint, svlang, Hunspell, git-diff och Gitleaks.
`msgfmt` är inte tillämpligt eftersom batchen är JSON för Lokalise API.

Detta bekräftar lokal granskning, arkivering och sparning i Lokalise, men inte
upstream-granskning, merge eller release.
