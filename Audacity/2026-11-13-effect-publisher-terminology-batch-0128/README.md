# Audacity: utgivare av insticksmoduler

- Datum: 2026-11-13
- Källcommit: `a0425e7`
- PR: [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759)
- Omfattning: 3 svenska PO-poster i effektinställningarna.

Batchen ersätter det tvetydiga **företag** med **utgivare** i sortering och gruppering av effekter. Det följer källtextens *publisher* och fungerar även när utgivaren inte är ett företag.

Kontroller: `msgfmt` (4 443 översatta poster), avgränsad Hunspell-sv, `l10n-lint`, `svlang`, diffkontroll och Gitleaks. Inga av verktygen träffar någon ändrad post.
