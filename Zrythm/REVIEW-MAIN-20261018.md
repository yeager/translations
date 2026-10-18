# Zrythm main, svensk granskning 2026-10-18

Katalogen innehåller 694 aktiva strängar. Alla är översatta och ingen sträng är markerad som osäker.

Granskningen omfattar bland annat licenser, insticksmoduler, förinställningar, projektåtgärder, spår- och objektkommandon samt inläsnings- och felmeddelanden. De sex återstående pluralsträngarna har kompletterats med svenska singular- och pluralformer.

Kontroller:

- `msgfmt --check --check-format`: godkänd
- `l10n-lint`: inga fel; en förväntad varning för svensk plural där båda formerna är identiska
- `svlang skrivregler`: godkänd
- `hunspell-sv`: 79 kvarvarande ord har granskats som projektnamn, ljudtekniska termer, förkortningar och sammansättningar
- `gitleaks`: inga läckor i katalogen
