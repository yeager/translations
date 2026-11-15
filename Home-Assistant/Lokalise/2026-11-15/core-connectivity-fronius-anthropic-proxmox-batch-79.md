# Home Assistant Core – anslutningar, Fronius, Anthropic och Proxmox VE

Datum: 2026-11-15

Femton kontextgranskade svenska strängar sparades via Lokalise API. Batchen
omfattar anslutningskategorierna X10, Zigbee och Z-Wave, Fronius
batteribegränsningar, Anthropic-konfiguration samt Proxmox VE.

Samtliga poster återlästes med `is_unverified=false`. Kontroller: JSON,
l10n-lint, svlang, Hunspell, git-diff och Gitleaks. `msgfmt` är inte
tillämpligt eftersom batchen är JSON för Lokalise API.

Detta bekräftar lokal granskning, arkivering och sparning i Lokalise, men inte
upstream-granskning, merge eller release.
