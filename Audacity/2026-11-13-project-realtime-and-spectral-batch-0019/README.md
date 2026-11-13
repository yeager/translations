# Audacity: Projekt, realtid och spektralverktyg, batch 0019

Den här radvisa granskningsbatchen omfattar 19 aktiva poster i
`au3/locale/sv.po` vid Audacity-huvudet `43c1ebf`.

Den rättar öppning av säkerhetskopior och AUP3-projekt, komprimering av
projektfiler, realtidseffekter och insticksmoduler samt spektralverktygets
kontroller och historikrader.

Kontroller som passerade: `msgfmt --check --statistics` (4 443 aktiva
översättningar), avgränsad Hunspell-sv-kontroll med AUP3-format och
platshållare som undantag, `git diff --check` samt Gitleaks.

Upstream: [Audacity PR #12759](https://github.com/audacity/audacity/pull/12759)
uppdaterades 2026-11-13 och inväntar upstreamgranskning.
