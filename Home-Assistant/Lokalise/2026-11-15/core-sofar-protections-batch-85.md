# Home Assistant Core – Sofar, batteri- och skyddsfel

Datum: 2026-11-15

Femton Sofar-fel för ljusbåge, matning, hjälpspänning och batteriskydd sparades
via Lokalise API. Samtliga poster återlästes med `is_unverified=false`.

Kontroller: JSON, l10n-lint, svlang, Hunspell, git-diff och Gitleaks.
`msgfmt` är inte tillämpligt eftersom batchen är JSON för Lokalise API.

Detta bekräftar lokal granskning, arkivering och sparning i Lokalise, men inte
upstream-granskning, merge eller release.
