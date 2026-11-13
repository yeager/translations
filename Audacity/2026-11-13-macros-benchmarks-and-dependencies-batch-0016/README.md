# Audacity: Makron, prestandatest och beroenden, batch 0016

Den här radvisa granskningsbatchen omfattar 18 aktiva poster i
`au3/locale/sv.po` vid Audacity-huvudet `975a4b4`.

Den rättar makrohanteringens kommandon, prestandatestets intervall och
diagnostik, brusprofilens instruktioner, externa filberoenden och
ljudbortfallsrapportering.

Kontroller som passerade: `msgfmt --check --statistics` (4 443 aktiva
översättningar), avgränsad Hunspell-sv-kontroll med Audacitys genitiv,
platshållare och acceleratoruppdelade ord som undantag, `git diff --check`
samt Gitleaks.

Upstream: [Audacity PR #12759](https://github.com/audacity/audacity/pull/12759)
uppdaterades 2026-11-13 och inväntar upstreamgranskning.
