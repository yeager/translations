# Audacity: AUP-importens attributfel

- Datum: 2026-11-13
- Källcommit: `588850c`
- PR: [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759)
- Omfattning: 9 svenska PO-poster för felhantering vid import av äldre AUP-projekt.

Batchen ersätter ofullständiga nominalfraser med fullständiga svenska felmeddelanden. Attributnamn och interna filtypsnamn, exempelvis `maxsamples`, `simpleblockfile` och `pcmaliasblockfile`, är kodidentifierare och behålls därför oförändrade. Det gör meddelandena begripliga utan att förvanska tekniska namn som användaren kan möta i projektdata och felsökning.

Kontroller: `msgfmt` (4 443 översatta poster), avgränsad Hunspell-sv, `l10n-lint`, `svlang`, diffkontroll och Gitleaks. Hunspell-sv markerar enbart de avsiktligt bibehållna kodidentifierarna. Varken l10n-lint eller svlang träffar någon ändrad sträng.
