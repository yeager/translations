# Status: Dwarf Fortress `text_set`, batch 2

Datum: 2026-11-13

## Omfattning och resultat

- Granskade och ändrade strängar: 7
- Kontext: boktitelsmallar. Källornas textset-id används för boknamn enligt Dwarf Fortress dokumentation.
- Uppladdning: Transifex REST API, ett anrop med 7 poster
- API-resultat: HTTP 200, 7 uppdateringar, inga API-fel
- Återläsning: 7 av 7 måltexter matchade exakt efter uppladdningen
- Kvar efter batchen: 332 oöversatta strängar, verifierat genom en paginerad Transifex API-inventering.

## Kontroller

| Kontroll | Resultat | Kommentar |
| --- | --- | --- |
| JSON | Godkänd | 7 giltiga JSONL-poster. |
| Platshållare | Godkänd | `[NAME]` bevarad i samtliga relevanta titlar. |
| Svenska sammansättningar | Godkänd | Ingen otillåten följd av tre identiska konsonanter. |
| Em dash | Godkänd | Ingen em dash tillagd. |
| hunspell-sv | Godkänd med medvetet undantag | Enda träffen var `NAME` i den bevarade kontrollsekvensen `[NAME]`. |
| svlang skrivregler | Godkänd | Samtliga 7 måltexter utan träffar. |
| l10n-lint | Godkänd | Inga fel eller varningar. Två informationsnotiser gäller den avsiktliga flytten av `[NAME]` i `Framåt med [NAME]`. |
| msgfmt | Ej tillämpligt | Batchen är JSONL, inte GNU gettext PO. |
| `git diff --check` | Godkänd | Inga blankstegsproblem. |
| Gitleaks | Godkänd | Inga hemligheter hittades i deltafilen. |

## Terminologi

Inga nya återkommande facktermer tillkom. Se `TERMINOLOGY.md` för tidigare beslut.
