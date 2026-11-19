# Foundation – militär, full radgranskning 2026-11-19

Samtliga 12 strängar i `military.json` granskades via Crowdin API. Två förbättringsförslag identifierades; övriga tio bedömdes korrekta.

| ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 21916 | Active {1} Fortification | Aktiv {1} Befästning | Aktiv {1} befästning |
| 21924 | Passive {1} Fortification | Passiv {1} Befästning | Passiv {1} befästning |

## Kontroller

- `l10n-lint --language sv` passerade utan anmärkningar.
- `hunspell -d sv_SE` passerade utan anmärkningar.
- Platshållaren `{1}` är bevarad.
- Förslagen har inte skickats till Crowdin.
