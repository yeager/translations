# Audacity: FFmpeg- och FLAC-diagnostik, batch 0009

Den här radvisa granskningsbatchen omfattar 17 aktiva poster i
`au3/locale/sv.po` vid Audacity-huvudet `a1e3ec4`.

Den rättar FFmpeg-bibliotekets inläsning och hämtning, FLAC-kodarens
diagnostik, filformatens bitdjup och LOF-filernas förskjutningar.

Kontroller som passerade: `msgfmt --check --statistics` (4 443 aktiva
översättningar), avgränsad Hunspell-sv-kontroll med formatnamn som undantag,
`git diff --check` samt Gitleaks.

Upstream: [Audacity PR #12759](https://github.com/audacity/audacity/pull/12759)
uppdaterades 2026-11-13. Den är öppen och mergebar, men inväntar
upstreamgranskning. Inga CI-resultat eller upstream-merge fanns vid kontrollen.
