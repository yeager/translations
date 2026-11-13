# Audacity: Nyquist och molnkonton

Tolv aktiva PO-poster har granskats rad för rad. Batchen använder samma
Nyquist-arbetsbänk i alla fönstertexter, naturliga söketiketter och konsekventa
åtgärder för att koppla respektive koppla från audio.com-konton.

Källcommit: [`93682c0`](https://github.com/yeager/audacity/commit/93682c0).
Ändringen är pushad till [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759).

`msgfmt`, avgränsad Hunspell-sv-kontroll, l10n-lint, svlang, diffkontroll och
Gitleaks passerade. Hunspell markerar endast domännamnet `audio.com`.
l10n-lint har inga fel och 29 befintliga varningar utanför batchen. svlangs
enda relaterade I/O-träff är en befintlig katalogtext. PR:n är öppen och
inväntar obligatorisk upstreamgranskning; den är inte mergad.
