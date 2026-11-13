# Audacity: Start, återställning och makron, batch 0015

Den här radvisa granskningsbatchen omfattar 11 aktiva poster i
`au3/locale/sv.po` vid Audacity-huvudet `6943327`.

Den rättar semaphore- och IPC-fel, kommandoradshjälp, automatisk
projektåterställning samt grammatik i makrohanteringens dialoger och kolumner.

Kontroller som passerade: `msgfmt --check --statistics` (4 443 aktiva
översättningar), avgränsad Hunspell-sv-kontroll med genitivformen
`Audacitys` som enda bedömda träff, `git diff --check` samt Gitleaks.

Upstream: [Audacity PR #12759](https://github.com/audacity/audacity/pull/12759)
uppdaterades 2026-11-13 och inväntar upstreamgranskning.
