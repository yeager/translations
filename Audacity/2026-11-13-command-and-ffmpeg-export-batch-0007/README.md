# Audacity: kommandorad och FFmpeg-export, batch 0007

Den här radvisa granskningsbatchen omfattar 24 aktiva poster i
`au3/locale/sv.po` vid Audacity-huvudet `0a73c37`.

Den rättar kommandoradsexportens standardindata, kodare, FFmpeg-format,
bithastighetsprofiler, kodekdiagnostik och svensk decimalnotation.

Kontroller som passerade: `msgfmt --check --statistics` (4 443 aktiva
översättningar), avgränsad Hunspell-sv-kontroll med endast tekniknamn och
platshållare som undantag, `git diff --check` samt Gitleaks.

Upstream: [Audacity PR #12759](https://github.com/audacity/audacity/pull/12759)
uppdaterades 2026-11-13. Den är öppen och mergebar, men inväntar
upstreamgranskning. Inga CI-resultat eller upstream-merge fanns vid kontrollen.
