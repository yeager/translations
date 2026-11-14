# Dwarf Fortress Steam — hardcoded_steam, batch 68

- Datum: 2026-11-14
- Språk: svenska (`sv`)
- Omfattning: 20 kompletta status-, gränssnitts- och samtalssträngar.
- Terminologi: `NSW` har bevarats som riktkod; `Magmasmältare` används för byggnaden `Magma smelter`.

## Kontroller och upstream

- JSON- och kantmellanslagsvalidering: godkänd, 20/20.
- `git diff --check` och Gitleaks: godkända.
- `hunspell-sv`: endast den avsedda sammansättningen `Magmasmältare` och riktkoden `NSW`.
- `svlang`: en falsk positiv V2-varning för det korrekta imperativet `Centrera på den länkade byggnaden`.
- `l10n-lint` och `msgfmt`: inte tillämpliga på JSON-deltafilen.
- Transifex bulk-`PATCH`: 20 uppdaterade, 0 fel; direkt återläsning: 20/20 exakt match.
- Uppladdad betyder inte granskad, godkänd eller publicerad av projektet.
