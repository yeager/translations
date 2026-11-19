# Foundation – handledning: befintliga svenska strängar, 2026-11-19

Radgranskning av samtliga 27 redan översatta strängar i `tutorial.json` via Crowdin API. Tre förbättringsförslag identifierades; övriga 24 bedömdes korrekta.

| ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 5046 | Left click drag | Vänsterklicka dra | Vänsterklicka och dra |
| 5068 | {1} on wall node to select/place new node | {1} på murnod för att flytta/placera ny nod | {1} på murnoden för att välja/placera en ny nod |
| 22716 | {1} and {2} to resize brush | {1} och {2} för att ändra borststorlek | {1} och {2} för att ändra penselstorleken |

## Kontroller

- `l10n-lint --language sv` passerade utan anmärkningar.
- `hunspell -d sv_SE` passerade utan anmärkningar.
- Platshållarna `{1}` och `{2}` har bevarats.
- Förslagen är utkast och har inte skickats till Crowdin.
