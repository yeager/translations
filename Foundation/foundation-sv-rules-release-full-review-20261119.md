# Foundation – regler: release, full radgranskning 2026-11-19

Samtliga 61 strängar i `rules.release.json` granskades via Crowdin API. Nio förbättringsförslag identifierades; övriga 52 bedömdes korrekta.

| ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 22604 | Your Combatants will not die, get wounded, or have their weapons broken. | Dina Kombattanter kommer inte att dö, bli skadade eller förstöra sina vapen. | Dina kombattanter kommer inte att dö, bli skadade eller få sina vapen förstörda. |
| 22614 | {1} Trade Routes are unlocked and upgraded. | {1} Handelsvägar är upplåsta och uppgraderade. | {1} handelsvägar är upplåsta och uppgraderade. |
| 22652 | {1} Privilege | {1} Privilegium | {1} privilegium |
| 22654 | Stonework Promotion | Främjande av stenarbete | Främjande av stenhuggeri |
| 22664 | Stonework Promotion Edict | Förordnande om befordran inom stenarbete | Påbud om främjande av stenhuggeri |
| 22670 | Careful Planning Edict | Försiktig planering Påbud | Påbud om noggrann planering |
| 22672 | Contractual Wage Edict | Avtalsenlig lönediktat | Påbud om avtalsenlig lön |
| 22704 | Protection Taxation | Skydd Beskattning | Skyddsbeskattning |
| 22712 | Unlock Tithe Taxes on Churches. | Lås upp tionde skatter på kyrkor. | Lås upp tiondeskatter på kyrkor. |

## Kontroller

- `l10n-lint --language sv` passerade utan anmärkningar.
- `hunspell -d sv_SE` passerade utan anmärkningar.
- Platshållarna `{1}` bevaras.
- Förslagen har inte skickats till Crowdin.
