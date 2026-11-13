# Audacity: Nyquist- och molndialoger, batch 0012

Den här radvisa granskningsbatchen omfattar 30 aktiva poster i
`au3/locale/sv.po` vid Audacity-huvudet `f140ed7`.

Den rättar Nyquist-arbetsbänkens navigering och acceleratortangenter samt
audio.com-dialogernas molnsparande, tokenhantering, synkronisering och
exportformuleringar.

Kontroller som passerade: `msgfmt --check --statistics` (4 443 aktiva
översättningar), avgränsad Hunspell-sv-kontroll med domännamn, filändelser och
tangenter som undantag, `git diff --check` samt Gitleaks.

Upstream: [Audacity PR #12759](https://github.com/audacity/audacity/pull/12759)
uppdaterades 2026-11-13 och inväntar upstreamgranskning.
