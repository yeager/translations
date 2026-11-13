# Audacity: PCM- och WavPack-export, batch 0011

Den här radvisa granskningsbatchen omfattar 15 aktiva poster i
`au3/locale/sv.po` vid Audacity-huvudet `a653ba5`.

Den rättar PCM-exportens felmeddelanden och filformat, numeriska PCM-format
och WavPack-exportens namn, kvalitetsetiketter och lägesnamn.

Kontroller som passerade: `msgfmt --check --statistics` (4 443 aktiva
översättningar), avgränsad Hunspell-sv-kontroll med formatnamn som undantag,
`git diff --check` samt Gitleaks.

Upstream: [Audacity PR #12759](https://github.com/audacity/audacity/pull/12759)
uppdaterades 2026-11-13 och inväntar upstreamgranskning.
