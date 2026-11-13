# Audacity: Insticksmoduler och projektfilsdiagnostik, batch 0018

Den här radvisa granskningsbatchen omfattar 10 aktiva poster i
`au3/locale/sv.po` vid Audacity-huvudet `ad663bc`.

Den normaliserar insticksmodulernas namn, samplingsfrekvens och ljudvärd samt
rättar projektfilens FAT32- och versionsdiagnostik. Meddelandet om 3.3.3
angav tidigare felaktigt motsatt versionsintervall.

Kontroller som passerade: `msgfmt --check --statistics` (4 443 aktiva
översättningar), avgränsad Hunspell-sv-kontroll med sammansättningen
`FAT32-formaterat` som undantag, `git diff --check` samt Gitleaks.

Upstream: [Audacity PR #12759](https://github.com/audacity/audacity/pull/12759)
uppdaterades 2026-11-13 och inväntar upstreamgranskning.
