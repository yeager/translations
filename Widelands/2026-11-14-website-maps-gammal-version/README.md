# Widelands Add-Ons: Website Maps, gammal version

En kartnotis har granskats lokalt och skickats till Transifex.

Projekt: Widelands Add-Ons
Resurs: Website Maps (`websitemaps`)
Språk: svenska (`sv`)
Transifex-sträng: 613406405

Webbadressen och de två radbrytningarna bevaras. Transifex återger källtextens kontrolltecken som två `br`-platshållare i redigeraren; sparad översättning har två motsvarande platshållare och ingen QA-varning.

## Verifiering

- `msgfmt --check --statistics`
- `l10n-lint --language sv --check`
- Hunspell-sv och svlang, med manuell kontextgranskning
- `git diff --check`
- Gitleaks
- Transifex: sparad och återläst; URL och två radbrytningar bevarade utan QA-varning
