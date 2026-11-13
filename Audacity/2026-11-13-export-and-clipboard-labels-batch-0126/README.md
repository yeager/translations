# Audacity: export- och urklippstexter

- Datum: 2026-11-13
- Källcommit: `fea07a2`
- PR: [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759)
- Omfattning: 5 svenska PO-poster i export- och redigeringsmenyerna.

Batchen ersätter den oidiomatiska formen **utkanaler** med **utgångskanaler** och gör urklippsfraserna naturliga med bestämd form: `från urklippet` och `till urklippet`.

Kontroller: `msgfmt` (4 443 översatta poster), avgränsad Hunspell-sv, `l10n-lint`, `svlang`, diffkontroll och Gitleaks. Inga av verktygen träffar någon ändrad post.
