# Audacity: Spektrum, insticksmoduler och etiketter, batch 0017

Den här radvisa granskningsbatchen omfattar 19 aktiva poster i
`au3/locale/sv.po` vid Audacity-huvudet `b8a6c0d`.

Den rättar spektrumanalysens fönsterfunktioner och feltexter,
insticksmodulernas laddningsfel, etikettfilernas formatnamn,
språkvalet och MIDI-mixerns anslagsstyrka.

Kontroller som passerade: `msgfmt --check --statistics` (4 443 aktiva
översättningar), avgränsad Hunspell-sv-kontroll med tekniska
sammansättningar och formatnamn som undantag, `git diff --check` samt
Gitleaks.

Upstream: [Audacity PR #12759](https://github.com/audacity/audacity/pull/12759)
uppdaterades 2026-11-13 och inväntar upstreamgranskning.
