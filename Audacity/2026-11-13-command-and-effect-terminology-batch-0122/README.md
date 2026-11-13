# Audacity: kommando- och effektterminologi

- Datum: 2026-11-13
- Källcommit: `04cba8e`
- PR: [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759)
- Omfattning: 4 svenska PO-poster i kommandoexport och effektförinställningar.

Batchen använder den etablerade termen **amplitudkurvor** i kommandoexportens JSON-information och **spektral markering** för spektrogramvalet. Felmeddelandena för filer med effektförinställningar behåller nu dessutom avskiljande kolon efter filnamnet.

Kontroller: `msgfmt` (4 443 översatta poster), avgränsad Hunspell-sv, `l10n-lint`, `svlang`, diffkontroll och Gitleaks. Hunspell-sv och l10n-lint har inga träffar i de ändrade posterna. svlang markerar den avsiktliga imperativfrasen `Aktivera spektral markering`.
