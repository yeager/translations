# Home Assistant Core – Satel Integra, felsignaler

Datum: 2026-11-15

Femton svenska namn på felsignaler för Satel Integra sparades via Lokalise API.
Förkortningarna DT1, DT2, DTM, EEPROM, RTC och DTR behålls som tekniska namn.
Alla poster återlästes med `is_unverified=false`.

Kontroller: JSON, l10n-lint, svlang, Hunspell, git-diff och Gitleaks.
`msgfmt` är inte tillämpligt eftersom batchen är JSON för Lokalise API.

Detta bekräftar lokal granskning, arkivering och sparning i Lokalise, men inte
upstream-granskning, merge eller release.
