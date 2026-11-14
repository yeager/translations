# Widelands Add-Ons: Website Maps, Skivvärlden

En kartbeskrivning har granskats lokalt och ska skickas till Transifex.

| Fält | Värde |
| --- | --- |
| Projekt | Widelands Add-Ons |
| Resurs | Website Maps (`websitemaps`) |
| Språk | svenska (`sv`) |
| Transifex-sträng | 629413269 |
| Ändring | Naturlig svensk kartbeskrivning med bevarade HTML-radbrytningar |

`Skivvärlden` är den etablerade svenska benämningen för Discworld. Den dubbelspråkiga källtexten återger samma innehåll på tyska och engelska; översättningen återger innehållet en gång på svenska.

## Verifiering

- `msgfmt --check --statistics`
- `l10n-lint --language sv --check`
- Hunspell-sv och svlang, med manuell kontextgranskning
- `git diff --check`
- Gitleaks
- Transifex: sparad och återläst; två `<br>`-platshållare bevarade utan QA-varning

Översättningen är lokalt granskad. Kontot saknar behörighet att markera den som officiellt granskad i Transifex.
