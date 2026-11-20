# Open Shaders – svensk fuzzy-granskning

Datum: 2026-11-20  
Projekt: Open Shaders / open-shaders  
Språk: svenska (`sv`)

## Resultat

- Före: 6 913/6 938 översatta, 25 fuzzy.
- Efter: 6 938/6 938 översatta, 0 fuzzy (100 %).
- Weblate-uppladdning: `accepted: 25`, `skipped: 6913`, `not_found: 0`.
- `msgfmt --check`: godkänd.
- `hunspell-sv`: inga träffar för den validerade filen.
- `l10n-lint`: inga anmärkningar i de 25 granskade strängarna. Komponenten innehåller sedan tidigare 30 fel och 71 varningar utanför detta ändringsset.

## Granskade områden

Fuzzy-markeringarna rörde mjuka skuggor, gräsoptimering, kontaktskuggor, kamera-/efterbehandlingsinställningar, linsöverstrålning, rörelseoskärpa, hudfukt och skuggriktning. Uppdateringarna bevarar formattering, radbrytningar och platshållare (bland annat `%.2f`, `%.0f` och `%.3f`), samt återställde saknad VR-information och korrigerade felaktigt inlagda värdeplatshållare i rubriker.
