# Audacity: dynamik- och insticksmodultermer

- Datum: 2026-11-13
- Källcommit: `b18cbb6`
- PR: [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759)
- Omfattning: 3 svenska PO-poster i dynamikprocessorn och equalizern.

Batchen normaliserar `Actual Compression` till **faktisk komprimering** i både graf och historik, använder **leverantör** för en insticksmoduls `Vendor` och hänvisar konsekvent till **equalizern** som effekt.

Kontroller: `msgfmt` (4 443 översatta poster), avgränsad Hunspell-sv, `l10n-lint`, `svlang`, diffkontroll och Gitleaks. Hunspell-sv markerar enbart den avsedda tekniska formen `equalizern`; l10n-lint och svlang har inga träffar i de ändrade posterna.
