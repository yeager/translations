# Validering — Resources main/po (2026-11-28)

- `msgfmt --check --check-format`: godkänd på färdig katalog.
- `msgcmp --use-fuzzy` mot senaste POT: godkänd.
- `l10n-lint --language sv --no-terminology`: 0 fel, 0 varningar. Linten ger informationsnotiser för `N/A` → `-` och grammatisk pluraländelse (`processer`); båda är avsiktliga.
- Platshållarjämförelse för samtliga singular- och pluralformer: 0 avvikelser.
- Hunspell `hunspell -d sv_SE -l` på ändrade översättningar: endast de tre dokumenterade tekniska termerna ovan.
- POT och PO innehåller 395 aktiva poster; 0 fuzzy och 0 tomma i granskad fil.
- Ingen uppladdning eller kommentar har skickats till GNOME.
