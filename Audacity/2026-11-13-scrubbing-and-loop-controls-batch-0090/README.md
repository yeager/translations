# Audacity: skrubbning och slingkontroller

Åtta aktiva PO-poster har granskats rad för rad i tidslinjens lyssnings- och
slingkontroller. Batchen normaliserar *Scrub* till *skrubba*, ersätter
*loopregion* med *slingområde* och översätter ett kvarvarande engelskt
rollnamn i Om-dialogen.

Källcommit: [`5742084`](https://github.com/yeager/audacity/commit/5742084).
Ändringen är pushad till [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759).

`msgfmt`, avgränsad Hunspell-sv-kontroll, `l10n-lint`, `svlang`, diffkontroll
och Gitleaks passerade. Hunspell-sv saknar endast det avsedda sammansatta
UI-ordet *slingområde*. `l10n-lint` har inga fel och 28 befintliga varningar
utanför batchen. Svlangs slingträffar är falska V2-varningar. PR:n är ett
utkast tills den radvisa genomgången är klar och är inte mergad.
