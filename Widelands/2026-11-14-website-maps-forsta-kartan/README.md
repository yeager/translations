# Widelands Add-Ons: Website Maps, första kartan

En kartpresentation med externa länkar har granskats lokalt och ska skickas till Transifex.

Projekt: Widelands Add-Ons
Resurs: Website Maps (websitemaps)
Språk: svenska (sv)
Transifex-sträng: 629413272

De två URL:erna är oförändrade. Samtliga sju HTML-radbrytningar och avdelaren med fem bindestreck bevaras.

## Verifiering

- msgfmt --check --statistics
- l10n-lint --language sv --check
- Hunspell-sv och svlang, med manuell kontextgranskning
- git diff --check
- Gitleaks
- Transifex: sparad och återläst; sju br-platshållare och båda URL:erna bevarade utan QA-varning

Översättningen är lokalt granskad. Kontot saknar behörighet att markera den som officiellt granskad i Transifex.
