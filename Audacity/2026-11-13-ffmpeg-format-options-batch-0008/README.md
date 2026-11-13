# Audacity: FFmpeg-formatalternativ, batch 0008

Den här radvisa granskningsbatchen omfattar 14 aktiva poster i
`au3/locale/sv.po` vid Audacity-huvudet `ef45ee9`.

Den rättar format- och kodeklistan, FFmpeg-alternativ, brytfrekvens,
språkregler och interna FLAC-parametrar.

Kontroller som passerade: `msgfmt --check --statistics` (4 443 aktiva
översättningar), avgränsad Hunspell-sv-kontroll med formatnamn som undantag,
`git diff --check` samt Gitleaks.

Upstream: [Audacity PR #12759](https://github.com/audacity/audacity/pull/12759)
uppdaterades 2026-11-13. Den är öppen och mergebar, men inväntar
upstreamgranskning. Inga CI-resultat eller upstream-merge fanns vid kontrollen.
