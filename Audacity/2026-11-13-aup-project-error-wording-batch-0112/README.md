# Audacity: AUP-importens projekt- och filfel

- Datum: 2026-11-13
- Källcommit: `e5a452c`
- PR: [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759)
- Omfattning: 12 svenska PO-poster för AUP-importens projekt-, fil- och positionsfel.

Batchen förenklar importdiagnostiken till kompletta svenska satser: projektattribut anges som felaktiga, en saknad projektfil blir subjekt i meningen och misslyckade fil- eller positionsåtgärder uttrycks med ”kunde inte”. Kodidentifierarna `vpos`, `sel0`, `sel1`, `selLow` och `selHigh` behålls oförändrade eftersom de är namn i AUP-projektformatet.

Kontroller: `msgfmt` (4 443 översatta poster), avgränsad Hunspell-sv, `l10n-lint`, `svlang`, diffkontroll och Gitleaks. Hunspell-sv markerar endast C-formatet `lld` och de avsiktligt bibehållna AUP-attributnamnen. l10n-lint träffar ingen ändrad sträng. Svlang markerar ”taggen kändes inte igen”, en korrekt svensk V2-sats, som falsk positiv.
