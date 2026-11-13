# Audacity: etikettplugin

- Datum: 2026-11-13
- Källcommit: `30b2281`
- PR: [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759)
- Omfattning: 7 svenska PO-poster i pluginet för regelbundna etiketter.

Batchen skiljer **regelbundna** från ”vanliga”, använder idiomatiska verb i kontrollerna och rättar bestämd form i etikettområden och felmeddelandet om ett enda detekterat ljud.

Kontroller: `msgfmt` (4 443 översatta poster), Hunspell-sv, `l10n-lint`, `svlang`, diffkontroll och Gitleaks. l10n-lint rapporterar 28 befintliga varningar utanför batchen.
