# Dwarf Fortress Steam — hardcoded_steam, batch 69

- Datum: 2026-11-14
- Språk: svenska (`sv`)
- Omfattning: 18 kompletta instruktioner, statusetiketter och samtalsrader.

## Kontroller och upstream

- JSON- och kantmellanslagsvalidering: godkänd, 18/18.
- `git diff --check` och Gitleaks: godkända.
- `hunspell-sv`: den första formuleringen `lerinsamling` ändrades till `zon för att samla lera` efter kontroll; inga kvarvarande stavningsfrågor.
- `svlang`: kvarvarande varning gäller korrekt ordföljd i `Den här varelsen är känd som död` och är en falsk positiv.
- `l10n-lint` och `msgfmt`: inte tillämpliga på JSON-deltafilen.
- Transifex bulk-`PATCH`: 18 uppdaterade, 0 fel; direkt återläsning: 18/18 exakt match.
- Uppladdad betyder inte granskad, godkänd eller publicerad av projektet.
