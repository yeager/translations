# Audacity: projektåterställning och timerinspelning

- Datum: 2026-11-13
- Källcommit: `dbcd41e`
- PR: [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759)
- Omfattning: 10 svenska PO-poster i projektkontroll, filhantering, spektralmarkering och timerinspelning.

Batchen gör återställningsdialogerna begripliga när vågformen inte kan visa tystnad, anger att saknade visningsdata fylls i med tystnad och skiljer `Compact` från komprimering: projektet **packas** för att frigöra oanvända byte. Den förtydligar även att den anpassade storleken gäller penseln i spektralverktyget samt förenklar varningen om ledigt diskutrymme före en timerinspelning.

Kontroller: `msgfmt` (4 443 översatta poster), avgränsad Hunspell-sv, `l10n-lint`, `svlang`, diffkontroll och Gitleaks. Hunspell-sv markerar endast den tekniska sammansättningen `sekvenstaggar`. l10n-lint har inga träffar i de ändrade posterna. svlang markerar två avsiktliga imperativfraser i gränssnittet: `Fyll i tystnad …` och `Väntar på att …`.
