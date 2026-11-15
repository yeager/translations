# Home Assistant Core – Satel, iCloud och Alpha Bidet

Datum: 2026-11-15

Femton kontextgranskade svenska strängar sparades via Lokalise API. De omfattar
återstående Satel Integra-felsignaler, iCloud-status, SwitchBot, Govee och
konfiguration av Alpha Bidet med infraröd sändare.

Samtliga poster återlästes med `is_unverified=false`. Kontroller: JSON,
l10n-lint, svlang, Hunspell, git-diff och Gitleaks. `msgfmt` är inte
tillämpligt eftersom batchen är JSON för Lokalise API.

Detta bekräftar lokal granskning, arkivering och sparning i Lokalise, men inte
upstream-granskning, merge eller release.
