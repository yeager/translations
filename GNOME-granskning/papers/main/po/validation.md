# Validering — Papers main/po (2026-11-28)

- `msgfmt --check --check-format`: godkänd.
- `msgcmp --use-fuzzy` mot senaste POT: godkänd.
- `l10n-lint --language sv --no-terminology`: 0 fel och 1 dokumenterad varning. Varningen gäller identiska svenska singular-/pluralformer för `{}` pending job in queue; ordet `jobb` har samma form i singular och plural.
- Platshållare, radbrytningar och acceleratorer jämförda: 0 avvikelser; inga nordiska acceleratorer (`_å`, `_ä`, `_ö`).
- Hunspell-undantag dokumenteras i `hunspell-exceptions.md`.
- Senaste POT har 493 aktiva strängar. Granskad fil: 493 översatta, 0 fuzzy, 0 oöversatta.
- Ingen GNOME-inskickning har gjorts.
