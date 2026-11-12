# iD Editor, svenska: kraftledningsfäste på byggnad

- Projekt/resurs: `o:openstreetmap:p:id-editor:r:presets`
- Källa: iD:s taggningsschema `power/terminal` och OSM-wikin för `power=terminal`, kontrollerade 2026-11-12.
- Omfattning: de sista 2 tidigare oöversatta strängarna i resursen.
- Status: uppladdade i ett Transifex API-anrop och lästa tillbaka. Resursen har 0 oöversatta svenska strängar efter uppladdningen. Strängarna är ännu inte formellt granskade i Transifex.

## Kontext och terminologi

`power=terminal` är anslutningspunkten där en luftledning avslutas på en byggnad eller vägg. Den svenska UI-texten är därför **Kraftledningsfäste på byggnad**. Söktermerna är `kraftledningsfäste`, `byggnadsfäste`, `kraftledningsankare` och `elanslutning`.

## Kontroller

- JSON-struktur och käll-/målparitet: godkända.
- `l10n-lint`: inga fel.
- `svlang svengelska`: inga engelska rester.
- `svlang check`: enda träffen är den avsiktliga facktermen `kraftledningsankare`.
- `hunspell-sv`: samma fackterm saknas i ordlistan men är korrekt i detta sammanhang.
- `git diff --check`: godkänt.
- `gitleaks detect --no-git --redact`: inga hemligheter.
- `msgfmt`: ej tillämpligt; resursen är JSON, inte Gettext.
