# Audacity: Nyquist-effekter och exportkontroller

Den här batchen innehåller 26 radgranskade poster från `au3/locale/sv.po`.
Den omfattar äldre begränsare, brusgrind, Nyquist-installation av insticksmoduler,
rytmspår och export av samplingsdata.

Ändringarna finns i källcommit [`b9f460f`](https://github.com/yeager/audacity/commit/b9f460f0b7643857503b2fa939e7f86101fe3d17)
på den öppna upstream-PR:n [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759).

Kontroller före arkivering:

- `msgfmt --check --statistics` passerade: 4 443 översatta poster.
- Avgränsad Hunspell-sv-kontroll gav endast fackorden `Brusgrind`, `Lisp-fil` och `mittfrekvens`.
- `l10n-lint` och `svlang` kördes; befintliga URL-varningar respektive tekniska kontextträffar berör inte denna batch.
- `git diff --check` och Gitleaks passerade.

Upstreamstatus: committen är pushad till PR-grenen. PR:n är öppen och väntar på obligatorisk upstreamgranskning; den är inte mergad.
