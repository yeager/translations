# Audacity: FFmpeg-exportens diagnostik

- Datum: 2026-11-13
- Källcommit: `e46a112`
- PR: [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759)
- Omfattning: 9 svenska PO-poster för FFmpeg-exportens etiketter och felmeddelanden.

Batchen gör exportdiagnostiken konsekvent med **aktuell kodek**, **utdatafil** och **samplingsbuffert**. Felmeddelandena använder svensk meningsbyggnad och konsekvent kolonplacering efter `FFmpeg`, men bevarar källans vanliga bindestreck efter felindikatorn. `FFmpeg`, `FIFO` och `nAudioFrameSizeOut` är tekniska namn och lämnas oförändrade.

Kontroller: `msgfmt` (4 443 översatta poster), avgränsad Hunspell-sv, `l10n-lint`, `svlang`, diffkontroll och Gitleaks. Hunspell-sv markerar enbart de avsiktligt bibehållna tekniska namnen. Varken l10n-lint eller svlang träffar någon ändrad sträng.
