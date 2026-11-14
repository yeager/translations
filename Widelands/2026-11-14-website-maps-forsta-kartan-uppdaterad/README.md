# Widelands Add-Ons: Website Maps, uppdaterad första karta

En kartbeskrivning har granskats lokalt och skickats till Transifex.

Projekt: Widelands Add-Ons
Resurs: Website Maps (`websitemaps`)
Språk: svenska (`sv`)
Transifex-sträng: 613204974

Kartbeskrivningens URL:er, avdelare och fem radbrytningar bevaras. "Stöd" används för YouTube-länken.

## Verifiering

- `msgfmt --check --statistics`
- `l10n-lint --language sv --check`
- Hunspell-sv och svlang, med manuell kontextgranskning
- `git diff --check`
- Gitleaks
- Transifex: sparad och återläst; fem radbrytningar och båda URL:erna bevarade utan QA-varning
