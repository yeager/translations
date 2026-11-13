# Audacity: återställning av projekt och realtidseffekter

- Datum: 2026-11-13
- Källcommit: `427ebee`
- PR: [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759)
- Omfattning: 8 svenska PO-poster i `ProjectFileManager.cpp` och `RealtimeEffectPanel.cpp`.

Granskningen använder konsekvent **återställ** för recovered/recover, normaliserar **samplingsfrekvens**, förtydligar osynkroniserade stereospår och beskriver realtidseffekter korrekt: de ändrar inte ljudet permanent.

Kontroller: `msgfmt` (4 443 översatta poster), Hunspell-sv, l10n-lint, svlang, diffkontroll och Gitleaks. l10n-lint rapporterar 28 befintliga varningar utanför batchen.
