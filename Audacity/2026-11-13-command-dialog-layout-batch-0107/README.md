# Audacity: layout i kommandodialoger

- Datum: 2026-11-13
- Källcommit: `069470e`
- PR: [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759)
- Omfattning: 2 svenska PO-poster i kommandodialoger.

Batchen tar bort två oavsiktliga radbrytningar i återkopplingen för Cmd+A och Ctrl+A. Översättningen följer därmed källans enradiga dialoglayout utan att ändra budskap eller kortkommandon.

Kontroller: `msgfmt` (4 443 översatta poster), Hunspell-sv, `l10n-lint`, `svlang`, diffkontroll och Gitleaks. Hunspell-sv markerar endast kortkommandots ”Cmd”. Varken l10n-lint eller svlang träffar någon ändrad sträng.
