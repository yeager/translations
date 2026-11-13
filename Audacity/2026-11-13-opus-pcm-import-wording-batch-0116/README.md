# Audacity: Opus-import och PCM-bitdjup

- Datum: 2026-11-13
- Källcommit: `bed72fe`
- PR: [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759)
- Omfattning: 7 svenska PO-poster för Opus-import och PCM-format.

Batchen gör Opus-felmeddelandet begripligt genom att ange att kanalantalet ändras mitt i filen. Den normaliserar även bitdjup enligt svensk sammansättningsform: `8-bitars`, `12-bitars`, `16-bitars` och `24-bitars`. Formatnamnen `DWVW` och `DPCM` är tekniska namn och behålls oförändrade.

Kontroller: `msgfmt` (4 443 översatta poster), avgränsad Hunspell-sv, `l10n-lint`, `svlang`, diffkontroll och Gitleaks. Hunspell-sv markerar enbart de avsiktligt bibehållna formatnamnen `DPCM` och `DWVW`. Varken l10n-lint eller svlang träffar någon ändrad sträng.
