# Audacity: redigering och etikettmenyer

- Datum: 2026-11-13
- Källcommit: `913338e`
- PR: [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759)
- Omfattning: 5 svenska PO-poster i klipp-, redigerings-, hjälp- och etikettmenyerna.

Batchen använder bestämd form i kommandot till klippmarkören, gör inklistringens förlopps- och felmeddelanden tydligare, förenklar snabbåtgärdens tomstatus och använder den etablerade historikformen **Lade till etikett**.

Kontroller: `msgfmt` (4 443 översatta poster), Hunspell-sv, `l10n-lint`, `svlang`, diffkontroll och Gitleaks. l10n-lint rapporterar 28 befintliga varningar utanför batchen.
