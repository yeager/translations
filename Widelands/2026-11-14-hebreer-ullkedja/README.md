# Widelands Add-Ons: hebreisk ullkedja

En introduktionstext för den hebreiska stammen har granskats lokalt och skickats till Transifex.

Projekt: Widelands Add-Ons
Resurs: rotresursen
Språk: svenska (`sv`)
Transifex-sträng: 614705703

"Tyg" följer den befintliga svenska Widelands-översättningen. Produktionskedjans tre led anges med svenska byggnads- och yrkestermer.

## Verifiering

- `msgfmt --check --statistics`
- `l10n-lint --language sv --check`
- Hunspell-sv och svlang, med manuell kontextgranskning
- `git diff --check`
- Gitleaks
- Transifex: sparad och återläst utan QA-varning
