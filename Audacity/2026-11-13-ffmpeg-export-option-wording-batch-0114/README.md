# Audacity: FFmpeg-exportens alternativ

- Datum: 2026-11-13
- Källcommit: `51ea148`
- PR: [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759)
- Omfattning: 5 svenska PO-poster för FFmpeg-exportalternativ och bibliotekshämtning.

I en ljudexport är en FFmpeg `Frame` en **ram**, inte en videobildruta. Batchen förtydligar dessutom hur format och kodek hittas, och använder direkta svenska åtgärdstexter för att hitta eller hämta FFmpeg. Produktnamnet `FFmpeg` lämnas oförändrat.

Kontroller: `msgfmt` (4 443 översatta poster), avgränsad Hunspell-sv, `l10n-lint`, `svlang`, diffkontroll och Gitleaks. Hunspell-sv markerar enbart produktnamnet `FFmpeg`. Varken l10n-lint eller svlang träffar någon ändrad sträng.
