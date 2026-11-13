# Audacity: upprepning, efterklang och filter

Elva aktiva PO-poster har granskats rad för rad. Batchen normaliserar
upprepningskommandot, förtydligar efterklangens effektljud och använder
filterordning och gränsfrekvens i filtergränssnittet.

Källcommit: [`e9b4239`](https://github.com/yeager/audacity/commit/e9b4239).
Ändringen är pushad till [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759).

`msgfmt`, avgränsad Hunspell-sv-kontroll, `l10n-lint`, `svlang`, diffkontroll
och Gitleaks passerade. Hunspell-sv markerar tidsformatet `dd:hh:mm:ss` och
den tekniska sammansättningen `salklangeffekt`. `l10n-lint` har inga fel och
29 befintliga varningar utanför batchen. PR:n är öppen och inväntar
obligatorisk upstreamgranskning; den är inte mergad.
