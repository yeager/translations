# Audacity: klipp- och spektrogramkontroller

- Datum: 2026-11-13
- Källcommit: `39af04f`
- PR: [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759)
- Omfattning: 9 svenska PO-poster i klipp- och spektrogramkontroller.

Batchen använder **hastighet** konsekvent för klippets speed, ersätter engelska expand-former med **fäll ut**, och korrigerar felöversättningen av **peak frequency** till **toppfrekvens**. Terminologilistan är uppdaterad med den termen.

Kontroller: `msgfmt` (4 443 översatta poster), Hunspell-sv, `l10n-lint`, `svlang`, diffkontroll och Gitleaks. l10n-lint rapporterar 28 befintliga varningar utanför batchen.
