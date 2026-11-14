# Widelands Add-Ons: Website Maps, surrealistisk dal

En kartbeskrivning har granskats lokalt och skickats till Transifex.

Projekt: Widelands Add-Ons
Resurs: Website Maps (`websitemaps`)
Språk: svenska (`sv`)
Transifex-sträng: 629413250

Två HTML-radbrytningar bevaras. Texten använder svenska former för kartans terräng, spelupplägg och datorstyrda motståndare.

## Verifiering

- `msgfmt --check --statistics`
- `l10n-lint --language sv --check`
- Hunspell-sv och svlang, med manuell kontextgranskning
- `git diff --check`
- Gitleaks
- Transifex: sparad och återläst; två br-platshållare bevarade utan QA-varning
