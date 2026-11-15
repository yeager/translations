# Home Assistant Core – Govee-ljuseffekter, fortsättning

Datum: 2026-11-15

Femton ytterligare namn på Govee-ljuseffekter har översatts och återlästs via
Lokalise API med `is_unverified=false`. Effektnamnet `Cover` är oförändrat
avsiktligt, eftersom dess funktion inte framgår av den korta produktsträngen.

Kontroller: JSON, l10n-lint, svlang, Hunspell, git-diff och Gitleaks.
`msgfmt` är inte tillämpligt eftersom batchen är JSON för Lokalise API.

Detta bekräftar lokal granskning, arkivering och sparning i Lokalise, men inte
upstream-granskning, merge eller release.
