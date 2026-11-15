# Home Assistant Core – Sofar, BMS och likströmsbuss

Datum: 2026-11-15

Femton Sofar-fel för BMS, BMU, likströmsbuss och AC-chip sparades via Lokalise
API. Förkortningarna BMS, BMU, RMS och AC behålls som tekniska namn. Samtliga
poster återlästes med `is_unverified=false`.

Kontroller: JSON, l10n-lint, svlang, Hunspell, git-diff och Gitleaks.
`msgfmt` är inte tillämpligt eftersom batchen är JSON för Lokalise API.

Detta bekräftar lokal granskning, arkivering och sparning i Lokalise, men inte
upstream-granskning, merge eller release.
