# Dwarf Fortress Steam — hardcoded_steam, batch 64

- Datum: 2026-11-14
- Språk: svenska (`sv`)
- Omfattning: 13 kompletta strängar för isterräng, spelinställningar, felmeddelanden, samtalsval och beskrivande UI-text. Meningsfragment med saknat sammanhang lämnades utanför batchen.
- Terminologi: sammanhängande med tidigare arkivarbete, inklusive `Isspår`, `gruvvagn`, `spår`, `förråd` och samtalsmönstret `Tillstå brist på …`.

## Kontroller

- JSON- och kantmellanslagsvalidering: godkänd, 13/13.
- `svlang`: godkänd utan varningar.
- `hunspell-sv`: endast domänspecifika, konsekventa isterrängsammansättningar (`Isspår`, `Isuppåtgående`, `Isnedåtgående`).
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --source … --redact`: godkänd, inga hemligheter hittades.
- `l10n-lint`: inte tillämplig på den egna Transifex-deltafilens metadataformat; schemafelet på fältet `batch` är en falsk positiv.
- `msgfmt`: inte tillämplig, eftersom detta är en JSON-deltafil för Transifex API och ingen gettext-katalog.

## Upstream

- Skickad via ett bulk-`PATCH` till Transifex API: 13 uppdaterade, 0 fel.
- Efterföljande direkt återläsning från Transifex: 13/13 översättningar matchar exakt.
- Uppladdad betyder inte granskad, godkänd eller publicerad av projektet.
