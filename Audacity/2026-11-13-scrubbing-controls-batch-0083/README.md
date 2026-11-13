# Audacity: skrubbningsreglage

Åtta aktiva PO-poster har granskats rad för rad i käll- och termkontext.
Batchen ersätter det oöversatta *scrubbing* med *skrubba* och *skrubbning* i
Audacitys reglage för variabel uppspelning. Den normaliserar även macOS-termen
*Cmd-klick*.

Källcommit: [`c9ca52e`](https://github.com/yeager/audacity/commit/c9ca52e).
Ändringen är pushad till [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759).

`msgfmt`, avgränsad Hunspell-sv-kontroll, `l10n-lint`, `svlang`, diffkontroll
och Gitleaks passerade. Hunspell-sv saknar de avsedda termerna *Cmd-klick* och
*skrubblinjal*. `l10n-lint` har inga fel och 28 befintliga varningar utanför
batchen. PR:n är ett utkast tills den radvisa genomgången är klar och är inte
mergad.
