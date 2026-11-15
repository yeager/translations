# Home Assistant Core – Sofar, AFCI-ljusbågsfel fortsättning

Datum: 2026-11-15

Femton ytterligare numrerade AFCI-ljusbågsfel för Sofar-växelriktare sparades
via Lokalise API. De tekniska felnumren bevaras. Samtliga poster återlästes
med `is_unverified=false`.

Kontroller: JSON, l10n-lint, svlang, Hunspell, git-diff och Gitleaks.
`msgfmt` är inte tillämpligt eftersom batchen är JSON för Lokalise API.

Detta bekräftar lokal granskning, arkivering och sparning i Lokalise, men inte
upstream-granskning, merge eller release.
