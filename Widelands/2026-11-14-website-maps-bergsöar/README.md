# Widelands Add-Ons: Website Maps, bergsöar

En kartbeskrivning har granskats lokalt och skickats till Transifex.

Projekt: Widelands Add-Ons
Resurs: Website Maps (`websitemaps`)
Språk: svenska (`sv`)
Transifex-sträng: 629413282

Sex HTML-radbrytningar är bevarade. Termerna resurs, bergsö och hamn är anpassade till Widelands kartkontext.

## Verifiering

- `msgfmt --check --statistics`
- `l10n-lint --language sv --check`
- Hunspell-sv och svlang, med manuell kontextgranskning
- `git diff --check`
- Gitleaks
- Transifex: sparad och återläst; sex br-platshållare bevarade utan QA-varning
