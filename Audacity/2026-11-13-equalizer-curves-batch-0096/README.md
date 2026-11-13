# Audacity: equalizerkurvor

- Datum: 2026-11-13
- Källcommit: `70dd9f7`
- PR: [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759)
- Omfattning: 9 svenska PO-poster i equalizerdialogerna.

Batchen ersätter det onödiga engelska lånet `rolloff` med **avrullning**, gör feltexten för equalizerkurvor konsekvent och använder svenska citattecken i kurvhanteringen.

Kontroller: `msgfmt` (4 443 översatta poster), Hunspell-sv, l10n-lint, svlang, diffkontroll och Gitleaks. l10n-lint rapporterar 28 befintliga varningar utanför batchen.
