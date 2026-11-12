# iD Editor, svenska: kraftledningsstolpar

- Projekt/resurs: `o:openstreetmap:p:id-editor:r:presets`
- Källa: Transifex, 2026-11-12
- Omfattning: 20 tidigare oöversatta strängar om utformningar av kraftledningsstolpar.
- Status: uppladdade i ett Transifex API-anrop och lästa tillbaka. De är inte formellt granskade i Transifex.
- Återstående i resursen efter batchen: 2 strängar ("Building Power Anchor" samt dess söktermer), avvaktande verifiering mot taggningsschemat.

## Terminologi

| Engelska | Svenska | Anmärkning |
| --- | --- | --- |
| H-Frame | H-stativ | Stolpkonstruktion med H-form. |
| Guyed H-Frame | Stagat H-stativ | `guyed` avser stagning. |
| Three-Level | Tre nivåer | Nivåer av ledare/isolatorer. |
| Monopolar | Enpolig | Enpolig konstruktion. |
| Barrel | Tunnformad | Formbeskrivning för konstruktionen. |

## Kontroller

- JSON-struktur och käll-/målparitet: godkända.
- `l10n-lint`: inga fel.
- `svlang`: inga engelska rester eller otillåtna stilträffar.
- `hunspell-sv`: godkänt efter facktermsbedömning.
- `git diff --check`: godkänt.
- `gitleaks detect --no-git --redact`: inga hemligheter.
- `msgfmt`: ej tillämpligt; resursen är JSON, inte Gettext.

Rådata har bevarats oförändrad som export- och API-filer. `candidates-before-upload.json` är granskningsbatchen.
