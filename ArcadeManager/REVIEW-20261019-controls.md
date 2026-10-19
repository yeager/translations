# ArcadeManager Swedish control review — 2026-10-19

- Reviewed all 16 Weblate checks.
- The checks were false positives from established technical and product names: ROM, MAME, RetroArch, and RetroPie.
- Corrected the older HTML help text `OVERLAYS_RATOMAME_TARGET_DESC`: Swedish abbreviation formatting is now `(t.ex. cmameartworks)`.
- Weblate API after review: 340/340 translated and 0 failing checks.
- Validation: `msgfmt --check --check-format`, `svlang skrivregler`, l10n-lint (0 errors; one intentional punctuation-style warning for `t.ex.` versus the source's `ex:`), and Gitleaks.
