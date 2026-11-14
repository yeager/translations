# Dwarf Fortress Steam — hardcoded_steam, batch 63

- Datum: 2026-11-14
- Språk: svenska (`sv`)
- Omfattning: 19 kompletta, kontextoberoende UI-, terräng-, objekt- och samtalssträngar. Sönderbrutna meningsfragment har medvetet lämnats för senare granskning i fullständigt sammanhang.
- Terminologi: följer den projektspecifika listan i `TERMINOLOGY.md`, bland annat `gruvvagn`, `spår`, `spårstopp` och `förråd`.

## Kontroller

- JSON- och kantmellanslagsvalidering: godkänd, 19/19.
- `svlang`: godkänd med en dokumenterad frekvensvarning för den avsiktliga terrängsammansättningen `Isuppåtgående`; den följer tidigare `Isspår` och `uppåtgående spår`.
- `hunspell-sv`: enbart samma avsedda domänspecifika sammansättning.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --source … --redact`: godkänd, inga hemligheter hittades.
- `l10n-lint`: inte tillämplig på den egna Transifex-deltafilens metadataformat; verktyget tolkar fältet `batch` som en katalogsträng och ger ett schemafel, inte ett språkfel.
- `msgfmt`: inte tillämplig, eftersom detta är en JSON-deltafil för Transifex API och ingen gettext-katalog.

## Upstream

- Skickad via ett bulk-`PATCH` till Transifex API: 19 uppdaterade, 0 fel.
- Efterföljande direkt återläsning från Transifex: 19/19 översättningar matchar exakt.
- Uppladdad betyder inte granskad, godkänd eller publicerad av projektet.
