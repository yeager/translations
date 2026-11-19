# Foundation – byhändelser: full radgranskning 2026-11-19

Samtliga 31 redan översatta strängar i `village_event.json` granskades via Crowdin API. Ett förbättringsförslag identifierades; resterande 30 bedömdes korrekta.

| ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 26076 | {1}'s {2} | {1}s {2} | {1}:s {2} |

## Kontroller

- `l10n-lint --language sv` passerade utan anmärkningar.
- `hunspell -d sv_SE` passerade utan anmärkningar.
- Båda platshållarna är bevarade; kolon används enligt svensk genitivnotation.
- Förslaget har inte skickats till Crowdin.
