# Zrythm main, svensk granskning 2026-10-18

Katalogen innehåller 694 aktiva strängar. Alla är översatta och ingen sträng är markerad som osäker.

Granskningen omfattar bland annat licenser, insticksmoduler, förinställningar, projektåtgärder, spår- och objektkommandon samt inläsnings- och felmeddelanden.

Kontroller:

- `msgfmt --check --check-format`: godkänd
- `l10n-lint`: inga fel; en förväntad informationsvarning för en svensk plural där båda formerna är identiska
- `svlang skrivregler`: godkänd
- `hunspell-sv`: 80 kvarvarande ord har granskats som projektnamn, ljudtekniska termer, förkortningar och sammansättningar
- `gitleaks`: inga läckor i katalogen

Weblate-importen återstår tills den lokala webbläsaranslutningen är tillgänglig igen.
