# Audacity: kodek-I/O och Nyquist-arbetsbänk

Åtta aktiva PO-poster har granskats rad för rad i Opus-, PCM-, WavPack- och
Nyquist-delarna. Batchen normaliserar I/O-skrivsättet, förtydligar filhuvud och
avkodningsfel samt använder svenska och begripliga etiketter i
Nyquist-arbetsbänken.

Källcommit: [`7361d33`](https://github.com/yeager/audacity/commit/7361d3360a46a7dc4a8e865b32a860ab8060e1a3).
Ändringen är pushad till [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759).

`msgfmt`, avgränsad Hunspell-sv-kontroll, l10n-lint, svlang, diffkontroll och
Gitleaks passerade. Hunspell markerar endast produktnamnet `WavPack`.
l10n-lint har inga fel och 29 befintliga varningar utanför batchen. svlangs
globala träffar är befintliga katalogvarningar. PR:n är öppen och inväntar
obligatorisk upstreamgranskning; den är inte mergad.
