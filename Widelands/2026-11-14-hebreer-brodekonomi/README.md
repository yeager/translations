# Widelands Add-Ons: hebreisk brödekonomi

En introduktionstext för den hebreiska stammen har granskats lokalt och skickats till Transifex.

Projekt: Widelands Add-Ons
Resurs: rotresursen
Språk: svenska (`sv`)
Transifex-sträng: 614705701

Byggnadskedjan uttrycks med svenska speltermer: gårdar, tröskplatser, kvarnar och bagerier.

## Verifiering

- `msgfmt --check --statistics`
- `l10n-lint --language sv --check`
- Hunspell-sv och svlang, med manuell kontextgranskning
- `git diff --check`
- Gitleaks
- Transifex: sparad och återläst utan QA-varning
