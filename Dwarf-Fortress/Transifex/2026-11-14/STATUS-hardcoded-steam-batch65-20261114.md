# Dwarf Fortress Steam — hardcoded_steam, batch 65

- Datum: 2026-11-14
- Språk: svenska (`sv`)
- Omfattning: 34 kompletta gränssnittstexter för kartläge, navigering, förråd, verkstäder, samtalsval, djurhållning och spelstatus.
- Terminologi: kontrollerad mot tidigare Dwarf Fortress-batcher; bland annat `invånare`, `förråd`, `verkstad`, `tangentbordsmarkör`, `karavan` och `bultar`.

## Kontroller

- JSON- och kantmellanslagsvalidering: godkänd, 34/34.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --source … --redact`: godkänd, inga hemligheter hittades.
- `hunspell-sv`: endast `nedåtpilar`, en korrekt svensk sammansättning.
- `svlang`: en falsk positiv V2-varning för det grammatiskt korrekta samordnade imperativet `Stå redo men öppna inte eld`.
- `l10n-lint`: inte tillämplig på den egna Transifex-deltafilens metadataformat; schemafelet på fältet `batch` är en falsk positiv.
- `msgfmt`: inte tillämplig, eftersom detta är en JSON-deltafil för Transifex API och ingen gettext-katalog.

## Upstream

- Skickad via ett bulk-`PATCH` till Transifex API: 34 uppdaterade, 0 fel.
- Efterföljande direkt återläsning från Transifex: 34/34 översättningar matchar exakt.
- Uppladdad betyder inte granskad, godkänd eller publicerad av projektet.
