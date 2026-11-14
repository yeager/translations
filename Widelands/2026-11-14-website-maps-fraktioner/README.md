# Widelands Add-Ons: Website Maps, fraktioner

En strukturtät kartbeskrivning har granskats lokalt och ska skickas till Transifex.

Projekt: Widelands Add-Ons
Resurs: Website Maps (websitemaps)
Språk: svenska (sv)
Transifex-sträng: 629413273

Källtexten innehåller tjugo HTML-radbrytningar, listor och otydliga fraktionsnamn. Strukturen bevaras exakt och de otydliga namnen återges försiktigt utan att tillföra ny spelinformation.

## Verifiering

- msgfmt --check --statistics
- l10n-lint --language sv --check
- Hunspell-sv och svlang, med manuell kontextgranskning
- git diff --check
- Gitleaks
- Transifex: sparad och återläst; tjugo br-platshållare bevarade utan QA-varning

Översättningen är lokalt granskad. Kontot saknar behörighet att markera den som officiellt granskad i Transifex.
