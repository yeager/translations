# Foundation – regler V, svensk granskning 2026-11-19

Den sista delen av `rules.json` har granskats via Crowdin API. Fyra förbättringsförslag identifierades.

| ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 22576 | Nondepletable Small Mineral Deposits | Icke-utvinningsbara små mineralfyndigheter | Ej uttömbara små mineralfyndigheter |
| 22578 | Small mineral deposits are nondepletable. | Små mineralfyndigheter är inte utvinningsbara. | Små mineralfyndigheter är inte uttömbara. |
| 23261 | This effect does not stack. | Denna effekt går inte att öka på. | Den här effekten kan inte staplas. |
| 26668 | Special rules | — | Särskilda regler |

## Kontroller

- `l10n-lint --language sv` passerade utan anmärkningar.
- `hunspell -d sv_SE` passerade utan anmärkningar.
- Förslagen har inte skickats till Crowdin.
