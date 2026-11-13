# Audacity: Audio Unit och Nyquist

Fyra aktiva PO-poster har granskats rad för rad. Batchen bevarar
plattformnamnet Audio Unit konsekvent i import och export, synkar
gränssnittets synliga alternativ med deras beskrivning och rättar
Nyquist-insticksmodulens versionsmeddelande.

Källcommit: [`6557d08`](https://github.com/yeager/audacity/commit/6557d08).
Ändringen är pushad till [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759).

`msgfmt`, avgränsad Hunspell-sv-kontroll, `l10n-lint`, `svlang`, diffkontroll
och Gitleaks passerade. `l10n-lint` har inga fel och 29 befintliga varningar
utanför batchen. PR:n är ett utkast tills den radvisa genomgången är klar och
är inte mergad.
