# Audacity: effektterminologi

- Datum: 2026-11-13
- Källcommit: `b4c606e`
- PR: [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759)
- Omfattning: 8 svenska PO-poster i `ClickRemoval.cpp` och `Distortion.cpp`.

Batchen använder den etablerade termen **brusgolv**, rättar en mekanisk beskrivning av klickborttagning och förtydligar resultatet när algoritmen inte kan bearbeta det valda ljudet.

Kontroller: `msgfmt` (4 443 översatta poster), Hunspell-sv, l10n-lint, svlang, diffkontroll och Gitleaks. l10n-lint rapporterar 28 befintliga varningar utanför batchen.
