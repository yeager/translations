# Widelands Add-Ons: Website Maps, laguppställning

En kort kartnotis har granskats lokalt och ska skickas till Transifex.

Projekt: Widelands Add-Ons
Resurs: Website Maps (websitemaps)
Språk: svenska (sv)
Transifex-sträng: 629413280

Tre HTML-radbrytningar och alla spelarnummer bevaras.

## Verifiering

- msgfmt --check --statistics
- l10n-lint --language sv --check
- Hunspell-sv och svlang, med manuell kontextgranskning
- git diff --check
- Gitleaks
- Transifex: sparad och återläst; tre br-platshållare och alla spelarnummer bevarade utan QA-varning
