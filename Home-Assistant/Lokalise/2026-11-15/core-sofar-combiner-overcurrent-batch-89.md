# Home Assistant Core – Sofar, överström i samlingslådans strängar fortsättning

Datum: 2026-11-15

Femton ytterligare Sofar-fel för överström i numrerade strängar i
samlingslådan sparades via Lokalise API. Tekniska strängnummer bevaras.
Samtliga poster återlästes med `is_unverified=false`.

Kontroller: JSON, l10n-lint, svlang, Hunspell, git-diff och Gitleaks.
`msgfmt` är inte tillämpligt eftersom batchen är JSON för Lokalise API.

Detta bekräftar lokal granskning, arkivering och sparning i Lokalise, men inte
upstream-granskning, merge eller release.
