# Widelands Add-Ons: Website Maps, Clear Lake

En kartbeskrivning har granskats lokalt och skickats till Transifex.

| Fält | Värde |
| --- | --- |
| Projekt | Widelands Add-Ons |
| Resurs | Website Maps (`websitemaps`) |
| Språk | svenska (`sv`) |
| Transifex-sträng | 629413267 |
| Källa | Kartbeskrivning för en sjö i norra Kalifornien |
| Ändring | Svensk, idiomatisk kartbeskrivning med bevarade HTML-radbrytningar |

`chaparral` är en etablerad svensk fackterm för den kaliforniska hårdbladsvegetationen. Kartnamnet `Lake Tahoe` och formatet `512 × 512` har behållits sakligt.

## Verifiering

- `msgfmt --check --statistics`
- `l10n-lint --language sv --check`
- Hunspell-sv, med manuell kontroll av egennamnet `Lake Tahoe` och facktermen `chaparral`
- svlang, med manuell språkgranskning
- `git diff --check`
- Gitleaks
- Transifex: sparad och återläst; fyra `<br>`-platshållare bevarade och ingen platshållarvarning visades

Översättningen är lokalt granskad. Kontot saknar behörighet att markera den som officiellt granskad i Transifex.
