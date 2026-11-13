# Audacity: Om-dialog, tidslinje och start, batch 0014

Den här radvisa granskningsbatchen omfattar 35 aktiva poster i
`au3/locale/sv.po` vid Audacity-huvudet `3212f00`.

Den rättar bygg- och biblioteksterminologi i Om-dialogen, tidslinjens
snabblyssning och sökning, samt startfel och dialoger för tillfälliga filer.

Kontroller som passerade: `msgfmt --check --statistics` (4 443 aktiva
översättningar), avgränsad Hunspell-sv-kontroll med identifierare och
sammansättningar som undantag, `git diff --check` samt Gitleaks.

`l10n-lint` och `svlang` kördes över hela katalogen. De rapporterar sedan
tidigare globala träffar utanför denna diff; inga träffar hänfördes till
batchens nya formuleringar.

Upstream: [Audacity PR #12759](https://github.com/audacity/audacity/pull/12759)
uppdaterades 2026-11-13 och inväntar upstreamgranskning.
