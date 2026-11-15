# Home Assistant Core – Sofar, batteri och BMS

Datum: 2026-11-15

Femton Sofar-fel för batteri, buck-boost-omvandlare, BCU, Bluetooth och BMS
sparades via Lokalise API. Förkortningarna BCU, BMS och CAN behålls som
tekniska namn. Samtliga poster återlästes med `is_unverified=false`.

Kontroller: JSON, l10n-lint, svlang, Hunspell, git-diff och Gitleaks.
`msgfmt` är inte tillämpligt eftersom batchen är JSON för Lokalise API.

Detta bekräftar lokal granskning, arkivering och sparning i Lokalise, men inte
upstream-granskning, merge eller release.
