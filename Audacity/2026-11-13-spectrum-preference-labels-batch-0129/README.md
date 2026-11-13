# Audacity: etiketter i spektruminställningar

- Datum: 2026-11-13
- Källcommit: `0ce4a2d`
- PR: [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759)
- Omfattning: 3 svenska PO-poster i spektruminställningarna.

Batchen rättar versaliseringen av **klassisk** och gör de två beskrivningarna av FFT-fönstrets bandbredd grammatiskt kompletta: **störst bandbredd** respektive **minst bandbredd**.

Kontroller: `msgfmt` (4 443 översatta poster), avgränsad Hunspell-sv, `l10n-lint`, `svlang`, diffkontroll och Gitleaks. Inga av verktygen träffar någon ändrad post.
