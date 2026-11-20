# Foundation – svenska granskning: tutorial.json, del 3

Datum: 2026-11-20  
Metod: Crowdin API; `l10n-lint --language sv`; `hunspell -d sv_SE`.

| Sträng-ID | Engelsk källa | Tidigare svenska | Föreslagen svenska | Resultat |
|---|---|---|---|---|
| 23581 | {1} to paint zone | {1} för att måla zon | {1} för att måla en zon | Sparad i Crowdin (201) |
| 23583 | {1} to unpaint zone | {1} för att avmåla zon | {1} för att ta bort en målad zon | Sparad i Crowdin (201) |
| 23697 | {1} when placing a part to place multiple | {1} vid placering av en del för att placera flera | {1} när du placerar en del för att placera flera delar | Sparad i Crowdin (201) |
| 23703 | {1} when selecting parts to select multiple | {1} vid val av delar för att välja flera | {1} när du väljer delar för att välja flera | Sparad i Crowdin (201) |

## Validering

- `l10n-lint`: inga problem.
- `hunspell-sv`: inga stavningsanmärkningar.
- Platshållaren `{1}` har bevarats.
