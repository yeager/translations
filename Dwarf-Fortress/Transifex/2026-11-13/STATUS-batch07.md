# Status: Dwarf Fortress `text_set`, batch 7

Datum: 2026-11-13

## Omfattning och resultat

- Granskade och ändrade strängar: 10
- Kontext: boktitelsmallar med dynamiska kontrollsekvenser.
- Uppladdning: Transifex REST API, ett anrop med 10 poster
- API-resultat: HTTP 200, 10 uppdateringar, inga API-fel
- Återläsning: 10 av 10 måltexter matchade exakt efter uppladdningen
- Kvar efter batchen: 282 oöversatta strängar, verifierat genom en paginerad Transifex API-inventering.

## Kontroller

| Kontroll | Resultat | Kommentar |
| --- | --- | --- |
| JSON | Godkänd | 10 giltiga JSONL-poster. |
| Platshållare | Godkänd | `[NAME]` och `[ANY_AGE]` bevarade. |
| Svenska sammansättningar | Godkänd | Ingen otillåten följd av tre identiska konsonanter. |
| Em dash | Godkänd | Ingen em dash tillagd. |
| hunspell-sv | Godkänd med medvetet undantag | Endast kontrollsekvenserna `NAME`, `ANY` och `AGE`. |
| svlang skrivregler | Godkänd | Samtliga 10 måltexter utan träffar. |
| l10n-lint | Godkänd | Inga fel eller varningar. Sex informationsnotiser gäller avsiktlig omflyttning av `[NAME]` i tre titlar. |
| msgfmt | Ej tillämpligt | Batchen är JSONL, inte GNU gettext PO. |
| `git diff --check` | Godkänd | Inga blankstegsproblem. |
| Gitleaks | Godkänd | Inga hemligheter hittades i deltafilen. |
