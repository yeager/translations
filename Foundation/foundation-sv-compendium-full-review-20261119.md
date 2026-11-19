# Foundation – kompendium, full radgranskning 2026-11-19

Samtliga 24 strängar i `compendium.json` granskades via Crowdin API. Tre förbättringsförslag identifierades; övriga 21 bedömdes korrekta.

| ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 25916 | Complete one of the 'Prospect a Mineral Deposit in proximity' mandates | Slutför ett av uppdragen ”Prospektera en mineralfyndighet i närheten” | Slutför ett av mandaten ”Prospektera en mineralfyndighet i närheten” |
| 25930 | Unlock '{1}' by progressing through the Harvest Festival tiers | Lås upp ”{1}” genom att avancera i skördefestens nivåer | Lås upp ”{1}” genom att avancera i skördefestivalens nivåer |
| 26702 | View in Compendium | — | Visa i kompendiet |

## Kontroller

- `l10n-lint --language sv`: inga fel eller varningar; en informationsnotering om ändrade engelska enkla citattecken till svenska typografiska citattecken i 25916.
- `hunspell -d sv_SE` passerade utan anmärkningar.
- Platshållaren `{1}` är bevarad.
- Förslagen har inte skickats till Crowdin.
