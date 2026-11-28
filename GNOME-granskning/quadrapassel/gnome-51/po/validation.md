# Validering — Quadrapassel gnome-51/po (2026-11-28)

- `msgfmt --check --check-format`: godkänd.
- `msgcmp --use-fuzzy` mot senaste POT: godkänd.
- `l10n-lint --language sv --no-terminology`: 0 fel, 0 varningar. Två informationsnotiser gäller att accelerator-understrecket flyttats med det svenska ordet; acceleratorerna finns kvar och använder latinska bokstäver.
- Platshållare och acceleratorer jämförda: inga avvikelser; inga `_å`, `_ä` eller `_ö`.
- Hunspell `hunspell -d sv_SE -l`: bara produktnamnet Quadrapassel flaggades; dokumenterat i `hunspell-exceptions.md`.
- 103/103 strängar översatta, 0 fuzzy, 0 oöversatta.
- Ingen GNOME-inskickning har gjorts.
