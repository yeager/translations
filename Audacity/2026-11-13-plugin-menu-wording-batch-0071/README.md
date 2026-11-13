# Audacity: insticksmodulernas menyer

Tre aktiva PO-poster har granskats rad för rad. Batchen rättar svensk
stavning, använder kommandot *Upprepa* konsekvent och beskriver
ljudbortfall utifrån inspelningsingången i stället för den bokstavliga och
missvisande formuleringen ”i uppströmmen”.

Källcommit: [`358268e`](https://github.com/yeager/audacity/commit/358268e).
Ändringen är pushad till [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759).

`msgfmt`, avgränsad Hunspell-sv-kontroll, `l10n-lint`, `svlang`, diffkontroll
och Gitleaks passerade. `l10n-lint` har inga fel och 29 befintliga varningar
utanför batchen. PR:n är ett utkast tills den radvisa genomgången är klar och
är inte mergad.
