# Audacity: uppspelning och teametiketter

- Datum: 2026-11-13
- Källcommit: `7e0fb6e`
- PR: [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759)
- Omfattning: 5 svenska PO-poster i huvudgränssnittet och Om-dialogen.

Batchen rättar sammansättningen `%s-teammedlemmar`, kongruensen i status för snabbuppspelning och använder den etablerade termen **uppspelningshuvud** i tidslinjevyn. Ingen ny termpost behövs; uppspelningshuvud finns redan i den projektspecifika terminologin.

Kontroller: `msgfmt` (4 443 översatta poster), avgränsad Hunspell-sv, `l10n-lint`, `svlang`, diffkontroll och Gitleaks. Varken Hunspell-sv, l10n-lint eller svlang träffar någon ändrad sträng.
