# Status: Dwarf Fortress `text_set`, batch 8

Datum: 2026-11-13

## Omfattning och resultat

- Granskade och ändrade strängar: 9
- Kontext: boktitelsmallar med den dynamiska kontrollsekvensen `[NAME]`.
- Uppladdning: Transifex REST API, ett anrop med 9 poster
- API-resultat: HTTP 200, 9 uppdateringar, inga API-fel
- Återläsning: 9 av 9 måltexter matchade exakt efter uppladdningen
- Kvar efter batchen: 273 oöversatta strängar, verifierat genom en paginerad Transifex API-inventering.

## Kontroller

| Kontroll | Resultat | Kommentar |
| --- | --- | --- |
| JSON | Godkänd | 9 giltiga JSONL-poster. |
| Platshållare | Godkänd | `[NAME]` bevarad i samtliga titlar. |
| Svenska sammansättningar | Godkänd | Ingen otillåten följd av tre identiska konsonanter. |
| Em dash | Godkänd | Ingen em dash tillagd. |
| hunspell-sv | Godkänd med medvetet undantag | Enda träffen var kontrollsekvensen `NAME`. |
| svlang skrivregler | Godkänd | Samtliga 9 måltexter utan träffar. |
| l10n-lint | Godkänd | Inga fel eller varningar. Fyra informationsnotiser gäller avsiktlig omflyttning av `[NAME]` i två titlar. |
| msgfmt | Ej tillämpligt | Batchen är JSONL, inte GNU gettext PO. |
| `git diff --check` | Godkänd | Inga blankstegsproblem. |
| Gitleaks | Godkänd | Inga hemligheter hittades i deltafilen. |
