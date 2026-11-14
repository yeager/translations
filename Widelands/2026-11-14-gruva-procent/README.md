# Widelands Add-Ons: gruvans resursutvinning

En gruvtext har granskats lokalt och skickats till Transifex.

Projekt: Widelands Add-Ons
Resurs: rotresursen
Språk: svenska (`sv`)
Transifex-sträng: 612431474

Platshållarna `%1%%%` och `%2%%%` är bevarade. Procenttecknen är en del av
Widelands egen platshållarsyntax och ska inte normaliseras.

## Verifiering

- `msgfmt --check --statistics`
- `l10n-lint --language sv --check`
- Hunspell-sv och svlang, med manuell kontextgranskning
- `git diff --check`
- Gitleaks
- Transifex: sparad och återläst utan QA-varning
