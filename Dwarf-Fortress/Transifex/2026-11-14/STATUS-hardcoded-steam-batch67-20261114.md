# Dwarf Fortress Steam — hardcoded_steam, batch 67

- Datum: 2026-11-14
- Språk: svenska (`sv`)
- Omfattning: 40 kompletta strängar för strids- och gruppkommandon, spelstatus, samtalsval, kart- och systemetiketter.
- Terminologi: följer den lokala Dwarf Fortress-listan. Koden `SEW` i en terrängetikett har bevarats ordagrant.

## Kontroller

- JSON- och kantmellanslagsvalidering: godkänd, 40/40.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --source … --redact`: godkänd, inga hemligheter hittades.
- `hunspell-sv`: endast avsedd terrängsammansättning och koden `SEW`.
- `svlang`: två falska V2-varningar för grammatiskt korrekta imperativ med bisats (`Uttryck …` och `Förklara att …`).
- `l10n-lint` och `msgfmt`: inte tillämpliga på denna JSON-deltafil för Transifex API.

## Upstream

- Skickad via ett bulk-`PATCH` till Transifex API: 40 uppdaterade, 0 fel.
- Efterföljande direkt återläsning från Transifex: 40/40 översättningar matchar exakt.
- Uppladdad betyder inte granskad, godkänd eller publicerad av projektet.
