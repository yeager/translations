# Foundation – svenska granskning: tutorial.json, del 2

Datum: 2026-11-20  
Metod: Crowdin API; `l10n-lint --language sv`; `hunspell -d sv_SE`.

| Sträng-ID | Engelsk källa | Tidigare svenska | Föreslagen svenska | Resultat |
|---|---|---|---|---|
| 5068 | {1} on wall node to select/place new node | {1} på murnod för att flytta/placera ny nod | {1} på murnod för att välja/placera en ny nod | Sparad i Crowdin (201) |
| 5074 | {1} and {2} to remove wall node/section | {1} och {2} för att ta bort väggnod/-sektion | {1} och {2} för att ta bort murnod/-sektion | Sparad i Crowdin (201) |
| 22716 | {1} and {2} to resize brush | {1} och {2} för att ändra borststorlek | {1} och {2} för att ändra penselstorlek | Sparad i Crowdin (201) |
| 23579 | {1} on arrows to manipulate the part | {1} på pilarna för att manipulera delen | {1} på pilarna för att justera delen | Sparad i Crowdin (201) |

## Validering

- `l10n-lint`: inga problem.
- `hunspell-sv`: inga stavningsanmärkningar.
- Platshållarna `{1}` och `{2}` har bevarats.
