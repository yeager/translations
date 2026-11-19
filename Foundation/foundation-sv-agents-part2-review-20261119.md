# Foundation – agenter II, svensk granskning 2026-11-19

Den andra delen av `agents.json` har granskats via Crowdin API. Förslagen är utkast och har inte skickats till Crowdin.

| Sträng-ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 3692 | Priors | Prior | Priorer |
| 3700 | No {1} in my workplace's building | Ingen {1} i min arbetsplats byggnad | Ingen {1} i arbetsplatsens byggnad |
| 4344 | Recently lost their house. Will fade with time. | Förlorade nyligen sitt hus. Kommer att avta med tiden. | Har nyligen förlorat sitt hus. Avtar med tiden. |
| 4378 | Villager path blocked | Bybons väg blockerad | Bybons väg är blockerad |

## Kontroller

- `l10n-lint --language sv` passerade utan anmärkningar.
- `hunspell -d sv_SE` passerade utan anmärkningar.
- Platshållaren `{1}` är bevarad.
