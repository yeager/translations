# Audacity: brusreducering och normalisering

Elva aktiva PO-poster har granskats rad för rad. Batchen normaliserar
terminologin för brusprofil, restsignal, DC-förskjutning och toppamplitud samt
förtydligar Paulstretchs meddelande om aktuell markering.

Källcommit: [`88e5c89`](https://github.com/yeager/audacity/commit/88e5c89).
Ändringen är pushad till [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759).

`msgfmt`, avgränsad Hunspell-sv-kontroll, `l10n-lint`, `svlang`, diffkontroll
och Gitleaks passerade. Hunspell-sv markerar endast sammansättningen
`brusprofilen`. `l10n-lint` har inga fel och 29 befintliga varningar utanför
batchen. PR:n är öppen och inväntar obligatorisk upstreamgranskning; den är
inte mergad.
