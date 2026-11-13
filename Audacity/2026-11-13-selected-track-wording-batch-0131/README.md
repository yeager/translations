# Audacity: valt spår och utsträckning

- Datum: 2026-11-13
- Källcommit: `ca77231`
- PR: [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759)
- Omfattning: 2 svenska PO-poster i notspårs- och klippkontroller.

Batchen använder det kompletta partikelverbet **sträcka ut** i draginstruktionen och ger spåråtgärden korrekt bestämd form: **Slå av/på ljudet för spåret**.

Kontroller: `msgfmt` (4 443 översatta poster), avgränsad Hunspell-sv, `l10n-lint`, `svlang`, diffkontroll och Gitleaks. Inga av verktygen träffar någon ändrad post.
