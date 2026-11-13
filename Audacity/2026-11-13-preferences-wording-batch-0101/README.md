# Audacity: inställningstexter

- Datum: 2026-11-13
- Källcommit: `787811c`
- PR: [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759)
- Omfattning: 9 svenska PO-poster i katalog-, effekt- och uppspelningsinställningar.

Batchen normaliserar katalogmeddelanden, gör rubriken för kataloguppdateringen substantivisk, använder **indelning** för effektmenyer och återställer den etablerade Audacity-termen **skrubba** i inställningen för ofäst uppspelningshuvud.

Kontroller: `msgfmt` (4 443 översatta poster), Hunspell-sv, `l10n-lint`, `svlang`, diffkontroll och Gitleaks. Hunspell-sv markerar endast den korrekta sammansättningen **ofäst**. l10n-lint rapporterar 28 befintliga varningar utanför batchen.
