# Widelands Add-Ons: Website Maps, barnkarta

En kartbeskrivning har granskats lokalt och ska skickas till Transifex.

Projekt: Widelands Add-Ons
Resurs: Website Maps (websitemaps)
Språk: svenska (sv)
Transifex-sträng: 629413279

Två HTML-radbrytningar bevaras. Uttrycket 1v1 återges naturligt som en mot en.

## Verifiering

- msgfmt --check --statistics
- l10n-lint --language sv --check
- Hunspell-sv och svlang, med manuell kontextgranskning
- git diff --check
- Gitleaks
- Transifex: sparad och återläst; två br-platshållare bevarade utan QA-varning
