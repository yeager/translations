# Widelands Add-Ons: Website Maps, hebreiskt byggmaterial

En kartinstruktion har granskats lokalt och skickats till Transifex.

Projekt: Widelands Add-Ons
Resurs: Website Maps (`websitemaps`)
Språk: svenska (`sv`)
Transifex-sträng: 614705700

"Lergropar" följer Widelands befintliga svenska resursterminologi. "Stugor för greninsamling" beskriver byggnadens funktion utan ett onaturligt sammansatt namn.

## Verifiering

- `msgfmt --check --statistics`
- `l10n-lint --language sv --check`
- Hunspell-sv och svlang, med manuell kontextgranskning
- `git diff --check`
- Gitleaks
- Transifex: sparad och återläst utan QA-varning
