# Status: Dwarf Fortress `text_set`, batch 1

Datum: 2026-11-13

## Resultat

- Granskade och ändrade strängar: 10
- Uppladdning: Transifex REST API, en batch med 10 poster
- API-resultat: HTTP 200, 10 uppdateringar, inga API-fel
- Återläsning: 10 av 10 måltexter matchade exakt efter uppladdning
- Kvar efter batchen: 339 oöversatta strängar, verifierat genom en paginerad Transifex API-inventering efter uppladdningen.

## Kontroller

| Kontroll | Resultat | Kommentar |
| --- | --- | --- |
| JSON | Godkänd | 10 giltiga JSONL-poster. |
| Platshållare | Godkänd | `[PRO_POS]` bevarad i båda berörda strängarna. |
| Svenska sammansättningar | Godkänd | Ingen otillåten följd av tre identiska konsonanter. |
| Em dash | Godkänd | Ingen em dash tillagd. |
| hunspell-sv | Godkänd med medvetet undantag | Enda träffen var `POS` i den bevarade kontrollsekvensen `[PRO_POS]`. |
| svlang skrivregler | Godkänd | Samtliga 10 måltexter utan träffar. |
| l10n-lint | Godkänd | Kördes mot en tillfällig explicit JSON-katalog med samma käll- och måltexter; verktyget saknar direktstöd för Transifex JSONL-deltat. |
| msgfmt | Ej tillämpligt | Batchen är JSONL, inte GNU gettext PO. |
| `git diff --check` | Godkänd | Inga blankstegsproblem. Ny fil returnerar den förväntade diffstatusen 1. |
| Gitleaks | Godkänd | Inga hemligheter hittades i deltafilen. |

## Återstående arbete

Fortsätt med en separat, kontextgranskad batch. Återanvänd denna terminologi tills en etablerad svensk projektterm eller tydligare spelkontext motiverar ett annat val.
