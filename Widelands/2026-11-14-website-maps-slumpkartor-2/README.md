# Widelands Add-Ons: Website Maps, tre slumpkartor

Tre maskinframställda kartparameterlistor har granskats lokalt och ska skickas till Transifex.

Projekt: Widelands Add-Ons
Resurs: Website Maps (websitemaps)
Språk: svenska (sv)
Transifex-strängar: 629413276, 629413277, 629413278

Alla numeriska värden och kart-ID:n är oförändrade. Det tyska nivåordet Hoch är översatt till Hög.

## Verifiering

- msgfmt --check --statistics
- l10n-lint --language sv --check
- Hunspell-sv och svlang, med manuell kontextgranskning
- git diff --check
- Gitleaks
- Transifex: samtliga tre sparade och återlästa utan QA-varning
