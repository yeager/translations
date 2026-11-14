# Widelands Add-Ons: Website Maps, karta för två spelare

En kort kartbeskrivning har granskats lokalt och ska skickas till Transifex.

Projekt: Widelands Add-Ons
Resurs: Website Maps (websitemaps)
Språk: svenska (sv)
Transifex-sträng: 629413271

Den dubbelspråkiga källtexten återger samma innehåll på tyska och engelska. Översättningen återger det en gång på svenska. Källans em dash och fyra HTML-radbrytningar bevaras.

## Verifiering

- msgfmt --check --statistics
- l10n-lint --language sv --check
- Hunspell-sv och svlang, med manuell kontextgranskning
- git diff --check
- Gitleaks
- Transifex: sparad och återläst; fyra br-platshållare bevarade utan QA-varning

Översättningen är lokalt granskad. Kontot saknar behörighet att markera den som officiellt granskad i Transifex.
