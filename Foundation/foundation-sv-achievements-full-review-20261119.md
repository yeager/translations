# Foundation – prestationer, full radgranskning 2026-11-19

Samtliga 14 strängar i `achievements.json` granskades via Crowdin API. Fyra förbättringsförslag identifierades; övriga tio bedömdes korrekta.

| ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 1858 | Achievement Progress | Prestations Framsteg | Prestationsframsteg |
| 23295 | Achievements cannot be earned while playing with the {1} Game Rule Preset. | Prestationer kan inte uppnås när du spelar med spelregel förvalet {1}. | Prestationer kan inte uppnås när du spelar med spelregelsförinställningen {1}. |
| 23297 | Some Achievements cannot be earned while playing with the {1} Game Rule Preset. | Några prestationer kan inte uppnås när du spelar med spelregel förvalet {1}. | Vissa prestationer kan inte uppnås när du spelar med spelregelsförinställningen {1}. |
| 23299 | This Achievement cannot be earned while playing with the {1} Game Rule Preset. | Denna prestation kan inte uppnås när du spelar med spelregel förvalet {1}. | Den här prestationen kan inte uppnås när du spelar med spelregelsförinställningen {1}. |

## Kontroller

- `l10n-lint --language sv` passerade utan anmärkningar.
- `hunspell -d sv_SE` passerade utan anmärkningar.
- Platshållaren `{1}` är bevarad.
- Förslagen har inte skickats till Crowdin.
