# Status: Dwarf Fortress `text_set`, batch 5

Datum: 2026-11-13

## Omfattning och resultat

- Granskade och ändrade strängar: 10
- Kontext: boktitelsmallar med enbart den dynamiska kontrollsekvensen `[NAME]`.
- Uppladdning: Transifex REST API, ett anrop med 10 poster
- API-resultat: HTTP 200, 10 uppdateringar, inga API-fel
- Återläsning: 10 av 10 måltexter matchade exakt efter uppladdningen
- Kvar efter batchen: 302 oöversatta strängar, verifierat genom en paginerad Transifex API-inventering.

## Kontroller

| Kontroll | Resultat | Kommentar |
| --- | --- | --- |
| JSON | Godkänd | 10 giltiga JSONL-poster. |
| Platshållare | Godkänd | `[NAME]` bevarad i samtliga titlar. |
| Svenska sammansättningar | Godkänd | Ingen otillåten följd av tre identiska konsonanter. |
| Em dash | Godkänd | Ingen em dash tillagd. |
| hunspell-sv | Godkänd med medvetet undantag | Enda träffen var `NAME` i den bevarade kontrollsekvensen `[NAME]`. |
| svlang skrivregler | Godkänd | Samtliga 10 måltexter utan träffar. |
| l10n-lint | Godkänd | Inga träffar. |
| msgfmt | Ej tillämpligt | Batchen är JSONL, inte GNU gettext PO. |
| `git diff --check` | Godkänd | Inga blankstegsproblem. |
| Gitleaks | Godkänd | Inga hemligheter hittades i deltafilen. |
