# Widelands Add-Ons: Website Maps, slumpkarta

En maskinframställd kartbeskrivning har granskats lokalt och ska skickas till Transifex.

Projekt: Widelands Add-Ons
Resurs: Website Maps (websitemaps)
Språk: svenska (sv)
Transifex-sträng: 629413275

Alla numeriska värden, kart-ID:t och sju HTML-radbrytningar bevaras. Det tyska nivåordet Hoch är översatt till Hög.

## Verifiering

- msgfmt --check --statistics
- l10n-lint --language sv --check
- Hunspell-sv och svlang, med manuell kontextgranskning
- git diff --check
- Gitleaks
- Transifex: sparad och återläst; sju br-platshållare och kart-ID bevarade utan QA-varning
