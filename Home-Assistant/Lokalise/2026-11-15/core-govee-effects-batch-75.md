# Home Assistant Core – Govee-ljuseffekter, del fyra

Datum: 2026-11-15

Femton ytterligare Govee-effektnamn har översatts och återlästs via Lokalise
API med `is_unverified=false`. Den etablerade svenska titeln *Den vitruvianske
mannen* används för Leonardos motiv.

Kontroller: JSON, l10n-lint, svlang, Hunspell, git-diff och Gitleaks.
`msgfmt` är inte tillämpligt eftersom batchen är JSON för Lokalise API.

Detta bekräftar lokal granskning, arkivering och sparning i Lokalise, men inte
upstream-granskning, merge eller release.
