# Audacity: dialogers sluttecken och layout

- Datum: 2026-11-13
- Källcommit: `7204203`
- PR: [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759)
- Omfattning: 6 svenska PO-poster i dialoger, tillgänglighetsbeskrivning och HTML-text.

Batchen synkroniserar sluttecken med källans dialog- och HTML-struktur, gör beskrivningen av stereospårens storlek till en sammanhängande svensk instruktion och använder svenskt tankstreck i upphovsrättsintervallet 1999–2024. Inga em dash har införts.

Kontroller: `msgfmt` (4 443 översatta poster), Hunspell-sv, `l10n-lint`, `svlang`, diffkontroll och Gitleaks. Hunspell-sv markerar endast produktnamn och sammansättningar i Muse Hub-texten. Varken l10n-lint eller svlang träffar någon ändrad sträng.
