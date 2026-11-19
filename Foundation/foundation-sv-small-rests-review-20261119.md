# Foundation – små reststrängar, svensk granskningsbatch 2026-11-19

Fyra oöversatta svenska strängar har granskats via Crowdin API. Förslagen är utkast och har inte sparats i Crowdin.

| Sträng-ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 26666 | Going to {1} | — | På väg till {1} |
| 26668 | Special rules | — | Särskilda regler |
| 26404 | Produce Cabbages at a Cabbage Farm | — | Producera kål på en kålodling |
| 26702 | View in Compendium | — | Visa i kompendiet |

## Kontroller

- `l10n-lint --language sv` passerade utan anmärkningar.
- `hunspell -d sv_SE` passerade utan anmärkningar.
- Platshållaren `{1}` är bevarad exakt.
