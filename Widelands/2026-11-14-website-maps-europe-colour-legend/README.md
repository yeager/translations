# Widelands Add-Ons: Website Maps, Europakarta

En kartförklaring har granskats lokalt och ska skickas till Transifex.

| Fält | Värde |
| --- | --- |
| Projekt | Widelands Add-Ons |
| Resurs | Website Maps (`websitemaps`) |
| Språk | svenska (`sv`) |
| Transifex-sträng | 629413268 |
| Ändring | Språkriktig kartbeskrivning och svensk färgförklaring |

Källtextens `europe` är normaliserat till `Europa`. Länder och färger återges med svenska namn, och likhetstecknen behålls eftersom de fungerar som kartnyckel.

## Verifiering

- `msgfmt --check --statistics`
- `l10n-lint --language sv --check`
- Hunspell-sv och svlang, med manuell kontextgranskning
- `git diff --check`
- Gitleaks
- Transifex: sparad och återläst utan QA-varning

Översättningen är lokalt granskad. Kontot saknar behörighet att markera den som officiellt granskad i Transifex.
