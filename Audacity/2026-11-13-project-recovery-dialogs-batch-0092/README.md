# Audacity: projektåterställning och ångrahistorik

- Datum: 2026-11-13
- Källcommit: `1e7f3a9dbc4b35022cda28732119880bf2c9b3c1`
- PR: [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759)
- Omfattning: 18 svenska PO-poster i `HistoryWindow.cpp`, `MenuCreator.cpp` och `ProjectFSCK.cpp`.

Granskningen ersätter det vardagliga **släng** med det precisa **ta bort** för ångranivåer, förtydligar genvägskonflikter och gör återställningsdialogerna för saknade alias-, sammanfattnings- och ljuddatablockfiler idiomatiska. Tekniska filformat och platshållare är bevarade.

Kontroller på källcommiten: `msgfmt` (4 443 översatta poster), diffkontroll, Gitleaks, Hunspell-sv, l10n-lint och svlang. l10n-lint rapporterar 28 befintliga varningar utanför batchen.
