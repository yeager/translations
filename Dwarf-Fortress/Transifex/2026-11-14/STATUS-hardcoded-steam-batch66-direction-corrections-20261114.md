# Dwarf Fortress Steam — hardcoded_steam, batch 66 correction

- Datum: 2026-11-14
- Språk: svenska (`sv`)
- Omfattning: tre terrängetiketter från batch 63–65.
- Rättning: väderstreck inom parentes är Dwarf Fortress-koder och ska bevaras oförändrade. `NE` och `W` återställdes därför från felaktigt lokaliserade `NO` respektive `V`.

## Kontroller och upstream

- JSON-validering, `git diff --check` och Gitleaks: godkända.
- `hunspell-sv`: endast avsedda domänsammansättningar och riktkoder.
- `msgfmt` och `l10n-lint`: inte tillämpliga på denna JSON-deltafil.
- Transifex bulk-`PATCH`: 3 uppdaterade, 0 fel.
- Direkt återläsning: 3/3 översättningar matchar exakt.
